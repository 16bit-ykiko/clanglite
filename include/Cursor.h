#pragma once
#include <pybind11/pybind11.h>

namespace py = pybind11;

namespace clanglite
{
    struct Cursor
    {
        const void* data;
        const void* content;

        template <typename T>
        const T* cast() const
        {
            return static_cast<const T*>(data);
        }
    };

    struct SourceLocation
    {
        const char* _filepath;
        unsigned int _filepath_length;
        unsigned int _line;
        unsigned int _column;
        unsigned int _offset;

        py::str filepath() const { return {_filepath, _filepath_length}; }

        py::int_ line() const { return {_line}; }

        py::int_ column() const { return {_column}; }

        py::int_ offset() const { return {_offset}; }
    };

    void register_basic(py::module& m);
}  // namespace clanglite
