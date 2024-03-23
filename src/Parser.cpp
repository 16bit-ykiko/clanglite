#include <Decl.h>

#include <clang/Tooling/Tooling.h>
#include <llvm/Support/CommandLine.h>
#include <clang/Tooling/CommonOptionsParser.h>

using namespace clang;
using namespace clang::ast_matchers;
namespace py = pybind11;

int run()
{
    llvm::outs() << "Running tool\n";
    llvm::cl::OptionCategory MyToolCategory("my-tool options");

    int argc = 2;
    const char* argv[] = {"xxx", "/home/ykiko/Project/Python/clanglite/build/test.cpp", "--"};
    auto OptionsParser = clang::tooling::CommonOptionsParser::create(argc, argv, MyToolCategory);

    clang::tooling::ClangTool Tool(OptionsParser->getCompilations(), OptionsParser->getSourcePathList());

    MatchFinder Finder;
    Finder.addMatcher(ast_matchers::decl().bind("decl"), &clanglite::DeclCallback::instance);

    return Tool.run(clang::tooling::newFrontendActionFactory(&Finder).get());
}

namespace clanglite
{
    void register_parser(py::module& m) { m.def("run", &run); }
}  // namespace clanglite

