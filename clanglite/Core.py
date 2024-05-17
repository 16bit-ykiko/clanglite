
from . import AST
from .internal import Core  # type: ignore
from typing import Callable, TypeVar, Any
T = TypeVar("T")


class Cache:
    def __init__(self):
        self.stmts: dict[int, type] = {}
        self.exprs: dict[int, type] = {}
        self.decls: dict[int, type] = {}

        for _, cls in AST.__dict__.items():
            if isinstance(cls, type):
                if issubclass(cls, AST.Stmt) and cls is not AST.Stmt:
                    self.stmts[cls.__kind__] = cls  # type: ignore
                elif issubclass(cls, AST.Expr) and cls is not AST.Expr:
                    self.exprs[cls.__kind__] = cls  # type: ignore
                elif issubclass(cls, AST.Decl) and cls is not AST.Decl:
                    self.decls[cls.__kind__] = cls  # type: ignore


class ClangTool:
    cache = Cache()

    def __init__(self) -> None:
        self.tool = Core.ClangTool()  # type: ignore

    def add_stmt_matcher(self, cls: type[T], callback: Callable[[T], None]) -> None:
        kind: int = cls.__kind__  # type: ignore
        if issubclass(cls, AST.Stmt):
            def wrapper(node: Any) -> None:
                callback(self.cache.stmts[kind](node))
            self.tool.add_stmt_matcher(kind, wrapper)  # type: ignore

    def run(self) -> None:
        self.tool.run()  # type: ignore
