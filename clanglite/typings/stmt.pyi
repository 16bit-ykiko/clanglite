from .basic import *
class DeclStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class NullStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class CompoundStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class CaseStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class DefaultStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class LabelStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class AttributedStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class IfStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class SwitchStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class WhileStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class DoStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class ForStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass
    def init(self) -> Decl: pass
    def condition(self) -> Expr: pass
    def increment(self) -> Expr: pass
    def body(self) -> Stmt: pass

class GotoStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class IndirectGotoStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class ContinueStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class BreakStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class ReturnStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

class GCCASMSStmt(Stmt):
    __kind__: int
    def __init__(self, stmt: Stmt) -> None: pass

