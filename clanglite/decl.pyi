
class SourceLocation:
    @property
    def filepath(self) -> str: ...

    @property
    def line(self) -> int: ...

    @property
    def column(self) -> int: ...

    @property
    def offset(self) -> int: ...


class SourceRange:
    @property
    def begin(self) -> SourceLocation: ...

    @property
    def end(self) -> SourceLocation: ...


class Type:

    @property
    def name(self) -> str: ...


class Decl:

    @property
    def location(self) -> SourceLocation: ...

    @property
    def range(self) -> SourceRange: ...


class NameDecl(Decl):

    @property
    def name(self) -> str: ...


class FieldDecl(NameDecl):
    """represents a field declaration"""

    @property
    def index(self) -> int:
        """returns the index of the field declaration"""

    @property
    def type(self) -> Type:
        """returns the type of the field declaration"""


class FunctionDecl(NameDecl):
    """represents a function declaration"""
    ...
