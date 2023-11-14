"""Miscellaneous utility functions."""

from typing import Sequence


def fmthex(data: bytes | bytearray | Sequence[int]) -> str:
	"""Format some hex bytes into a minimalist string."""
	return " ".join([f"{b:02X}" for b in data])
