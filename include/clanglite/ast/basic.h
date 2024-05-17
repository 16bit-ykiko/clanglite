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

    struct Type
    {
        char data[8];
        const void* context = nullptr;

        template <typename T, typename U = std::decay_t<T>>
            requires (std::is_trivially_copyable_v<U> && sizeof(U) <= 8)
        Type(T&& t, const void* context)
        {
            ::new (data) T(std::forward<T>(t));
            this->context = context;
        }

        std::string spelling();
        bool is_const();
        bool is_volatile();
        bool is_restrict();
    };

    struct Stmt
    {
        const void* data = nullptr;
        const void* context = nullptr;

        int kind();
        std::string_view kind_spelling();
    };

}  // namespace clang::annotate("ignore")
