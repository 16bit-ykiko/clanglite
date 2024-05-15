#pragma once

#include <string_view>

namespace pybind11
{
    class module_;
}

namespace clanglite
{
    struct Attr;
    struct Decl;
    struct Stmt;
    struct Expr;
    struct Type;

    extern void register_stmt(pybind11::module_& m);
}  // namespace clanglite
