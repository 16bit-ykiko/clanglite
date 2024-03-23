#include <pybind11/pybind11.h>

namespace clanglite
{
    extern void register_parser(pybind11::module&);
    // extern void register_expr(pybind11::module&);
    extern void register_decl(pybind11::module&);
    // extern void register_stmt(pybind11::module&);
    // extern void register_type(pybind11::module&);

}  // namespace clanglite

PYBIND11_MODULE(clanglite, m)
{
    clanglite::register_parser(m);
    // clanglite::register_expr(m);
    clanglite::register_decl(m);
    // clanglite::register_stmt(m);
    // clanglite::register_type(m);
}

