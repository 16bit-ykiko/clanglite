from clanglite.binding.cursor import Cursor


class Ref(Cursor):
    pass


class TypeRef(Ref):
    """
    A reference to a type declaration.

    A type reference occurs anywhere where a type is named but not
    declared. For example, given:

    ```cpp
    typedef unsigned size_type;
    size_type size;
    ```

    The typedef is a declaration of `size_type(TypedefDecl)`,
    while the type of the variable `size` is referenced. The cursor
    referenced by the type of size is the typedef for `size_type`.
    """

    __cursor_kind__ = 43


class CXXBaseSpecifier(Ref):

    __cursor_kind__ = 44


class TemplateRef(Ref):
    """
    A reference to a class template, function template, template
    template parameter, or class template partial specialization.
    """

    __cursor_kind__ = 45


class NamespaceRef(Ref):
    """A reference to a namespace or namespace alias."""
    __cursor_kind__ = 46


class MemberRef(Ref):
    """
    A reference to a member of a struct, union, or class that occurs in
    some non-expression context, e.g., a designated initializer.
    """
    __cursor_kind__ = 47


class LabelRef(Ref):
    """
    A reference to a labeled statement.

    This cursor kind is used to describe the jump to "start_over" in the
    goto statement in the following example:

    ```cpp
      start_over:
        ++counter;

        goto start_over;
    ```

    A label reference cursor refers to a label statement.

    """
    __cursor_kind__ = 48


class OverloadedDeclRef(Ref):
    """
    A reference to a set of overloaded functions or function templates
    that has not yet been resolved to a specific function or function template.

    An overloaded declaration reference cursor occurs in C++ templates where
    a dependent name refers to a function. For example:

    ```cpp
    template<typename T> void swap(T&, T&);

    struct X { ... };
    void swap(X&, X&);

    template<typename T>
    void reverse(T first, T last) {
      while (first < last - 1) {
        swap(first, --last);
        ++first;
      }
    }

    struct Y { };
    void swap(Y&, Y&);
    ```

    Here, the identifier `swap` is associated with an overloaded declaration
    reference. In the template definition, `swap` refers to either of the two
    `swap` functions declared above, so both results will be available. At
    instantiation time, `swap` may also refer to other functions found via
    argument-dependent lookup (e.g., the `swap` function at the end of the
    example).

    The functions `getNumOverloadedDecls` and `getOverloadedDecl`can be 
    used to retrieve the definitions referenced by this cursor.
    """

    __cursor_kind__ = 49


class VariableRef(Ref):
    """
    A reference to a variable that occurs in some non-expression
    context, e.g., a C++ lambda capture list.
    """
    __cursor_kind__ = 50


def register():
    import inspect
    for name, cls in globals().items():
        if inspect.isclass(cls) and issubclass(cls, Ref) and cls is not Ref:
            Cursor.__all_kinds__[cls.__cursor_kind__] = cls


register()
