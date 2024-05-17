#include <clanglite/core/core.h>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>

namespace py = pybind11;

namespace clanglite
{
    void register_main(pybind11::module_& m)
    {

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
}  // namespace clanglite

