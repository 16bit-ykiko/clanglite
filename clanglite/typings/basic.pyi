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
