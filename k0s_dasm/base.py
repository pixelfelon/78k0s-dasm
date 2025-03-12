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

	branches: dict[int, int] = field(default_factory=dict)
	"""
	Branches found in the program. Key is source, value is dest.

	This is branches caused as an explicit effect of any instruction, but not
	those caused by simple forward flow.

	No instruction in 78K0 has multiple destinations, other than forward flow
	for conditionals, but we're ignoring that for this field.
	"""

	def flash_word(self, addr: int) -> int:
		"""Read 16-bit big-endian word from the flash data."""
		if not 0 <= addr <= (len(self.flash) - 2):
			raise ValueError(f"Address OOB for 16-bit word: 0x{addr:04X}")
		return int.from_bytes(self.flash[addr : addr + 2], "little", signed=False)

	def entry_points(self) -> Sequence[int]:
		"""Get all defined entry points in the vector and call tables."""
		out: list[int] = []
		for addr in range(0, 0x80, 2):
			vect = self.flash_word(addr)
			if vect != 0xFFFF:
				out.append(vect)
		return out

	def get_label(self, addr: int) -> str:
		"""Get label for an address."""
		if addr in self.labels:
			return self.labels[addr]
		else:
			return f"label_{addr:04X}"

	def branch_sources(self) -> dict[int, set[int]]:
		"""Get mapping of branch destination to all sources."""
		out: dict[int, set[int]] = {}
		for source in self.branches:
			dest = self.branches[source]
			if dest not in out:
				out[dest] = set()
			out[dest].add(source)
		return out


@dataclass(frozen=True)
class Field:
	"""Abstract base field."""

	is_addr: ClassVar[bool] = False
	"""True iff the value is an absolute address."""

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

		If returning multiple next addresses, it is preferred that if the
		address of the linearly next instruction is present, that it will be
		first in the returned sequence.
		"""
		raise NotImplementedError
