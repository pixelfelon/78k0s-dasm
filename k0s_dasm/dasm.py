"""Disassembly harness script."""

from k0s_dasm.defs import PROG_BASE
from k0s_dasm.ibase import Instruction, Program
from k0s_dasm.util import fmthex

with open(r"C:\Users\jrowley\Downloads\BP10140_41807201810293003049.bin", "rb") as f:
	prog = Program(bytearray(f.read()))
	prog.pc = PROG_BASE
	print(f".label_{prog.pc:04X}")
	while True:
		oldpc = prog.pc
		try:
			instr = Instruction.autoload(prog)
		except ValueError:
			break
		word = prog.flash[oldpc : prog.pc]
		print(f"\t{instr.render():<30};{oldpc:04X}  {fmthex(word)}")
	print(f"; BAD INSTRUCTION AT 0x{prog.pc:04X}")
