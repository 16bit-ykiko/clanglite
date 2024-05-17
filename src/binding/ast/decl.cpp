
#include <pybind11/pybind11.h>
#include <clanglite/ast/decl.h>

namespace py = pybind11;

namespace clanglite{

void register_decl(py::module &m){py::class_<NamespaceDecl, Decl>(m, "NamespaceDecl")
.def_readonly_static("__kind__", &NamespaceDecl::kind)
.def(py::init<>([](Decl decl){ return NamespaceDecl(decl); }))
.def_property_readonly("spelling", &NamespaceDecl::spelling)
.def("is_anonymous", &NamespaceDecl::is_anonymous)
.def("is_inline", &NamespaceDecl::is_inline)
.def("is_nested", &NamespaceDecl::is_nested)
;

py::class_<VarDecl, Decl>(m, "VarDecl")
.def_readonly_static("__kind__", &VarDecl::kind)
.def(py::init<>([](Decl decl){ return VarDecl(decl); }))
.def_property_readonly("spelling", &VarDecl::spelling)
.def_property_readonly("type", &VarDecl::type)
.def_property_readonly("init", &VarDecl::init)
.def("is_constexpr", &VarDecl::is_constexpr)
.def("is_inline", &VarDecl::is_inline)
;

py::class_<FunctionDecl, Decl>(m, "FunctionDecl")
.def_readonly_static("__kind__", &FunctionDecl::kind)
.def(py::init<>([](Decl decl){ return FunctionDecl(decl); }))
.def_property_readonly("spelling", &FunctionDecl::spelling)
;

py::class_<ParmDecl, Decl>(m, "ParmDecl")
.def_readonly_static("__kind__", &ParmDecl::kind)
.def(py::init<>([](Decl decl){ return ParmDecl(decl); }))
;

py::class_<RecordDecl, Decl>(m, "RecordDecl")
.def_readonly_static("__kind__", &RecordDecl::kind)
.def(py::init<>([](Decl decl){ return RecordDecl(decl); }))
;

py::class_<FieldDecl, Decl>(m, "FieldDecl")
.def_readonly_static("__kind__", &FieldDecl::kind)
.def(py::init<>([](Decl decl){ return FieldDecl(decl); }))
;

py::class_<EnumDecl, Decl>(m, "EnumDecl")
.def_readonly_static("__kind__", &EnumDecl::kind)
.def(py::init<>([](Decl decl){ return EnumDecl(decl); }))
;

py::class_<EnumConstantDecl, Decl>(m, "EnumConstantDecl")
.def_readonly_static("__kind__", &EnumConstantDecl::kind)
.def(py::init<>([](Decl decl){ return EnumConstantDecl(decl); }))
;

py::class_<TypedefDecl, Decl>(m, "TypedefDecl")
.def_readonly_static("__kind__", &TypedefDecl::kind)
.def(py::init<>([](Decl decl){ return TypedefDecl(decl); }))
;

py::class_<TypeAliasDecl, Decl>(m, "TypeAliasDecl")
.def_readonly_static("__kind__", &TypeAliasDecl::kind)
.def(py::init<>([](Decl decl){ return TypeAliasDecl(decl); }))
;

}
}