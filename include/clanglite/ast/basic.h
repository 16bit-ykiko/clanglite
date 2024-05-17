#pragma once

#include <string_view>

namespace clanglite [[clang::annotate("ignore")]]
{
    struct Attr;

    struct Decl
    {
        const void* data = nullptr;
        const void* context = nullptr;

        int kind();
        std::string_view kind_spelling();
    };

    struct Expr
    {
        const void* data = nullptr;
        const void* context = nullptr;

        int kind();
        std::string_view kind_spelling();
    };

    struct Type;

    struct Stmt
    {
        const void* data = nullptr;
        const void* context = nullptr;

        int kind();
        std::string_view kind_spelling();
    };

}  // namespace clang::annotate("ignore")
