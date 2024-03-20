import os
from ctypes import *


class CXString(Structure):
    _fields_ = [
        ("data", c_void_p),
        ("private_flags", c_uint)
    ]


class CXSourceLocation(Structure):
    _fields_ = [
        ("ptr_data", c_void_p * 2),
        ("int_data", c_uint)
    ]


class CXSourceRange(Structure):
    _fields_ = [
        ("ptr_data", c_void_p * 2),
        ("begin_int_data", c_uint),
        ("end_int_data", c_uint)
    ]


class CXCursor(Structure):
    _fields_ = [
        ("kind", c_int),
        ("xdata", c_int),
        ("data", c_void_p * 3)
    ]


class CXType(Structure):
    _fields_ = [
        ("kind", c_int),
        ("data", c_void_p * 2)
    ]


class CXToken(Structure):
    _fields_ = [
        ("int_data", c_uint * 4),
        ("ptr_data", c_void_p)
    ]


class CXIndex(c_void_p):
    pass


class CXTranslationUnit(c_void_p):
    pass


functions = [
    # CXString.h
    ("clang_getCString", [CXString], c_char_p),
    ("clang_disposeString", [CXString], None),

    # Index.h

    # CXIndex
    ("clang_createIndex", [c_int, c_int], CXIndex),
    ("clang_disposeIndex", [CXIndex], None),

    # CXTranslationUnit
    ("clang_parseTranslationUnit", [c_void_p, c_char_p, c_void_p, c_int,
                                    c_void_p, c_uint, c_uint], CXTranslationUnit),
    ("clang_disposeTranslationUnit", [CXTranslationUnit], None),

    # CXCursor
    ("clang_getNullCursor", [], CXCursor),  # Index.h 2283
    ("clang_getTranslationUnitCursor", [c_void_p], CXCursor),
    ("clang_equalCursors", [CXCursor, CXCursor], c_uint),
    ("clang_Cursor_isNull", [CXCursor], c_uint),
    ("clang_hashCursor", [CXCursor], c_uint),
    ("clang_getCursorKind", [CXCursor], c_int),
    ("clang_isDeclaration", [c_int], c_uint),
    ("clang_isInvalidDeclaration", [c_int], c_uint),  # Index.h 2326
    ("clang_getCursorKindSpelling", [c_int], CXString),
    ("clang_getCursorSpelling", [CXCursor], CXString),
    ("clang_visitChildren", [CXCursor, c_void_p,
     c_void_p], c_uint),  # Index.h 3875
    # CXType

]


def register_function(lib):
    for func in functions:
        try:
            f = getattr(lib, func[0])
            f.argtypes = func[1]
            f.restype = func[2]
        except:
            print(func[0], "error")


dll = CDLL("llvm-project/build/lib/libclang.so")

register_function(dll)
