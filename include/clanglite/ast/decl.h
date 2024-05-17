#pragma once

#include "basic.h"

namespace clanglite
{
    struct NamespaceDecl : Decl
    {
        static int kind;
    };

    struct VarDecl : Decl
    {
        static int kind;
    };

    struct FunctionDecl : Decl
    {
        static int kind;
        std::string_view name();
    };
}  // namespace clanglite
