"""Concrete instruction flow types."""

from typing import TYPE_CHECKING, Sequence

from k0s_dasm.base import Flow

if TYPE_CHECKING:
	from k0s_dasm.ibase import Instruction


class Forward(Flow):
	"""Simple linear instruction flow (no branching)."""

	def next(self, inst: "Instruction", /) -> Sequence[int]:
		"""Get sequentially next instruction address."""
		pc_next = inst.pc + inst.bytecount
		return (pc_next,)
