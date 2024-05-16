#pragma once

#include <clanglite/basic.h>

namespace clanglite
{

    struct DeclStmt : Stmt
    {
        static int kind;
    };

    struct NullStmt : Stmt
    {
        static int kind;
    };

    struct CompoundStmt : Stmt
    {
        static int kind;
    };

    struct CaseStmt : Stmt
    {
        static int kind;
    };

    struct DefaultStmt : Stmt
    {
        static int kind;
    };

    struct LabelStmt : Stmt
    {
        static int kind;
    };

    struct AttributedStmt : Stmt
    {
        static int kind;
    };

    struct IfStmt : Stmt
    {
        static int kind;
    };

    struct SwitchStmt : Stmt
    {
        static int kind;
    };

    struct WhileStmt : Stmt
    {
        static int kind;
    };

    struct DoStmt : Stmt
    {
        static int kind;
    };

    struct ForStmt : Stmt
    {
        static int kind;
        Decl init();
        Expr condition();
        Expr increment();
        Stmt body();
    };

    struct GotoStmt : Stmt
    {
        static int kind;
    };

    struct IndirectGotoStmt : Stmt
    {
        static int kind;
    };

    struct ContinueStmt : Stmt
    {
        static int kind;
    };

    struct BreakStmt : Stmt
    {
        static int kind;
    };

    struct ReturnStmt : Stmt
    {
        static int kind;
    };

    // struct ASMStmt : Stmt
    //{
    //     static int kind;
    // };

    struct GCCASMSStmt : Stmt
    {
        static int kind;
    };

    // TODO:
}  // namespace clanglite
