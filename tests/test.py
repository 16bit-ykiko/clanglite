
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from clanglite.ast import *

tool = ClangTool()

def callback(stmt: Stmt) -> None:
    print("find stmt: ", stmt.kind)

    stmt2 = ForStmt(stmt)
    print(stmt2.init.kind)

tool.add_stmt_matcher(223, callback)

tool.run()
