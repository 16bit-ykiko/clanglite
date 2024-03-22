from .type import Type
from ..config import dll
from ..cursor import Cursor


class Attr(Cursor):
    pass


class Decl(Cursor):

    def attributes(self) -> list[Attr]:
        """get the attributes of a declaration."""
        return []


class Expr(Cursor):

    @property
    def type(self) -> Type:
        """get the type of the expression"""
        return dll.clang_getCursorType(self)

    @property
    def is_constant(self) -> bool:
        """judge an expression can be constant"""
        # TODO add is constant expression to libclang
        return False


class Ref(Cursor):
    pass


class Stmt(Cursor):
    pass
