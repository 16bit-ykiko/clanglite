
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


if __name__ == "__main__":
    from clanglite.Core import *
    # from clanglite.AST import *
    import clanglite.AST as AST

    # classes = inspect.getmembers(AST)
#
    # for name, cls in classes:
    #    if inspect.isclass(cls):
    #        print(name, cls)

    tool = ClangTool()

    def callback(stmt: AST.IfStmt) -> None:
        print("find stmt: ", stmt.kind_spelling)

    tool.add_stmt_matcher(AST.IfStmt, callback)

    tool.run()
