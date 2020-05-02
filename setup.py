"""Setup file for ingredients."""

import pathlib
import setuptools


current_dir = pathlib.Path(__file__).parent

readme = (current_dir / "README.md").read_text()

setuptools.setup(
    name="ingredients",
    version="0.0.1",
    description="A lot of ingredients",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/eegkno/ingredients.git",
    author="Edgar Garcia Cano",
    author_email="eegkno@gmail.com",
    classifiers=["Programming Language :: Python"],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)
