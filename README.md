# pytest-subinterpreter

A Pytest extension for running the pytest session inside a [sub interpreter](https://peps.python.org/554). This extension is mainly targeted for Python extension library maintainers that want to verify their existing test suite works inside a sub interpreter.

Requirements:

- Python 3.13.0-alpha.2 or above
- Pytest 7 or above

## Installation

```console
pip install pytest-subinterpreter
```

## Usage

The extension arguments are:

- `--interpreter-per` Defaults to `session` (also the only option at the moment).

```console
pytest  tests/test_simple.py 
```
