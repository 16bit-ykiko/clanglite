#pragma once

#include <string_view>

namespace pybind11
{
    class module_;
}

namespace clanglite
{
    struct Attr;

    struct Decl
    {
        const void* data = nullptr;
        const void* context = nullptr;

        int Kind();
    };

    struct Expr
    {
        const void* data = nullptr;
        const void* context = nullptr;

        int Kind();
    };

    struct Type;

    struct Stmt
    {
        const void* data = nullptr;
        const void* context = nullptr;

        int Kind();
    };

    extern void register_decl(pybind11::module_& m);
    extern void register_expr(pybind11::module_& m);
    extern void register_stmt(pybind11::module_& m);
}  // namespace clanglite
