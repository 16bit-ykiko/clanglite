#pragma once

#include <string_view>
#include <clanglite/ast/basic.h>

#define ignore clang::annotate("ignore")
#define property clang::annotate("property")
#define function clang::annotate("function")

namespace clanglite
{
    struct NamespaceDecl : Decl
    {
        static int kind;
        /// return the spelling of the namespace
        [[property]] std::string_view spelling();
        /// return true if the namespace is anonymous
        [[function]] bool is_anonymous();
        /// return true if the namespace is inline
        [[function]] bool is_inline();
        /// return true if the namespace is nested
        [[function]] bool is_nested();
    };

    struct VarDecl : Decl
    {
        static int kind;
        /// return the spelling of the variable
        [[property]] std::string_view spelling();
        /// return the type of the variable
        [[property]] Type type();
        /// return the initialization expression of the variable
        [[property]] Expr init();
        /// return true if the variable is a constexpr
        [[function]] bool is_constexpr();
        /// return true if the variable is (C++17) inline
        [[function]] bool is_inline();
    };

    struct FunctionDecl : Decl
    {
        static int kind;
        /// return the spelling of the function
        [[property]] std::string_view spelling();
    };

    struct ParmDecl : Decl
    {
        static int kind;
    };

    struct RecordDecl : Decl
    {
        static int kind;
    };

    struct FieldDecl : Decl
    {
        static int kind;
    };

    struct EnumDecl : Decl
    {
        static int kind;
    };

    struct EnumConstantDecl : Decl
    {
        static int kind;
    };

    struct TypedefDecl : Decl
    {
        static int kind;
    };

    struct TypeAliasDecl : Decl
    {
        static int kind;
    };

}  // namespace clanglite

#undef ignore
#undef property
#undef function
