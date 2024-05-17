#pragma once

#include <functional>
#include <clanglite/ast/stmt.h>

namespace clanglite
{
    struct ClangTool
    {
        void* impl;
        void add_stmt_matcher(int, const std::function<void(Stmt)>&);
        void add_expr_matcher(int, const std::function<void(Expr)>&);
        void add_decl_matcher(int, const std::function<void(Decl)>&);
        int run(int argc, const char** argv);

        ClangTool();
        ~ClangTool();
    };

}  // namespace clanglite
