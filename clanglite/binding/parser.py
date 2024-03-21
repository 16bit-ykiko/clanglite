from os import fspath
from ctypes import c_char_p
from clanglite.binding.config import dll, CXIndex, CXTranslationUnit
from clanglite.binding.cursor import Cursor
from typing import Callable, TypeVar, Any


class Index(CXIndex):

    def __init__(self, index: CXIndex) -> None:
        super().__init__(index.value)

    @staticmethod
    def create(cxx: int = 0, exclude_decls: int = 0) -> 'Index':
        return Index(dll.clang_createIndex(cxx, exclude_decls))

    def parse(self, filepath: str, args: list[str]) -> 'TranslationUnit':
        fpath = c_char_p(fspath(filepath).encode("utf8"))
        return TranslationUnit(dll.clang_parseTranslationUnit(self, fpath, None, 0, None, 0, 0))

    def __del__(self) -> None:
        dll.clang_disposeIndex(self)


class TranslationUnit(CXTranslationUnit):

    def __init__(self, tu: CXTranslationUnit) -> None:
        super().__init__(tu.value)

    @property
    def cursor(self) -> Cursor:
        """Retrieve the cursor that represents the given translation unit."""
        return Cursor(dll.clang_getTranslationUnitCursor(self))

    @property
    def spelling(self) -> str:
        """Get the original translation unit source file name."""
        return dll.clang_getTranslationUnitSpelling(self)

    def __del__(self) -> None:
        dll.clang_disposeTranslationUnit(self)


T = TypeVar('T')


class Parser:

    def __init__(self, filepath: str, args: list[str] = []) -> None:
        self.filepath = filepath
        self.args = args
        self.index = Index.create()
        self.tu = self.index.parse(filepath, args)
        self.matchers: dict[type, Any] = {}

    def add_matcher(self, cls: type[T], matcher: Callable[[T], Any]) -> None:
        self.matchers[cls] = matcher

    def run(self) -> None:

        def tarverse(cursor: Cursor):
            cls = cursor.kind
            if cls in self.matchers:
                self.matchers[cls](cls(cursor))

            for child in cursor.get_children():
                tarverse(child)

        tarverse(self.tu.cursor)
