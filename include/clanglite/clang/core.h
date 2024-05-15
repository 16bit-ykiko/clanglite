#pragma once

#include <clang/Tooling/Tooling.h>
#include <llvm/Support/CommandLine.h>
#include <clang/ASTMatchers/ASTMatchFinder.h>
#include <clang/Tooling/CommonOptionsParser.h>

namespace clanglite {

    int run(int argc, const char** argv);

}