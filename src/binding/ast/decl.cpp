#include <pybind11/pybind11.h>
#include <clanglite/ast/decl.h>

namespace py = pybind11;

namespace clanglite
{

    void register_decl(pybind11::module_& m)
    {
        py::class_<Decl>(m, "Decl")
            .def(py::init<>())
            .def_property_readonly("kind", &Decl::Kind);
    }
}  // namespace clanglite
