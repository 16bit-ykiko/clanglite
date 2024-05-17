#include <clanglite/register.h>
#include <clanglite/core/core.h>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>

PYBIND11_MODULE(internal, m)
{
    namespace py = pybind11;
    using namespace clanglite;
    py::module_ Core = m.def_submodule("Core");
    register_main(Core);

    py::module_ AST = m.def_submodule("AST");
    register_basic(AST);
    register_expr(AST);
    register_decl(AST);
    register_stmt(AST);
}
