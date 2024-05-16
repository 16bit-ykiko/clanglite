#pragma once

#include <clanglite/basic.h>

namespace clanglite
{

    struct DeclStmt : Stmt
    {
    };

    struct NullStmt : Stmt
    {
    };

    struct CompoundStmt : Stmt
    {
    };

    struct CaseStmt : Stmt
    {
    };

    struct DefaultStmt : Stmt
    {
    };

    struct ValueStmt : Stmt
    {
    };

    struct LabelStmt : Stmt
    {
    };

    struct AttributedStmt : Stmt
    {
    };

    struct IfStmt : Stmt
    {
    };

    struct SwitchStmt : Stmt
    {
    };

    struct WhileStmt : Stmt
    {
    };

    struct DoStmt : Stmt
    {
    };

    struct ForStmt : Stmt
    {
        Decl init();
        Expr condition();
        Expr increment();
        Stmt body();
    };

    struct GotoStmt : Stmt
    {
    };

    struct IndirectGotoStmt : Stmt
    {
    };

    struct ContinueStmt : Stmt
    {
    };

    struct BreakStmt : Stmt
    {
    };

    struct ReturnStmt : Stmt
    {
    };

    struct ASMStmt : Stmt
    {
    };

    struct GCCASMSStmt : Stmt
    {
    };

    // TODO:
}  // namespace clanglite
