
class SourceLocation:
    @property
    def filepath(self) -> str: ...

    @property
    def line(self) -> int: ...

    @property
    def column(self) -> int: ...

    @property
    def offset(self) -> int: ...


class Decl:

    @property
    def location(self) -> SourceLocation: ...


class NameDecl(Decl):

    @property
    def name(self) -> str: ...


class FieldDecl(NameDecl):
    """represents a field declaration"""
    ...


class FunctionDecl(NameDecl):
    """represents a function declaration"""
    ...
