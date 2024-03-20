from clanglite.binding.ast import attr, decl, expr, other, ref, stmt


def register():
    attr.register()
    decl.register()
    expr.register()
    other.register()
    ref.register()
    stmt.register()


register()
