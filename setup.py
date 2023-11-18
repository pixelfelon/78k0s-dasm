"""Setup script for this package."""

from distutils.core import Command
from distutils.errors import DistutilsError
import os
from pathlib import Path

from setuptools import setup  # type: ignore


class CheckFormat(Command):
	"""Check code style/formatting with configured external tools."""

	description = "Check code style/formatting."
	user_options: list[str] = []

	def initialize_options(self) -> None:
		"""No options."""
		pass

	def finalize_options(self) -> None:
		"""No options."""
		pass

	def run(self) -> None:
		"""Run command."""
		pkgdir = Path(__file__).parent.absolute()
		commands = {
			"black": f'python -m black --check "{pkgdir}"',
			"flake8": f'python -m flake8 "{pkgdir}"',
			"mypy": f'python -m mypy "{pkgdir}"',
		}

		try:
			(pkgdir / "build").unlink()
		except OSError:
			pass

		results = {}
		for command in commands:
			result = os.system(commands[command])
			if os.name == "posix":
				results[command] = os.waitstatus_to_exitcode(result)
			else:
				results[command] = result

		ok = True
		for command in results:
			if results[command] != 0:
				print(f"{command} exited with code {results[command]}!")
				ok = False
		if not ok:
			raise DistutilsError("Code formatting needs work.")


setup(
	name="k0s-dasm",
	description="NEC 78K/0S Disassembler",
	python_requires=">=3.10.0",
	install_requires=[],
	use_scm_version=True,
	setup_requires=["setuptools_scm"],
	packages=["k0s_dasm"],
	scripts=[],
	entry_points={},
	cmdclass={"checkfmt": CheckFormat},
	extras_require={
		"dev": [
			"black-with-tabs[jupyter]",
			"flake8",
			"flake8-docstrings",
			"flake8-isort",
			"flake8-noqa",
			"isort",
			"mypy",
			"mypy-extensions",
			"pep8-naming",
			"pydocstyle",
			"setuptools",
			"setuptools_scm",
			"sphinx",
			"typing_extensions",
			"wheel",
		]
	},
	test_suite="tests",
)
