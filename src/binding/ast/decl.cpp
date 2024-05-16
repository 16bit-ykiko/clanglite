
#include <pybind11/pybind11.h>
#include <clanglite/ast/decl.h>

namespace py = pybind11;

namespace clanglite{

void register_decl(py::module &m){py::class_<NamespaceDecl, Decl>(m, "NamespaceDecl")
.def_readonly_static("__kind__", &NamespaceDecl::kind)
.def(py::init<>([](Decl decl){ return NamespaceDecl(decl); }))
;

py::class_<VarDecl, Decl>(m, "VarDecl")
.def_readonly_static("__kind__", &VarDecl::kind)
.def(py::init<>([](Decl decl){ return VarDecl(decl); }))
;

py::class_<FunctionDecl, Decl>(m, "FunctionDecl")
.def_readonly_static("__kind__", &FunctionDecl::kind)
.def(py::init<>([](Decl decl){ return FunctionDecl(decl); }))
.def_property_readonly("name", &FunctionDecl::name)
;

}
}