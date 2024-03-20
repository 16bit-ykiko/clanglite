from clanglite.binding.parser import *
from clanglite.binding.ast.decl import *
from clanglite.binding.ast.expr import *


def OnFieldDecl(decl: FieldDecl):
    print(decl.name)


def OnFunctionDecl(decl: FunctionDecl):
    print(f"found function {decl.spelling}")


def OnBinaryExpr(expr: BinaryExpr):
    print(f"found binary expression {expr.operator}")


def main():
    parser = Parser("/home/ykiko/Project/Python/clanglite/main.cpp")

    parser.add_matcher(FunctionDecl, OnFunctionDecl)
    parser.add_matcher(BinaryExpr, OnBinaryExpr)
    parser.run()


if __name__ == "__main__":
    main()
