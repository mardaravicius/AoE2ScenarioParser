from pathlib import Path

from Cython.Build import cythonize
from setuptools import setup
from setuptools.extension import Extension

root_directory = Path(__file__).parent
source_directory = root_directory / 'AoE2ScenarioParser'

extensions = [
    Extension(
        name='.'.join(file.with_suffix("").relative_to(root_directory).parts),
        sources=[str(file)]
    ) for file in source_directory.rglob("*.pyx")
]

setup(
    name='Hello world app',
    ext_modules=cythonize(
        extensions,
        force=True,
        compiler_directives={
            'language_level': '3'
        }
    ),
)
