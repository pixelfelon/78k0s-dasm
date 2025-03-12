"""Miscellaneous utility functions."""

from typing import Sequence, TYPE_CHECKING

if TYPE_CHECKING:
	from k0s_dasm.ibase import Instruction


def fmthex(data: bytes | bytearray | Sequence[int]) -> str:
	"""Format some hex bytes into a minimalist string."""
	return " ".join([f"{b:02X}" for b in data])


def fsl_remap(addr: int, inst: "Instruction") -> int:
	"""Remap 0x8000-0xBFFF to 0x0000-0x3FFF for convenience."""
	# This is really specific to analyzing the Flash ROM and shouldn't
	#  normally be present. So it's commented out in Git...
	# if 0x8000 <= addr <= 0xBFFF:
	# 	addr -= 0x8000
	# 	note = f"Remapped 0x{addr + 0x8000:04X} to 0x{addr:04X}"
	# 	if note not in inst.notes:
	# 		# Remap could get called a few times
	# 		inst.notes.append(note)
	return addr
