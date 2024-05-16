#pragma once

#include <string_view>

namespace pybind11
{
    class module_;
}

namespace clanglite [[clang::annotate("ignore")]]
{
    struct Attr;

    struct Decl
    {
        const void* data = nullptr;
        const void* context = nullptr;

        int kind();
    };

    struct Expr
    {
        const void* data = nullptr;
        const void* context = nullptr;

        int kind();
    };

    struct Type;

    struct Stmt
    {
        const void* data = nullptr;
        const void* context = nullptr;

        int kind();
    };

    extern void register_basic(pybind11::module_& m);
    extern void register_decl(pybind11::module_& m);
    extern void register_expr(pybind11::module_& m);
    extern void register_stmt(pybind11::module_& m);
}  // namespace clang::annotate("ignore")
