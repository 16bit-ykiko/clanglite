from typing import TypeVar, Callable, Any

T = TypeVar('T')


class FieldDecl:

    @property
    def name(self) -> str: ...


def add_matcher(cls: type[T], call_back: Callable[[T], Any]) -> None: 
    """1111111111111111111"""
    ...

def run() -> None: ...
