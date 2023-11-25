# sample ./setup.py file
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pytest-subinterpreter",
    version="0.0.1",
    description="Run pytest in a subinterpreter",
    long_description=long_description,
    packages=["pytest_subinterpreter"],
    python_requires=">=3.13",
    install_requires=["pytest>=7.0.0"],
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["subinterpreter = pytest_subinterpreter.plugin"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)