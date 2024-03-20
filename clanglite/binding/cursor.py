from clanglite.binding.config import dll, CXCursor
from ctypes import *


class Cursor(CXCursor):
    __all_kinds__: dict[int, type] = {}

    def __init__(self, cursor: CXCursor):
        super().__init__(
            cursor.xkind,
            cursor.xdata,
            cursor.data
        )

    @property
    def kind(self) -> int:
        return dll.clang_getCursorKind(self)

    @property
    def spelling(self) -> str:
        cxstr = dll.clang_getCursorSpelling(self)
        ctsr = dll.clang_getCString(cxstr)
        return ctsr.decode("utf8")

    def get_children(self) -> list['Cursor']:
        """get the children of a cursor"""
        def visitor(child, parent, children):

            # Create reference to TU so it isn't GC'd before Cursor.
            # child._tu = self._tu
            children.append(Cursor(child))
            return 1  # continue

        children = []
        CALLBACK = CFUNCTYPE(c_uint, CXCursor, CXCursor, py_object)
        dll.clang_visitChildren(self, CALLBACK(visitor), children)
        return iter(children)

    def down_cast(self):
        cls = Cursor.__all_kinds__[self.kind]
        return cls(self)
