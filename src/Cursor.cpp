#include <Cursor.h>

namespace clanglite
{
    void register_basic(py::module& m)
    {
        py::class_<SourceLocation> c(m, "SourceLocation");
        c.def(py::init<const SourceLocation&>());
        c.def_property_readonly("filepath", &SourceLocation::filepath);
        c.def_property_readonly("line", &SourceLocation::line);
        c.def_property_readonly("column", &SourceLocation::column);
        c.def_property_readonly("offset", &SourceLocation::offset);
    }
}  // namespace clanglite

