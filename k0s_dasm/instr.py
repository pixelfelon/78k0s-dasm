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


class MovwSaddrpAx(Instruction):
	"""MOVW saddrp, AX."""

	mnemonic: ClassVar[str] = "MOVW saddrp, AX"
	match: ClassVar[int] = 0b11100110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=0, bits=8, styler=styler.addr_short, name="saddrp"),
	)
	format: ClassVar[str] = "MOVW {0}, AX"


class CallAddr16(Instruction):
	"""CALL !addr16."""

	mnemonic: ClassVar[str] = "CALL !addr16"
	match: ClassVar[int] = 0b00100010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldW(offset_bytes=0, styler=styler.addr_abs, name="addr16"),
	)
	format: ClassVar[str] = "CALL {0}"


class XorAR(Instruction):
	"""XOR A, r."""

	mnemonic: ClassVar[str] = "XOR A, r"
	match: ClassVar[int] = 0b00001010_01000001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=1, bits=3, styler=styler.reg8, name="r"),
	)
	format: ClassVar[str] = "XOR A, {0}"


class MovAddr16A(Instruction):
	"""MOV !addr16, A."""

	mnemonic: ClassVar[str] = "MOV !addr16, A"
	match: ClassVar[int] = 0b11101001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldW(offset_bytes=0, styler=styler.addr_abs, name="addr16"),
	)
	format: ClassVar[str] = "MOV {0}, A"


class MovRByte(Instruction):
	"""MOV r, #byte."""

	mnemonic: ClassVar[str] = "MOV r, #byte"
	match: ClassVar[int] = 0b00001010_11110001_00000000
	mmask: ClassVar[int] = 0b11111111_11110001_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=9, bits=3, styler=styler.reg8, name="r"),
		FieldB(offset=0, bits=8, styler=styler.imm8, name="byte"),
	)
	format: ClassVar[str] = "MOV {0}, {1}"


class MovPhlA(Instruction):
	"""MOV [HL], A."""

	mnemonic: ClassVar[str] = "MOV [HL], A"
	match: ClassVar[int] = 0b11101111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV [HL], A"


class IncwRp(Instruction):
	"""INCW rp."""

	mnemonic: ClassVar[str] = "INCW rp"
	match: ClassVar[int] = 0b10000000
	mmask: ClassVar[int] = 0b11110011
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=2, bits=2, styler=styler.reg16, name="rp"),
	)
	format: ClassVar[str] = "INCW {0}"


class DbnzBAddr16(Instruction):
	"""DBNZ B, $addr16."""

	mnemonic: ClassVar[str] = "DBNZ B, $addr16"
	match: ClassVar[int] = 0b00110110_00000000
	mmask: ClassVar[int] = 0b11110011_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=0, bits=8, styler=styler.addr_pcrel, name="addr16"),
	)
	format: ClassVar[str] = "DBNZ B, {0}"


# TODO: The Instructions
