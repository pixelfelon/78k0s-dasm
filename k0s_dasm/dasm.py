"""Disassembly harness script."""

from k0s_dasm.base import Program
from k0s_dasm.defs import PROG_BASE
from k0s_dasm.ibase import Instruction
from k0s_dasm.util import fmthex

with open(r"C:\Users\jrowley\Downloads\BP10140_41807201810293003049.bin", "rb") as f:
	prog = Program(bytearray(f.read()))
	pc = PROG_BASE
	print(f"label_{pc:04X}:")
	while True:
		oldpc = pc
		try:
			instr = Instruction.autoload(prog, pc)
			if len(instr.next) != 1:
				raise RuntimeError("Branching NYI")
			pc = instr.next[0]
		except ValueError:
			break
		word = prog.flash[oldpc:pc]
		print(f"\t{instr.render():<30};{oldpc:04X}  {fmthex(word)}")
	badword = prog.flash[pc : pc + 4]
	print(f"; BAD INSTRUCTION AT 0x{pc:04X}: {fmthex(badword)} ...")
