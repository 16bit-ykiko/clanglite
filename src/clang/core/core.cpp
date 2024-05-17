
#include <clanglite/core/core.h>

#include <clang/Tooling/Tooling.h>
#include <llvm/Support/CommandLine.h>
#include <clang/ASTMatchers/ASTMatchFinder.h>
#include <clang/Tooling/CommonOptionsParser.h>

namespace clanglite
{

    struct StmtMatcher : public clang::ast_matchers::MatchFinder::MatchCallback
    {
        using Callback = std::function<void(Stmt)>;
        std::multimap<int, Callback> callbacks;

        virtual void
            run(const clang::ast_matchers::MatchFinder::MatchResult& Result)
        {
            const clang::Stmt* stmt =
                Result.Nodes.getNodeAs<clang::Stmt>("stmt");

            auto range = callbacks.equal_range(stmt->getStmtClass());

            for(auto it = range.first; it != range.second; ++it)
            {
                it->second(Stmt(stmt, Result.Context));
            }
        }
    };

    struct ExprMathcer : public clang::ast_matchers::MatchFinder::MatchCallback
    {
        using Callback = std::function<void(Expr)>;
        std::multimap<int, Callback> callbacks;

        virtual void
            run(const clang::ast_matchers::MatchFinder::MatchResult& Result)
        {
            const clang::Expr* expr =
                Result.Nodes.getNodeAs<clang::Expr>("expr");

            auto range = callbacks.equal_range(expr->getStmtClass());

            for(auto it = range.first; it != range.second; ++it)
            {
                it->second(Expr(expr, Result.Context));
            }
        }
    };

    struct DeclMatcher : public clang::ast_matchers::MatchFinder::MatchCallback
    {
        using Callback = std::function<void(Decl)>;
        std::multimap<int, Callback> callbacks;

        virtual void
            run(const clang::ast_matchers::MatchFinder::MatchResult& Result)
        {
            const clang::Decl* decl =
                Result.Nodes.getNodeAs<clang::Decl>("decl");

            auto range = callbacks.equal_range(decl->getKind());

            for(auto it = range.first; it != range.second; ++it)
            {
                it->second(Decl(decl, Result.Context));
            }
        }
    };

    struct Data
    {
        StmtMatcher stmtMatcher;
        ExprMathcer exprMatcher;
        DeclMatcher declMatcher;
    };

    ClangTool::ClangTool() { impl = new Data(); }

    ClangTool::~ClangTool() { delete static_cast<Data*>(impl); }

    void ClangTool::add_stmt_matcher(int stmt_kind,
                                     const std::function<void(Stmt)>& callback)
    {
        StmtMatcher& stmtMatcher = static_cast<Data*>(impl)->stmtMatcher;
        stmtMatcher.callbacks.insert({stmt_kind, callback});
    }

    void ClangTool::add_expr_matcher(int expr_kind,
                                     const std::function<void(Expr)>& callback)
    {
        ExprMathcer& exprMatcher = static_cast<Data*>(impl)->exprMatcher;
        exprMatcher.callbacks.insert({expr_kind, callback});
    }

    void ClangTool::add_decl_matcher(int decl_kind,
                                     const std::function<void(Decl)>& callback)
    {
        DeclMatcher& declMatcher = static_cast<Data*>(impl)->declMatcher;
        llvm::outs() << "Adding decl matcher\n";
        declMatcher.callbacks.insert({decl_kind, callback});
    }

    int ClangTool::run(int argc, const char** argv)
    {
        llvm::outs() << "Running tool\n";
        llvm::cl::OptionCategory MyToolCategory("my-tool options");

        auto OptionsParser =
            clang::tooling::CommonOptionsParser::create(argc,
                                                        argv,
                                                        MyToolCategory);

        clang::tooling::ClangTool Tool(OptionsParser->getCompilations(),
                                       OptionsParser->getSourcePathList());

        clang::ast_matchers::MatchFinder Finder;

        auto& data = *static_cast<Data*>(impl);

        Finder.addMatcher(clang::ast_matchers::stmt().bind("stmt"),
                          &data.stmtMatcher);
        Finder.addMatcher(clang::ast_matchers::expr().bind("expr"),
                          &data.exprMatcher);
        Finder.addMatcher(clang::ast_matchers::decl().bind("decl"),
                          &data.declMatcher);
        // Finder.addDynamicMatcher()

        return Tool.run(
            clang::tooling::newFrontendActionFactory(&Finder).get());
    }
}  // namespace clanglite
