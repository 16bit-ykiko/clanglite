#pragma once

#include <Cursor.h>
#include <pybind11/pybind11.h>
#include <clang/ASTMatchers/ASTMatchers.h>
#include <clang/ASTMatchers/ASTMatchFinder.h>

namespace py = pybind11;
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

    void register_decl(py::module& m);
}  // namespace clanglite

namespace clanglite
{
    struct Decl : Cursor
    {
        static void register_(py::module_& m)
        {
            py::class_<Decl> c(m, "Decl");
            // c.def_static("_kind_", clang::Decl::Kind::)
        }
    };

    struct NamedDecl : Decl
    {
        py::str name()
        {
            auto decl = static_cast<const clang::NamedDecl*>(data);
            auto name_ref = decl->getName();
            return py::str(name_ref.data(), name_ref.size());
        }

        static void register_(py::module_& m)
        {
            py::class_<NamedDecl, Decl> c(m, "NamedDecl");

            c.def_property_readonly("name", &NamedDecl::name);
        }
    };

    struct FieldDecl : NamedDecl
    {
        static void register_(py::module_& m)
        {
            py::class_<FieldDecl, NamedDecl> c(m, "FieldDecl");
            static int kind = clang::Decl::Kind::Field;
            c.def_readonly_static("_kind_", &kind);
        }
    };
}  // namespace clanglite
