from clanglite.binding.cursor import Cursor


class Expr(Cursor):
    pass


class UnexposedExpr(Expr):
    """
    An expression whose specific kind is not exposed via this interface.

    Unexposed expressions have the same operations as any other kind of
    expression; one can extract their location information, spelling,
    children, etc. However, the specific kind of the expression is not
    reported.
    """
    __kind__ = 100


class DeclRefExpr(Expr):
    """
    An expression that refers to some value declaration, such as a function,
    variable, or enumerator.

    For example, in the following code:

    ```cpp
    int foo;
    int bar;
    foo = bar;
    ```

    The expression `bar` is a `DeclRefExpr` that refers to the variable
    `bar`.
    """
    __kind__ = 101


class MemberRefExpr(Expr):
    """
    An expression that refers to a member of a struct, union,
    class, Objective-C class, etc.
    """

    __kind__ = 102


class CallExpr(Expr):
    """
    An expression that calls a function.
    """

    __kind__ = 103


class BlockExpr(Expr):
    """
    An expression that represents a block literal.
    """

    __kind__ = 105


class IntegerLiteral(Expr):
    """
    An integer literal.
    """

    __kind__ = 106


class FloatingLiteral(Expr):
    """
    A floating point number literal.
    """

    __kind__ = 107


class ImaginaryLiteral(Expr):
    """
    An imaginary number literal.
    """

    __kind__ = 108


class StringLiteral(Expr):
    """
    A string literal.
    """

    __kind__ = 109


class CharacterLiteral(Expr):
    """
    A character literal.
    """

    __kind__ = 110


class ParenExpr(Expr):
    """
    A parenthesized expression, e.g. `(1)`.
    """

    __kind__ = 111


class UnaryOperator(Expr):
    """
    A unary operator expression.
    """

    __kind__ = 112


class ArraySubscriptExpr(Expr):
    """
    An array subscript expression.
    """

    __kind__ = 113


class BinaryOperator(Expr):
    """
    A binary operator expression.
    """

    __kind__ = 114


class CompoundAssignOperator(Expr):
    """
    A compound assignment operator expression.
    """

    __kind__ = 115


class ConditionalOperator(Expr):
    """
    The ?: ternary operator.
    """

    __kind__ = 116


class CStyleCastExpr(Expr):
    """
    CStyleCastExpr = 117,
    An explicit cast in C (C99 6.5.4) or a C-style cast in C++
    (C++ [expr.cast]), which uses the syntax (Type)expr.

    For example: (int)f.
    """

    __kind__ = 117


class CompoundLiteralExpr(Expr):
    """
    CompoundLiteralExpr = 118,
    A compound literal expression.

    This kind of expression has no direct equivalent in the C++ AST.

    For example: (struct s { int i; }){ 42 }.
    """

    __kind__ = 118


class InitListExpr(Expr):
    """
    Describes an C or C++ initializer list.
    """

    __kind__ = 119


class AddrLabelExpr(Expr):
    """
    The GNU address of label extension, representing &&label.
    """

    __kind__ = 120


class StmtExpr(Expr):
    """
    This is the GNU Statement Expression extension: ({int X=4; X;})
    """

    __kind__ = 121


class GenericSelectionExpr(Expr):
    """
    Represents a C11 generic selection.

    A generic selection is a C11 feature that allows a multi-way
    branch based on the type of an expression.

    This represents the GNU style of generic selection, where the
    controlling expression is followed by at least one type and one
    expression. The controlling expression is a constant expression,
    the type is a type, and the expression is an expression of that type.
    """

    __kind__ = 122


class GNUNullExpr(Expr):
    """
    Represents the GNU __null extension, which is a name for a null pointer
    constant that has integral type (e.g., int or long) and is the same size
    and alignment as a pointer.
    """

    __kind__ = 123


class CXXStaticCastExpr(Expr):
    """
    C++'s static_cast<> expression.
    """

    __kind__ = 124


class CXXDynamicCastExpr(Expr):
    """
    C++'s dynamic_cast<> expression.
    """

    __kind__ = 125


class CXXReinterpretCastExpr(Expr):
    """
    C++'s reinterpret_cast<> expression.
    """

    __kind__ = 126


class CXXConstCastExpr(Expr):
    """
    C++'s const_cast<> expression.
    """

    __kind__ = 127


class CXXFunctionalCastExpr(Expr):
    """
    Represents an explicit C++ type conversion that uses "functional"
    notion (C++ [expr.type.conv]).

    Example:
    ```cpp
      x = int(0.5);
    ```
    """

    __kind__ = 128


class CXXTypeidExpr(Expr):
    """
    A C++ typeid expression (C++ [expr.typeid]).
    """

    __kind__ = 129


class CXXBoolLiteralExpr(Expr):
    """
    A C++ Boolean literal.
    """

    __kind__ = 130


class CXXNullPtrLiteralExpr(Expr):
    """
    Represents the C++0x nullptr literal.
    """

    __kind__ = 131


class CXXThisExpr(Expr):
    """
    Represents the "this" expression in C++
    """

    __kind__ = 132


class CXXThrowExpr(Expr):
    """
    This handles the C++ throw expression.
    """

    __kind__ = 133


class CXXNewExpr(Expr):
    """
    A new expression for memory allocation and constructor calls, e.g:
    `new CXXNewExpr(foo)`.
    """

    __kind__ = 134


class CXXDeleteExpr(Expr):
    """
    A delete expression for memory deallocation and destructor calls, e.g:
    `delete[] pArray`.
    """

    __kind__ = 135


class UnaryExpr(Expr):
    """
    A unary expression.
    """

    __kind__ = 136


class PackExpansionExpr(Expr):
    """
    Represents a C++0x pack expansion that produces a sequence of
    expressions.

    A pack expansion expression contains a pattern (which itself is an
    expression) followed by an ellipsis. For example:

    ```cpp
    template<typename F, typename ...Types>
    void forward(F f, Types &&...args) {
     f(static_cast<Types&&>(args)...);
    }
    ```
    """

    __kind__ = 142


class SizeOfPackExpr(Expr):
    """
    Represents an expression that computes the length of a parameter pack.

    ```cpp
    template<typename ...Types>
    struct count {
      const static unsigned value = sizeof...(Types);
    };
    ```
    """
    __kind__ = 143


class LambdaExpr(Expr):
    """
    Represents a C++ lambda expression that produces a local function object.
    """
    __kind__ = 144


# FixedPointLiteral CXXAddrspaceCastExpr not support in C++
class ConceptSpecializationExpr(Expr):
    """
    Represents a C++20 concept specialization expression.
    """
    __kind__ = 153


class RequiresExpr(Expr):
    """
    Represents a C++20 requires expression.
    """
    __kind__ = 154


class CXXParenListInitExpr(Expr):
    """
    Represents a C++20 parenthesized list initialization expression.
    """
    __kind__ = 155


class PackIndexingExpr(Expr):
    """
    Represents a C++20 pack indexing expression.
    """
    __kind__ = 156


class BuiltinBitCastExpr(Expr):
    """
    Represents a C++20 builtin bit_cast expression.
    """
    __kind__ = 157


def register():
    import inspect
    for name, cls in globals().items():
        if inspect.isclass(cls) and issubclass(cls, Expr):
            if cls is not Cursor and cls is not Expr:
                Cursor.__all_kinds__[cls.__kind__] = cls


register()
