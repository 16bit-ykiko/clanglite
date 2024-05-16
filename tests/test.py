
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


if __name__ == "__main__":
    from clanglite.ast import *
    from typing import Callable, TypeVar

    T = TypeVar("T")

    class Tool:
        def __init__(self) -> None:
            self.tool = ClangTool()

        def add_stmt_matcher(self, cls: type[T], callback: Callable[[T], None]) -> None:
            self.tool.add_stmt_matcher(cls.__kind__, callback)  # type: ignore

        def run(self) -> None:
            self.tool.run()

    tool = Tool()

    def callback(stmt: IfStmt) -> None:
        print("find stmt: ", stmt.kind_spelling)

    tool.add_stmt_matcher(IfStmt, callback)

    tool.run()
