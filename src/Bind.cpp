#include <Cursor.h>
#include <pybind11/pybind11.h>

namespace py = pybind11;

namespace clanglite
{

    extern void register_parser(pybind11::module&);

    // extern void register_expr(pybind11::module&);
    struct Decl : Cursor
    {
        static void register_(py::module_& m);
    };

    // extern void register_stmt(pybind11::module&);
    // extern void register_type(pybind11::module&);

}  // namespace clanglite

PYBIND11_MODULE(clanglite, m)
{
    clanglite::register_basic(m);
    clanglite::register_parser(m);
    // clanglite::register_expr(m);
    clanglite::Decl::register_(m);
    // clanglite::register_stmt(m);
    // clanglite::register_type(m);
}

