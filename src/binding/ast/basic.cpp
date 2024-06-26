#include <pybind11/pybind11.h>
#include <clanglite/ast/basic.h>

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

        py::class_<Type>(m, "Type")
            .def_property_readonly("spelling", &Type::spelling)
            .def("is_const", &Type::is_const)
            .def("is_volatile", &Type::is_volatile)
            .def("is_restrict", &Type::is_restrict);
    }
}  // namespace clanglite
