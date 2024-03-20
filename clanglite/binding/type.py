from clanglite.binding.config import dll, CXType


class Type(CXType):
    __all_kinds__ = {}

    @property
    def kind(self) -> int:
        return dll.clang_getCursorKind(self)

    @property
    def spelling(self) -> str:
        return dll.clang_getCursorSpelling(self)

    pass
