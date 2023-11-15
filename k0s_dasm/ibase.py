"""Instruction type definitions."""

from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, Sequence, Type, TypeVar

from k0s_dasm.flow import Forward as FlowForward
from k0s_dasm.util import fmthex

if TYPE_CHECKING:
	from k0s_dasm.base import Field, Flow, Operand, Program


_T = TypeVar("_T", bound="Instruction")


@dataclass
class Instruction:
	"""
	Definition of a 78K/0S instruction mnemonic and its encoding.

	There should be one definition (subclass) for each row in the
	"instruction code list" from the manual.

	Instruction words are in BIG ENDIAN for consistent reading with the list
	in the datasheet, but data words are generally in little endian.
	"""

	mnemonic: ClassVar[str] = NotImplemented
	"""
	Class constant: text representation of the instruction format.

	This is in the abstract case, with the names of the operands instead
	of the actual values for an instance of the instruction.
	"""

	match: ClassVar[int] = NotImplemented
	"""
	Class constant: bits consumed by the instruction.

	Program data must match exactly when masked with mmask.
	"""

	mmask: ClassVar[int] = NotImplemented
	"""Class constant: mask applied to match and data when finding instructions."""

	bytecount: ClassVar[int] = NotImplemented
	"""Class constant: instruction byte count."""

	field_defs: ClassVar[Sequence["Field"]] = tuple()
	"""Class constant: tuple of Field instances for instruction fields."""

	flow: ClassVar["Flow"] = FlowForward()
	"""Class constant: instruction flow type."""

	format: ClassVar[str] = NotImplemented
	"""
	Class constant: format string with entries for operands.

	The format things (i.e. {0}, {1}) will be filled in with the string from
	rendering that operand, with indices per ``field_defs``.
	"""

	word: int
	"""Raw instruction word (8-32 bits)."""

	pc: int
	"""Address of (the first byte of) this instruction."""

	next: Sequence[int]
	"""
	Address(es) of the next instruction(s).

	In general this is the next sequential instruction in the program. But, if
	it's a branch instruction, it will be something different. If it's a
	conditional branch, there would be multiple next addresses. If the next
	address is calculated at runtime, then this field may be empty (requiring
	manual intervention).
	"""

	operands: dict["Field", "Operand"]
	"""
	Operand values for each defined Field.

	Preferred order is as per ``field_defs``.
	"""

	program: "Program"
	"""The containing Program."""

	notes: str = ""
	"""Notes or warnings from analysis."""

	@classmethod
	def load(cls: Type[_T], program: "Program", addr: int | None = None) -> _T | None:
		"""
		Attempt to match some program data to this instruction def.

		If no start address is provided, the PC in the Program is used, and
		then updated according to the actual word length. If a start address
		is provided, the Program's PC is ignored and not updated.
		"""
		if addr is None:
			pc = program.pc
		else:
			pc = addr
		pc_next = pc + cls.bytecount
		data = program.flash[pc:pc_next]

		if len(data) < cls.bytecount:
			return None
		word = int.from_bytes(data[: cls.bytecount], byteorder="big", signed=False)
		if (word & cls.mmask) != (cls.match & cls.mmask):
			return None
		# else, matched.

		fields: dict[Field, Operand] = {}
		out = cls(
			word=word,
			pc=pc,
			next=tuple(),
			operands=fields,
			program=program,
		)

		for fdef in cls.field_defs:
			fields[fdef] = fdef.from_inst_word(word, out)
		out.next = out.flow.next(out)

		if addr is None:
			program.pc += cls.bytecount
		return out

	@staticmethod
	def autoload(program: "Program", addr: int | None = None) -> "Instruction":
		"""Attempt to match some program data to any instruction subclass."""
		try:
			# defs live here
			import k0s_dasm.instr  # noqa
		except ImportError:
			pass

		if addr is None:
			pc = program.pc
		else:
			pc = addr

		results: list[Instruction] = []
		for cls in Instruction.__subclasses__():
			if cls.mnemonic is NotImplemented or cls.match is NotImplemented:
				continue  # intermediate class
			result = cls.load(program, pc)
			if result is not None:
				results.append(result)

		debug_data = program.flash[pc : pc + 4]
		if len(results) == 0:
			raise ValueError(
				f"Could not match instruction data: {fmthex(debug_data)} ..."
			)
		elif len(results) > 1:
			debug = "\n\t".join([result.render() for result in results])
			raise RuntimeError(
				"Multiple matches for instruction data! "
				f"[ {fmthex(debug_data)} ... ] -> \n\t{debug}"
			)

		else:
			result = results[0]
			if addr is None:
				program.pc += result.bytecount
			return result

	def render(self) -> str:
		"""Render instruction mnemonic with field values."""
		ren_fields: list[str] = []
		for fdef in self.field_defs:
			ren_fields.append(self.operands[fdef].render())
		return self.format.format(*ren_fields)
