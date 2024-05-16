#include <clanglite/ast/stmt.h>
#include <clang/AST/Stmt.h>

namespace clanglite
{
    int Stmt::Kind()
    {
        const clang::Stmt* stmt = static_cast<const clang::Stmt*>(data);
        return stmt->getStmtClass();
    }

    Decl ForStmt::init()
    {
        const clang::ForStmt* stmt = static_cast<const clang::ForStmt*>(data);
        return Decl{stmt->getInit()};
    }

    Expr ForStmt::condition()
    {
        const clang::ForStmt* stmt = static_cast<const clang::ForStmt*>(data);
        return Expr{stmt->getCond()};
    }

    Expr ForStmt::increment()
    {
        const clang::ForStmt* stmt = static_cast<const clang::ForStmt*>(data);
        return Expr{stmt->getInc()};
    }

    Stmt ForStmt::body()
    {
        const clang::ForStmt* stmt = static_cast<const clang::ForStmt*>(data);
        return Stmt{stmt->getBody()};
    }
}  // namespace clanglite
