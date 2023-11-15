"""
Program/instruction data base types.

Other than Instruction, anyways. There were some circular dependencies.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, ClassVar, Sequence

if TYPE_CHECKING:
	from k0s_dasm.ibase import Instruction


@dataclass
class Program:
	"""Assembly program and other flash contents."""

	flash: bytearray
	"""The full flash data."""

	pc: int = 0
	"""A program counter mainly used during analysis."""

	instrs: dict[int, "Instruction"] = field(default_factory=dict)
	"""
	Instructions found in the program. Keys are absolute addresses.

	No particular order or contiguity.
	"""

	labels: dict[int, str] = field(default_factory=dict)
	"""Labels found in the program. Keys are absolute addresses."""


@dataclass(frozen=True)
class Field:
	"""Abstract base field."""

	name: str
	"""A short name for this field; should match the mnemonic."""

	is_branch: ClassVar[bool] = False
	"""True iff the value is an absolute address that may be jumped to."""

	def from_inst_word(self, instr_word: int, inst: "Instruction", /) -> "Operand":
		"""Load field word from instruction word."""
		raise NotImplementedError

	# noinspection PyMethodMayBeStatic
	def render(self, val: int, inst: "Instruction", /) -> str:
		"""Render the value based on the type of the field."""
		# Neutral default.
		return str(val)


@dataclass
class Operand:
	"""Instruction operand, i.e. unique instantiation of a specific field."""

	fdef: Field
	"""The relevant field definition."""

	inst: "Instruction"
	"""The specific instruction this field belongs to."""

	val: int
	"""
	The user-preferred form of the operand value.

	This may not be the actual value encoded in the opcode, e.g. for PC-relative
	or short addresses. If the value displayed in the assembly mnemonic is
	numeric, this must be that value, especially that any address values will
	be stored and shown as absolute. Enums are less defined.
	"""

	def render(self) -> str:
		"""Render own value based on the field definition."""
		return self.fdef.render(self.val, self.inst)


class Flow:
	"""Instruction flow provider."""

	def next(self, inst: "Instruction", /) -> Sequence[int]:
		"""
		Get the address(es) of the next instruction(s).

		If guessing a computed address, it would be prudent to add a note to
		the Instruction object.
		"""
		raise NotImplementedError
