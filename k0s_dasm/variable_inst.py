from collections import deque
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



# Uaed only for find_variant_exec_traces
inst_traces = list()

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
					#print(f"{'-'*50}\n\t({len(var_flash)} leftover bits)\n\t")
					#print("\n\t".join(f"{i['inst'].__name__}, {i['inst'].flow.__class__.__name__}, {i['inst_val']}" for i in sub_exec_trace))


def find_variant_exec_traces_bfs(var_flash: str) -> list:
    """
    Performs a BFS-like parse of 'var_flash'.
    Each path (trace) is a list of positions,
    and each position is a list of possible instructions.

    Returns a list of such traces, each trace leading from start to finish.
    """

    # Each queue element: (remaining_bits, trace_so_far)
    # where trace_so_far is a list of positions (each position = list of dicts).
    queue = deque([(var_flash, [])])
    results = []

    while queue:
        current_bits, current_trace = queue.popleft()

        # If no bits remain, we've reached the end of this parse
        if not current_bits:
            # Decide if we want to store it:
            # For example, you might require at least one "non-FlowForward" in the trace.
            # But here we'll just store it unconditionally.
            results.append(current_trace)
            continue

        # We attempt to match instructions on the next chunk
        # (the first 'bytecount * 8' bits).
        # We'll collect expansions in leftover_groups,
        # keyed by the leftover bits, and valued by a list of dicts
        # representing each matching instruction.
        leftover_groups = {}

        for cls in Instruction.__subclasses__():
            if cls.mnemonic is NotImplemented or cls.match is NotImplemented:
                continue
            # If not enough bits to match this instruction, skip
            needed_bits = cls.bytecount * 8
            if len(current_bits) < needed_bits:
                continue

            chunk = current_bits[:needed_bits]
            if (res := could_be_inst(chunk, cls)) is not None:
                remainder = current_bits[needed_bits:]
                # Build the dictionary describing this match
                match_dict = {"inst": cls, "inst_val": res}
                leftover_groups.setdefault(remainder, []).append(match_dict)

        # For each unique leftover, we create a new path that includes
        # a new "position" (list of dicts) with all matching instructions
        # that share that leftover.
        for leftover, variant_list in leftover_groups.items():
            # copy the trace
            new_trace = deepcopy(current_trace)
            # add a new position containing all these matching variants
            new_trace.append(variant_list)
            queue.append((leftover, new_trace))

    return results



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

def print_all_variants(traces: list):
    """
    For each trace in 'traces', print each 'position'.
    Each position is a list of dicts: [{"inst": cls, "inst_val": "..."}, ...].
    We join them with slash '/' to show they are alternatives at the same place.
    """
    for trace in traces:
        print("-" * 50)
        for position in trace:
            # position is [dict1, dict2, ...]
            # We build strings like "INSTNAME, FLOWNAME, BITS"
            variant_strs = []
            for variant in position:
                inst_name = variant["inst"].__name__
                flow_name = variant["inst"].flow.__class__.__name__
                bits_str  = variant["inst_val"]
                variant_strs.append(f"{inst_name}, {flow_name}, {bits_str}")
            # Print them slash-separated on one line
            print("    " + " / ".join(variant_strs))

available_bytes_clean = clean_input(available_bytes)

res = find_variant_exec_traces_bfs(available_bytes_clean)
print_all_variants(res)

#find_variant_exec_traces(available_bytes_clean)

print(len(inst_traces))
pbar.close()
