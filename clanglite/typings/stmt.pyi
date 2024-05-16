from .basic import *
class DeclStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class NullStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class CompoundStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class CaseStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class DefaultStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class ValueStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class LabelStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class AttributedStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class IfStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class SwitchStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class WhileStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class DoStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class ForStmt:
    def __init__(self, stmt: Stmt) -> None: pass
    @property
    def init(self) -> Decl: pass
    @property
    def condition(self) -> Expr: pass
    @property
    def increment(self) -> Expr: pass
    @property
    def body(self) -> Stmt: pass

class GotoStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class IndirectGotoStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class ContinueStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class BreakStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class ReturnStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class ASMStmt:
    def __init__(self, stmt: Stmt) -> None: pass

class GCCASMSStmt:
    def __init__(self, stmt: Stmt) -> None: pass

