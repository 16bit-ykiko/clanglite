#include <clanglite/ast/decl.h>
#include <clang/AST/Decl.h>

namespace clanglite
{
    int Decl::kind()
    {
        const clang::Decl* decl = static_cast<const clang::Decl*>(data);
        return decl->getKind();
    }

    std::string_view Decl::kind_spelling()
    {
        const clang::Decl* decl = static_cast<const clang::Decl*>(data);
        return decl->getDeclKindName();
    }

    int NamespaceDecl::kind = clang::Decl::Namespace;

    std::string_view NamespaceDecl::spelling()
    {
        const clang::NamespaceDecl* decl =
            static_cast<const clang::NamespaceDecl*>(data);
        return decl->getName();
    }

    bool NamespaceDecl::is_anonymous()
    {
        const clang::NamespaceDecl* decl =
            static_cast<const clang::NamespaceDecl*>(data);
        return decl->isAnonymousNamespace();
    }

    bool NamespaceDecl::is_inline()
    {
        const clang::NamespaceDecl* decl =
            static_cast<const clang::NamespaceDecl*>(data);
        return decl->isInline();
    }

    bool NamespaceDecl::is_nested()
    {
        const clang::NamespaceDecl* decl =
            static_cast<const clang::NamespaceDecl*>(data);
        return decl->isNested();
    }

    int VarDecl::kind = clang::Decl::Var;

    std::string_view VarDecl::spelling()
    {
        const clang::VarDecl* decl = static_cast<const clang::VarDecl*>(data);
        return decl->getName();
    }

    Type VarDecl::type()
    {
        const clang::VarDecl* decl = static_cast<const clang::VarDecl*>(data);
        return Type{decl->getType(), &decl->getASTContext()};
    }

    Expr VarDecl::init()
    {
        const clang::VarDecl* decl = static_cast<const clang::VarDecl*>(data);
        return Expr{decl->getInit(), &decl->getASTContext()};
    }

    bool VarDecl::is_constexpr()
    {
        const clang::VarDecl* decl = static_cast<const clang::VarDecl*>(data);
        return decl->isConstexpr();
    }

    bool VarDecl::is_inline()
    {
        const clang::VarDecl* decl = static_cast<const clang::VarDecl*>(data);
        return decl->isInline();
    }

    int FunctionDecl::kind = clang::Decl::Function;

    std::string_view FunctionDecl::spelling()
    {
        const clang::FunctionDecl* decl =
            static_cast<const clang::FunctionDecl*>(data);
        return decl->getName();
    }

    int ParmDecl::kind = clang::Decl::ParmVar;

    int RecordDecl::kind = clang::Decl::Record;

    int FieldDecl::kind = clang::Decl::Field;

    int EnumDecl::kind = clang::Decl::Enum;

    int EnumConstantDecl::kind = clang::Decl::EnumConstant;

    int TypedefDecl::kind = clang::Decl::Typedef;

    int TypeAliasDecl::kind = clang::Decl::TypeAlias;
}  // namespace clanglite
