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
