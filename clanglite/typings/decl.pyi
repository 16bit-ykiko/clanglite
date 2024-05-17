from .basic import *
class NamespaceDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass
    @property
    def spelling(self) -> int: pass
    def is_anonymous(self) -> bool: pass
    def is_inline(self) -> bool: pass
    def is_nested(self) -> bool: pass

class VarDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass
    @property
    def spelling(self) -> int: pass
    @property
    def type(self) -> Type: pass
    @property
    def init(self) -> Expr: pass
    def is_constexpr(self) -> bool: pass
    def is_inline(self) -> bool: pass

class FunctionDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass
    @property
    def spelling(self) -> int: pass

class ParmDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass

class RecordDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass

class FieldDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass

class EnumDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass

class EnumConstantDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass

class TypedefDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass

class TypeAliasDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass

