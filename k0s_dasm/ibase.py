"""Instruction type definitions."""

from dataclasses import dataclass, field
from typing import ClassVar, Sequence, Type, TypeVar

from k0s_dasm.styler import Styler
from k0s_dasm.util import fmthex


@dataclass
class Program:
	"""Assembly program and other flash contents."""

	flash: bytearray
	pc: int = 0
	instrs: dict[int, "Instruction"] = field(default_factory=dict)
	labels: dict[int, str] = field(default_factory=dict)


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
	fields: dict["Field", int]  # order as per field_defs
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

		if addr is None:
			program.pc += cls.bytecount

		fields: dict[Field, int] = {}
		for fdef in cls.field_defs:
			fields[fdef] = fdef.from_inst_word(word)

		return cls(
			word=word,
			pc=pc,
			fields=fields,
			program=program,
		)

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
			ren_fields.append(fdef.styler(self.fields[fdef], self))
		return self.format.format(*ren_fields)


@dataclass(frozen=True)
class Field:
	"""Abstract base field."""

	styler: Styler
	name: str

	def from_inst_word(self, word: int) -> int:
		"""Load field word from instruction word."""
		raise NotImplementedError


@dataclass(frozen=True)
class FieldB(Field):
	"""N-bit unaligned field."""

	offset: int
	bits: int

	def from_inst_word(self, word: int) -> int:
		"""Load field word from instruction word."""
		mask = (2**self.bits) - 1
		fword = (word >> self.offset) & mask
		assert isinstance(fword, int), "MyPy was right i guess"
		return fword


@dataclass(frozen=True)
class FieldW(Field):
	"""Two-byte big-endian byte-aligned field."""

	offset_bytes: int

	def from_inst_word(self, word: int) -> int:
		"""Load field word from instruction word."""
		offset = self.offset_bytes * 8
		byte_h = (word >> offset) & 0xFF
		byte_l = (word >> (offset + 8)) & 0xFF
		fword = byte_l | (byte_h << 8)
		return fword
