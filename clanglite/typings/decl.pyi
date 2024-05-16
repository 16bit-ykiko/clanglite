from .basic import *
class NamespaceDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass

class VarDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass

class FunctionDecl(Decl):
    __kind__: int
    def __init__(self, decl: Decl) -> None: pass
    @property
    def name(self) -> int: pass

