#include <clanglite/ast/expr.h>
#include <clang/AST/Expr.h>

namespace clanglite
{
    int Expr::kind()
    {
        const clang::Expr* expr = static_cast<const clang::Expr*>(data);
        return expr->getStmtClass();
    }

}  // namespace clanglite
