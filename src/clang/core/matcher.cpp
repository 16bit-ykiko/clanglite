
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

    ClangTool::ClangTool() { impl = new StmtMatcher(); }

    ClangTool::~ClangTool() { delete static_cast<StmtMatcher*>(impl); }

    void ClangTool::add_stmt_matcher(int stmt_kind,
                                     const std::function<void(Stmt)>& callback)
    {
        static_cast<StmtMatcher*>(impl)->callbacks.insert(
            std::make_pair(stmt_kind, callback));
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

        StmtMatcher& stmtMatcher = *static_cast<StmtMatcher*>(impl);

        Finder.addMatcher(clang::ast_matchers::stmt().bind("stmt"),
                          &stmtMatcher);
        // Finder.addDynamicMatcher()
        return Tool.run(
            clang::tooling::newFrontendActionFactory(&Finder).get());
    }
}  // namespace clanglite
