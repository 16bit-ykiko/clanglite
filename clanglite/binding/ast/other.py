from clanglite.binding.cursor import Cursor


class TranslationUnit(Cursor):
    """
    Cursor that represents the translation unit itself.

    The translation unit cursor exists primarily to act as the root
    cursor for traversing the contents of a translation unit.
    """
    __kind__ = 350


class PreprocessingDirective(Cursor):
    __kind__ = 500


class MacroDefinition(Cursor):
    __kind__ = 501


class MacroExpansion(Cursor):
    __kind__ = 502


class InclusionDirective(Cursor):
    __kind__ = 503


class StaticAssert(Cursor):
    """
    A static_assert or _Static_assert node
    """
    __kind__ = 602


def register():
    import inspect
    for name, cls in globals().items():
        if inspect.isclass(cls) and cls is not Cursor:
            Cursor.__all_kinds__[cls.__kind__] = cls


register()
