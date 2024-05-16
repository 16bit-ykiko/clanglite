#include <pybind11/pybind11.h>
#include <clanglite/ast/stmt.h>

namespace py = pybind11;

namespace clanglite
{
    void register_stmt(pybind11::module_& m)
    {
        py::class_<Stmt>(m, "Stmt")
            .def(py::init<>())
            .def_property_readonly("kind", &Stmt::Kind);

        py::class_<ForStmt>(m, "ForStmt")
            .def(py::init<>())
            .def(py::init([](Stmt stmt) { return ForStmt(stmt); }))
            .def_property_readonly("init", &ForStmt::init)
            .def_property_readonly("condition", &ForStmt::condition)
            .def_property_readonly("increment", &ForStmt::increment)
            .def_property_readonly("body", &ForStmt::body);
    }
}  // namespace clanglite

