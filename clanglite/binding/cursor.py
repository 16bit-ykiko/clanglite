from clanglite.binding.config import dll, CXCursor
from ctypes import py_object, c_uint, CFUNCTYPE
from clanglite.binding.location import SourceLocation, SourceRange


class Cursor(CXCursor):

    __all_kinds__: dict[int, type] = {}
    CALLBACK = CFUNCTYPE(c_uint, CXCursor, CXCursor, py_object)

    def __init__(self, cursor: CXCursor):
        super().__init__(cursor.xkind, cursor.xdata, cursor.data)

    @property
    def kind(self) -> type:
        if self.xkind in Cursor.__all_kinds__:
            return Cursor.__all_kinds__[self.xkind]
        else:
            raise ValueError(f"Unknown cursor kind {self.xkind}")

    @property
    def location(self) -> SourceLocation:
        """
        Return the source location (the starting character) of the entity
        pointed at by the cursor.
        """
        if not hasattr(self, "_location"):
            self._location = SourceLocation(dll.clang_getCursorLocation(self))
        return self._location

    @property
    def extent(self) -> SourceRange:
        """
        Return the source range (the range of text) occupied by the entity
        pointed at by the cursor.
        """
        if not hasattr(self, "_extent"):
            self._extent = SourceRange(dll.clang_getCursorExtent(self))
        return self._extent

    @property
    def spelling(self) -> str:
        """Return the spelling of the entity pointed at by the cursor."""
        if not hasattr(self, "_spelling"):
            self._spelling = dll.clang_getCursorSpelling(self)
        return self._spelling

    @property
    def display_name(self) -> str:
        """
        Return the display name for the entity referenced by this cursor.

        The display name contains extra information that helps identify the
        cursor, such as the parameters of a function or template or the
        arguments of a class template specialization.
        """
        if not hasattr(self, "_display_name"):
            self._display_name = dll.clang_getCursorDisplayName(self)
        return self._display_name

    @property
    def mangled_name(self) -> str:
        """Return the mangled name of the entity pointed at by the cursor."""
        if not hasattr(self, "_mangled_name"):
            self._mangled_name = dll.clang_Cursor_getMangling(self)
        return self._mangled_name

    def get_children(self) -> list['Cursor']:
        """get the children of a cursor"""
        def visitor(child: CXCursor, _: CXCursor, children: list[Cursor]) -> int:
            children.append(Cursor(child))
            return 1

        children: list[Cursor] = []
        dll.clang_visitChildren(self, Cursor.CALLBACK(visitor), children)
        return children
