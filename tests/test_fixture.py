import pytest

from dataclasses import dataclass
from pytest_class_fixture import class_fixture


@pytest.fixture
def sample() -> str:
    return "abc"


@class_fixture("fixture")
@dataclass
class Fixture:
    sample: str

    def __call__(self, count: int = 1) -> str:
        return self.sample * count


def test_fixture(fixture: Fixture) -> None:
    assert fixture(count=2) == "abcabc"
