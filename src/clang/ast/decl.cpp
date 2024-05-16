#include <clanglite/ast/decl.h>
#include <clang/AST/Decl.h>

namespace clanglite
{
    int Decl::kind()
    {
        const clang::Decl* decl = static_cast<const clang::Decl*>(data);
        return decl->getKind();
    }

    int NamespaceDecl::kind = clang::Decl::Namespace;

    int VarDecl::kind = clang::Decl::Var;

    int FunctionDecl::kind = clang::Decl::Function;

    std::string_view Decl::kind_spelling()
    {
        const clang::Decl* decl = static_cast<const clang::Decl*>(data);
        return decl->getDeclKindName();
    }

    std::string_view FunctionDecl::name()
    {
        const clang::FunctionDecl* decl =
            static_cast<const clang::FunctionDecl*>(data);
        return decl->getName();
    }

}  // namespace clanglite
