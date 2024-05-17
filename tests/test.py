
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


if __name__ == "__main__":
    from clanglite import AST
    from clanglite.Core import ClangTool

    tool = ClangTool()

    def callback(var: AST.VarDecl) -> None:
        print(f"Found Var: {var.spelling}, type is {var.type.spelling}")

    tool.add_matcher(AST.VarDecl, callback)

    tool.run()
