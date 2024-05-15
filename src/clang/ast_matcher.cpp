#include "clang/ASTMatchers/ASTMatchers.h"
#include "clang/ASTMatchers/ASTMatchFinder.h"
#include "clang/Tooling/CommonOptionsParser.h"
#include "clang/Tooling/Tooling.h"
#include "clang/Frontend/FrontendActions.h"
#include "clang/Frontend/CompilerInstance.h"
#include "llvm/Support/CommandLine.h"
#include "clang/AST/ASTContext.h"

using namespace clang;
using namespace clang::ast_matchers;
using namespace clang::tooling;

// ASTMatcher to match function declarations
auto FunctionDeclMatcher = functionDecl().bind("function");

class FunctionUsageFinder : public MatchFinder::MatchCallback
{
public:
    virtual void run(const MatchFinder::MatchResult& Result)
    {
        const FunctionDecl* FD =
            Result.Nodes.getNodeAs<FunctionDecl>("function");
        if(FD && !FD->isUsed())
        {
            // If the function is not used, print its name
            llvm::outs() << "Unused function: " << FD->getNameAsString()
                         << "\n";
        }
    }
};

int main(int argc, const char** argv)
{

    // auto OptionsParser = CommonOptionsParser::create(argc, argv);
    // ClangTool Tool(OptionsParser.getCompilations(),
    //                OptionsParser.getSourcePathList());
    //
    //// Create an instance of FunctionUsageFinder to handle matches
    // FunctionUsageFinder FnFinder;
    //
    //// Create a MatchFinder
    // MatchFinder Finder;
    //// Add the FunctionDeclMatcher to the MatchFinder
    // Finder.addMatcher(FunctionDeclMatcher, &FnFinder);
    //
    //// Run the tool with the MatchFinder and FunctionUsageFinder
    // Tool.run(newFrontendActionFactory(&Finder).get());
    // return 0;
}
