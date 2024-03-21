
from ctypes import c_uint, byref
from clanglite.binding.config import dll, CXSourceLocation, CXSourceRange, CXFile


class File(CXFile):

    def __init__(self, file: CXFile) -> None:
        super().__init__(file.value)


class SourceLocation(CXSourceLocation):

    def __init__(self, other: CXSourceLocation) -> None:

        super().__init__(other.ptr_data, other.int_data)

        file, line, column, offset = CXFile(), c_uint(), c_uint(), c_uint()
        dll.clang_getInstantiationLocation(self, byref(
            file), byref(line), byref(column), byref(offset))

        self._file = File(file)
        self._line = int(line.value)
        self._column = int(column.value)
        self._offset = int(offset.value)

    @property
    def file(self) -> File:
        return self._file

    @property
    def line(self) -> int:
        return self._line

    @property
    def column(self) -> int:
        return self._column

    @property
    def offset(self) -> int:
        return self._offset

    def __eq__(self, other: 'SourceLocation') -> bool:
        return dll.clang_equalLocations(self, other)

    def __str__(self) -> str:
        return f"SourceLocation(file={self._file}, line={self._line}, column={self._column})"


class SourceRange(CXSourceRange):

    def __init__(self, other: CXSourceRange) -> None:
        super().__init__(other.ptr_data, other.begin_int_data, other.end_int_data)

    @staticmethod
    def from_location(start: SourceLocation, end: SourceLocation) -> 'SourceRange':
        return SourceRange(dll.clang_getRange(start, end))

    @property
    def start(self) -> SourceLocation:
        return SourceLocation(dll.clang_getRangeStart(self))

    @property
    def end(self) -> SourceLocation:
        return SourceLocation(dll.clang_getRangeEnd(self))

    def __eq__(self, other: 'SourceRange') -> bool:
        return dll.clang_equalRanges(self, other)

    def __ne__(self, other: 'SourceRange') -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return f"SourceRange(start={self.start}, end={self.end})"
