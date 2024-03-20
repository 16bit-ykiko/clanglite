from clanglite.binding.config import dll, CXCursor


class Cursor(CXCursor):
    __all_kinds__: dict[int, type] = {}

    @property
    def kind(self) -> int:
        return dll.clang_getCursorKind(self)

    @property
    def spelling(self) -> str:
        return dll.clang_getCursorSpelling(self)

    pass
