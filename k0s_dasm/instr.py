"""Instruction mnemonic definitions."""

from typing import ClassVar, Sequence

from k0s_dasm import field
from k0s_dasm.base import Field
from k0s_dasm.ibase import Instruction


class MOVrbyte(Instruction):
	"""MOV r, #byte."""

	mnemonic: ClassVar[str] = "MOV r, #byte"
	match: ClassVar[int] = 0b00001010_11110001_00000000
	mmask: ClassVar[int] = 0b11111111_11110001_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.Reg8(offset=9),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "MOV {0}, {1}"


class MOVsaddrbyte(Instruction):
	"""MOV saddr, #byte."""

	mnemonic: ClassVar[str] = "MOV saddr, #byte"
	match: ClassVar[int] = 0b11110101_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "MOV {0}, {1}"


class MOVsfrbyte(Instruction):
	"""MOV sfr, #byte."""

	mnemonic: ClassVar[str] = "MOV sfr, #byte"
	match: ClassVar[int] = 0b11110111_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "MOV {0}, {1}"


class MOVAr(Instruction):
	"""MOV A, r."""

	mnemonic: ClassVar[str] = "MOV A, r"
	match: ClassVar[int] = 0b00001010_00100001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "MOV A, {0}"


class MOVrA(Instruction):
	"""MOV r, A."""

	mnemonic: ClassVar[str] = "MOV r, A"
	match: ClassVar[int] = 0b00001010_11100001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "MOV {0}, A"


class MOVAsaddr(Instruction):
	"""MOV A, saddr."""

	mnemonic: ClassVar[str] = "MOV A, saddr"
	match: ClassVar[int] = 0b00100101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "MOV A, {0}"


class MOVsaddrA(Instruction):
	"""MOV saddr, A."""

	mnemonic: ClassVar[str] = "MOV saddr, A"
	match: ClassVar[int] = 0b11100101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "MOV {0}, A"


class MOVAsfr(Instruction):
	"""MOV A, sfr."""

	mnemonic: ClassVar[str] = "MOV A, sfr"
	match: ClassVar[int] = 0b00100111_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SFR(offset=0),)
	format: ClassVar[str] = "MOV A, {0}"


class MOVsfrA(Instruction):
	"""MOV sfr, A."""

	mnemonic: ClassVar[str] = "MOV sfr, A"
	match: ClassVar[int] = 0b11100111_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SFR(offset=0),)
	format: ClassVar[str] = "MOV {0}, A"


class MOVAaddr(Instruction):
	"""MOV A, !addr16."""

	mnemonic: ClassVar[str] = "MOV A, !addr16"
	match: ClassVar[int] = 0b00101001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "MOV A, {0}"


class MOVaddrA(Instruction):
	"""MOV !addr16, A."""

	mnemonic: ClassVar[str] = "MOV !addr16, A"
	match: ClassVar[int] = 0b11101001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "MOV {0}, A"


class MOVPSWbyte(Instruction):
	"""MOV PSW, #byte."""

	mnemonic: ClassVar[str] = "MOV PSW, #byte"
	match: ClassVar[int] = 0b11110101_00011110_00000000
	mmask: ClassVar[int] = 0b11111111_11111111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "MOV PSW, {0}"


class MOVAPSW(Instruction):
	"""MOV A, PSW."""

	mnemonic: ClassVar[str] = "MOV A, PSW"
	match: ClassVar[int] = 0b00100101_00011110
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV A, PSW"


class MOVPSWA(Instruction):
	"""MOV PSW, A."""

	mnemonic: ClassVar[str] = "MOV PSW, A"
	match: ClassVar[int] = 0b11100101_00011110
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV PSW, A"


class MOVADE(Instruction):
	"""MOV A, [DE]."""

	mnemonic: ClassVar[str] = "MOV A, [DE]"
	match: ClassVar[int] = 0b00101011
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV A, [DE]"


class MOVDEA(Instruction):
	"""MOV [DE], A."""

	mnemonic: ClassVar[str] = "MOV [DE], A"
	match: ClassVar[int] = 0b11101011
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV [DE], A"


class MOVAHL(Instruction):
	"""MOV A, [HL]."""

	mnemonic: ClassVar[str] = "MOV A, [HL]"
	match: ClassVar[int] = 0b00101111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV A, [HL]"


class MOVHLA(Instruction):
	"""MOV [HL], A."""

	mnemonic: ClassVar[str] = "MOV [HL], A"
	match: ClassVar[int] = 0b11101111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV [HL], A"


class MOVAHLbyte(Instruction):
	"""MOV A, [HL + byte]."""

	mnemonic: ClassVar[str] = "MOV A, [HL + byte]"
	match: ClassVar[int] = 0b00101101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "MOV A, [HL + {0}]"


class MOVHLbyteA(Instruction):
	"""MOV [HL + byte], A."""

	mnemonic: ClassVar[str] = "MOV [HL + byte], A"
	match: ClassVar[int] = 0b11101101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "MOV [HL + {0}], A"


class XCHAX(Instruction):
	"""XCH A, X."""

	mnemonic: ClassVar[str] = "XCH A, X"
	match: ClassVar[int] = 0b11000000
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XCH A, X"


class XCHAr(Instruction):
	"""XCH A, r."""

	mnemonic: ClassVar[str] = "XCH A, r"
	match: ClassVar[int] = 0b00001010_00000001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "XCH A, {0}"


class XCHAsaddr(Instruction):
	"""XCH A, saddr."""

	mnemonic: ClassVar[str] = "XCH A, saddr"
	match: ClassVar[int] = 0b00000101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "XCH A, {0}"


class XCHAsfr(Instruction):
	"""XCH A, sfr."""

	mnemonic: ClassVar[str] = "XCH A, sfr"
	match: ClassVar[int] = 0b00000111_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SFR(offset=0),)
	format: ClassVar[str] = "XCH A, {0}"


class XCHADE(Instruction):
	"""XCH A, [DE]."""

	mnemonic: ClassVar[str] = "XCH A, [DE]"
	match: ClassVar[int] = 0b00001011
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XCH A, [DE]"


class XCHAHL(Instruction):
	"""XCH A, [HL]."""

	mnemonic: ClassVar[str] = "XCH A, [HL]"
	match: ClassVar[int] = 0b00001111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XCH A, [HL]"


class XCHAHLbyte(Instruction):
	"""XCH A, [HL + byte]."""

	mnemonic: ClassVar[str] = "XCH A, [HL + byte]"
	match: ClassVar[int] = 0b00001101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "XCH A, [HL + {0}]"


class MOVWrpword(Instruction):
	"""MOVW rp, #word."""

	mnemonic: ClassVar[str] = "MOVW rp, #word"
	match: ClassVar[int] = 0b11110000_00000000_00000000
	mmask: ClassVar[int] = 0b11110011_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.Reg16(offset=18),
		field.Imm16(offset=0),
	)
	format: ClassVar[str] = "MOVW {0}, {1}"


class MOVWAXsaddrp(Instruction):
	"""MOVW AX, saddrp."""

	mnemonic: ClassVar[str] = "MOVW AX, saddrp"
	match: ClassVar[int] = 0b11010110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "MOVW AX, {0}"


class MOVWsaddrpAX(Instruction):
	"""MOVW saddrp, AX."""

	mnemonic: ClassVar[str] = "MOVW saddrp, AX"
	match: ClassVar[int] = 0b11100110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "MOVW {0}, AX"


class MOVWAXrp(Instruction):
	"""MOVW AX, rp."""

	mnemonic: ClassVar[str] = "MOVW AX, rp"
	match: ClassVar[int] = 0b11010000
	mmask: ClassVar[int] = 0b11110011
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=2),)
	format: ClassVar[str] = "MOVW AX, {0}"


class MOVWrpAX(Instruction):
	"""MOVW rp, AX."""

	mnemonic: ClassVar[str] = "MOVW rp, AX"
	match: ClassVar[int] = 0b11100000
	mmask: ClassVar[int] = 0b11110011
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=2),)
	format: ClassVar[str] = "MOVW {0}, AX"


class XCHWAXrp(Instruction):
	"""XCHW AX, rp."""

	mnemonic: ClassVar[str] = "XCHW AX, rp"
	match: ClassVar[int] = 0b11000000
	mmask: ClassVar[int] = 0b11110011
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=2),)
	format: ClassVar[str] = "XCHW AX, {0}"


class ADDAbyte(Instruction):
	"""ADD A, #byte."""

	mnemonic: ClassVar[str] = "ADD A, #byte"
	match: ClassVar[int] = 0b10000011_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "ADD A, {0}"


class ADDsaddrbyte(Instruction):
	"""ADD saddr, #byte."""

	mnemonic: ClassVar[str] = "ADD saddr, #byte"
	match: ClassVar[int] = 0b10000001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "ADD {0}, {1}"


class ADDAr(Instruction):
	"""ADD A, r."""

	mnemonic: ClassVar[str] = "ADD A, r"
	match: ClassVar[int] = 0b00001010_10000001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "ADD A, {0}"


class ADDAsaddr(Instruction):
	"""ADD A, saddr."""

	mnemonic: ClassVar[str] = "ADD A, saddr"
	match: ClassVar[int] = 0b10000101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "ADD A, {0}"


class ADDAaddr(Instruction):
	"""ADD A, !addr16."""

	mnemonic: ClassVar[str] = "ADD A, !addr16"
	match: ClassVar[int] = 0b10001001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "ADD A, {0}"


class ADDAHL(Instruction):
	"""ADD A, [HL]."""

	mnemonic: ClassVar[str] = "ADD A, [HL]"
	match: ClassVar[int] = 0b10001111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ADD A, [HL]"


class ADDAHLbyte(Instruction):
	"""ADD A, [HL + byte]."""

	mnemonic: ClassVar[str] = "ADD A, [HL + byte]"
	match: ClassVar[int] = 0b10001101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "ADD A, [HL + {0}]"


class ADDCAbyte(Instruction):
	"""ADDC A, #byte."""

	mnemonic: ClassVar[str] = "ADDC A, #byte"
	match: ClassVar[int] = 0b10100011_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "ADDC A, {0}"


class ADDCsaddrbyte(Instruction):
	"""ADDC saddr, #byte."""

	mnemonic: ClassVar[str] = "ADDC saddr, #byte"
	match: ClassVar[int] = 0b10100001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "ADDC {0}, {1}"


class ADDCAr(Instruction):
	"""ADDC A, r."""

	mnemonic: ClassVar[str] = "ADDC A, r"
	match: ClassVar[int] = 0b00001010_10100001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "ADDC A, {0}"


class ADDCAsaddr(Instruction):
	"""ADDC A, saddr."""

	mnemonic: ClassVar[str] = "ADDC A, saddr"
	match: ClassVar[int] = 0b10100101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "ADDC A, {0}"


class ADDCAaddr(Instruction):
	"""ADDC A, !addr16."""

	mnemonic: ClassVar[str] = "ADDC A, !addr16"
	match: ClassVar[int] = 0b10101001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "ADDC A, {0}"


class ADDCAHL(Instruction):
	"""ADDC A, [HL]."""

	mnemonic: ClassVar[str] = "ADDC A, [HL]"
	match: ClassVar[int] = 0b10101111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ADDC A, [HL]"


class ADDCAHLbyte(Instruction):
	"""ADDC A, [HL + byte]."""

	mnemonic: ClassVar[str] = "ADDC A, [HL + byte]"
	match: ClassVar[int] = 0b10101101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "ADDC A, [HL + {0}]"


class SUBAbyte(Instruction):
	"""SUB A, #byte."""

	mnemonic: ClassVar[str] = "SUB A, #byte"
	match: ClassVar[int] = 0b10010011_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "SUB A, {0}"


class SUBsaddrbyte(Instruction):
	"""SUB saddr, #byte."""

	mnemonic: ClassVar[str] = "SUB saddr, #byte"
	match: ClassVar[int] = 0b10010001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "SUB {0}, {1}"


class SUBAr(Instruction):
	"""SUB A, r."""

	mnemonic: ClassVar[str] = "SUB A, r"
	match: ClassVar[int] = 0b00001010_10010001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "SUB A, {0}"


class SUBAsaddr(Instruction):
	"""SUB A, saddr."""

	mnemonic: ClassVar[str] = "SUB A, saddr"
	match: ClassVar[int] = 0b10010101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "SUB A, {0}"


class SUBAaddr(Instruction):
	"""SUB A, !addr16."""

	mnemonic: ClassVar[str] = "SUB A, !addr16"
	match: ClassVar[int] = 0b10011001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "SUB A, {0}"


class SUBAHL(Instruction):
	"""SUB A, [HL]."""

	mnemonic: ClassVar[str] = "SUB A, [HL]"
	match: ClassVar[int] = 0b10011111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "SUB A, [HL]"


class SUBAHLbyte(Instruction):
	"""SUB A, [HL + byte]."""

	mnemonic: ClassVar[str] = "SUB A, [HL + byte]"
	match: ClassVar[int] = 0b10011101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "SUB A, [HL + {0}]"


class SUBCAbyte(Instruction):
	"""SUBC A, #byte."""

	mnemonic: ClassVar[str] = "SUBC A, #byte"
	match: ClassVar[int] = 0b10110011_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "SUBC A, {0}"


class SUBCsaddrbyte(Instruction):
	"""SUBC saddr, #byte."""

	mnemonic: ClassVar[str] = "SUBC saddr, #byte"
	match: ClassVar[int] = 0b10110001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "SUBC {0}, {1}"


class SUBCAr(Instruction):
	"""SUBC A, r."""

	mnemonic: ClassVar[str] = "SUBC A, r"
	match: ClassVar[int] = 0b00001010_10110001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "SUBC A, {0}"


class SUBCAsaddr(Instruction):
	"""SUBC A, saddr."""

	mnemonic: ClassVar[str] = "SUBC A, saddr"
	match: ClassVar[int] = 0b10110101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "SUBC A, {0}"


class SUBCAaddr(Instruction):
	"""SUBC A, !addr16."""

	mnemonic: ClassVar[str] = "SUBC A, !addr16"
	match: ClassVar[int] = 0b10111001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "SUBC A, {0}"


class SUBCAHL(Instruction):
	"""SUBC A, [HL]."""

	mnemonic: ClassVar[str] = "SUBC A, [HL]"
	match: ClassVar[int] = 0b10111111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "SUBC A, [HL]"


class SUBCAHLbyte(Instruction):
	"""SUBC A, [HL + byte]."""

	mnemonic: ClassVar[str] = "SUBC A, [HL + byte]"
	match: ClassVar[int] = 0b10111101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "SUBC A, [HL + {0}]"


class ANDAbyte(Instruction):
	"""AND A, #byte."""

	mnemonic: ClassVar[str] = "AND A, #byte"
	match: ClassVar[int] = 0b01100011_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "AND A, {0}"


class ANDsaddrbyte(Instruction):
	"""AND saddr, #byte."""

	mnemonic: ClassVar[str] = "AND saddr, #byte"
	match: ClassVar[int] = 0b01100001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "AND {0}, {1}"


class ANDAr(Instruction):
	"""AND A, r."""

	mnemonic: ClassVar[str] = "AND A, r"
	match: ClassVar[int] = 0b00001010_01100001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "AND A, {0}"


class ANDAsaddr(Instruction):
	"""AND A, saddr."""

	mnemonic: ClassVar[str] = "AND A, saddr"
	match: ClassVar[int] = 0b01100101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "AND A, {0}"


class ANDAaddr(Instruction):
	"""AND A, !addr16."""

	mnemonic: ClassVar[str] = "AND A, !addr16"
	match: ClassVar[int] = 0b01101001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "AND A, {0}"


class ANDAHL(Instruction):
	"""AND A, [HL]."""

	mnemonic: ClassVar[str] = "AND A, [HL]"
	match: ClassVar[int] = 0b01101111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "AND A, [HL]"


class ANDAHLbyte(Instruction):
	"""AND A, [HL + byte]."""

	mnemonic: ClassVar[str] = "AND A, [HL + byte]"
	match: ClassVar[int] = 0b01101101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "AND A, [HL + {0}]"


class ORAbyte(Instruction):
	"""OR A, #byte."""

	mnemonic: ClassVar[str] = "OR A, #byte"
	match: ClassVar[int] = 0b01110011_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "OR A, {0}"


class ORsaddrbyte(Instruction):
	"""OR saddr, #byte."""

	mnemonic: ClassVar[str] = "OR saddr, #byte"
	match: ClassVar[int] = 0b01110001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "OR {0}, {1}"


class ORAr(Instruction):
	"""OR A, r."""

	mnemonic: ClassVar[str] = "OR A, r"
	match: ClassVar[int] = 0b00001010_01110001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "OR A, {0}"


class ORAsaddr(Instruction):
	"""OR A, saddr."""

	mnemonic: ClassVar[str] = "OR A, saddr"
	match: ClassVar[int] = 0b01110101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "OR A, {0}"


class ORAaddr(Instruction):
	"""OR A, !addr16."""

	mnemonic: ClassVar[str] = "OR A, !addr16"
	match: ClassVar[int] = 0b01111001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "OR A, {0}"


class ORAHL(Instruction):
	"""OR A, [HL]."""

	mnemonic: ClassVar[str] = "OR A, [HL]"
	match: ClassVar[int] = 0b01111111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "OR A, [HL]"


class ORAHLbyte(Instruction):
	"""OR A, [HL + byte]."""

	mnemonic: ClassVar[str] = "OR A, [HL + byte]"
	match: ClassVar[int] = 0b01111101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "OR A, [HL + {0}]"


class XORAbyte(Instruction):
	"""XOR A, #byte."""

	mnemonic: ClassVar[str] = "XOR A, #byte"
	match: ClassVar[int] = 0b01000011_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "XOR A, {0}"


class XORsaddrbyte(Instruction):
	"""XOR saddr, #byte."""

	mnemonic: ClassVar[str] = "XOR saddr, #byte"
	match: ClassVar[int] = 0b01000001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "XOR {0}, {1}"


class XORAr(Instruction):
	"""XOR A, r."""

	mnemonic: ClassVar[str] = "XOR A, r"
	match: ClassVar[int] = 0b00001010_01000001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "XOR A, {0}"


class XORAsaddr(Instruction):
	"""XOR A, saddr."""

	mnemonic: ClassVar[str] = "XOR A, saddr"
	match: ClassVar[int] = 0b01000101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "XOR A, {0}"


class XORAaddr(Instruction):
	"""XOR A, !addr16."""

	mnemonic: ClassVar[str] = "XOR A, !addr16"
	match: ClassVar[int] = 0b01001001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "XOR A, {0}"


class XORAHL(Instruction):
	"""XOR A, [HL]."""

	mnemonic: ClassVar[str] = "XOR A, [HL]"
	match: ClassVar[int] = 0b01001111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XOR A, [HL]"


class XORAHLbyte(Instruction):
	"""XOR A, [HL + byte]."""

	mnemonic: ClassVar[str] = "XOR A, [HL + byte]"
	match: ClassVar[int] = 0b01001101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "XOR A, [HL + {0}]"


class CMPAbyte(Instruction):
	"""CMP A, #byte."""

	mnemonic: ClassVar[str] = "CMP A, #byte"
	match: ClassVar[int] = 0b00010011_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "CMP A, {0}"


class CMPsaddrbyte(Instruction):
	"""CMP saddr, #byte."""

	mnemonic: ClassVar[str] = "CMP saddr, #byte"
	match: ClassVar[int] = 0b00010001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "CMP {0}, {1}"


class CMPAr(Instruction):
	"""CMP A, r."""

	mnemonic: ClassVar[str] = "CMP A, r"
	match: ClassVar[int] = 0b00001010_00010001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "CMP A, {0}"


class CMPAsaddr(Instruction):
	"""CMP A, saddr."""

	mnemonic: ClassVar[str] = "CMP A, saddr"
	match: ClassVar[int] = 0b00010101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "CMP A, {0}"


class CMPAaddr(Instruction):
	"""CMP A, !addr16."""

	mnemonic: ClassVar[str] = "CMP A, !addr16"
	match: ClassVar[int] = 0b00011001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "CMP A, {0}"


class CMPAHL(Instruction):
	"""CMP A, [HL]."""

	mnemonic: ClassVar[str] = "CMP A, [HL]"
	match: ClassVar[int] = 0b00011111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "CMP A, [HL]"


class CMPAHLbyte(Instruction):
	"""CMP A, [HL + byte]."""

	mnemonic: ClassVar[str] = "CMP A, [HL + byte]"
	match: ClassVar[int] = 0b00011101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "CMP A, [HL + {0}]"


class ADDWAXword(Instruction):
	"""ADDW AX, #word."""

	mnemonic: ClassVar[str] = "ADDW AX, #word"
	match: ClassVar[int] = 0b11010010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm16(offset=0),)
	format: ClassVar[str] = "ADDW AX, {0}"


class SUBWAXword(Instruction):
	"""SUBW AX, #word."""

	mnemonic: ClassVar[str] = "SUBW AX, #word"
	match: ClassVar[int] = 0b11000010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm16(offset=0),)
	format: ClassVar[str] = "SUBW AX, {0}"


class CMPWAXword(Instruction):
	"""CMPW AX, #word."""

	mnemonic: ClassVar[str] = "CMPW AX, #word"
	match: ClassVar[int] = 0b11100010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm16(offset=0),)
	format: ClassVar[str] = "CMPW AX, {0}"


class INCr(Instruction):
	"""INC r."""

	mnemonic: ClassVar[str] = "INC r"
	match: ClassVar[int] = 0b00001010_11000001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "INC {0}"


class INCsaddr(Instruction):
	"""INC saddr."""

	mnemonic: ClassVar[str] = "INC saddr"
	match: ClassVar[int] = 0b11000101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "INC {0}"


class DECr(Instruction):
	"""DEC r."""

	mnemonic: ClassVar[str] = "DEC r"
	match: ClassVar[int] = 0b00001010_11010001
	mmask: ClassVar[int] = 0b11111111_11110001
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=1),)
	format: ClassVar[str] = "DEC {0}"


class DECsaddr(Instruction):
	"""DEC saddr."""

	mnemonic: ClassVar[str] = "DEC saddr"
	match: ClassVar[int] = 0b11010101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "DEC {0}"


class INCWrp(Instruction):
	"""INCW rp."""

	mnemonic: ClassVar[str] = "INCW rp"
	match: ClassVar[int] = 0b10000000
	mmask: ClassVar[int] = 0b11110011
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=2),)
	format: ClassVar[str] = "INCW {0}"


class DECWrp(Instruction):
	"""DECW rp."""

	mnemonic: ClassVar[str] = "DECW rp"
	match: ClassVar[int] = 0b10010000
	mmask: ClassVar[int] = 0b11110011
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=2),)
	format: ClassVar[str] = "DECW {0}"


class RORA(Instruction):
	"""ROR A, 1."""

	mnemonic: ClassVar[str] = "ROR A, 1"
	match: ClassVar[int] = 0b00000000
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ROR A, 1"


class ROLA(Instruction):
	"""ROL A, 1."""

	mnemonic: ClassVar[str] = "ROL A, 1"
	match: ClassVar[int] = 0b00010000
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ROL A, 1"


class RORCA(Instruction):
	"""RORC A, 1."""

	mnemonic: ClassVar[str] = "RORC A, 1"
	match: ClassVar[int] = 0b00000010
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "RORC A, 1"


class ROLCA(Instruction):
	"""ROLC A, 1."""

	mnemonic: ClassVar[str] = "ROLC A, 1"
	match: ClassVar[int] = 0b00010010
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ROLC A, 1"


class SETsaddrbit(Instruction):
	"""SET1 saddr.bit."""

	mnemonic: ClassVar[str] = "SET1 saddr.bit"
	match: ClassVar[int] = 0b00001010_00001010_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.SAddr(offset=0),
	)
	format: ClassVar[str] = "SET1 {0}{1}"


class SETsfrbit(Instruction):
	"""SET1 sfr.bit."""

	mnemonic: ClassVar[str] = "SET1 sfr.bit"
	match: ClassVar[int] = 0b00001010_00000110_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.SFR(offset=0),
	)
	format: ClassVar[str] = "SET1 {0}{1}"


class SETAbit(Instruction):
	"""SET1 A.bit."""

	mnemonic: ClassVar[str] = "SET1 A.bit"
	match: ClassVar[int] = 0b00001010_00000010
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "SET1 A{0}"


class SETPSWbit(Instruction):
	"""SET1 PSW.bit."""

	mnemonic: ClassVar[str] = "SET1 PSW.bit"
	match: ClassVar[int] = 0b00001010_00001010_00011110
	mmask: ClassVar[int] = 0b11111111_10001111_11111111
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=12),)
	format: ClassVar[str] = "SET1 PSW{0}"


class SETHLbit(Instruction):
	"""SET1 [HL].bit."""

	mnemonic: ClassVar[str] = "SET1 [HL].bit"
	match: ClassVar[int] = 0b00001010_00001110
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "SET1 [HL]{0}"


class CLRsaddrbit(Instruction):
	"""CLR1 saddr.bit."""

	mnemonic: ClassVar[str] = "CLR1 saddr.bit"
	match: ClassVar[int] = 0b00001010_10001010_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.SAddr(offset=0),
	)
	format: ClassVar[str] = "CLR1 {0}{1}"


class CLRsfrbit(Instruction):
	"""CLR1 sfr.bit."""

	mnemonic: ClassVar[str] = "CLR1 sfr.bit"
	match: ClassVar[int] = 0b00001010_10000110_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.SFR(offset=0),
	)
	format: ClassVar[str] = "CLR1 {0}{1}"


class CLRAbit(Instruction):
	"""CLR1 A.bit."""

	mnemonic: ClassVar[str] = "CLR1 A.bit"
	match: ClassVar[int] = 0b00001010_10000010
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "CLR1 A{0}"


class CLRPSWbit(Instruction):
	"""CLR1 PSW.bit."""

	mnemonic: ClassVar[str] = "CLR1 PSW.bit"
	match: ClassVar[int] = 0b00001010_10001010_00011110
	mmask: ClassVar[int] = 0b11111111_10001111_11111111
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=12),)
	format: ClassVar[str] = "CLR1 PSW{0}"


class CLRHLbit(Instruction):
	"""CLR1 [HL].bit."""

	mnemonic: ClassVar[str] = "CLR1 [HL].bit"
	match: ClassVar[int] = 0b00001010_10001110
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "CLR1 [HL]{0}"


class SETCY(Instruction):
	"""SET1 CY."""

	mnemonic: ClassVar[str] = "SET1 CY"
	match: ClassVar[int] = 0b00010100
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "SET1 CY"


class CLRCY(Instruction):
	"""CLR1 CY."""

	mnemonic: ClassVar[str] = "CLR1 CY"
	match: ClassVar[int] = 0b00000100
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "CLR1 CY"


class NOTCY(Instruction):
	"""NOT1 CY."""

	mnemonic: ClassVar[str] = "NOT1 CY"
	match: ClassVar[int] = 0b00000110
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "NOT1 CY"


class CALLaddr(Instruction):
	"""CALL !addr16."""

	mnemonic: ClassVar[str] = "CALL !addr16"
	match: ClassVar[int] = 0b00100010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "CALL {0}"


class CALLTaddr(Instruction):
	"""CALLT [addr5]."""

	mnemonic: ClassVar[str] = "CALLT [addr5]"
	match: ClassVar[int] = 0b01000000
	mmask: ClassVar[int] = 0b11000001
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr5(offset=1),)
	format: ClassVar[str] = "CALLT {0}"


class RET(Instruction):
	"""RET."""

	mnemonic: ClassVar[str] = "RET"
	match: ClassVar[int] = 0b00100000
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "RET"


class RETI(Instruction):
	"""RETI."""

	mnemonic: ClassVar[str] = "RETI"
	match: ClassVar[int] = 0b00100100
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "RETI"


class PUSHPSW(Instruction):
	"""PUSH PSW."""

	mnemonic: ClassVar[str] = "PUSH PSW"
	match: ClassVar[int] = 0b00101110
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "PUSH PSW"


class PUSHrp(Instruction):
	"""PUSH rp."""

	mnemonic: ClassVar[str] = "PUSH rp"
	match: ClassVar[int] = 0b10100010
	mmask: ClassVar[int] = 0b11110011
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=2),)
	format: ClassVar[str] = "PUSH {0}"


class POPPSW(Instruction):
	"""POP PSW."""

	mnemonic: ClassVar[str] = "POP PSW"
	match: ClassVar[int] = 0b00101100
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "POP PSW"


class POPrp(Instruction):
	"""POP rp."""

	mnemonic: ClassVar[str] = "POP rp"
	match: ClassVar[int] = 0b10100000
	mmask: ClassVar[int] = 0b11110011
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=2),)
	format: ClassVar[str] = "POP {0}"


class MOVWSPAX(Instruction):
	"""MOVW SP,AX."""

	mnemonic: ClassVar[str] = "MOVW SP,AX"
	match: ClassVar[int] = 0b11100110_00011100
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOVW SP,AX"


class MOVWAXSP(Instruction):
	"""MOVW AX,SP."""

	mnemonic: ClassVar[str] = "MOVW AX,SP"
	match: ClassVar[int] = 0b11010110_00011100
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOVW AX,SP"


class BRaddr(Instruction):
	"""BR !addr16."""

	mnemonic: ClassVar[str] = "BR !addr16"
	match: ClassVar[int] = 0b10110010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "BR {0}"


class BRReladdr(Instruction):
	"""BR $addr16."""

	mnemonic: ClassVar[str] = "BR $addr16"
	match: ClassVar[int] = 0b00110000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	format: ClassVar[str] = "BR {0}"


class BRAX(Instruction):
	"""BR AX."""

	mnemonic: ClassVar[str] = "BR AX"
	match: ClassVar[int] = 0b10110000
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "BR AX"


class BCReladdr(Instruction):
	"""BC $addr16."""

	mnemonic: ClassVar[str] = "BC $addr16"
	match: ClassVar[int] = 0b00111000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	format: ClassVar[str] = "BC {0}"


class BNCReladdr(Instruction):
	"""BNC $addr16."""

	mnemonic: ClassVar[str] = "BNC $addr16"
	match: ClassVar[int] = 0b00111010_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	format: ClassVar[str] = "BNC {0}"


class BZReladdr(Instruction):
	"""BZ $addr16."""

	mnemonic: ClassVar[str] = "BZ $addr16"
	match: ClassVar[int] = 0b00111100_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	format: ClassVar[str] = "BZ {0}"


class BNZReladdr(Instruction):
	"""BNZ $addr16."""

	mnemonic: ClassVar[str] = "BNZ $addr16"
	match: ClassVar[int] = 0b00111110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	format: ClassVar[str] = "BNZ {0}"


class BTsaddrbitReladdr(Instruction):
	"""BT saddr.bit, $addr16."""

	mnemonic: ClassVar[str] = "BT saddr.bit, $addr16"
	match: ClassVar[int] = 0b00001010_10001000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=20),
		field.SAddr(offset=8),
		field.JAddrRel(offset=0),
	)
	format: ClassVar[str] = "BT {0}{1}, {2}"


class BTsfrbitReladdr(Instruction):
	"""BT sfr.bit, $addr16."""

	mnemonic: ClassVar[str] = "BT sfr.bit, $addr16"
	match: ClassVar[int] = 0b00001010_10000100_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=20),
		field.SFR(offset=8),
		field.JAddrRel(offset=0),
	)
	format: ClassVar[str] = "BT {0}{1}, {2}"


class BTAbitReladdr(Instruction):
	"""BT A.bit, $addr16."""

	mnemonic: ClassVar[str] = "BT A.bit, $addr16"
	match: ClassVar[int] = 0b00001010_10000000_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.JAddrRel(offset=0),
	)
	format: ClassVar[str] = "BT A{0}, {1}"


class BTPSWbitReladdr(Instruction):
	"""BT PSW.bit, $addr16."""

	mnemonic: ClassVar[str] = "BT PSW.bit, $addr16"
	match: ClassVar[int] = 0b00001010_10001000_00011110_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_11111111_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=20),
		field.JAddrRel(offset=0),
	)
	format: ClassVar[str] = "BT PSW{0}, {1}"


class BFsaddrbitReladdr(Instruction):
	"""BF saddr.bit, $addr16."""

	mnemonic: ClassVar[str] = "BF saddr.bit, $addr16"
	match: ClassVar[int] = 0b00001010_00001000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=20),
		field.SAddr(offset=8),
		field.JAddrRel(offset=0),
	)
	format: ClassVar[str] = "BF {0}{1}, {2}"


class BFsfrbitReladdr(Instruction):
	"""BF sfr.bit, $addr16."""

	mnemonic: ClassVar[str] = "BF sfr.bit, $addr16"
	match: ClassVar[int] = 0b00001010_00000100_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=20),
		field.SFR(offset=8),
		field.JAddrRel(offset=0),
	)
	format: ClassVar[str] = "BF {0}{1}, {2}"


class BFAbitReladdr(Instruction):
	"""BF A.bit, $addr16."""

	mnemonic: ClassVar[str] = "BF A.bit, $addr16"
	match: ClassVar[int] = 0b00001010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.JAddrRel(offset=0),
	)
	format: ClassVar[str] = "BF A{0}, {1}"


class BFPSWbitReladdr(Instruction):
	"""BF PSW.bit, $addr16."""

	mnemonic: ClassVar[str] = "BF PSW.bit, $addr16"
	match: ClassVar[int] = 0b00001010_00001000_00011110_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_11111111_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=20),
		field.JAddrRel(offset=0),
	)
	format: ClassVar[str] = "BF PSW{0}, {1}"


class DBNZBReladdr(Instruction):
	"""DBNZ B, $addr16."""

	mnemonic: ClassVar[str] = "DBNZ B, $addr16"
	match: ClassVar[int] = 0b00110110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	format: ClassVar[str] = "DBNZ B, {0}"


class DBNZCReladdr(Instruction):
	"""DBNZ C, $addr16."""

	mnemonic: ClassVar[str] = "DBNZ C, $addr16"
	match: ClassVar[int] = 0b00110100_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	format: ClassVar[str] = "DBNZ C, {0}"


class DBNZsaddrReladdr(Instruction):
	"""DBNZ saddr, $addr16."""

	mnemonic: ClassVar[str] = "DBNZ saddr, $addr16"
	match: ClassVar[int] = 0b00110010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.JAddrRel(offset=0),
	)
	format: ClassVar[str] = "DBNZ {0}, {1}"


class NOP(Instruction):
	"""NOP."""

	mnemonic: ClassVar[str] = "NOP"
	match: ClassVar[int] = 0b00001000
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "NOP"


class EI(Instruction):
	"""EI."""

	mnemonic: ClassVar[str] = "EI"
	match: ClassVar[int] = 0b00001010_01111010_00011110
	mmask: ClassVar[int] = 0b11111111_11111111_11111111
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "EI"


class DI(Instruction):
	"""DI."""

	mnemonic: ClassVar[str] = "DI"
	match: ClassVar[int] = 0b00001010_11111010_00011110
	mmask: ClassVar[int] = 0b11111111_11111111_11111111
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "DI"


class HALT(Instruction):
	"""HALT."""

	mnemonic: ClassVar[str] = "HALT"
	match: ClassVar[int] = 0b00001100
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "HALT"


class STOP(Instruction):
	"""STOP."""

	mnemonic: ClassVar[str] = "STOP"
	match: ClassVar[int] = 0b00001110
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "STOP"
