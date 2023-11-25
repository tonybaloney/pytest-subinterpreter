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
$ pytest tests/test_simple.py
============================================================================== test session starts ===============================================================================
platform darwin -- Python 3.13.0a1+, pytest-7.4.3, pluggy-1.3.0
rootdir: /Users/anthonyshaw/projects/pytest-subinterpreter
plugins: subinterpreter-0.0.0
collected 1 item                                                                                                                                                                 

tests/test_simple.py .                                                                                                                                                     [100%]

=============================================================================== 1 passed in 0.02s ================================================================================

```
