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


class MovAPde(Instruction):
	"""MOV A, [DE]."""

	mnemonic: ClassVar[str] = "MOV A, [DE]"
	match: ClassVar[int] = 0b00101011
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV A, [DE]"


class MovPdeA(Instruction):
	"""MOV [DE], A."""

	mnemonic: ClassVar[str] = "MOV [DE], A"
	match: ClassVar[int] = 0b11101011
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV [DE], A"


class MovAPhl(Instruction):
	"""MOV A, [HL]."""

	mnemonic: ClassVar[str] = "MOV A, [HL]"
	match: ClassVar[int] = 0b00101111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV A, [HL]"


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


class DbnzBAddrRel(Instruction):
	"""DBNZ B, $addr16."""

	mnemonic: ClassVar[str] = "DBNZ B, $addr16"
	match: ClassVar[int] = 0b00110110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=0, bits=8, styler=styler.addr_pcrel, name="addr16"),
	)
	format: ClassVar[str] = "DBNZ B, {0}"


class DbnzCAddrRel(Instruction):
	"""DBNZ C, $addr16."""

	mnemonic: ClassVar[str] = "DBNZ C, $addr16"
	match: ClassVar[int] = 0b00110100_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=0, bits=8, styler=styler.addr_pcrel, name="addr16"),
	)
	format: ClassVar[str] = "DBNZ C, {0}"


class DbnzSaddrAddrRel(Instruction):
	"""DBNZ saddr, $addr16."""

	mnemonic: ClassVar[str] = "DBNZ saddr, $addr16"
	match: ClassVar[int] = 0b00110010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=8, bits=8, styler=styler.addr_short, name="saddr"),
		FieldB(offset=0, bits=8, styler=styler.addr_pcrel, name="addr16"),
	)
	format: ClassVar[str] = "DBNZ {0}, {1}"


class MovwAxRp(Instruction):
	"""MOVW AX, rp."""

	mnemonic: ClassVar[str] = "MOVW AX, rp"
	match: ClassVar[int] = 0b11010000
	mmask: ClassVar[int] = 0b11110011
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=2, bits=2, styler=styler.reg16, name="rp"),
	)
	format: ClassVar[str] = "MOVW AX, {0}"


class CmpwAxWord(Instruction):
	"""CMPW AX, #word."""

	mnemonic: ClassVar[str] = "CMPW AX, #word"
	match: ClassVar[int] = 0b11100010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldW(offset_bytes=0, styler=styler.imm16, name="word"),
	)
	format: ClassVar[str] = "CMPW AX, {0}"


class BzAddrRel(Instruction):
	"""BZ $addr16."""

	mnemonic: ClassVar[str] = "BZ $addr16"
	match: ClassVar[int] = 0b00111100_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=0, bits=8, styler=styler.addr_pcrel, name="addr16"),
	)
	format: ClassVar[str] = "BZ {0}"


class BrAddrRel(Instruction):
	"""BR $addr16."""

	mnemonic: ClassVar[str] = "BR $addr16"
	match: ClassVar[int] = 0b00110000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=0, bits=8, styler=styler.addr_pcrel, name="addr16"),
	)
	format: ClassVar[str] = "BR {0}"


class CmpSaddrByte(Instruction):
	"""CMP saddr, #byte."""

	mnemonic: ClassVar[str] = "CMP saddr, #byte"
	match: ClassVar[int] = 0b00010001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		FieldB(offset=8, bits=8, styler=styler.addr_short, name="saddr"),
		FieldB(offset=0, bits=8, styler=styler.imm8, name="byte"),
	)
	format: ClassVar[str] = "CMP {0}, {1}"


class Clr1Cy(Instruction):
	"""CLR1 CY."""

	mnemonic: ClassVar[str] = "CLR1 CY"
	match: ClassVar[int] = 0b00000100
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "CLR1 CY"


class RorcA1(Instruction):
	"""RORC A, 1."""

	mnemonic: ClassVar[str] = "RORC A, 1"
	match: ClassVar[int] = 0b00000010
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "RORC A, 1"


class XchAX(Instruction):
	"""XCH A, X."""

	mnemonic: ClassVar[str] = "XCH A, X"
	match: ClassVar[int] = 0b11000000
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XCH A, X"


class RolA1(Instruction):
	"""ROL A, 1."""

	mnemonic: ClassVar[str] = "ROL A, 1"
	match: ClassVar[int] = 0b00010000
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ROL A, 1"


class Ret(Instruction):
	"""RET."""

	mnemonic: ClassVar[str] = "RET"
	match: ClassVar[int] = 0b00100000
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "RET"


# TODO: The Instructions
