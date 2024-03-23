#pragma once

#include <Cursor.h>

#include <clang/ASTMatchers/ASTMatchers.h>
#include <clang/ASTMatchers/ASTMatchFinder.h>

namespace ast_matchers = clang::ast_matchers;
using MatchFinder = clang::ast_matchers::MatchFinder;

namespace clanglite
{

    struct DeclCallback : public MatchFinder::MatchCallback
    {
        static DeclCallback instance;
        std::vector<std::pair<int, py::function>> callbacks;
        virtual void run(const MatchFinder::MatchResult& Result);
    };

    struct Decl : Cursor
    {
        SourceLocation location();
        static void register_(py::module_& m);
    };

    struct NamedDecl : Decl
    {
        py::str name();
        static void register_(py::module_& m);
    };

    struct FieldDecl : NamedDecl
    {
        static void register_(py::module_& m);
    };

    struct StructDecl : NamedDecl
    {
        static void register_(py::module_& m);
    };
}  // namespace clanglite
