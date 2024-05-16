
#include <pybind11/pybind11.h>
#include <clanglite/ast/stmt.h>

namespace py = pybind11;

namespace clanglite{

void register_stmt(py::module &m){py::class_<DeclStmt, Stmt>(m, "DeclStmt")
.def_readonly_static("__kind__", &DeclStmt::kind)
.def(py::init<>([](Stmt stmt){ return DeclStmt(stmt); }))
;

py::class_<NullStmt, Stmt>(m, "NullStmt")
.def_readonly_static("__kind__", &NullStmt::kind)
.def(py::init<>([](Stmt stmt){ return NullStmt(stmt); }))
;

py::class_<CompoundStmt, Stmt>(m, "CompoundStmt")
.def_readonly_static("__kind__", &CompoundStmt::kind)
.def(py::init<>([](Stmt stmt){ return CompoundStmt(stmt); }))
;

py::class_<CaseStmt, Stmt>(m, "CaseStmt")
.def_readonly_static("__kind__", &CaseStmt::kind)
.def(py::init<>([](Stmt stmt){ return CaseStmt(stmt); }))
;

py::class_<DefaultStmt, Stmt>(m, "DefaultStmt")
.def_readonly_static("__kind__", &DefaultStmt::kind)
.def(py::init<>([](Stmt stmt){ return DefaultStmt(stmt); }))
;

py::class_<LabelStmt, Stmt>(m, "LabelStmt")
.def_readonly_static("__kind__", &LabelStmt::kind)
.def(py::init<>([](Stmt stmt){ return LabelStmt(stmt); }))
;

py::class_<AttributedStmt, Stmt>(m, "AttributedStmt")
.def_readonly_static("__kind__", &AttributedStmt::kind)
.def(py::init<>([](Stmt stmt){ return AttributedStmt(stmt); }))
;

py::class_<IfStmt, Stmt>(m, "IfStmt")
.def_readonly_static("__kind__", &IfStmt::kind)
.def(py::init<>([](Stmt stmt){ return IfStmt(stmt); }))
;

py::class_<SwitchStmt, Stmt>(m, "SwitchStmt")
.def_readonly_static("__kind__", &SwitchStmt::kind)
.def(py::init<>([](Stmt stmt){ return SwitchStmt(stmt); }))
;

py::class_<WhileStmt, Stmt>(m, "WhileStmt")
.def_readonly_static("__kind__", &WhileStmt::kind)
.def(py::init<>([](Stmt stmt){ return WhileStmt(stmt); }))
;

py::class_<DoStmt, Stmt>(m, "DoStmt")
.def_readonly_static("__kind__", &DoStmt::kind)
.def(py::init<>([](Stmt stmt){ return DoStmt(stmt); }))
;

py::class_<ForStmt, Stmt>(m, "ForStmt")
.def_readonly_static("__kind__", &ForStmt::kind)
.def(py::init<>([](Stmt stmt){ return ForStmt(stmt); }))
.def_property_readonly("init", &ForStmt::init)
.def_property_readonly("condition", &ForStmt::condition)
.def_property_readonly("increment", &ForStmt::increment)
.def_property_readonly("body", &ForStmt::body)
;

py::class_<GotoStmt, Stmt>(m, "GotoStmt")
.def_readonly_static("__kind__", &GotoStmt::kind)
.def(py::init<>([](Stmt stmt){ return GotoStmt(stmt); }))
;

py::class_<IndirectGotoStmt, Stmt>(m, "IndirectGotoStmt")
.def_readonly_static("__kind__", &IndirectGotoStmt::kind)
.def(py::init<>([](Stmt stmt){ return IndirectGotoStmt(stmt); }))
;

py::class_<ContinueStmt, Stmt>(m, "ContinueStmt")
.def_readonly_static("__kind__", &ContinueStmt::kind)
.def(py::init<>([](Stmt stmt){ return ContinueStmt(stmt); }))
;

py::class_<BreakStmt, Stmt>(m, "BreakStmt")
.def_readonly_static("__kind__", &BreakStmt::kind)
.def(py::init<>([](Stmt stmt){ return BreakStmt(stmt); }))
;

py::class_<ReturnStmt, Stmt>(m, "ReturnStmt")
.def_readonly_static("__kind__", &ReturnStmt::kind)
.def(py::init<>([](Stmt stmt){ return ReturnStmt(stmt); }))
;

py::class_<GCCASMSStmt, Stmt>(m, "GCCASMSStmt")
.def_readonly_static("__kind__", &GCCASMSStmt::kind)
.def(py::init<>([](Stmt stmt){ return GCCASMSStmt(stmt); }))
;

}
}