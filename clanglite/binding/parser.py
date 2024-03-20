from os import fspath
from ctypes import *
from clanglite.binding.config import dll, CXIndex, CXTranslationUnit
from clanglite.binding.cursor import Cursor
from typing import Callable


class Index(c_void_p):

    @staticmethod
    def create(cxx=0, exclude_decls=0) -> 'Index':
        return Index(dll.clang_createIndex(cxx, exclude_decls))

    def parse(self, filepath: str, args: list[str]) -> 'TranslationUnit':
        fpath = c_char_p(fspath(filepath).encode("utf8"))
        return TranslationUnit(dll.clang_parseTranslationUnit(self, fpath, None, 0, None, 0, 0))

    def __del__(self) -> None:
        dll.clang_disposeIndex(self)


class TranslationUnit(c_void_p):

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


class Parser:

    def __init__(self, filepath: str, args: list[str] = []) -> None:
        self.filepath = filepath
        self.args = args
        self.index = Index.create()
        self.tu = self.index.parse(filepath, args)
        self.matchers: dict[int, (type, Callable)] = {}

    def add_matcher(self, ast_node: type, matcher: Callable) -> None:
        kind = ast_node.__cursor_kind__
        if isinstance(kind, int):
            self.matchers[kind] = (ast_node, matcher)
        elif isinstance(kind, list):
            for k in kind:
                self.matchers[k] = (ast_node, matcher)

    def run(self) -> None:

        def tarverse(cursor: Cursor):
            kind = cursor.kind

            if kind in self.matchers:
                ast_node, matcher = self.matchers[kind]
                matcher(ast_node(cursor))

            for child in cursor.get_children():
                tarverse(child)

        tarverse(self.tu.cursor)
