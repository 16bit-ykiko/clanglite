#include <clanglite/ast/stmt.h>
#include <clang/AST/Stmt.h>

namespace clanglite
{
    int Stmt::Kind()
    {
        const clang::Stmt* stmt = static_cast<const clang::Stmt*>(data);
        return stmt->getStmtClass();
    }
}  // namespace clanglite
