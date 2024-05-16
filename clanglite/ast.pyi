from typing import Callable
from .typings.stmt import *
from .typings.decl import *
from .typings.expr import *



class ClangTool:
    def __init__(self) -> None:
        pass

    def add_stmt_matcher(self, stmt_kind: int, callback: Callable[[Stmt], None]) -> None:
        pass

    def run(self) -> None:
        pass
