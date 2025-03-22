from copy import deepcopy
from typing import Type

import k0s_dasm.instr
from k0s_dasm.base import Program
from k0s_dasm.ibase import Instruction
import itertools
from k0s_dasm.flow import Forward as FlowForward


from tqdm.auto import tqdm


def clean_input(input_text: str) -> str:
	"""Cleans a string removing all commented lines (; comment char) then removing all chars not 0/1/x (case sensitive)"""
	allowed_chars = "01x"
	lines = input_text.splitlines()
	no_comments = [line.split(";")[0] for line in lines]
	joined_text = "\n".join(no_comments)

	# Filter only allowed characters
	cleaned = "".join(char for char in joined_text if char in allowed_chars)

	return cleaned


def find_variants(input_text: str):
	# Indices where 'x' occurs
	x = [i for i, c in enumerate(input_text) if c == "x"]
	# Generate all possible 0/1 combinations for those 'x' indices
	for combo in itertools.product("01", repeat=len(x)):
		s = list(input_text)
		for i, bit in zip(x, combo):
			s[i] = bit  # fill in
		bit_str = "".join(s)
		yield bytearray(int(bit_str[i : i + 8], 2) for i in range(0, len(bit_str), 8))


def could_be_inst(bitstring: str, cls) -> str | None:
	if len(bitstring) != cls.bytecount * 8:
		return None

	result = []
	for i, c in enumerate(bitstring):
		shift = (len(bitstring) - 1) - i

		# If instruction forces this bit
		if cls.mmask & (1 << shift):
			forced_bit = (cls.match >> shift) & 1
			# If the input bit is not 'x', ensure no conflict
			if c != "x" and int(c) != forced_bit:
				return None
			result.append(str(forced_bit))
		else:
			# Not forced by the instruction
			result.append(c if c in ("0", "1") else "x")

	return "".join(result)

inst_traces = list()
pbar = tqdm(desc="Inst_Vars")


def find_variant_exec_traces(var_flash: str, exec_trace = None):
	if exec_trace is None:
		exec_trace = list()
	for cls in Instruction.__subclasses__():
		if cls.mnemonic is NotImplemented or cls.match is NotImplemented:
			continue  # intermediate class
		if len(var_flash) // 8 < cls.bytecount:
			# print(f"Can't bs {cls.__name__} too short! ( {len(var_flash) // 8} < {cls.bytecount})")
			continue
		if (res := could_be_inst(var_flash[: cls.bytecount * 8], cls)) is not None:

			add_item = {
				"inst": cls,
				"inst_val": res,
			}

			sub_exec_trace = deepcopy(exec_trace) + [add_item]

			# todo render single line of possible vairants
			"""
			fields = dict()

			for fdef in cls.field_defs:
				for var in 
				fields[fdef] = fdef.from_inst_word(word, out)

			ren_fields: list[str] = []
			for fdef in cls.field_defs:
				ren_fields.append(cls.operands[fdef].render())
			cls._rendered = cls.format.format(*ren_fields)
			"""

			if len(var_flash) - cls.bytecount * 8 > 0:
				find_variant_exec_traces(var_flash[cls.bytecount * 8 :], sub_exec_trace)
			else:
				# filter
				if any(type(i["inst"].flow) != FlowForward for i in sub_exec_trace):
					inst_traces.append(deepcopy(sub_exec_trace))
					pbar.update(1)
					#print(f"{'-'*50}\n\t({len(var_flash)} leftover bits)\n\t")
					#print("\n\t".join(f"{i['inst'].__name__}, {i['inst'].flow.__class__.__name__}, {i['inst_val']}" for i in sub_exec_trace))





#  Set preset vaslues, variable values are x
# ignores non 1/0/x chars (whitespace comments etc
available_bytes = """
0000 00xx; Port 0
xxxx xxxx; Port 1
xxxx xxxx; Port 2
0000 xxxx; Port 3
0000 00xx; Port 4
0000 0000; Port 5
0000 xxxx; Port 6
000x xxxx; Port 7
0000 0000; Port 8
0000 0000; Port 9
1111 1111; Port 10
0010 0000; Port 11
000x xxxx; Port 12
0000 000x; Port 13
0000 000x; Port 14
"""

available_bytes_clean = clean_input(available_bytes)
find_variant_exec_traces(available_bytes_clean)

print(len(inst_traces))
pbar.close()
