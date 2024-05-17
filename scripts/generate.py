import os.path as path
import clang.cindex as CX


def is_ignored(cursor: CX.Cursor):
    for attr in cursor.get_children():
        if attr.kind == CX.CursorKind.ANNOTATE_ATTR:
            if attr.spelling == "ignore":
                return True

    return False


def is_property(cursor: CX.Cursor):
    for attr in cursor.get_children():
        if attr.kind == CX.CursorKind.ANNOTATE_ATTR:
            if attr.spelling == "property":
                return True

    return False


def source(namespace: CX.Cursor, name: str):
    result = f"""
#include <pybind11/pybind11.h>
#include <clanglite/ast/{name}.h>

namespace py = pybind11;

namespace clanglite{{

void register_{name}(py::module &m){{"""

    for cls in namespace.get_children():
        result += f'py::class_<{cls.spelling}, {name.capitalize()}>(m, "{cls.spelling}")\n'
        result += f'.def_readonly_static("__kind__", &{cls.spelling}::kind)\n'
        result += f'.def(py::init<>([]({name.capitalize()} {name}){{ return {cls.spelling}({name}); }}))\n'

        for fn in cls.get_children():
            if fn.kind == CX.CursorKind.CXX_METHOD:
                if is_ignored(fn):
                    continue
                if is_property(fn):
                    result += f'.def_property_readonly("{fn.spelling}", &{cls.spelling}::{fn.spelling})\n'
                else:
                    result += f'.def("{fn.spelling}", &{cls.spelling}::{fn.spelling})\n'
        result += ';\n\n'

    result += "}\n}"
    return result


def typing(namespace: CX.Cursor, name: str):
    result = "from .basic import *\n"
    for cls in namespace.get_children():
        result += f'class {cls.spelling}({name.capitalize()}):\n'
        result += f'    __kind__: int\n'
        result += f'    def __init__(self, {name}: {name.capitalize()}) -> None: pass\n'

        for fn in cls.get_children():
            if fn.kind == CX.CursorKind.CXX_METHOD:
                if is_ignored(fn):
                    continue
                if is_property(fn):
                    result += f'    @property\n'
                result += f'    def {fn.spelling}(self) -> {fn.result_type.spelling}: pass\n'

        result += '\n'
    return result


def traverse(tu: CX.TranslationUnit, name: str):

    namespace: CX.Cursor | None = None

    for node in tu.cursor.get_children():
        if node.kind == CX.CursorKind.NAMESPACE and node.spelling == "clanglite":
            if not is_ignored(node):
                namespace = node
                break

    assert namespace is not None

    return source(namespace, name), typing(namespace, name)


def generate(name: str):
    index = CX.Index.create()
    header = path.join("include/clanglite/ast", name + ".h")
    src = path.join("src/binding/ast", name + ".cpp")
    with open(header, "r") as f:
        src = f.read()
        tu = index.parse("src.cpp", args=["-I./include",
                         "-std=c++20"], unsaved_files=[("src.cpp", src)])

        source, typing = traverse(tu, name)
        with open("src/binding/ast/" + name + ".cpp", "w") as f:
            f.write(source)

        with open("clanglite/typings/" + name + ".pyi", "w") as f:
            f.write(typing)


def main():
    generate("stmt")
    generate("expr")
    generate("decl")


if __name__ == "__main__":
    main()
