#include <pybind11/pybind11.h>
#include <clanglite/ast/stmt.h>

namespace py = pybind11;

namespace clanglite
{
    void register_stmt(pybind11::module_& m)
    {
        using namespace clanglite;

        py::class_<Stmt>(m, "Stmt").def(py::init<>()).def("kind", &Stmt::Kind);
    }
}  // namespace clanglite

