from clanglite.binding.cursor import Cursor


class Stmt(Cursor):
    pass


class UnexposedStmt(Stmt):
    """
    A statement whose specific kind is not exposed via this
    interface.

    Unexposed statements have the same operations as any other kind of
    statement; one can extract their location information, spelling,
    children, etc. However, the specific kind of the statement is not
    reported.
    """
    __cursor_kind__ = 200


class LabelStmt(Stmt):
    """
    A statement that represents a label.

    In the following example, `start_over` is a label statement:

    ```cpp
    start_over:
      ++counter;
    ```
    """
    __cursor_kind__ = 201


class CompoundStmt(Stmt):
    """
    A group of statements like { stmt stmt }.

    This cursor kind is used to describe compound statements, e.g. function
    bodies.
    """
    __cursor_kind__ = 202


class CaseStmt(Stmt):
    """
    A case statement.
    """
    __cursor_kind__ = 203


class DefaultStmt(Stmt):
    """
    A default statement.
    """
    __cursor_kind__ = 204


class IfStmt(Stmt):
    """
    An if statement
    """
    __cursor_kind__ = 205


class SwitchStmt(Stmt):
    """
    A switch statement.
    """
    __cursor_kind__ = 206


class WhileStmt(Stmt):
    """
    A while statement.
    """
    __cursor_kind__ = 207


class DoStmt(Stmt):
    """
    A do statement.
    """
    __cursor_kind__ = 208


class ForStmt(Stmt):
    """
    A for statement.
    """
    __cursor_kind__ = 209


class GotoStmt(Stmt):
    """
    A goto statement.
    """
    __cursor_kind__ = 210


class IndirectGotoStmt(Stmt):
    """
    An indirect goto statement.
    """
    __cursor_kind__ = 211


class ContinueStmt(Stmt):
    """
    A continue statement.
    """
    __cursor_kind__ = 212


class BreakStmt(Stmt):
    """
    A break statement.
    """
    __cursor_kind__ = 213


class ReturnStmt(Stmt):
    """
    A return statement.
    """
    __cursor_kind__ = 214


class GCCAsmStmt(Stmt):
    """
    A GCC inline assembly statement extension.
    """
    __cursor_kind__ = 215


class AsmStmt(Stmt):
    """
    An inline assembly statement.
    """
    __cursor_kind__ = 216


class CXXCatchStmt(Stmt):
    """
    A C++ catch statement.
    """
    __cursor_kind__ = 223


class CXXTryStmt(Stmt):
    """
    A C++ try statement.
    """
    __cursor_kind__ = 224


class CXXForRangeStmt(Stmt):
    """
    A C++11 range-based for statement.
    """
    __cursor_kind__ = 225


class SEHTryStmt(Stmt):
    """
    Windows Structured Exception Handling's try statement.
    """
    __cursor_kind__ = 226


class SEHExceptStmt(Stmt):
    """
    Windows Structured Exception Handling's except statement.
    """
    __cursor_kind__ = 227


class SEHFinallyStmt(Stmt):
    """
    Windows Structured Exception Handling's finally statement.
    """
    __cursor_kind__ = 228


class MSAsmStmt(Stmt):
    """
    A MS inline assembly statement extension.
    """
    __cursor_kind__ = 229


class NullStmt(Stmt):
    """
    The null statement.
    """
    __cursor_kind__ = 230


class DeclStmt(Stmt):
    """
    Adaptor class for mixing declarations with statements and
    expressions.
    """
    __cursor_kind__ = 231


class SEHLeaveStmt(Stmt):
    """
    Windows Structured Exception Handling's leave statement.
    """
    __cursor_kind__ = 247


def register():
    import inspect

    all_kinds = Cursor.__all_kinds__
    for _, cls in globals().items():
        if inspect.isclass(cls) and hasattr(cls, "__cursor_kind__"):
            kind: int | list[int] = cls.__cursor_kind__

            if isinstance(kind, int):
                all_kinds[kind] = cls
            else:
                for k in kind:
                    all_kinds[k] = cls


register()
