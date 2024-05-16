#include <pybind11/pybind11.h>
#include <clanglite/ast/expr.h>

namespace py = pybind11;

namespace clanglite
{

    void register_expr(py::module& m)
    {
        py::class_<Expr>(m, "Expr")
            .def(py::init<>())
            .def_property_readonly("kind", &Expr::Kind);
    }
}  // namespace clanglite
