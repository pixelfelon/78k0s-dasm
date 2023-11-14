"""Disassembly harness script."""

from k0s_dasm.ibase import Instruction, Program
from k0s_dasm.util import fmthex

with open(r"C:\Users\jrowley\Downloads\BP10140_41807201810293003049.bin", "rb") as f:
	prog = Program(bytearray(f.read()))
	prog.pc = 0x82
	while True:
		instr = Instruction.autoload(prog)
		word = prog.flash[prog.pc - instr.bytecount : prog.pc]
		print(f"0x{prog.pc:04X}: {fmthex(word)} - {instr.render()}")
