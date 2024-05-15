
#include <clanglite/clang/core.h>
#include <clanglite/binding/ast/stmt.h>

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

    int run(int argc, const char** argv)
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

        StmtMatcher stmtMatcher;
        Finder.addMatcher(clang::ast_matchers::stmt().bind("stmt"),
                          &stmtMatcher);
        // Finder.addDynamicMatcher()
        return Tool.run(
            clang::tooling::newFrontendActionFactory(&Finder).get());
    }
}  // namespace clanglite
