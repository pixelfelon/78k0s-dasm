"""Instruction mnemonic definitions."""
from typing import ClassVar, Sequence

from k0s_dasm import styler
from k0s_dasm.ibase import Field, FieldB, FieldW, Instruction


class MovwRpWord(Instruction):
	"""MOVW rp, #word."""

	mnemonic: ClassVar[str] = "MOVW rp, #word"
	match: ClassVar[int] = 0b11110000_00000000_00000000
	mmask: ClassVar[int] = 0b11110011_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=18, bits=2, styler=styler.reg16, name="rp"),
		FieldW(offset_bytes=0, styler=styler.imm16, name="word"),
	)
	format: ClassVar[str] = "MOVW {0}, {1}"


# TODO: The Instructions
