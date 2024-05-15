#pragma once

#include <functional>
#include <clanglite/ast/stmt.h>

namespace clanglite
{
    struct ClangTool
    {
        void* impl;
        void add_stmt_matcher(int, const std::function<void(Stmt)>&);
        int run(int argc, const char** argv);

        ClangTool();
        ~ClangTool();
    };

}  // namespace clanglite
