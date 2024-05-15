
#include <clang/Tooling/Tooling.h>
#include <llvm/Support/CommandLine.h>
#include <clang/Tooling/CommonOptionsParser.h>
#include <clang/ASTMatchers/ASTMatchFinder.h>

#include <iostream>
using namespace clang;
using namespace clang::ast_matchers;

namespace clanglite
{
    using MatchFinder = clang::ast_matchers::MatchFinder;

    struct Decl
    {
        const void* data;
        const void* content;
    };

    struct DeclCallback : public MatchFinder::MatchCallback
    {
        static DeclCallback instance;
        using Callback = std::function<void(Decl)>;
        std::multimap<int, Callback> callbacks;

        virtual void run(const MatchFinder::MatchResult& Result)
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

    DeclCallback DeclCallback::instance;

    void add_decl(int kind, DeclCallback::Callback callback)
    {
        DeclCallback::instance.callbacks.emplace(kind, callback);
        clang::Type* type;
        auto c = type->getTypeClass();
        std::cout << std::endl;
        std::endl(std::cout);
    }
}  // namespace clanglite

int run()
{
    llvm::outs() << "Running tool\n";
    llvm::cl::OptionCategory MyToolCategory("my-tool options");

    int argc = 2;
    const char* argv[] = {"xxx",
                          "/home/ykiko/Project/Python/clanglite/build/test.cpp",
                          "--"};
    auto OptionsParser =
        clang::tooling::CommonOptionsParser::create(argc, argv, MyToolCategory);

    clang::tooling::ClangTool Tool(OptionsParser->getCompilations(),
                                   OptionsParser->getSourcePathList());

    MatchFinder Finder;
    Finder.addMatcher(ast_matchers::decl().bind("decl"),
                      &clanglite::DeclCallback::instance);
    // Finder.addDynamicMatcher()
    return Tool.run(clang::tooling::newFrontendActionFactory(&Finder).get());
}
