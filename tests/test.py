from ..clanglite import src

tool = clanglite.ClangTool()


def callback(stmt):
    print("find stmt: ", stmt.kind)

    stmt = clanglite.ForStmt(stmt)
    print(stmt.init.kind)


tool.add_stmt_matcher(223, callback)

tool.run()
