"""Instruction mnemonic definitions."""

from typing import ClassVar, Sequence

from k0s_dasm import field
from k0s_dasm.base import Field, Flow
from k0s_dasm.defs import PSW_MAGIC_ADDR, SP_MAGIC_ADDR, Reg8, Reg16
from k0s_dasm.flow import (
	CallReturn,
	ComputedCallT,
	ComputedUnknown,
	ConditionalBranch,
	Return,
	UnconditionalBranch,
)
from k0s_dasm.ibase import Instruction


class MOVrbyte(Instruction):
	"""MOV r, #byte."""

	mnemonic: ClassVar[str] = "MOV r, #byte"
	match: ClassVar[int] = 0b10100000_00000000
	mmask: ClassVar[int] = 0b11111000_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (
		field.Reg8(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "MOV {0}, {1}"


class MOVsaddrbyte(Instruction):
	"""MOV saddr, #byte."""

	mnemonic: ClassVar[str] = "MOV saddr, #byte"
	match: ClassVar[int] = 0b00010001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.Imm8(offset=0),
	)
	format: ClassVar[str] = "MOV {0}, {1}"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class MOVsfrbyte(Instruction):
	"""MOV sfr, #byte."""

	mnemonic: ClassVar[str] = "MOV sfr, #byte"
	match: ClassVar[int] = 0b00010011_00000000_00000000
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
	match: ClassVar[int] = 0b01100000
	mmask: ClassVar[int] = 0b11111000
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "MOV A, {0}"

	def _check_fields(self) -> bool:
		"""Check that r is not A."""
		r = self.operands[self.field_defs[0]].val
		if r == Reg8.A:
			return False
		else:
			return True


class MOVrA(Instruction):
	"""MOV r, A."""

	mnemonic: ClassVar[str] = "MOV r, A"
	match: ClassVar[int] = 0b01110000
	mmask: ClassVar[int] = 0b11111000
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "MOV {0}, A"

	def _check_fields(self) -> bool:
		"""Check that r is not A."""
		r = self.operands[self.field_defs[0]].val
		if r == Reg8.A:
			return False
		else:
			return True


class MOVAsaddr(Instruction):
	"""MOV A, saddr."""

	mnemonic: ClassVar[str] = "MOV A, saddr"
	match: ClassVar[int] = 0b11110000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "MOV A, {0}"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class MOVsaddrA(Instruction):
	"""MOV saddr, A."""

	mnemonic: ClassVar[str] = "MOV saddr, A"
	match: ClassVar[int] = 0b11110010_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "MOV {0}, A"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class MOVAsfr(Instruction):
	"""MOV A, sfr."""

	mnemonic: ClassVar[str] = "MOV A, sfr"
	match: ClassVar[int] = 0b11110100_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SFR(offset=0),)
	format: ClassVar[str] = "MOV A, {0}"


class MOVsfrA(Instruction):
	"""MOV sfr, A."""

	mnemonic: ClassVar[str] = "MOV sfr, A"
	match: ClassVar[int] = 0b11110110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SFR(offset=0),)
	format: ClassVar[str] = "MOV {0}, A"


class MOVAaddr(Instruction):
	"""MOV A, !addr16."""

	mnemonic: ClassVar[str] = "MOV A, !addr16"
	match: ClassVar[int] = 0b10001110_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "MOV A, {0}"


class MOVaddrA(Instruction):
	"""MOV !addr16, A."""

	mnemonic: ClassVar[str] = "MOV !addr16, A"
	match: ClassVar[int] = 0b10011110_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "MOV {0}, A"


class MOVPSWbyte(Instruction):
	"""MOV PSW, #byte."""

	mnemonic: ClassVar[str] = "MOV PSW, #byte"
	match: ClassVar[int] = 0b00010001_00011110_00000000
	mmask: ClassVar[int] = 0b11111111_11111111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "MOV PSW, {0}"


class MOVAPSW(Instruction):
	"""MOV A, PSW."""

	mnemonic: ClassVar[str] = "MOV A, PSW"
	match: ClassVar[int] = 0b11110000_00011110
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV A, PSW"


class MOVPSWA(Instruction):
	"""MOV PSW, A."""

	mnemonic: ClassVar[str] = "MOV PSW, A"
	match: ClassVar[int] = 0b11110010_00011110
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV PSW, A"


class MOVADE(Instruction):
	"""MOV A, [DE]."""

	mnemonic: ClassVar[str] = "MOV A, [DE]"
	match: ClassVar[int] = 0b10000101
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV A, [DE]"


class MOVDEA(Instruction):
	"""MOV [DE], A."""

	mnemonic: ClassVar[str] = "MOV [DE], A"
	match: ClassVar[int] = 0b10010101
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV [DE], A"


class MOVAHL(Instruction):
	"""MOV A, [HL]."""

	mnemonic: ClassVar[str] = "MOV A, [HL]"
	match: ClassVar[int] = 0b10000111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV A, [HL]"


class MOVHLA(Instruction):
	"""MOV [HL], A."""

	mnemonic: ClassVar[str] = "MOV [HL], A"
	match: ClassVar[int] = 0b10010111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV [HL], A"


class MOVAHLbyte(Instruction):
	"""MOV A, [HL + byte]."""

	mnemonic: ClassVar[str] = "MOV A, [HL + byte]"
	match: ClassVar[int] = 0b10101110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "MOV A, [HL + {0}]"


class MOVHLbyteA(Instruction):
	"""MOV [HL + byte], A."""

	mnemonic: ClassVar[str] = "MOV [HL + byte], A"
	match: ClassVar[int] = 0b10111110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "MOV [HL + {0}], A"


class MOVAHLB(Instruction):
	"""MOV A, [HL + B]."""

	mnemonic: ClassVar[str] = "MOV A, [HL + B]"
	match: ClassVar[int] = 0b10101011
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV A, [HL + B]"


class MOVHLBA(Instruction):
	"""MOV [HL + B], A."""

	mnemonic: ClassVar[str] = "MOV [HL + B], A"
	match: ClassVar[int] = 0b10111011
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV [HL + B], A"


class MOVAHLC(Instruction):
	"""MOV A, [HL + C]."""

	mnemonic: ClassVar[str] = "MOV A, [HL + C]"
	match: ClassVar[int] = 0b10101010
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV A, [HL + C]"


class MOVHLCA(Instruction):
	"""MOV [HL + C], A."""

	mnemonic: ClassVar[str] = "MOV [HL + C], A"
	match: ClassVar[int] = 0b10111010
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOV [HL + C], A"


class XCHAr(Instruction):
	"""XCH A, r."""

	mnemonic: ClassVar[str] = "XCH A, r"
	match: ClassVar[int] = 0b00110000
	mmask: ClassVar[int] = 0b11111000
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "XCH A, {0}"

	def _check_fields(self) -> bool:
		"""Check that r is not A."""
		r = self.operands[self.field_defs[0]].val
		if r == Reg8.A:
			return False
		else:
			return True


class XCHAsaddr(Instruction):
	"""XCH A, saddr."""

	mnemonic: ClassVar[str] = "XCH A, saddr"
	match: ClassVar[int] = 0b10000011_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "XCH A, {0}"


class XCHAsfr(Instruction):
	"""XCH A, sfr."""

	mnemonic: ClassVar[str] = "XCH A, sfr"
	match: ClassVar[int] = 0b10010011_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SFR(offset=0),)
	format: ClassVar[str] = "XCH A, {0}"


class XCHAaddr16(Instruction):
	"""XCH A, !addr16."""

	mnemonic: ClassVar[str] = "XCH A, !addr16"
	match: ClassVar[int] = 0b11001110_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "XCH A, {0}"


class XCHADE(Instruction):
	"""XCH A, [DE]."""

	mnemonic: ClassVar[str] = "XCH A, [DE]"
	match: ClassVar[int] = 0b00000101
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XCH A, [DE]"


class XCHAHL(Instruction):
	"""XCH A, [HL]."""

	mnemonic: ClassVar[str] = "XCH A, [HL]"
	match: ClassVar[int] = 0b00000111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XCH A, [HL]"


class XCHAHLbyte(Instruction):
	"""XCH A, [HL + byte]."""

	mnemonic: ClassVar[str] = "XCH A, [HL + byte]"
	match: ClassVar[int] = 0b11011110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "XCH A, [HL + {0}]"


class XCHAHLB(Instruction):
	"""XCH A, [HL + B]."""

	mnemonic: ClassVar[str] = "XCH A, [HL + B]"
	match: ClassVar[int] = 0b00110001_10001011
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XCH A, [HL + B]"


class XCHAHLC(Instruction):
	"""XCH A, [HL + C]."""

	mnemonic: ClassVar[str] = "XCH A, [HL + C]"
	match: ClassVar[int] = 0b00110001_10001010
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XCH A, [HL + C]"


class MOVWrpword(Instruction):
	"""MOVW rp, #word."""

	mnemonic: ClassVar[str] = "MOVW rp, #word"
	match: ClassVar[int] = 0b00010000_00000000_00000000
	mmask: ClassVar[int] = 0b11111001_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.Reg16(offset=17),
		field.Imm16(offset=0),
	)
	format: ClassVar[str] = "MOVW {0}, {1}"


class MOVWsaddrpword(Instruction):
	"""MOVW saddrp, #word."""

	mnemonic: ClassVar[str] = "MOVW saddrp, #word"
	match: ClassVar[int] = 0b11101110_00000000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=16),
		field.Imm16(offset=0),
	)
	format: ClassVar[str] = "MOVW {0}, {1}"

	def _check_fields(self) -> bool:
		"""Check that saddrp is not 0b00011100 (which refers to SP)."""
		addr = self.operands[self.field_defs[0]].val
		if addr == SP_MAGIC_ADDR:
			return False
		else:
			return True


class MOVWsfrpword(Instruction):
	"""MOVW sfrp, #word."""

	mnemonic: ClassVar[str] = "MOVW sfrp, #word"
	match: ClassVar[int] = 0b11111110_00000000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=16),
		field.Imm16(offset=0),
	)
	format: ClassVar[str] = "MOVW {0}, {1}"


class MOVWAXsaddrp(Instruction):
	"""MOVW AX, saddrp."""

	mnemonic: ClassVar[str] = "MOVW AX, saddrp"
	match: ClassVar[int] = 0b10001001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "MOVW AX, {0}"

	def _check_fields(self) -> bool:
		"""Check that saddrp is not 0b00011100 (which refers to SP)."""
		addr = self.operands[self.field_defs[0]].val
		if addr == SP_MAGIC_ADDR:
			return False
		else:
			return True


class MOVWsaddrpAX(Instruction):
	"""MOVW saddrp, AX."""

	mnemonic: ClassVar[str] = "MOVW saddrp, AX"
	match: ClassVar[int] = 0b10011001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "MOVW {0}, AX"

	def _check_fields(self) -> bool:
		"""Check that saddrp is not 0b00011100 (which refers to SP)."""
		addr = self.operands[self.field_defs[0]].val
		if addr == SP_MAGIC_ADDR:
			return False
		else:
			return True


class MOVWAXsfrp(Instruction):
	"""MOVW AX, sfrp."""

	mnemonic: ClassVar[str] = "MOVW AX, sfrp"
	match: ClassVar[int] = 0b10101001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SFR(offset=0),)
	format: ClassVar[str] = "MOVW AX, {0}"


class MOVWsfrpAX(Instruction):
	"""MOVW sfrp, AX."""

	mnemonic: ClassVar[str] = "MOVW sfrp, AX"
	match: ClassVar[int] = 0b10111001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SFR(offset=0),)
	format: ClassVar[str] = "MOVW {0}, AX"


class MOVWAXrp(Instruction):
	"""MOVW AX, rp."""

	mnemonic: ClassVar[str] = "MOVW AX, rp"
	match: ClassVar[int] = 0b11000000
	mmask: ClassVar[int] = 0b11111001
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=1),)
	format: ClassVar[str] = "MOVW AX, {0}"

	def _check_fields(self) -> bool:
		"""Check that rp is not AX."""
		rp = self.operands[self.field_defs[0]].val
		if rp == Reg16.AX:
			return False
		else:
			return True


class MOVWrpAX(Instruction):
	"""MOVW rp, AX."""

	mnemonic: ClassVar[str] = "MOVW rp, AX"
	match: ClassVar[int] = 0b11010000
	mmask: ClassVar[int] = 0b11111001
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=1),)
	format: ClassVar[str] = "MOVW {0}, AX"

	def _check_fields(self) -> bool:
		"""Check that rp is not AX."""
		rp = self.operands[self.field_defs[0]].val
		if rp == Reg16.AX:
			return False
		else:
			return True


class MOVWAXaddr16(Instruction):
	"""MOVW AX, !addr16."""

	mnemonic: ClassVar[str] = "MOVW AX, !addr16"
	match: ClassVar[int] = 0b00000010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "MOVW AX, {0}"


class MOVWaddr16AX(Instruction):
	"""MOVW !addr16, AX."""

	mnemonic: ClassVar[str] = "MOVW !addr16, AX"
	match: ClassVar[int] = 0b00000011_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "MOVW {0}, AX"


class XCHWAXrp(Instruction):
	"""XCHW AX, rp."""

	mnemonic: ClassVar[str] = "XCHW AX, rp"
	match: ClassVar[int] = 0b11100000
	mmask: ClassVar[int] = 0b11111001
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=1),)
	format: ClassVar[str] = "XCHW AX, {0}"

	def _check_fields(self) -> bool:
		"""Check that rp is not AX."""
		rp = self.operands[self.field_defs[0]].val
		if rp == Reg16.AX:
			return False
		else:
			return True


class ADDAbyte(Instruction):
	"""ADD A, #byte."""

	mnemonic: ClassVar[str] = "ADD A, #byte"
	match: ClassVar[int] = 0b00001101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "ADD A, {0}"


class ADDsaddrbyte(Instruction):
	"""ADD saddr, #byte."""

	mnemonic: ClassVar[str] = "ADD saddr, #byte"
	match: ClassVar[int] = 0b10001000_00000000_00000000
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
	match: ClassVar[int] = 0b01100001_00001000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "ADD A, {0}"

	def _check_fields(self) -> bool:
		"""Check that r is not A."""
		r = self.operands[self.field_defs[0]].val
		if r == Reg8.A:
			return False
		else:
			return True


class ADDrA(Instruction):
	"""ADD r, A."""

	mnemonic: ClassVar[str] = "ADD r, A"
	match: ClassVar[int] = 0b01100001_00000000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "ADD {0}, A"


class ADDAsaddr(Instruction):
	"""ADD A, saddr."""

	mnemonic: ClassVar[str] = "ADD A, saddr"
	match: ClassVar[int] = 0b00001110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "ADD A, {0}"


class ADDAaddr(Instruction):
	"""ADD A, !addr16."""

	mnemonic: ClassVar[str] = "ADD A, !addr16"
	match: ClassVar[int] = 0b00001000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "ADD A, {0}"


class ADDAHL(Instruction):
	"""ADD A, [HL]."""

	mnemonic: ClassVar[str] = "ADD A, [HL]"
	match: ClassVar[int] = 0b00001111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ADD A, [HL]"


class ADDAHLbyte(Instruction):
	"""ADD A, [HL + byte]."""

	mnemonic: ClassVar[str] = "ADD A, [HL + byte]"
	match: ClassVar[int] = 0b00001001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "ADD A, [HL + {0}]"


class ADDAHLB(Instruction):
	"""ADD A, [HL + B]."""

	mnemonic: ClassVar[str] = "ADD A, [HL + B]"
	match: ClassVar[int] = 0b00110001_00001011
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ADD A, [HL + B]"


class ADDAHLC(Instruction):
	"""ADD A, [HL + C]."""

	mnemonic: ClassVar[str] = "ADD A, [HL + C]"
	match: ClassVar[int] = 0b00110001_00001010
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ADD A, [HL + C]"


class ADDCAbyte(Instruction):
	"""ADDC A, #byte."""

	mnemonic: ClassVar[str] = "ADDC A, #byte"
	match: ClassVar[int] = 0b00101101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "ADDC A, {0}"


class ADDCsaddrbyte(Instruction):
	"""ADDC saddr, #byte."""

	mnemonic: ClassVar[str] = "ADDC saddr, #byte"
	match: ClassVar[int] = 0b10101000_00000000_00000000
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
	match: ClassVar[int] = 0b01100001_00101000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "ADDC A, {0}"

	def _check_fields(self) -> bool:
		"""Check that r is not A."""
		r = self.operands[self.field_defs[0]].val
		if r == Reg8.A:
			return False
		else:
			return True


class ADDCrA(Instruction):
	"""ADDC r, A."""

	mnemonic: ClassVar[str] = "ADDC r, A"
	match: ClassVar[int] = 0b01100001_00100000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "ADDC {0}, A"


class ADDCAsaddr(Instruction):
	"""ADDC A, saddr."""

	mnemonic: ClassVar[str] = "ADDC A, saddr"
	match: ClassVar[int] = 0b00101110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "ADDC A, {0}"


class ADDCAaddr(Instruction):
	"""ADDC A, !addr16."""

	mnemonic: ClassVar[str] = "ADDC A, !addr16"
	match: ClassVar[int] = 0b00101000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "ADDC A, {0}"


class ADDCAHL(Instruction):
	"""ADDC A, [HL]."""

	mnemonic: ClassVar[str] = "ADDC A, [HL]"
	match: ClassVar[int] = 0b00101111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ADDC A, [HL]"


class ADDCAHLbyte(Instruction):
	"""ADDC A, [HL + byte]."""

	mnemonic: ClassVar[str] = "ADDC A, [HL + byte]"
	match: ClassVar[int] = 0b00101001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "ADDC A, [HL + {0}]"


class ADDCAHLB(Instruction):
	"""ADDC A, [HL + B]."""

	mnemonic: ClassVar[str] = "ADDC A, [HL + B]"
	match: ClassVar[int] = 0b00110001_00101011
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ADDC A, [HL + B]"


class ADDCAHLC(Instruction):
	"""ADDC A, [HL + C]."""

	mnemonic: ClassVar[str] = "ADDC A, [HL + C]"
	match: ClassVar[int] = 0b00110001_00101010
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ADDC A, [HL + C]"


class SUBAbyte(Instruction):
	"""SUB A, #byte."""

	mnemonic: ClassVar[str] = "SUB A, #byte"
	match: ClassVar[int] = 0b00011101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "SUB A, {0}"


class SUBsaddrbyte(Instruction):
	"""SUB saddr, #byte."""

	mnemonic: ClassVar[str] = "SUB saddr, #byte"
	match: ClassVar[int] = 0b10011000_00000000_00000000
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
	match: ClassVar[int] = 0b01100001_00011000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "SUB A, {0}"

	def _check_fields(self) -> bool:
		"""Check that r is not A."""
		r = self.operands[self.field_defs[0]].val
		if r == Reg8.A:
			return False
		else:
			return True


class SUBrA(Instruction):
	"""SUB r, A."""

	mnemonic: ClassVar[str] = "SUB r, A"
	match: ClassVar[int] = 0b01100001_00010000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "SUB {0}, A"


class SUBAsaddr(Instruction):
	"""SUB A, saddr."""

	mnemonic: ClassVar[str] = "SUB A, saddr"
	match: ClassVar[int] = 0b00011110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "SUB A, {0}"


class SUBAaddr(Instruction):
	"""SUB A, !addr16."""

	mnemonic: ClassVar[str] = "SUB A, !addr16"
	match: ClassVar[int] = 0b00011000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "SUB A, {0}"


class SUBAHL(Instruction):
	"""SUB A, [HL]."""

	mnemonic: ClassVar[str] = "SUB A, [HL]"
	match: ClassVar[int] = 0b00011111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "SUB A, [HL]"


class SUBAHLbyte(Instruction):
	"""SUB A, [HL + byte]."""

	mnemonic: ClassVar[str] = "SUB A, [HL + byte]"
	match: ClassVar[int] = 0b00011001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "SUB A, [HL + {0}]"


class SUBAHLB(Instruction):
	"""SUB A, [HL + B]."""

	mnemonic: ClassVar[str] = "SUB A, [HL + B]"
	match: ClassVar[int] = 0b00110001_00011011
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "SUB A, [HL + B]"


class SUBAHLC(Instruction):
	"""SUB A, [HL + C]."""

	mnemonic: ClassVar[str] = "SUB A, [HL + C]"
	match: ClassVar[int] = 0b00110001_00011010
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "SUB A, [HL + C]"


class SUBCAbyte(Instruction):
	"""SUBC A, #byte."""

	mnemonic: ClassVar[str] = "SUBC A, #byte"
	match: ClassVar[int] = 0b00111101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "SUBC A, {0}"


class SUBCsaddrbyte(Instruction):
	"""SUBC saddr, #byte."""

	mnemonic: ClassVar[str] = "SUBC saddr, #byte"
	match: ClassVar[int] = 0b10111000_00000000_00000000
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
	match: ClassVar[int] = 0b01100001_00111000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "SUBC A, {0}"

	def _check_fields(self) -> bool:
		"""Check that r is not A."""
		r = self.operands[self.field_defs[0]].val
		if r == Reg8.A:
			return False
		else:
			return True


class SUBCrA(Instruction):
	"""SUBC r, A."""

	mnemonic: ClassVar[str] = "SUBC r, A"
	match: ClassVar[int] = 0b01100001_00110000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "SUBC {0}, A"


class SUBCAsaddr(Instruction):
	"""SUBC A, saddr."""

	mnemonic: ClassVar[str] = "SUBC A, saddr"
	match: ClassVar[int] = 0b00111110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "SUBC A, {0}"


class SUBCAaddr(Instruction):
	"""SUBC A, !addr16."""

	mnemonic: ClassVar[str] = "SUBC A, !addr16"
	match: ClassVar[int] = 0b00111000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "SUBC A, {0}"


class SUBCAHL(Instruction):
	"""SUBC A, [HL]."""

	mnemonic: ClassVar[str] = "SUBC A, [HL]"
	match: ClassVar[int] = 0b00111111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "SUBC A, [HL]"


class SUBCAHLbyte(Instruction):
	"""SUBC A, [HL + byte]."""

	mnemonic: ClassVar[str] = "SUBC A, [HL + byte]"
	match: ClassVar[int] = 0b00111001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "SUBC A, [HL + {0}]"


class SUBCAHLB(Instruction):
	"""SUBC A, [HL + B]."""

	mnemonic: ClassVar[str] = "SUBC A, [HL + B]"
	match: ClassVar[int] = 0b00110001_00111011
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "SUBC A, [HL + B]"


class SUBCAHLC(Instruction):
	"""SUBC A, [HL + C]."""

	mnemonic: ClassVar[str] = "SUBC A, [HL + C]"
	match: ClassVar[int] = 0b00110001_00111010
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "SUBC A, [HL + C]"


class ANDAbyte(Instruction):
	"""AND A, #byte."""

	mnemonic: ClassVar[str] = "AND A, #byte"
	match: ClassVar[int] = 0b01011101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "AND A, {0}"


class ANDsaddrbyte(Instruction):
	"""AND saddr, #byte."""

	mnemonic: ClassVar[str] = "AND saddr, #byte"
	match: ClassVar[int] = 0b11011000_00000000_00000000
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
	match: ClassVar[int] = 0b01100001_01011000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "AND A, {0}"

	def _check_fields(self) -> bool:
		"""Check that r is not A."""
		r = self.operands[self.field_defs[0]].val
		if r == Reg8.A:
			return False
		else:
			return True


class ANDrA(Instruction):
	"""AND r, A."""

	mnemonic: ClassVar[str] = "AND r, A"
	match: ClassVar[int] = 0b01100001_01010000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "AND {0}, A"


class ANDAsaddr(Instruction):
	"""AND A, saddr."""

	mnemonic: ClassVar[str] = "AND A, saddr"
	match: ClassVar[int] = 0b01011110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "AND A, {0}"


class ANDAaddr(Instruction):
	"""AND A, !addr16."""

	mnemonic: ClassVar[str] = "AND A, !addr16"
	match: ClassVar[int] = 0b01011000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "AND A, {0}"


class ANDAHL(Instruction):
	"""AND A, [HL]."""

	mnemonic: ClassVar[str] = "AND A, [HL]"
	match: ClassVar[int] = 0b01011111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "AND A, [HL]"


class ANDAHLbyte(Instruction):
	"""AND A, [HL + byte]."""

	mnemonic: ClassVar[str] = "AND A, [HL + byte]"
	match: ClassVar[int] = 0b01011001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "AND A, [HL + {0}]"


class ANDAHLB(Instruction):
	"""AND A, [HL + B]."""

	mnemonic: ClassVar[str] = "AND A, [HL + B]"
	match: ClassVar[int] = 0b00110001_01011011
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "AND A, [HL + B]"


class ANDAHLC(Instruction):
	"""AND A, [HL + C]."""

	mnemonic: ClassVar[str] = "AND A, [HL + C]"
	match: ClassVar[int] = 0b00110001_01011010
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "AND A, [HL + C]"


class ORAbyte(Instruction):
	"""OR A, #byte."""

	mnemonic: ClassVar[str] = "OR A, #byte"
	match: ClassVar[int] = 0b01101101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "OR A, {0}"


class ORsaddrbyte(Instruction):
	"""OR saddr, #byte."""

	mnemonic: ClassVar[str] = "OR saddr, #byte"
	match: ClassVar[int] = 0b11101000_00000000_00000000
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
	match: ClassVar[int] = 0b01100001_01101000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "OR A, {0}"

	def _check_fields(self) -> bool:
		"""Check that r is not A."""
		r = self.operands[self.field_defs[0]].val
		if r == Reg8.A:
			return False
		else:
			return True


class ORrA(Instruction):
	"""OR r, A."""

	mnemonic: ClassVar[str] = "OR r, A"
	match: ClassVar[int] = 0b01100001_01100000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "OR {0}, A"


class ORAsaddr(Instruction):
	"""OR A, saddr."""

	mnemonic: ClassVar[str] = "OR A, saddr"
	match: ClassVar[int] = 0b01101110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "OR A, {0}"


class ORAaddr(Instruction):
	"""OR A, !addr16."""

	mnemonic: ClassVar[str] = "OR A, !addr16"
	match: ClassVar[int] = 0b01101000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "OR A, {0}"


class ORAHL(Instruction):
	"""OR A, [HL]."""

	mnemonic: ClassVar[str] = "OR A, [HL]"
	match: ClassVar[int] = 0b01101111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "OR A, [HL]"


class ORAHLbyte(Instruction):
	"""OR A, [HL + byte]."""

	mnemonic: ClassVar[str] = "OR A, [HL + byte]"
	match: ClassVar[int] = 0b01101001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "OR A, [HL + {0}]"


class ORAHLB(Instruction):
	"""OR A, [HL + B]."""

	mnemonic: ClassVar[str] = "OR A, [HL + B]"
	match: ClassVar[int] = 0b00110001_01101011
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "OR A, [HL + B]"


class ORAHLC(Instruction):
	"""OR A, [HL + C]."""

	mnemonic: ClassVar[str] = "OR A, [HL + C]"
	match: ClassVar[int] = 0b00110001_01101010
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "OR A, [HL + C]"


class XORAbyte(Instruction):
	"""XOR A, #byte."""

	mnemonic: ClassVar[str] = "XOR A, #byte"
	match: ClassVar[int] = 0b01111101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "XOR A, {0}"


class XORsaddrbyte(Instruction):
	"""XOR saddr, #byte."""

	mnemonic: ClassVar[str] = "XOR saddr, #byte"
	match: ClassVar[int] = 0b11111000_00000000_00000000
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
	match: ClassVar[int] = 0b01100001_01111000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "XOR A, {0}"

	def _check_fields(self) -> bool:
		"""Check that r is not A."""
		r = self.operands[self.field_defs[0]].val
		if r == Reg8.A:
			return False
		else:
			return True


class XORrA(Instruction):
	"""XOR r, A."""

	mnemonic: ClassVar[str] = "XOR r, A"
	match: ClassVar[int] = 0b01100001_01110000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "XOR {0}, A"


class XORAsaddr(Instruction):
	"""XOR A, saddr."""

	mnemonic: ClassVar[str] = "XOR A, saddr"
	match: ClassVar[int] = 0b01111110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "XOR A, {0}"


class XORAaddr(Instruction):
	"""XOR A, !addr16."""

	mnemonic: ClassVar[str] = "XOR A, !addr16"
	match: ClassVar[int] = 0b01111000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "XOR A, {0}"


class XORAHL(Instruction):
	"""XOR A, [HL]."""

	mnemonic: ClassVar[str] = "XOR A, [HL]"
	match: ClassVar[int] = 0b01111111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XOR A, [HL]"


class XORAHLbyte(Instruction):
	"""XOR A, [HL + byte]."""

	mnemonic: ClassVar[str] = "XOR A, [HL + byte]"
	match: ClassVar[int] = 0b01111001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "XOR A, [HL + {0}]"


class XORAHLB(Instruction):
	"""XOR A, [HL + B]."""

	mnemonic: ClassVar[str] = "XOR A, [HL + B]"
	match: ClassVar[int] = 0b00110001_01111011
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XOR A, [HL + B]"


class XORAHLC(Instruction):
	"""XOR A, [HL + C]."""

	mnemonic: ClassVar[str] = "XOR A, [HL + C]"
	match: ClassVar[int] = 0b00110001_01111010
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "XOR A, [HL + C]"


class CMPAbyte(Instruction):
	"""CMP A, #byte."""

	mnemonic: ClassVar[str] = "CMP A, #byte"
	match: ClassVar[int] = 0b01001101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "CMP A, {0}"


class CMPsaddrbyte(Instruction):
	"""CMP saddr, #byte."""

	mnemonic: ClassVar[str] = "CMP saddr, #byte"
	match: ClassVar[int] = 0b11001000_00000000_00000000
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
	match: ClassVar[int] = 0b01100001_01001000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "CMP A, {0}"

	def _check_fields(self) -> bool:
		"""Check that r is not A."""
		r = self.operands[self.field_defs[0]].val
		if r == Reg8.A:
			return False
		else:
			return True


class CMPrA(Instruction):
	"""CMP r, A."""

	mnemonic: ClassVar[str] = "CMP r, A"
	match: ClassVar[int] = 0b01100001_01000000
	mmask: ClassVar[int] = 0b11111111_11111000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "CMP {0}, A"


class CMPAsaddr(Instruction):
	"""CMP A, saddr."""

	mnemonic: ClassVar[str] = "CMP A, saddr"
	match: ClassVar[int] = 0b01001110_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "CMP A, {0}"


class CMPAaddr(Instruction):
	"""CMP A, !addr16."""

	mnemonic: ClassVar[str] = "CMP A, !addr16"
	match: ClassVar[int] = 0b01001000_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Addr16(offset=0),)
	format: ClassVar[str] = "CMP A, {0}"


class CMPAHL(Instruction):
	"""CMP A, [HL]."""

	mnemonic: ClassVar[str] = "CMP A, [HL]"
	match: ClassVar[int] = 0b01001111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "CMP A, [HL]"


class CMPAHLbyte(Instruction):
	"""CMP A, [HL + byte]."""

	mnemonic: ClassVar[str] = "CMP A, [HL + byte]"
	match: ClassVar[int] = 0b01001001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm8(offset=0),)
	format: ClassVar[str] = "CMP A, [HL + {0}]"


class CMPAHLB(Instruction):
	"""CMP A, [HL + B]."""

	mnemonic: ClassVar[str] = "CMP A, [HL + B]"
	match: ClassVar[int] = 0b00110001_01001011
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "CMP A, [HL + B]"


class CMPAHLC(Instruction):
	"""CMP A, [HL + C]."""

	mnemonic: ClassVar[str] = "CMP A, [HL + C]"
	match: ClassVar[int] = 0b00110001_01001010
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "CMP A, [HL + C]"


class ADDWAXword(Instruction):
	"""ADDW AX, #word."""

	mnemonic: ClassVar[str] = "ADDW AX, #word"
	match: ClassVar[int] = 0b11001010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm16(offset=0),)
	format: ClassVar[str] = "ADDW AX, {0}"


class SUBWAXword(Instruction):
	"""SUBW AX, #word."""

	mnemonic: ClassVar[str] = "SUBW AX, #word"
	match: ClassVar[int] = 0b11011010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm16(offset=0),)
	format: ClassVar[str] = "SUBW AX, {0}"


class CMPWAXword(Instruction):
	"""CMPW AX, #word."""

	mnemonic: ClassVar[str] = "CMPW AX, #word"
	match: ClassVar[int] = 0b11101010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm16(offset=0),)
	format: ClassVar[str] = "CMPW AX, {0}"


class MULUX(Instruction):
	"""MULU X."""

	mnemonic: ClassVar[str] = "MULU X"
	match: ClassVar[int] = 0b00110001_10001000
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MULU X"


class DIVUWC(Instruction):
	"""DIVUW C."""

	mnemonic: ClassVar[str] = "DIVUW C"
	match: ClassVar[int] = 0b00110001_10000010
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "DIVUW C"


class INCr(Instruction):
	"""INC r."""

	mnemonic: ClassVar[str] = "INC r"
	match: ClassVar[int] = 0b01000000
	mmask: ClassVar[int] = 0b11111000
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "INC {0}"


class INCsaddr(Instruction):
	"""INC saddr."""

	mnemonic: ClassVar[str] = "INC saddr"
	match: ClassVar[int] = 0b10000001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "INC {0}"


class DECr(Instruction):
	"""DEC r."""

	mnemonic: ClassVar[str] = "DEC r"
	match: ClassVar[int] = 0b01010000
	mmask: ClassVar[int] = 0b11111000
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg8(offset=0),)
	format: ClassVar[str] = "DEC {0}"


class DECsaddr(Instruction):
	"""DEC saddr."""

	mnemonic: ClassVar[str] = "DEC saddr"
	match: ClassVar[int] = 0b10010001_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.SAddr(offset=0),)
	format: ClassVar[str] = "DEC {0}"


class INCWrp(Instruction):
	"""INCW rp."""

	mnemonic: ClassVar[str] = "INCW rp"
	match: ClassVar[int] = 0b10000000
	mmask: ClassVar[int] = 0b11111001
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=1),)
	format: ClassVar[str] = "INCW {0}"


class DECWrp(Instruction):
	"""DECW rp."""

	mnemonic: ClassVar[str] = "DECW rp"
	match: ClassVar[int] = 0b10010000
	mmask: ClassVar[int] = 0b11111001
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=1),)
	format: ClassVar[str] = "DECW {0}"


class RORA1(Instruction):
	"""ROR A, 1."""

	mnemonic: ClassVar[str] = "ROR A, 1"
	match: ClassVar[int] = 0b00100100
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ROR A, 1"


class ROLA1(Instruction):
	"""ROL A, 1."""

	mnemonic: ClassVar[str] = "ROL A, 1"
	match: ClassVar[int] = 0b00100110
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ROL A, 1"


class RORCA1(Instruction):
	"""RORC A, 1."""

	mnemonic: ClassVar[str] = "RORC A, 1"
	match: ClassVar[int] = 0b00100101
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "RORC A, 1"


class ROLCA1(Instruction):
	"""ROLC A, 1."""

	mnemonic: ClassVar[str] = "ROLC A, 1"
	match: ClassVar[int] = 0b00100111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ROLC A, 1"


class ROR4HL(Instruction):
	"""ROR4 [HL]."""

	mnemonic: ClassVar[str] = "ROR4 [HL]"
	match: ClassVar[int] = 0b00110001_10010000
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ROR4 [HL]"


class ROL4HL(Instruction):
	"""ROL4 [HL]."""

	mnemonic: ClassVar[str] = "ROL4 [HL]"
	match: ClassVar[int] = 0b00110001_10000000
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ROL4 [HL]"


class ADJBA(Instruction):
	"""ADJBA."""

	mnemonic: ClassVar[str] = "ADJBA"
	match: ClassVar[int] = 0b01100001_10010000
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ADJBA"


class ADJBS(Instruction):
	"""ADJBS."""

	mnemonic: ClassVar[str] = "ADJBS"
	match: ClassVar[int] = 0b01100001_10010000
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "ADJBS"


class MOV1saddrbitCY(Instruction):
	"""MOV1 saddr.bit, CY."""

	mnemonic: ClassVar[str] = "MOV1 saddr.bit, CY"
	match: ClassVar[int] = 0b01110001_00000100_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "MOV1 {0}{1}, CY"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class MOV1sfrbitCY(Instruction):
	"""MOV1 sfr.bit, CY."""

	mnemonic: ClassVar[str] = "MOV1 sfr.bit, CY"
	match: ClassVar[int] = 0b01110001_00001100_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "MOV1 {0}{1}, CY"


class MOV1AbitCY(Instruction):
	"""MOV1 A.bit, CY."""

	mnemonic: ClassVar[str] = "MOV1 A.bit, CY"
	match: ClassVar[int] = 0b01100001_10001100
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "MOV1 A{0}, CY"


class MOV1PSWbitCY(Instruction):
	"""MOV1 PSW.bit, CY."""

	mnemonic: ClassVar[str] = "MOV1 PSW.bit, CY"
	match: ClassVar[int] = 0b01110001_00000100_00011110
	mmask: ClassVar[int] = 0b11111111_10001111_11111111
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=12),)
	format: ClassVar[str] = "MOV1 PSW{0}, CY"


class MOV1HLbitCY(Instruction):
	"""MOV1 [HL].bit, CY."""

	mnemonic: ClassVar[str] = "MOV1 [HL].bit, CY"
	match: ClassVar[int] = 0b01110001_10000100
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "MOV1 [HL]{0}, CY"


class MOV1CYsaddrbit(Instruction):
	"""MOV1 CY, saddr.bit."""

	mnemonic: ClassVar[str] = "MOV1 CY, saddr.bit"
	match: ClassVar[int] = 0b01110001_00000001_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "MOV1 CY, {0}{1}"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class MOV1CYsfrbit(Instruction):
	"""MOV1 CY, sfr.bit."""

	mnemonic: ClassVar[str] = "MOV1 CY, sfr.bit"
	match: ClassVar[int] = 0b01110001_00001001_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "MOV1 CY, {0}{1}"


class MOV1CYAbit(Instruction):
	"""MOV1 CY, A.bit."""

	mnemonic: ClassVar[str] = "MOV1 CY, A.bit"
	match: ClassVar[int] = 0b01100001_10001001
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "MOV1 CY, A{0}"


class MOV1CYPSWbit(Instruction):
	"""MOV1 CY, PSW.bit."""

	mnemonic: ClassVar[str] = "MOV1 CY, PSW.bit"
	match: ClassVar[int] = 0b01110001_00000001_00011110
	mmask: ClassVar[int] = 0b11111111_10001111_11111111
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=12),)
	format: ClassVar[str] = "MOV1 CY, PSW{0}"


class MOV1CYHLbit(Instruction):
	"""MOV1 CY, [HL].bit."""

	mnemonic: ClassVar[str] = "MOV1 CY, [HL].bit"
	match: ClassVar[int] = 0b01110001_10000001
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "MOV1 CY, [HL]{0}"


class AND1CYsaddrbit(Instruction):
	"""AND1 CY, saddr.bit."""

	mnemonic: ClassVar[str] = "AND1 CY, saddr.bit"
	match: ClassVar[int] = 0b01110001_00000101_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "AND1 CY, {0}{1}"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class AND1CYsfrbit(Instruction):
	"""AND1 CY, sfr.bit."""

	mnemonic: ClassVar[str] = "AND1 CY, sfr.bit"
	match: ClassVar[int] = 0b01110001_00001101_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "AND1 CY, {0}{1}"


class AND1CYAbit(Instruction):
	"""AND1 CY, A.bit."""

	mnemonic: ClassVar[str] = "AND1 CY, A.bit"
	match: ClassVar[int] = 0b01100001_10001101
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "AND1 CY, A{0}"


class AND1CYPSWbit(Instruction):
	"""AND1 CY, PSW.bit."""

	mnemonic: ClassVar[str] = "AND1 CY, PSW.bit"
	match: ClassVar[int] = 0b01110001_00000101_00011110
	mmask: ClassVar[int] = 0b11111111_10001111_11111111
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=12),)
	format: ClassVar[str] = "AND1 CY, PSW{0}"


class AND1CYHLbit(Instruction):
	"""AND1 CY, [HL].bit."""

	mnemonic: ClassVar[str] = "AND1 CY, [HL].bit"
	match: ClassVar[int] = 0b01110001_10000101
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "AND1 CY, [HL]{0}"


class OR1CYsaddrbit(Instruction):
	"""OR1 CY, saddr.bit."""

	mnemonic: ClassVar[str] = "OR1 CY, saddr.bit"
	match: ClassVar[int] = 0b01110001_00000110_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "OR1 CY, {0}{1}"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class OR1CYsfrbit(Instruction):
	"""OR1 CY, sfr.bit."""

	mnemonic: ClassVar[str] = "OR1 CY, sfr.bit"
	match: ClassVar[int] = 0b01110001_00001110_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "OR1 CY, {0}{1}"


class OR1CYAbit(Instruction):
	"""OR1 CY, A.bit."""

	mnemonic: ClassVar[str] = "OR1 CY, A.bit"
	match: ClassVar[int] = 0b01100001_10001110
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "OR1 CY, A{0}"


class OR1CYPSWbit(Instruction):
	"""OR1 CY, PSW.bit."""

	mnemonic: ClassVar[str] = "OR1 CY, PSW.bit"
	match: ClassVar[int] = 0b01110001_00000110_00011110
	mmask: ClassVar[int] = 0b11111111_10001111_11111111
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=12),)
	format: ClassVar[str] = "OR1 CY, PSW{0}"


class OR1CYHLbit(Instruction):
	"""OR1 CY, [HL].bit."""

	mnemonic: ClassVar[str] = "OR1 CY, [HL].bit"
	match: ClassVar[int] = 0b01110001_10000110
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "OR1 CY, [HL]{0}"


class XOR1CYsaddrbit(Instruction):
	"""XOR1 CY, saddr.bit."""

	mnemonic: ClassVar[str] = "XOR1 CY, saddr.bit"
	match: ClassVar[int] = 0b01110001_00000111_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "XOR1 CY, {0}{1}"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class XOR1CYsfrbit(Instruction):
	"""XOR1 CY, sfr.bit."""

	mnemonic: ClassVar[str] = "XOR1 CY, sfr.bit"
	match: ClassVar[int] = 0b01110001_00001111_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "XOR1 CY, {0}{1}"


class XOR1CYAbit(Instruction):
	"""XOR1 CY, A.bit."""

	mnemonic: ClassVar[str] = "XOR1 CY, A.bit"
	match: ClassVar[int] = 0b01100001_10001111
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "XOR1 CY, A{0}"


class XOR1CYPSWbit(Instruction):
	"""XOR1 CY, PSW.bit."""

	mnemonic: ClassVar[str] = "XOR1 CY, PSW.bit"
	match: ClassVar[int] = 0b01110001_00000111_00011110
	mmask: ClassVar[int] = 0b11111111_10001111_11111111
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=12),)
	format: ClassVar[str] = "XOR1 CY, PSW{0}"


class XOR1CYHLbit(Instruction):
	"""XOR1 CY, [HL].bit."""

	mnemonic: ClassVar[str] = "XOR1 CY, [HL].bit"
	match: ClassVar[int] = 0b01110001_10000111
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "XOR1 CY, [HL]{0}"


class SET1saddrbit(Instruction):
	"""SET1 saddr.bit."""

	mnemonic: ClassVar[str] = "SET1 saddr.bit"
	match: ClassVar[int] = 0b00001010_00000000
	mmask: ClassVar[int] = 0b10001111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "SET1 {0}{1}"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class SET1sfrbit(Instruction):
	"""SET1 sfr.bit."""

	mnemonic: ClassVar[str] = "SET1 sfr.bit"
	match: ClassVar[int] = 0b01110001_00001010_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "SET1 {0}{1}"


class SET1Abit(Instruction):
	"""SET1 A.bit."""

	mnemonic: ClassVar[str] = "SET1 A.bit"
	match: ClassVar[int] = 0b01100001_10001010
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "SET1 A{0}"


class SET1PSWbit(Instruction):
	"""SET1 PSW.bit."""

	mnemonic: ClassVar[str] = "SET1 PSW.bit"
	match: ClassVar[int] = 0b00001010_00011110
	mmask: ClassVar[int] = 0b10001111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=12),)
	format: ClassVar[str] = "SET1 PSW{0}"

	def _check_fields(self) -> bool:
		"""Check that bit is not 7 (IE)."""
		bit = self.operands[self.field_defs[0]].val
		if bit == 7:
			return False
		else:
			return True


class SET1HLbit(Instruction):
	"""SET1 [HL].bit."""

	mnemonic: ClassVar[str] = "SET1 [HL].bit"
	match: ClassVar[int] = 0b01110001_10000010
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "SET1 [HL]{0}"


class CLR1saddrbit(Instruction):
	"""CLR1 saddr.bit."""

	mnemonic: ClassVar[str] = "CLR1 saddr.bit"
	match: ClassVar[int] = 0b00001011_00000000
	mmask: ClassVar[int] = 0b10001111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "CLR1 {0}{1}"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class CLR1sfrbit(Instruction):
	"""CLR1 sfr.bit."""

	mnemonic: ClassVar[str] = "CLR1 sfr.bit"
	match: ClassVar[int] = 0b01110001_00001011_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=0),
		field.BitIdx3(offset=12),
	)
	format: ClassVar[str] = "CLR1 {0}{1}"


class CLR1Abit(Instruction):
	"""CLR1 A.bit."""

	mnemonic: ClassVar[str] = "CLR1 A.bit"
	match: ClassVar[int] = 0b01100001_10001011
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "CLR1 A{0}"


class CLR1PSWbit(Instruction):
	"""CLR1 PSW.bit."""

	mnemonic: ClassVar[str] = "CLR1 PSW.bit"
	match: ClassVar[int] = 0b00001011_00011110
	mmask: ClassVar[int] = 0b10001111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=12),)
	format: ClassVar[str] = "CLR1 PSW{0}"

	def _check_fields(self) -> bool:
		"""Check that bit is not 7 (IE)."""
		bit = self.operands[self.field_defs[0]].val
		if bit == 7:
			return False
		else:
			return True


class CLR1HLbit(Instruction):
	"""CLR1 [HL].bit."""

	mnemonic: ClassVar[str] = "CLR1 [HL].bit"
	match: ClassVar[int] = 0b01110001_10000011
	mmask: ClassVar[int] = 0b11111111_10001111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.BitIdx3(offset=4),)
	format: ClassVar[str] = "CLR1 [HL]{0}"


class SET1CY(Instruction):
	"""SET1 CY."""

	mnemonic: ClassVar[str] = "SET1 CY"
	match: ClassVar[int] = 0b00100000
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "SET1 CY"


class CLR1CY(Instruction):
	"""CLR1 CY."""

	mnemonic: ClassVar[str] = "CLR1 CY"
	match: ClassVar[int] = 0b00100001
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "CLR1 CY"


class NOT1CY(Instruction):
	"""NOT1 CY."""

	mnemonic: ClassVar[str] = "NOT1 CY"
	match: ClassVar[int] = 0b00000001
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "NOT1 CY"


class CALLaddr16(Instruction):
	"""CALL !addr16."""

	mnemonic: ClassVar[str] = "CALL !addr16"
	match: ClassVar[int] = 0b10011010_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddr16(offset=0),)
	flow: ClassVar[Flow] = CallReturn(branch_field_idx=0)
	format: ClassVar[str] = "CALL {0}"


class CALLFaddr11(Instruction):
	"""CALLF !addr11."""

	mnemonic: ClassVar[str] = "CALLF !addr11"
	match: ClassVar[int] = 0b00001100_00000000
	mmask: ClassVar[int] = 0b10001111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddr11(offsl=0, offsh=12),)
	flow: ClassVar[Flow] = CallReturn(branch_field_idx=0)
	format: ClassVar[str] = "CALLF {0}"


class CALLTaddr5(Instruction):
	"""CALLT [addr5]."""

	mnemonic: ClassVar[str] = "CALLT [addr5]"
	match: ClassVar[int] = 0b11000001
	mmask: ClassVar[int] = 0b11000001
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddr5(offset=1),)
	flow: ClassVar[Flow] = ComputedCallT(callt_idx_field_idx=0)
	format: ClassVar[str] = "CALLT {0}"


class BRK(Instruction):
	"""BRK."""

	mnemonic: ClassVar[str] = "BRK"
	match: ClassVar[int] = 0b10111111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	flow: ClassVar[Flow] = Return()
	format: ClassVar[str] = "BRK"


class RET(Instruction):
	"""RET."""

	mnemonic: ClassVar[str] = "RET"
	match: ClassVar[int] = 0b10101111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	flow: ClassVar[Flow] = Return()
	format: ClassVar[str] = "RET"


class RETB(Instruction):
	"""RETB."""

	mnemonic: ClassVar[str] = "RETB"
	match: ClassVar[int] = 0b10011111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	flow: ClassVar[Flow] = Return()
	format: ClassVar[str] = "RETB"


class RETI(Instruction):
	"""RETI."""

	mnemonic: ClassVar[str] = "RETI"
	match: ClassVar[int] = 0b10001111
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	flow: ClassVar[Flow] = Return()
	format: ClassVar[str] = "RETI"


class PUSHPSW(Instruction):
	"""PUSH PSW."""

	mnemonic: ClassVar[str] = "PUSH PSW"
	match: ClassVar[int] = 0b00100010
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "PUSH PSW"


class PUSHrp(Instruction):
	"""PUSH rp."""

	mnemonic: ClassVar[str] = "PUSH rp"
	match: ClassVar[int] = 0b10110001
	mmask: ClassVar[int] = 0b11111001
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=1),)
	format: ClassVar[str] = "PUSH {0}"


class POPPSW(Instruction):
	"""POP PSW."""

	mnemonic: ClassVar[str] = "POP PSW"
	match: ClassVar[int] = 0b00100011
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "POP PSW"


class POPrp(Instruction):
	"""POP rp."""

	mnemonic: ClassVar[str] = "POP rp"
	match: ClassVar[int] = 0b10110000
	mmask: ClassVar[int] = 0b11111001
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = (field.Reg16(offset=1),)
	format: ClassVar[str] = "POP {0}"


class MOVWSPword(Instruction):
	"""MOVW SP, #word."""

	mnemonic: ClassVar[str] = "MOVW SP, #word"
	match: ClassVar[int] = 0b11101110_00011100_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_11111111_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (field.Imm16(offset=0),)
	format: ClassVar[str] = "MOVW SP, {0}"


class MOVWSPAX(Instruction):
	"""MOVW SP, AX."""

	mnemonic: ClassVar[str] = "MOVW SP, AX"
	match: ClassVar[int] = 0b10011001_00011100
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOVW SP, AX"


class MOVWAXSP(Instruction):
	"""MOVW AX, SP."""

	mnemonic: ClassVar[str] = "MOVW AX, SP"
	match: ClassVar[int] = 0b10001001_00011100
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "MOVW AX, SP"


class BRaddr(Instruction):
	"""BR !addr16."""

	mnemonic: ClassVar[str] = "BR !addr16"
	match: ClassVar[int] = 0b10011011_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddr16(offset=0),)
	flow: ClassVar[Flow] = UnconditionalBranch(branch_field_idx=0)
	format: ClassVar[str] = "BR {0}"


class BRReladdr(Instruction):
	"""BR $addr16."""

	mnemonic: ClassVar[str] = "BR $addr16"
	match: ClassVar[int] = 0b11111010_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	flow: ClassVar[Flow] = UnconditionalBranch(branch_field_idx=0)
	format: ClassVar[str] = "BR {0}"


class BRAX(Instruction):
	"""BR AX."""

	mnemonic: ClassVar[str] = "BR AX"
	match: ClassVar[int] = 0b00110001_10011000
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	flow: ClassVar[Flow] = ComputedUnknown()
	format: ClassVar[str] = "BR AX"


class BCReladdr(Instruction):
	"""BC $addr16."""

	mnemonic: ClassVar[str] = "BC $addr16"
	match: ClassVar[int] = 0b10001101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=0)
	format: ClassVar[str] = "BC {0}"


class BNCReladdr(Instruction):
	"""BNC $addr16."""

	mnemonic: ClassVar[str] = "BNC $addr16"
	match: ClassVar[int] = 0b10011101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=0)
	format: ClassVar[str] = "BNC {0}"


class BZReladdr(Instruction):
	"""BZ $addr16."""

	mnemonic: ClassVar[str] = "BZ $addr16"
	match: ClassVar[int] = 0b10101101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=0)
	format: ClassVar[str] = "BZ {0}"


class BNZReladdr(Instruction):
	"""BNZ $addr16."""

	mnemonic: ClassVar[str] = "BNZ $addr16"
	match: ClassVar[int] = 0b10111101_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=0)
	format: ClassVar[str] = "BNZ {0}"


class BTsaddrbitReladdr(Instruction):
	"""BT saddr.bit, $addr16."""

	mnemonic: ClassVar[str] = "BT saddr.bit, $addr16"
	match: ClassVar[int] = 0b10001100_00000000_00000000
	mmask: ClassVar[int] = 0b10001111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.BitIdx3(offset=20),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=2)
	format: ClassVar[str] = "BT {0}{1}, {2}"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class BTsfrbitReladdr(Instruction):
	"""BT sfr.bit, $addr16."""

	mnemonic: ClassVar[str] = "BT sfr.bit, $addr16"
	match: ClassVar[int] = 0b00110001_00000110_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=8),
		field.BitIdx3(offset=20),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=2)
	format: ClassVar[str] = "BT {0}{1}, {2}"


class BTAbitReladdr(Instruction):
	"""BT A.bit, $addr16."""

	mnemonic: ClassVar[str] = "BT A.bit, $addr16"
	match: ClassVar[int] = 0b00110001_00001110_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=1)
	format: ClassVar[str] = "BT A{0}, {1}"


class BTPSWbitReladdr(Instruction):
	"""BT PSW.bit, $addr16."""

	mnemonic: ClassVar[str] = "BT PSW.bit, $addr16"
	match: ClassVar[int] = 0b10001100_00011110_00000000
	mmask: ClassVar[int] = 0b10001111_11111111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=20),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=1)
	format: ClassVar[str] = "BT PSW{0}, {1}"


class BTHLbitReladdr(Instruction):
	"""BT [HL].bit, $addr16."""

	mnemonic: ClassVar[str] = "BT [HL].bit, $addr16"
	match: ClassVar[int] = 0b00110001_10000110_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=1)
	format: ClassVar[str] = "BT [HL]{0}, {1}"


class BFsaddrbitReladdr(Instruction):
	"""BF saddr.bit, $addr16."""

	mnemonic: ClassVar[str] = "BF saddr.bit, $addr16"
	match: ClassVar[int] = 0b00110001_00000011_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.BitIdx3(offset=20),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=2)
	format: ClassVar[str] = "BF {0}{1}, {2}"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class BFsfrbitReladdr(Instruction):
	"""BF sfr.bit, $addr16."""

	mnemonic: ClassVar[str] = "BF sfr.bit, $addr16"
	match: ClassVar[int] = 0b00110001_00000111_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=8),
		field.BitIdx3(offset=20),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=2)
	format: ClassVar[str] = "BF {0}{1}, {2}"


class BFAbitReladdr(Instruction):
	"""BF A.bit, $addr16."""

	mnemonic: ClassVar[str] = "BF A.bit, $addr16"
	match: ClassVar[int] = 0b00110001_00001111_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=1)
	format: ClassVar[str] = "BF A{0}, {1}"


class BFPSWbitReladdr(Instruction):
	"""BF PSW.bit, $addr16."""

	mnemonic: ClassVar[str] = "BF PSW.bit, $addr16"
	match: ClassVar[int] = 0b00110001_00000011_00011110_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_11111111_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=20),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=1)
	format: ClassVar[str] = "BF PSW{0}, {1}"


class BFHLbitReladdr(Instruction):
	"""BF [HL].bit, $addr16."""

	mnemonic: ClassVar[str] = "BF [HL].bit, $addr16"
	match: ClassVar[int] = 0b00110001_10000111_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=1)
	format: ClassVar[str] = "BF [HL]{0}, {1}"


class BTCLRsaddrbitReladdr(Instruction):
	"""BTCLR saddr.bit, $addr16."""

	mnemonic: ClassVar[str] = "BTCLR saddr.bit, $addr16"
	match: ClassVar[int] = 0b00110001_00000001_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.BitIdx3(offset=20),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=2)
	format: ClassVar[str] = "BTCLR {0}{1}, {2}"

	def _check_fields(self) -> bool:
		"""Check that saddr is not PSW."""
		addr = self.operands[self.field_defs[0]].val
		if addr == PSW_MAGIC_ADDR:
			return False
		else:
			return True


class BTCLRsfrbitReladdr(Instruction):
	"""BTCLR sfr.bit, $addr16."""

	mnemonic: ClassVar[str] = "BTCLR sfr.bit, $addr16"
	match: ClassVar[int] = 0b00110001_00000101_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SFR(offset=8),
		field.BitIdx3(offset=20),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=2)
	format: ClassVar[str] = "BTCLR {0}{1}, {2}"


class BTCLRAbitReladdr(Instruction):
	"""BTCLR A.bit, $addr16."""

	mnemonic: ClassVar[str] = "BTCLR A.bit, $addr16"
	match: ClassVar[int] = 0b00110001_00001101_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=1)
	format: ClassVar[str] = "BTCLR A{0}, {1}"


class BTCLRPSWbitReladdr(Instruction):
	"""BTCLR PSW.bit, $addr16."""

	mnemonic: ClassVar[str] = "BTCLR PSW.bit, $addr16"
	match: ClassVar[int] = 0b00110001_00000001_00011110_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_11111111_00000000
	bytecount: ClassVar[int] = 4
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=20),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=1)
	format: ClassVar[str] = "BTCLR PSW{0}, {1}"


class BTCLRHLbitReladdr(Instruction):
	"""BTCLR [HL].bit, $addr16."""

	mnemonic: ClassVar[str] = "BTCLR [HL].bit, $addr16"
	match: ClassVar[int] = 0b00110001_10000101_00000000
	mmask: ClassVar[int] = 0b11111111_10001111_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.BitIdx3(offset=12),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=1)
	format: ClassVar[str] = "BTCLR [HL]{0}, {1}"


class DBNZBReladdr(Instruction):
	"""DBNZ B, $addr16."""

	mnemonic: ClassVar[str] = "DBNZ B, $addr16"
	match: ClassVar[int] = 0b10001011_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=0)
	format: ClassVar[str] = "DBNZ B, {0}"


class DBNZCReladdr(Instruction):
	"""DBNZ C, $addr16."""

	mnemonic: ClassVar[str] = "DBNZ C, $addr16"
	match: ClassVar[int] = 0b10001010_00000000
	mmask: ClassVar[int] = 0b11111111_00000000
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.JAddrRel(offset=0),)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=0)
	format: ClassVar[str] = "DBNZ C, {0}"


class DBNZsaddrReladdr(Instruction):
	"""DBNZ saddr, $addr16."""

	mnemonic: ClassVar[str] = "DBNZ saddr, $addr16"
	match: ClassVar[int] = 0b00000100_00000000_00000000
	mmask: ClassVar[int] = 0b11111111_00000000_00000000
	bytecount: ClassVar[int] = 3
	field_defs: ClassVar[Sequence["Field"]] = (
		field.SAddr(offset=8),
		field.JAddrRel(offset=0),
	)
	flow: ClassVar[Flow] = ConditionalBranch(branch_field_idx=1)
	format: ClassVar[str] = "DBNZ {0}, {1}"


class SEL(Instruction):
	"""SEL RBn."""

	mnemonic: ClassVar[str] = "SEL RBn"
	match: ClassVar[int] = 0b01100001_11011000
	mmask: ClassVar[int] = 0b11111111_11010111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = (field.RB2(offsl=3, offsh=5),)
	format: ClassVar[str] = "SEL {0}"


class NOP(Instruction):
	"""NOP."""

	mnemonic: ClassVar[str] = "NOP"
	match: ClassVar[int] = 0b00000000
	mmask: ClassVar[int] = 0b11111111
	bytecount: ClassVar[int] = 1
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "NOP"


class EI(Instruction):
	"""EI."""

	mnemonic: ClassVar[str] = "EI"
	match: ClassVar[int] = 0b01111010_00011110
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "EI"


class DI(Instruction):
	"""DI."""

	mnemonic: ClassVar[str] = "DI"
	match: ClassVar[int] = 0b01111011_00011110
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "DI"


class HALT(Instruction):
	"""HALT."""

	mnemonic: ClassVar[str] = "HALT"
	match: ClassVar[int] = 0b01110001_00010000
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "HALT"


class STOP(Instruction):
	"""STOP."""

	mnemonic: ClassVar[str] = "STOP"
	match: ClassVar[int] = 0b01110001_00000000
	mmask: ClassVar[int] = 0b11111111_11111111
	bytecount: ClassVar[int] = 2
	field_defs: ClassVar[Sequence["Field"]] = tuple()
	format: ClassVar[str] = "STOP"
