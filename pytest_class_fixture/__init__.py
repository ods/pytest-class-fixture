import inspect
import sys
from typing import TypeVar

import pytest

_T = TypeVar('_T', bound=type)


def class_fixture(name: str):
    def decorator(cls: _T) -> _T:
        def fixture_function(*args, **kwargs):
            return cls(*args, **kwargs)

        signature = inspect.signature(cls.__init__)
        parameters = list(signature.parameters.values())[1:]  # remove self
        fixture_function.__signature__ = signature.replace(parameters=parameters)

        fixture_value = pytest.fixture(name=name)(fixture_function)
        # pytest inspects module namespace for fixtures, so we need to add it
        # to the module where decorator is applied
        sys._getframe(1).f_globals[f"@class_fixture_{name}"] = fixture_value

        return cls

    return decorator
