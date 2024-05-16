#include <clanglite/ast/stmt.h>
#include <clang/AST/Stmt.h>

namespace clanglite
{
    int Stmt::kind()
    {
        const clang::Stmt* stmt = static_cast<const clang::Stmt*>(data);
        return stmt->getStmtClass();
    }

    int DeclStmt::kind = clang::Stmt::StmtClass::DeclStmtClass;

    int NullStmt::kind = clang::Stmt::StmtClass::NullStmtClass;

    int CompoundStmt::kind = clang::Stmt::StmtClass::CompoundStmtClass;

    int CaseStmt::kind = clang::Stmt::StmtClass::CaseStmtClass;

    int DefaultStmt::kind = clang::Stmt::StmtClass::DefaultStmtClass;

    int LabelStmt::kind = clang::Stmt::StmtClass::LabelStmtClass;

    int AttributedStmt::kind = clang::Stmt::StmtClass::AttributedStmtClass;

    int IfStmt::kind = clang::Stmt::StmtClass::IfStmtClass;

    int SwitchStmt::kind = clang::Stmt::StmtClass::SwitchStmtClass;

    int WhileStmt::kind = clang::Stmt::StmtClass::WhileStmtClass;

    int DoStmt::kind = clang::Stmt::StmtClass::DoStmtClass;

    int ForStmt::kind = clang::Stmt::StmtClass::ForStmtClass;

    int GotoStmt::kind = clang::Stmt::StmtClass::GotoStmtClass;

    int IndirectGotoStmt::kind = clang::Stmt::StmtClass::IndirectGotoStmtClass;

    int ContinueStmt::kind = clang::Stmt::StmtClass::ContinueStmtClass;

    int BreakStmt::kind = clang::Stmt::StmtClass::BreakStmtClass;

    int ReturnStmt::kind = clang::Stmt::StmtClass::ReturnStmtClass;

    int GCCASMSStmt::kind = clang::Stmt::StmtClass::GCCAsmStmtClass;

    std::string_view Stmt::kind_spelling()
    {
        const clang::Stmt* stmt = static_cast<const clang::Stmt*>(data);
        return stmt->getStmtClassName();
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
