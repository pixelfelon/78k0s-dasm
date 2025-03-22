"""Disassembly harness script."""

import sys

from k0s_dasm.base import Program
from k0s_dasm.flow import Forward
from k0s_dasm.ibase import Instruction
from k0s_dasm.util import fmthex

print(sys.argv[1])
with open(sys.argv[1], "rb") as f:
	prog = Program(bytearray(f.read()))

pcs: list[int] = []
# pcs.extend(prog.entry_points())
pcs = [0x0100]
orig_pcs = list(pcs)

while True:
	# multi flow loop
	try:
		pc = pcs.pop()
	except IndexError:
		break
	while True:
		# single flow loop
		if pc in prog.instrs:
			# already looked at this path
			break
		try:
			instr = Instruction.autoload(prog, pc)
		except ValueError:
			badword = prog.flash[pc : pc + 4]
			print(f"; BAD INSTRUCTION AT 0x{pc:04X}: {fmthex(badword)} {int.from_bytes(badword, 'big'):032b}...")
			break

		prog.instrs[instr.pc] = instr
		if not isinstance(instr.flow, Forward) and len(instr.next) > 0:
			# Cheating a bit here, idea of [-1] is to skip forward flow in
			# conditional flows, which is conventionally returned first.
			prog.branches[instr.pc] = instr.next[-1]

		word = prog.flash[instr.pc : instr.pc + instr.bytecount]
		if word == b"\xFF":
			break

		if len(instr.next) > 1:
			pcs.extend(instr.next[1:])
		if len(instr.next) < 1:
			break
		pc = instr.next[0]

iaddrs = sorted(prog.instrs.keys())
bdest = prog.branch_sources()
last_instr: Instruction | None = None
SILENCE_BRANCHNOTE_DIST = 8
for iaddr in iaddrs:
	if last_instr is not None and iaddr != last_instr.next_addr:
		# Break in flow, print newlines for visual separation.
		# We do several because instruction notes also kinda look like
		# a newline when scanning the left side.
		print()
		print()
		print()
	if iaddr in bdest or iaddr in orig_pcs:
		# This address is a branch destination, or entry point.
		label_text = f"{prog.get_label(iaddr)}:"
		label_note = ""
		max_dist = 0
		if iaddr in bdest:
			for bsrc in bdest[iaddr]:
				max_dist = max(max_dist, abs(bsrc - iaddr))
		if iaddr in orig_pcs:
			label_note = "Entry Point"
			if max_dist > SILENCE_BRANCHNOTE_DIST:
				label_note += ", Also "
		if max_dist > SILENCE_BRANCHNOTE_DIST:
			label_note += "From"
			for bsrc in sorted(bdest[iaddr]):
				label_note += f" {bsrc:04X}H,"
			label_note = label_note.rstrip(",")
		if len(label_note):
			label_note = "; " + label_note
		print(f"{label_text:<34}{label_note}")

	instr = prog.instrs[iaddr]
	word = prog.flash[instr.pc : instr.pc + instr.bytecount]
	instr.render()
	if last_instr is not None and instr.pc < last_instr.next_addr:
		instr.notes.append("WARNING: Overlaps with last instruction!")

	snotes = [f"{instr.pc:04X}", fmthex(word)]
	snotes.extend(instr.smallnotes)
	snote = "  ".join(snotes)
	print(f"    {instr.render():<30};{snote}")
	for note in instr.notes:
		print(f"                                  ; {note}")

	last_instr = instr
