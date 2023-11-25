import pytest
import _xxsubinterpreters as interpreters

def pytest_addoption(parser):
    group = parser.getgroup("subinterpreter")
    group.addoption(
        "--interpreter-per",
        action="store",
        dest="interpreter-per",
        default="session",
        help='Interpreter scope.',
    )

def wrap_pytest():
    # args: tuple[str], plugins: tuple[str]
    import sys
    from pytest_subinterpreter.faulthandler import FaultHandler

    from _pytest.main import wrap_session, _main
    from _pytest.config import get_config

    config = get_config(list(args), plugins)
    config.parse(list(args))

    # The CPython faulthandler isn't supported, patch it with a dummy.
    sys.modules["faulthandler"] = FaultHandler()

    wrap_session(config, _main)


@pytest.hookimpl(tryfirst=True)
def pytest_cmdline_main(config: pytest.Config):
    scope = config.getoption("interpreter-per")

    args = tuple(config.args)
    plugins = tuple(config.invocation_params.plugins) if config.invocation_params.plugins else ()
    interp = interpreters.create()

    if scope == "session":
        interpreters.run_func(interp, wrap_pytest, shared={
            "args": args,
            "plugins": plugins
        })
    else:
        raise NotImplementedError(f"Scope {scope} not implemented")
    
    interpreters.destroy(interp)
    return 1 # don't run main pytest script
