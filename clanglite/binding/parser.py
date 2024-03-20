from clanglite.binding.config import dll, CXIndex


class Index(CXIndex):

    @staticmethod
    def create(cxx: int, exclude_decls: int) -> 'Index':
        return Index(dll.clang_createIndex(cxx, exclude_decls))

    def __del__(self: CXIndex) -> None:
        dll.clang_disposeIndex(self)


class TranslationUnit(CXIndex):

    @staticmethod
    def parse(index: Index, file: str, args: list[str], unsaved_files: list[str], options: int) -> 'TranslationUnit':
        return TranslationUnit(dll.clang_parseTranslationUnit(index, file, args, len(args), unsaved_files, len(unsaved_files), options))

    def __del__(self: CXIndex) -> None:
        dll.clang_disposeTranslationUnit(self)


class Parser:
    pass
