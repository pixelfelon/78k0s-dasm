"""Architecture and processor definitions."""

from enum import IntEnum


class Reg8(IntEnum):
	"""8-bit single register (r) index."""

	X = 0
	A = 1
	C = 2
	B = 3
	E = 4
	D = 5
	L = 6
	H = 7


class Reg16(IntEnum):
	"""16-bit register pair (rp) index."""

	AX = 0
	BC = 1
	DE = 2
	HL = 3


VECT_BASE = 0
CALLT_BASE = 0x40
OPT_BYTE_ADDR = 0x80
PROT_BYTE_ADDR = 0x81
PROG_BASE = 0x82
SADDR_BASE = 0xFE20
SFR_BASE = 0xFF00

UPD78F9202_VECT: dict[int, str] = {
	0x00: "Reset",
	0x02: "Unused1",
	0x04: "Unused2",
	0x06: "INTLVI",
	0x08: "INTP0",
	0x0A: "INTP1",
	0x0C: "INTTMH1",
	0x0E: "INTTM000",
	0x10: "INTTM010",
	0x12: "INTAD",
}

UPD78F9202_SFR: dict[int, str] = {
	0xFF02: "P2",
	0xFF03: "P3",
	0xFF04: "P4",
	0xFF0E: "CMP01",
	0xFF0F: "CMP11",
	0xFF12: "TM00",  # pure 16-bit
	0xFF14: "CR000",  # pure 16-bit
	0xFF16: "CR010",  # pure 16-bit
	0xFF18: "ADCR",  # pure 16-bit
	0xFF1A: "ADCRH",
	0xFF22: "PM2",
	0xFF23: "PM3",
	0xFF24: "PM4",
	0xFF32: "PU2",
	0xFF33: "PU3",
	0xFF34: "PU4",
	0xFF48: "WDTM",
	0xFF49: "WDTE",
	0xFF50: "LVIM",
	0xFF51: "LVIS",
	0xFF54: "RESF",
	0xFF58: "LSRCM",
	0xFF60: "TMC00",
	0xFF61: "PRM00",
	0xFF62: "CRC00",
	0xFF63: "TOC00",
	0xFF70: "TMHMD1",
	0xFF80: "ADM",
	0xFF81: "ADS",
	0xFF84: "PMC2",
	0xFFA0: "PFCMD",
	0xFFA1: "PFS",
	0xFFA2: "FLPMC",
	0xFFA3: "FLCMD",
	0xFFA4: "FLAPL",
	0xFFA5: "FLAPH",
	0xFFA6: "FLAPHC",
	0xFFA7: "FLAPLC",
	0xFFA8: "FLW",
	0xFFE0: "IF0",
	0xFFE4: "MK0",
	0xFFEC: "INTM0",
	0xFFF3: "PPCC",
	0xFFF4: "OSTS",
	0xFFFB: "PCC",
}

PSW_BIT_CY = 0
PSW_BIT_ONE = 1
PSW_BIT_ZERO = 2
PSW_BIT_ZERO1 = 3
PSW_BIT_AC = 4
PSW_BIT_ZERO2 = 5
PSW_BIT_Z = 6
PSW_BIT_IE = 7
