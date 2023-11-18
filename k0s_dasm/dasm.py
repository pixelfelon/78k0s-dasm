"""Disassembly harness script."""

from k0s_dasm.base import Program
from k0s_dasm.ibase import Instruction
from k0s_dasm.util import fmthex

with open(r"C:\Users\jrowley\Downloads\BP10140_41807201810293003049.bin", "rb") as f:
	prog = Program(bytearray(f.read()))
	pcs: list[int] = []
	pcs.extend(prog.entry_points())
	while True:
		# multi flow loop
		try:
			pc = pcs.pop()
		except IndexError:
			break
		if pc not in prog.instrs:
			print(f"\nlabel_{pc:04X}:")
		while True:
			# single flow loop
			if pc in prog.instrs:
				# already looked at this path
				break
			try:
				instr = Instruction.autoload(prog, pc)
			except ValueError:
				badword = prog.flash[pc : pc + 4]
				print(f"; BAD INSTRUCTION AT 0x{pc:04X}: {fmthex(badword)} ...")
				break

			word = prog.flash[instr.pc : instr.pc + instr.bytecount]
			prog.instrs[instr.pc] = instr
			print(f"\t{instr.render():<30};{instr.pc:04X}  {fmthex(word)}")
			for note in instr.notes:
				print(f"\t                              ; {note}")

			if len(instr.next) > 1:
				pcs.extend(instr.next[1:])
			if len(instr.next) < 1:
				break
			pc = instr.next[0]
