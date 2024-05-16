#include <clanglite/ast/decl.h>
#include <clang/AST/Decl.h>

namespace clanglite
{
    int Decl::kind()
    {
        const clang::Decl* decl = static_cast<const clang::Decl*>(data);
        return decl->getKind();
    }

}  // namespace clanglite
