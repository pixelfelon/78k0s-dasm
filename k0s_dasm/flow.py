"""Concrete instruction flow types."""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Sequence

from k0s_dasm.base import Flow

if TYPE_CHECKING:
	from k0s_dasm.ibase import Instruction


class Forward(Flow):
	"""Simple linear instruction flow (unconditional, no branching)."""

	def next(self, inst: "Instruction", /) -> Sequence[int]:
		"""Get sequentially next instruction address."""
		pc_next = inst.pc + inst.bytecount
		return (pc_next,)


@dataclass(frozen=True)
class ConditionalBranch(Flow):
	"""Conditionally branched (otherwise forward) instruction flow."""

	branch_field_idx: int

	def next(self, inst: "Instruction", /) -> Sequence[int]:
		"""Get forward and branch instruction addresses."""
		forward = inst.pc + inst.bytecount
		branch = inst.operands[inst.field_defs[self.branch_field_idx]].val
		return forward, branch


class CallReturn(ConditionalBranch):
	"""Analyzes the same as conditional branch, but semantically different."""


@dataclass(frozen=True)
class UnconditionalBranch(Flow):
	"""Unconditionally branched instruction flow."""

	branch_field_idx: int

	def next(self, inst: "Instruction", /) -> Sequence[int]:
		"""Get branch instruction address."""
		branch = inst.operands[inst.field_defs[self.branch_field_idx]].val
		return (branch,)


class ComputedUnknown(Flow):
	"""Abstract computed branch that we don't know how to analyze."""

	def next(self, inst: "Instruction", /) -> Sequence[int]:
		"""Get no addresses (we don't know where to go)."""
		inst.notes.append("WARNING: Computed branch unknown.")
		return tuple()


class Return(ComputedUnknown):
	"""Return instruction (not sure where to jump back to, but callsite knows)."""

	def next(self, inst: "Instruction", /) -> Sequence[int]:
		"""Get no addresses (we don't know where to go)."""
		# inst.notes.append("INFO: Function return.")
		return tuple()


@dataclass(frozen=True)
class ComputedCallT(Flow):
	"""Computed branch via call table."""

	callt_idx_field_idx: int = 0

	def next(self, inst: "Instruction", /) -> Sequence[int]:
		"""Get forward address and relevant address from call table."""
		forward = inst.pc + inst.bytecount
		callt_idx = inst.operands[inst.field_defs[self.callt_idx_field_idx]].val
		callt_addr = inst.program.flash_word(callt_idx)
		inst.notes.append(
			f"INFO: Initial CALLT[{callt_idx:02X}H] -> !{callt_addr:04X}H"
		)
		# N.B.: It's possible the program could change the call table later,
		# but this would be a major operation as it's in flash.
		return forward, callt_addr
