from clanglite import *

src = """
struct S {
    int operator+(int a) { return a; }
    int add(int a) { return a; }
};

S x; // default constructor call, line 7
int y = x + 1; // overloaded operator call, line 8
int z = x.add(2); // member function call, line 9

struct D : S {
    D(int, int) : S(0) {} // inherited constructor call, line 12
};

D d = D(1, 1); // temporary object, line 15

int operator""       _s(unsigned long long x) { return x; }
int w = 1_s; // user defined literal, line 18
"""


def on_call_expr(expr: CallExpr):
    line = expr.location.line

    if expr.is_constructor_call():
        assert line == 7
        assert expr.spelling == 'S'

    if expr.is_operator_call():
        assert line == 8
        assert expr.spelling == 'operator+'

    if expr.is_member_call():
        assert line == 9
        assert expr.spelling == 'add'

    if expr.is_inherited_constructor_call():
        assert line == 12
        assert expr.spelling == 'S'

    if expr.is_temporary_object():
        assert line == 15
        assert expr.spelling == 'D'

    if expr.is_user_defined_literal():
        assert line == 18
        assert expr.spelling == 'operator""_s'


def test_CallExpr():
    parser = Parser("main.cpp", unsaved_files=[("main.cpp", src)])
    parser.add_matcher(CallExpr, on_call_expr)
    parser.run()
