namespace pybind11
{
    class module_;
}

namespace clanglite
{
    // Main
    extern void register_main(pybind11::module_& m);

    // AST
    extern void register_basic(pybind11::module_& m);
    extern void register_decl(pybind11::module_& m);
    extern void register_expr(pybind11::module_& m);
    extern void register_stmt(pybind11::module_& m);
}  // namespace clanglite
