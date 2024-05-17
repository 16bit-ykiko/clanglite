class Decl:
    @property
    def kind(self) -> int: pass

    @property
    def kind_spelling(self) -> str: pass


class Expr:
    @property
    def kind(self) -> int: pass

    @property
    def kind_spelling(self) -> str: pass


class Stmt:
    @property
    def kind(self) -> int: pass

    @property
    def kind_spelling(self) -> str: pass


class Type:
    @property
    def spelling(self) -> str: pass

    def is_const(self) -> bool: pass

    def is_volatile(self) -> bool: pass

    def is_restrict(self) -> bool: pass
