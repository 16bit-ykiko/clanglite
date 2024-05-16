#include <pybind11/pybind11.h>
#include <clanglite/basic.h>

namespace py = pybind11;

namespace clanglite
{
    void register_basic(pybind11::module_& m)
    {
        py::class_<Decl>(m, "Decl")
            .def_property_readonly("kind", &Decl::kind)
            .def_property_readonly("kind_spelling", &Decl::kind_spelling);

        py::class_<Expr>(m, "Expr")
            .def_property_readonly("kind", &Expr::kind)
            .def_property_readonly("kind_spelling", &Expr::kind_spelling);

        py::class_<Stmt>(m, "Stmt")
            .def_property_readonly("kind", &Stmt::kind)
            .def_property_readonly("kind_spelling", &Stmt::kind_spelling);
    }
}  // namespace clanglite
