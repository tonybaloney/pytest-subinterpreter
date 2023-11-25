import pytest
import _xxsubinterpreters as interpreters


def wrap_pytest():
    # args: tuple[str], plugins: tuple[str]
    from _pytest.main import wrap_session, _main
    from _pytest.config import get_config

    config = get_config(list(args), plugins)
    config.parse(list(args))

    wrap_session(config, _main)


@pytest.hookimpl(tryfirst=True)
def pytest_cmdline_main(config: pytest.Config):
    args = tuple(config.args)
    plugins = tuple(config.invocation_params.plugins) if config.invocation_params.plugins else ()
    interp = interpreters.create()
    interpreters.run_func(interp, wrap_pytest, shared={
        "args": args,
        "plugins": plugins
    })
    interpreters.destroy(interp)
    return 1
