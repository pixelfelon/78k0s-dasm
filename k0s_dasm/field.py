"""Concrete instruction field types."""

from dataclasses import dataclass
from typing import ClassVar

from k0s_dasm.base import Field, Operand
from k0s_dasm.defs import UPD78F9202_SFR
from k0s_dasm.defs import Reg8 as _EnumReg8
from k0s_dasm.defs import Reg16 as _EnumReg16
from k0s_dasm.ibase import Instruction


@dataclass(frozen=True)
class _Short(Field):
	"""N-bit unaligned field."""

	offset: int
	bits: ClassVar[int] = NotImplemented

	def from_inst_word(self, instr_word: int, inst: "Instruction", /) -> "Operand":
		"""Load field word from instruction word."""
		mask = (2**self.bits) - 1
		fword = (instr_word >> self.offset) & mask
		return Operand(fdef=self, inst=inst, val=fword)


@dataclass(frozen=True)
class Imm8(_Short):
	"""8-bit unaligned field for data byte."""

	bits: ClassVar[int] = 8

	def render(self, val: int, inst: "Instruction", /) -> str:
		"""Style immediate value (byte) operand."""
		return f"#{val:02X}H"


@dataclass(frozen=True)
class SFR(_Short):
	"""
	8-bit unaligned field for SFR address.

	The converted address is 16-bit absolute.
	"""

	bits: ClassVar[int] = 8

	def from_inst_word(self, instr_word: int, inst: "Instruction", /) -> "Operand":
		"""Load field word from instruction word."""
		operand = super().from_inst_word(instr_word, inst)
		operand.val += 0xFF00
		return operand

	def render(self, val: int, inst: "Instruction", /) -> str:
		"""Style SFR address (sfr) operand."""
		# TODO: not assume which processor
		if val in UPD78F9202_SFR:
			return UPD78F9202_SFR[val]
		else:
			return f"SFR_{val:04X}H?"


@dataclass(frozen=True)
class SAddr(_Short):
	"""
	8-bit unaligned field for short address (saddr/saddrp).

	The converted address is 16-bit absolute.
	"""

	bits: ClassVar[int] = 8

	def from_inst_word(self, instr_word: int, inst: "Instruction", /) -> "Operand":
		"""Load field word from instruction word."""
		operand = super().from_inst_word(instr_word, inst)
		if operand.val < 0x20:
			operand.val += 0xFF00
		else:
			operand.val += 0xFE00
		return operand

	def render(self, val: int, inst: "Instruction", /) -> str:
		"""Style short address (saddr) operand."""
		return f"{val:04X}H"


@dataclass(frozen=True)
class JAddrRel(_Short):
	"""8-bit unaligned field for PC-relative address (jdisp)."""

	bits: ClassVar[int] = 8
	is_branch: ClassVar[bool] = True  # actually true for all such instructions.

	def from_inst_word(self, instr_word: int, inst: "Instruction", /) -> "Operand":
		"""Load field word from instruction word."""
		operand = super().from_inst_word(instr_word, inst)
		pc_next = inst.pc + inst.bytecount
		if operand.val > 0x80:
			# jdisp is guaranteed 8-bit signed, so manually do two's complement
			operand.val -= 0x100
		operand.val += pc_next
		return operand

	def render(self, val: int, inst: "Instruction", /) -> str:
		"""Style PC-relative address (jdisp) operand."""
		return f"${val:04X}H"


@dataclass(frozen=True)
class Addr5(_Short):
	"""5-bit unaligned field for call table index."""

	bits: ClassVar[int] = 5
	# is_branch??? Sort of, but call table isn't const, and should be
	# analyzed separately.

	def from_inst_word(self, instr_word: int, inst: "Instruction", /) -> "Operand":
		"""Load field word from instruction word."""
		operand = super().from_inst_word(instr_word, inst)
		operand.val = 0x40 + (operand.val << 1)
		return operand

	def render(self, val: int, inst: "Instruction", /) -> str:
		"""Style CALLT address (addr5) operand."""
		return f"[{val:02X}H]"


@dataclass(frozen=True)
class Reg8(_Short):
	"""3-bit unaligned field for 8-bit (unpaired) register index."""

	bits: ClassVar[int] = 3

	def render(self, val: int, inst: "Instruction", /) -> str:
		"""Style 8-bit register (r) operand."""
		try:
			val = _EnumReg8(val)
		except ValueError:
			return f"?{val}?"
		else:
			return val.name


@dataclass(frozen=True)
class Reg16(_Short):
	"""2-bit unaligned field for 16-bit (paired) register index."""

	bits: ClassVar[int] = 2

	def render(self, val: int, inst: "Instruction", /) -> str:
		"""Style 16-bit register (rp) operand."""
		try:
			val = _EnumReg16(val)
		except ValueError:
			return f"?{val}?"
		else:
			return val.name


@dataclass(frozen=True)
class BitIdx3(_Short):
	"""3-bit unaligned field bit index within byte."""

	bits: ClassVar[int] = 3


@dataclass(frozen=True)
class _Wide(Field):
	"""Two-byte big-endian byte-aligned field."""

	offset: int = 0  # always, afaict

	def __post_init__(self) -> None:
		assert self.offset % 8 == 0

	def from_inst_word(self, instr_word: int, inst: "Instruction", /) -> "Operand":
		"""Load field word from instruction word."""
		offset = self.offset
		byte_h = (instr_word >> offset) & 0xFF
		byte_l = (instr_word >> (offset + 8)) & 0xFF
		fword = byte_l | (byte_h << 8)
		return Operand(fdef=self, inst=inst, val=fword)


@dataclass(frozen=True)
class Imm16(_Wide):
	"""16-bit byte-aligned field for data word."""

	def render(self, val: int, inst: "Instruction", /) -> str:
		"""Style immediate value (word) operand."""
		return f"#{val:04X}H"


@dataclass(frozen=True)
class Addr16(_Wide):
	"""16-bit byte-aligned field for absolute DATA address."""

	def render(self, val: int, inst: "Instruction", /) -> str:
		"""Style absolute address (addr16) operand."""
		return f"!{val:04X}H"


@dataclass(frozen=True)
class JAddr16(_Wide):
	"""16-bit byte-aligned field for absolute BRANCH address."""

	is_branch: ClassVar[bool] = True

	def render(self, val: int, inst: "Instruction", /) -> str:
		"""Style absolute address (addr16) operand."""
		return f"!{val:04X}H"
