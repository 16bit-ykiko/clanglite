#include <pybind11/pybind11.h>
#include <clanglite/binding/ast/stmt.h>

namespace py = pybind11;

PYBIND11_MODULE(clanglite, m) {

    using namespace clanglite;
    
    py::class_<Stmt>(m, "Stmt")
        .def(py::init<>())
        .def("kind", &Stmt::Kind);
}
