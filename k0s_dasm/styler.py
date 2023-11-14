"""Methods to render a single integer argument value to a string."""

from enum import IntEnum
from typing import TYPE_CHECKING, Protocol, Type

from k0s_dasm.defs import UPD78F9202_SFR, Reg8, Reg16

if TYPE_CHECKING:
	from k0s_dasm.ibase import Instruction


class Styler(Protocol):
	"""Callable to style argument value."""

	def __call__(self, val: int, inst: "Instruction", /) -> str:
		"""
		Style value according to self-contained rules, and instruction context.

		The implementer may assume that ``val`` is positive.
		"""
		...


class _StylerEnum:
	"""Styler for enum-based values."""

	def __init__(self, t: Type[IntEnum]) -> None:
		self._t = t

	def __call__(self, val: int, _: "Instruction", /) -> str:
		"""Style value per enum tag."""
		try:
			val = self._t(val)
		except ValueError:
			return f"?{val}?"
		else:
			return val.name


def default(val: int, _: "Instruction", /) -> str:
	"""Style integer in most neutral way."""
	return str(val)


def imm8(val: int, _: "Instruction", /) -> str:
	"""Style immediate value (byte) operand."""
	return f"#{val:02X}H"


def imm16(val: int, _: "Instruction", /) -> str:
	"""Style immediate value (word) operand."""
	return f"#{val:04X}H"


def addr_abs(val: int, _: "Instruction", /) -> str:
	"""Style absolute address (addr16) operand."""
	return f"!{val:04X}H"


def addr_pcrel(val: int, inst: "Instruction", /) -> str:
	"""Style PC-relative address (jdisp) operand."""
	pc_next = inst.pc + inst.bytecount
	if val > 0x80:
		# jdisp is guaranteed 8-bit signed, so manually do two's complement
		val = val - 0x100
	pc_jdisp = pc_next + val
	return f"${pc_jdisp:04X}H"


def addr_callt(val: int, _: "Instruction", /) -> str:
	"""Style CALLT address (addr5) operand."""
	return f"[{val:02X}H]"


def addr_short(val: int, _: "Instruction", /) -> str:
	"""Style absolute address (addr16) operand."""
	if val < 0x20:
		return f"FF{val:02X}H"
	else:
		return f"FE{val:02X}H"


def addr_sfr(val: int, _: "Instruction", /) -> str:
	"""Style SFR address (sfr) operand."""
	# TODO: not assume which processor
	addr = 0xFF00 + val
	if addr in UPD78F9202_SFR:
		return UPD78F9202_SFR[addr]
	else:
		return f"SFR_FF{val:02X}H?"


reg8 = _StylerEnum(Reg8)
reg16 = _StylerEnum(Reg16)
