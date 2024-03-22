import inspect
from types import ModuleType
from clanglite.binding.ast import attr, decl, expr, other, ref, stmt
from clanglite.binding.cursor import Cursor


def register(module: ModuleType):
    all_kinds = Cursor.__all_kinds__
    for _, cls in module.__dict__.items():
        if inspect.isclass(cls) and hasattr(cls, "__cursor_kind__"):
            kind: int | list[int] = cls.__cursor_kind__

            if isinstance(kind, int):
                all_kinds[kind] = cls
            else:
                for k in kind:
                    all_kinds[k] = cls


def main():
    register(attr)
    register(decl)
    register(expr)
    register(other)
    register(ref)
    register(stmt)


main()
