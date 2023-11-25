# sample ./setup.py file
from setuptools import setup

setup(
    name="pytest-subinterpreter",
    packages=["pytest_subinterpreter"],
    python_requires=">=3.13",
    install_requires=["pytest>=7.0.0"],
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["subinterpreter = pytest_subinterpreter.plugin"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)