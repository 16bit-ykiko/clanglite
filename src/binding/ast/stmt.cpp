
#include <pybind11/pybind11.h>
#include <clanglite/ast/stmt.h>

namespace py = pybind11;

namespace clanglite{

void register_stmt(py::module &m){py::class_<DeclStmt>(m, "DeclStmt")
.def(py::init<>([](Stmt stmt){ return DeclStmt(stmt); }))
;

py::class_<NullStmt>(m, "NullStmt")
.def(py::init<>([](Stmt stmt){ return NullStmt(stmt); }))
;

py::class_<CompoundStmt>(m, "CompoundStmt")
.def(py::init<>([](Stmt stmt){ return CompoundStmt(stmt); }))
;

py::class_<CaseStmt>(m, "CaseStmt")
.def(py::init<>([](Stmt stmt){ return CaseStmt(stmt); }))
;

py::class_<DefaultStmt>(m, "DefaultStmt")
.def(py::init<>([](Stmt stmt){ return DefaultStmt(stmt); }))
;

py::class_<ValueStmt>(m, "ValueStmt")
.def(py::init<>([](Stmt stmt){ return ValueStmt(stmt); }))
;

py::class_<LabelStmt>(m, "LabelStmt")
.def(py::init<>([](Stmt stmt){ return LabelStmt(stmt); }))
;

py::class_<AttributedStmt>(m, "AttributedStmt")
.def(py::init<>([](Stmt stmt){ return AttributedStmt(stmt); }))
;

py::class_<IfStmt>(m, "IfStmt")
.def(py::init<>([](Stmt stmt){ return IfStmt(stmt); }))
;

py::class_<SwitchStmt>(m, "SwitchStmt")
.def(py::init<>([](Stmt stmt){ return SwitchStmt(stmt); }))
;

py::class_<WhileStmt>(m, "WhileStmt")
.def(py::init<>([](Stmt stmt){ return WhileStmt(stmt); }))
;

py::class_<DoStmt>(m, "DoStmt")
.def(py::init<>([](Stmt stmt){ return DoStmt(stmt); }))
;

py::class_<ForStmt>(m, "ForStmt")
.def(py::init<>([](Stmt stmt){ return ForStmt(stmt); }))
.def_property_readonly("init", &ForStmt::init)
.def_property_readonly("condition", &ForStmt::condition)
.def_property_readonly("increment", &ForStmt::increment)
.def_property_readonly("body", &ForStmt::body)
;

py::class_<GotoStmt>(m, "GotoStmt")
.def(py::init<>([](Stmt stmt){ return GotoStmt(stmt); }))
;

py::class_<IndirectGotoStmt>(m, "IndirectGotoStmt")
.def(py::init<>([](Stmt stmt){ return IndirectGotoStmt(stmt); }))
;

py::class_<ContinueStmt>(m, "ContinueStmt")
.def(py::init<>([](Stmt stmt){ return ContinueStmt(stmt); }))
;

py::class_<BreakStmt>(m, "BreakStmt")
.def(py::init<>([](Stmt stmt){ return BreakStmt(stmt); }))
;

py::class_<ReturnStmt>(m, "ReturnStmt")
.def(py::init<>([](Stmt stmt){ return ReturnStmt(stmt); }))
;

py::class_<ASMStmt>(m, "ASMStmt")
.def(py::init<>([](Stmt stmt){ return ASMStmt(stmt); }))
;

py::class_<GCCASMSStmt>(m, "GCCASMSStmt")
.def(py::init<>([](Stmt stmt){ return GCCASMSStmt(stmt); }))
;

}
}