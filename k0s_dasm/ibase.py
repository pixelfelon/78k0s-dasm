"""Instruction type definitions."""

from dataclasses import dataclass, field
from typing import ClassVar, Sequence, Type, TypeVar

from k0s_dasm.util import fmthex


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
	"""Text representation of the instruction"""

	match: ClassVar[int] = NotImplemented
	"""Bits consumed by the instruction, value must match exactly when masked with mmask"""

	mmask: ClassVar[int] = NotImplemented
	"""Mask applied to match when finding instructions"""

	bytecount: ClassVar[int] = NotImplemented
	"""Instruction Byte Count"""

	field_defs: ClassVar[Sequence["Field"]] = tuple()
	"""Tuple of Field instances for instruction fields"""

	format: ClassVar[str] = NotImplemented
	"""Format string with field entries"""

	word: int
	pc: int
	fields: dict["Field", "Operand"]  # order as per field_defs
	program: Program

	@classmethod
	def load(cls: Type[_T], program: Program, addr: int | None = None) -> _T | None:
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
		data = program.flash[pc : pc + cls.bytecount]

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
			fields=fields,
			program=program,
		)

		for fdef in cls.field_defs:
			fields[fdef] = fdef.from_inst_word(word, out)

		if addr is None:
			program.pc += cls.bytecount
		return out

	@staticmethod
	def autoload(program: Program, addr: int | None = None) -> "Instruction":
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
			ren_fields.append(self.fields[fdef].render())
		return self.format.format(*ren_fields)


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

	inst: Instruction
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
