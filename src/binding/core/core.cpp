#include <pybind11/pybind11.h>
#include <clanglite/core/core.h>

namespace py = pybind11;

PYBIND11_MODULE(clanglite, m)
{
    using namespace clanglite;

    register_stmt(m);
    py::class_<ClangTool>(m, "ClangTool")
        .def(py::init<>())
        .def("add_stmt_matcher", &ClangTool::add_stmt_matcher);
}
