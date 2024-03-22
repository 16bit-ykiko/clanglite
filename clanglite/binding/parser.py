from os import fspath, path
from ctypes import c_char_p
from typing import Callable, TypeVar, Any

from .cursor import Cursor
from .config import dll, CXIndex, CXTranslationUnit, CXUnsavedFile


class Index(CXIndex):

    def __init__(self, index: CXIndex) -> None:
        super().__init__(index.value)

    @staticmethod
    def create(cxx: int = 0, exclude_decls: int = 0) -> 'Index':
        return Index(dll.clang_createIndex(cxx, exclude_decls))

    def parse(self, filepath: str, args: list[str], unsaved_files: list[tuple[str, str]] = []) -> 'TranslationUnit':
        if unsaved_files == [] and not path.exists(filepath):
            raise ValueError(f"File {filepath} does not exist")

        fpath = c_char_p(fspath(filepath).encode("utf8"))

        args_array = None if len(args) == 0 else (
            c_char_p * len(args))(*[x.encode("utf8") for x in args])

        unsaved_array = None
        if len(unsaved_files) > 0:
            unsaved_array = (CXUnsavedFile * len(unsaved_files))()
            for i, (name, contents) in enumerate(unsaved_files):
                unsaved_array[i].filename = c_char_p(fspath(name).encode("utf8"))
                unsaved_array[i].contents = c_char_p(contents.encode("utf8"))
                unsaved_array[i].length = len(contents)

        ptr: CXTranslationUnit = dll.clang_parseTranslationUnit(
            self, fpath, args_array, len(args), unsaved_array, len(unsaved_files), 0)

        if not ptr:
            raise ValueError("Failed to parse translation unit")

        return TranslationUnit(ptr)

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

    def __init__(self, filepath: str, args: list[str] = [], unsaved_files: list[tuple[str, str]] = []) -> None:
        self.filepath = filepath
        self.args = args
        self.index = Index.create()
        self.tu = self.index.parse(filepath, args, unsaved_files)
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
