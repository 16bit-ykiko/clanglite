from clanglite.binding.cursor import Cursor


class TranslationUnit(Cursor):
    """
    Cursor that represents the translation unit itself.

    The translation unit cursor exists primarily to act as the root
    cursor for traversing the contents of a translation unit.
    """
    __cursor_kind__ = 350


class PreprocessingDirective(Cursor):
    __cursor_kind__ = 500


class MacroDefinition(Cursor):
    __cursor_kind__ = 501


class MacroExpansion(Cursor):
    __cursor_kind__ = 502


class InclusionDirective(Cursor):
    __cursor_kind__ = 503


class StaticAssert(Cursor):
    """
    A static_assert or _Static_assert node
    """
    __cursor_kind__ = 602


def register():
    import inspect

    all_kinds = Cursor.__all_kinds__
    for _, cls in globals().items():
        if inspect.isclass(cls) and hasattr(cls, "__cursor_kind__"):
            kind: int | list[int] = cls.__cursor_kind__

            if isinstance(kind, int):
                all_kinds[kind] = cls
            else:
                for k in kind:
                    all_kinds[k] = cls


register()
