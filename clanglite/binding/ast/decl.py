from clanglite.binding.cursor import Cursor


class Decl(Cursor):
    pass


class UnexposedDecl(Decl):
    """A declaration whose specific kind is not exposed via this interface."""

    __kind__ = 1


class StructDecl(Decl):
    """A C or C++ struct."""

    __kind__ = 2


class UnionDecl(Decl):
    """A C or C++ union."""

    __kind__ = 3


class ClassDecl(Decl):
    """A C++ class."""

    __kind__ = 4


class EnumDecl(Decl):
    """An enumeration."""

    __kind__ = 5


class FieldDecl(Decl):
    """A field (non-static data member) in a struct, union, or C++ class."""

    __kind__ = 6


class EnumConstantDecl(Decl):
    """An enumerator constant."""

    __kind__ = 7


class FunctionDecl(Decl):
    """A function."""

    __kind__ = 8


class VarDecl(Decl):
    """A variable."""

    __kind__ = 9


class ParmDecl(Decl):
    """A function or method parameter."""

    __kind__ = 10

# some OBJC decls have been removed


class TypedefDecl(Decl):
    """A typedef."""

    __kind__ = 20


class CXXMethod(Decl):
    """A C++ class method."""

    __kind__ = 21


class Namespace(Decl):
    """A C++ namespace."""

    __kind__ = 22


class LinkageSpec(Decl):
    """A linkage specification, e.g. 'extern "C" { ... }'."""

    __kind__ = 23


class Constructor(Decl):
    """A C++ constructor."""

    __kind__ = 24


class Destructor(Decl):
    """A C++ destructor."""

    __kind__ = 25


class ConversionFunction(Decl):
    """A C++ conversion function."""

    __kind__ = 26


class TemplateTypeParameter(Decl):
    """A C++ template type parameter."""

    __kind__ = 27


class NonTypeTemplateParameter(Decl):
    """A C++ non-type template parameter."""

    __kind__ = 28


class TemplateTemplateParameter(Decl):
    """A C++ template template parameter."""

    __kind__ = 29


class FunctionTemplate(Decl):
    """A C++ function template."""

    __kind__ = 30


class ClassTemplate(Decl):
    """A C++ class template."""

    __kind__ = 31


class ClassTemplatePartialSpecialization(Decl):
    """A C++ class template partial specialization."""

    __kind__ = 32


class NamespaceAlias(Decl):
    """A C++ namespace alias declaration."""

    __kind__ = 33


class UsingDirective(Decl):
    """A C++ using directive."""

    __kind__ = 34


class UsingDeclaration(Decl):
    """A C++ using declaration."""

    __kind__ = 35


class TypeAliasDecl(Decl):
    """A C++ alias declaration."""

    __kind__ = 36


class CXXAccessSpecifier(Decl):
    """A C++ access specifier."""

    __kind__ = 39


class ModuleImportDecl(Decl):
    """A module import declaration."""

    __kind__ = 600


class TypeAliasTemplateDecl(Decl):
    """A C++ alias template declaration."""

    __kind__ = 601


class FriendDecl(Decl):
    """A friend declaration."""

    __kind__ = 603


class ConceptDecl(Decl):
    """A C++20 concept declaration."""

    __kind__ = 604


def register():
    import inspect
    for name, cls in globals().items():
        if inspect.isclass(cls) and issubclass(cls, Decl):
            if cls is not Cursor and cls is not Decl:
                Cursor.__all_kinds__[cls.__kind__] = cls


register()
