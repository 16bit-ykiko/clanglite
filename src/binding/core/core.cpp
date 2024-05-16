#include <pybind11/pybind11.h>
#include <clanglite/core/core.h>
#include <pybind11/functional.h>

namespace py = pybind11;

#define PYBIND11_DETAILED_ERROR_MESSAGES 1

PYBIND11_MODULE(clanglite, m)
{
    using namespace clanglite;

    register_basic(m);
    register_expr(m);
    register_decl(m);
    register_stmt(m);

    py::class_<ClangTool>(m, "ClangTool")
        .def(py::init<>())
        .def("run",
             [](ClangTool& tool)
             {
                 const char* argv[] = {
                     "clanglite",
                     "/home/ykiko/Project/Python/clanglite/build/test.cpp",
                     "--"};
                 int result = tool.run(3, argv);
                 return result;
             })
        .def("add_stmt_matcher", &ClangTool::add_stmt_matcher);
}
