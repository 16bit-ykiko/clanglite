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
        ("xkind", c_int),
        ("xdata", c_int),
        ("data", c_void_p * 3)
    ]

    

class CXType(Structure):
    _fields_ = [
        ("xkind", c_int),
        ("data", c_void_p * 2)
    ]


class CXToken(Structure):
    _fields_ = [
        ("int_data", c_uint * 4),
        ("ptr_data", c_void_p)
    ]


class CXUnsavedFile(Structure):
    _fields_ = [
        ("filename", c_char_p),
        ("contents", c_char_p),
        ("length", c_ulong)
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
    ("clang_createIndex", [c_int, c_int], c_void_p),
    ("clang_disposeIndex", [c_void_p], None),

    # CXTranslationUnit
    ("clang_parseTranslationUnit", [c_void_p, c_char_p, c_void_p, c_int,
                                    c_void_p, c_uint, c_uint], c_void_p),
    ("clang_getTranslationUnitCursor", [c_void_p], CXCursor),
    ("clang_getTranslationUnitSpelling", [c_void_p], CXString),
    ("clang_disposeTranslationUnit", [c_void_p], None),



    # CXCursor
    ("clang_getNullCursor", [], CXCursor),  # Index.h 2283

    ("clang_equalCursors", [CXCursor, CXCursor], c_uint),
    ("clang_Cursor_isNull", [CXCursor], c_uint),
    ("clang_hashCursor", [CXCursor], c_uint),
    ("clang_getCursorKind", [CXCursor], c_int),
    ("clang_isDeclaration", [c_int], c_uint),
    ("clang_isInvalidDeclaration", [c_int], c_uint),  # Index.h 2326
    ("clang_getCursorKindSpelling", [c_int], CXString),
    ("clang_getCursorSpelling", [CXCursor], CXString),
    ("clang_visitChildren", [CXCursor, c_void_p, py_object], c_uint),

    # Enum
    ("clang_getEnumDeclIntegerType", [CXCursor], CXType),
    ("clang_getEnumConstantDeclValue", [CXCursor], c_longlong),
    ("clang_getEnumConstantDeclUnsignedValue", [CXCursor], c_ulonglong),
    ("clang_EnumDecl_isScoped", [CXCursor], c_uint),

    # CXOperator
    ("clang_getCursorUnaryOperatorKind", [CXCursor], c_int),
    ("clang_getCursorBinaryOperatorKind", [CXCursor], c_int),

    # CXType



]


def register_function(lib):
    for func in functions:
        f = getattr(lib, func[0])
        f.argtypes = func[1]
        f.restype = func[2]


dll = CDLL("/home/ykiko/Project/C++/llvm-project/build/lib/libclang.so")

register_function(dll)
