#include <pybind11/pybind11.h>
#include <clanglite/basic.h>

namespace py = pybind11;

namespace clanglite
{
    void register_basic(pybind11::module_& m)
    {
        py::class_<Decl>(m, "Decl")
            .def(py::init<>())
            .def_property_readonly("kind", &Decl::kind);

        py::class_<Expr>(m, "Expr")
            .def(py::init<>())
            .def_property_readonly("kind", &Expr::kind);

        py::class_<Stmt>(m, "Stmt")
            .def(py::init<>())
            .def_property_readonly("kind", &Stmt::kind);
    }
}  // namespace clanglite
