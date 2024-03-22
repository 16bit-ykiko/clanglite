from .basic import *


class UnexposedDecl(Decl):
    """A declaration whose specific kind is not exposed via this interface."""

    __cursor_kind__ = 1


class StructDecl(Decl):
    """A C or C++ struct."""

    __cursor_kind__ = 2

    @property
    def name(self) -> str:
        """get the name of a struct declaration."""
        return self.spelling

    @property
    def fields(self) -> list['FieldDecl']:
        """get the non-static data member of a struct declaration."""
        return [FieldDecl(c) for c in self.get_children() if c.kind == FieldDecl]

    @property
    def methods(self) -> list['MethodDecl']:
        """get the methods of a struct declaration."""
        return [MethodDecl(c) for c in self.get_children() if c.kind == MethodDecl]


class UnionDecl(Decl):
    """A C or C++ union."""

    __cursor_kind__ = 3


class ClassDecl(Decl):
    """A C++ class."""

    __cursor_kind__ = 4

    @property
    def name(self) -> str:
        """get the name of a struct declaration."""
        return self.spelling

    @property
    def fields(self) -> list['FieldDecl']:
        """get the non-static data member of a struct declaration."""
        return [FieldDecl(c) for c in self.get_children() if c.kind == FieldDecl]

    @property
    def methods(self) -> list['MethodDecl']:
        """get the methods of a struct declaration."""
        return [MethodDecl(c) for c in self.get_children() if c.kind == MethodDecl]


class EnumDecl(Decl):
    """An enumeration."""

    __cursor_kind__ = 5

    @property
    def name(self) -> str:
        """get the name of a struct declaration."""
        return self.spelling

    @property
    def underlying_type(self) -> Type:
        """get the integer type of an enum declaration."""

        if not hasattr(self, "_enum_type"):
            self._enum_type = dll.clang_getEnumDeclIntegerType(self)
        return self._enum_type

    @property
    def enumerators(self) -> list['EnumConstantDecl']:
        """get the enumerators of an enum declaration."""
        return [EnumConstantDecl(c) for c in self.get_children() if c.kind == EnumConstantDecl]

    def is_scoop_enum(self) -> bool:
        """judge an enum declaration is a scoped enum."""
        return dll.clang_EnumDecl_isScoped(self)


class FieldDecl(Decl):
    """A field (non-static data member) in a struct, union, or C++ class."""

    __cursor_kind__ = 6

    @property
    def name(self) -> str:
        """get the name of a field declaration."""
        return self.spelling

    @property
    def type(self) -> Type:
        """get the type of a field declaration."""
        return dll.clang_getCursorType(self)

    @property
    def default_value(self) -> Expr | None:
        """get the default value of a field declaration."""
        # TODO with get children

        # return dll.clang_getCursorDefaultValue(self)


class EnumConstantDecl(Decl):
    """An enumerator constant."""

    __cursor_kind__ = 7

    @property
    def name(self) -> str:
        """get the name of an enum constant declaration."""
        return self.spelling

    @property
    def type(self) -> Type:
        """get the integer type of an enum constant declaration."""
        return dll.clang_getEnumDeclIntegerType(self)

    @property
    def value(self) -> int:
        """retrieve the integer value of an enum constant declaration."""
        if self.type.is_signed:
            self._enum_value = dll.clang_getEnumConstantDeclValue(self)
        else:
            self._enum_value = dll.clang_getEnumConstantDeclUnsignedValue(self)

        return self._enum_value


class FunctionDecl(Decl):
    """A function."""

    __cursor_kind__ = 8


class VarDecl(Decl):
    """A variable."""

    __cursor_kind__ = 9


class ParmDecl(Decl):
    """A function or method parameter."""

    __cursor_kind__ = 10

# some OBJC decls have been removed


class TypedefDecl(Decl):
    """A typedef."""

    __cursor_kind__ = 20


class MethodDecl(Decl):
    """A C++ class method."""

    __cursor_kind__ = 21


class Namespace(Decl):
    """A C++ namespace."""

    __cursor_kind__ = 22


class LinkageSpec(Decl):
    """A linkage specification, e.g. 'extern "C" { ... }'."""

    __cursor_kind__ = 23


class Constructor(Decl):
    """A C++ constructor."""

    __cursor_kind__ = 24


class Destructor(Decl):
    """A C++ destructor."""

    __cursor_kind__ = 25


class ConversionFunction(Decl):
    """A C++ conversion function."""

    __cursor_kind__ = 26


class TemplateTypeParameter(Decl):
    """A C++ template type parameter."""

    __cursor_kind__ = 27


class NonTypeTemplateParameter(Decl):
    """A C++ non-type template parameter."""

    __cursor_kind__ = 28


class TemplateTemplateParameter(Decl):
    """A C++ template template parameter."""

    __cursor_kind__ = 29


class FunctionTemplate(Decl):
    """A C++ function template."""

    __cursor_kind__ = 30


class ClassTemplate(Decl):
    """A C++ class template."""

    __cursor_kind__ = 31


class ClassTemplatePartialSpecialization(Decl):
    """A C++ class template partial specialization."""

    __cursor_kind__ = 32


class NamespaceAlias(Decl):
    """A C++ namespace alias declaration."""

    __cursor_kind__ = 33


class UsingDirective(Decl):
    """A C++ using directive."""

    __cursor_kind__ = 34


class UsingDeclaration(Decl):
    """A C++ using declaration."""

    __cursor_kind__ = 35


class TypeAliasDecl(Decl):
    """A C++ alias declaration."""

    __cursor_kind__ = 36


class CXXAccessSpecifier(Decl):
    """A C++ access specifier."""

    __cursor_kind__ = 39


class ModuleImportDecl(Decl):
    """A module import declaration."""

    __cursor_kind__ = 600


class TypeAliasTemplateDecl(Decl):
    """A C++ alias template declaration."""

    __cursor_kind__ = 601


class FriendDecl(Decl):
    """A friend declaration."""

    __cursor_kind__ = 603


class ConceptDecl(Decl):
    """A C++20 concept declaration."""

    __cursor_kind__ = 604
