import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):
    def test_redeclared_global_var_vs_global_var_diff_type(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Var: z[2][1];

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Redeclared(Variable(), r"""z"""))
        self.assertTrue(TestChecker.test(testcase, expect, 402))

    def test_redeclared_global_var_vs_built_in_func(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Var: float_to_int;

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Redeclared(Variable(), r"""float_to_int"""))
        self.assertTrue(TestChecker.test(testcase, expect, 403))

    def test_redeclared_func_vs_built_in_func(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: printLn
        Body:
            Return;
        EndBody.

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Redeclared(Function(), r"""printLn"""))
        self.assertTrue(TestChecker.test(testcase, expect, 404))

    def test_redeclared_func_vs_global_var(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: x
        Body:
            Return;
        EndBody.

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Redeclared(Function(), r"""x"""))
        self.assertTrue(TestChecker.test(testcase, expect, 405))

    def test_redeclared_func_vs_func(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: foo
        Body:
            Return;
        EndBody.

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Redeclared(Function(), r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 406))

    def test_redeclared_func_var_vs_global_var_diff_type(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, x[1], k[1][1];
            i = m;
            x = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Undeclared(Identifier(), r"""j"""))
        self.assertTrue(TestChecker.test(testcase, expect, 414))

    def test_redeclared_func_var_vs_param(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    Var: y;
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 417))

    def test_redeclared_inner_var_vs_outer_var(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Var: y;
                        Continue;
                    Else
                        Var: y;
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    Var: y;
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    Var: y;
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 420))

    def test_redeclared_many_block(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            Var: x;
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Var: y;
                        Continue;
                    Else
                        Var: y;
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                Var: m, n, p;
                While x != 1 Do
                    Var: y;
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Var: x, y;
                Do
                    Var: y;
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                Var: z;
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: x;
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 421))

    def test_undeclared_arith_expr(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = m + 1;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Undeclared(Identifier(), r"""m"""))
        self.assertTrue(TestChecker.test(testcase, expect, 424))

    def test_undeclared_call_expr_arg(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = x;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, m)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Undeclared(Identifier(), r"""m"""))
        self.assertTrue(TestChecker.test(testcase, expect, 425))

    def test_undeclared_var_diff_block(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = x;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Var: m;
                        Continue;
                    Else
                        m = 0;
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Undeclared(Identifier(), r"""m"""))
        self.assertTrue(TestChecker.test(testcase, expect, 428))

    def test_undeclared_method_name_call_stmt(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = x;
            z = a;
            b = c;
            printStringLine(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Undeclared(Function(), r"""printStringLine"""))
        self.assertTrue(TestChecker.test(testcase, expect, 431))

    def test_undeclared_method_name_hidden_by_inner_var(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            Var: foo = "foo";
            y = x;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Undeclared(Function(), r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 433))

    def test_type_cannot_be_inferred_assign_lhs(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 436))

    def test_type_cannot_be_inferred_assign_rhs(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = x;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 437))

    def test_type_cannot_be_inferred_assign_both(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = x;
            z = z;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id(r"""z"""), Id(r"""z"""))))
        self.assertTrue(TestChecker.test(testcase, expect, 438))

    def test_type_cannot_be_inferred_assign_lhs_call_idx(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = x;
            goo()[0] = a[0];
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.

        Function: goo
        Body:
            Return {"string"};
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id(r"""goo"""), []), [IntLiteral(0)]), ArrayCell(Id(r"""a"""), [IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(testcase, expect, 439))

    def test_type_cannot_be_inferred_call_expr_return(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = x;
            z = a;
            b = foo(x, z, c);
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id(r"""b"""), CallExpr(Id(r"""foo"""), [Id(r"""x"""), Id(r"""z"""), Id(r"""c""")]))))
        self.assertTrue(TestChecker.test(testcase, expect, 442))

    def test_type_cannot_be_inferred_call_stmt_arg(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = x;
            z = a;
            foo(x, z, b);
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(CallStmt(Id(r"""foo"""), [Id(r"""x"""), Id(r"""z"""), Id(r"""b""")])))
        self.assertTrue(TestChecker.test(testcase, expect, 443))

    # def test_type_cannot_be_inferred_depth_2(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         Var: m[1];
    #         m[x] = x;
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id(r"""m"""), [Id(r"""x""")]), Id(r"""x"""))))
    #     self.assertTrue(TestChecker.test(testcase, expect, 448))

    def test_type_cannot_be_inferred_depth_n(self):
        testcase = r"""
** U stands for UnknownType, I for IntegerType, V for VoidType **

** f1 is inferred: (U) -> array(0..0, I) **
Function: f1
    Parameter: x
    Body:
        Return { 0 };
    EndBody.

Function: main
    Body:
        Var: a[1]; ** a is inferred: array(0..0, U) **
        Var: n; ** n is still U **

        ** !!! Problem **
        f1( f2( f3(n) ) )[0] = a[ f3( f2(n) ) ];
        **
        Infer type on lhs:
            f1( f2( f3(n) ) )[0]: I  * This is due to f1: (U) -> array(0..0, I)

        Infer type on rhs:
            a[ f3( f2(n) ) ]: I  * This is due to lhs: I
        and a: array(0..0, I)  * This is due to a being followed by [
        and f3: (U) -> I  * This is due to f3 being enclosed by [,]

        Infer type on lhs AGAIN:
            f2: (I) -> U  * This is due to f3: (U) -> I

        Infer type on rhs AGAIN:
            n: I  * This is due to f2: (I) -> U

        Infer type on lhs AGAIN:
            f3: (I) -> I  * This is due to n: I

        Infer type on rhs AGAIN:
            f2: (I) -> I  * This is due to f3: (I) -> I

        Infer type on lhs AGAIN:
            f1: (I) -> array(0..0, I)  * This is due to f2: (I) -> I

        In conclusion, type CAN be fully inferred for all symbols used.
        **
    EndBody.

** f2 matches inferred type: (I) -> I **
Function: f2
    Parameter: x
    Body:
        Return 0;
    EndBody.

** f3 matches inferred type: (I) -> I **
Function: f3
    Parameter: x
    Body:
        Return 0;
    EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id(r"""f1"""), [CallExpr(Id(r"""f2"""), [CallExpr(Id(r"""f3"""), [Id(r"""n""")])])]), [IntLiteral(0)]), ArrayCell(Id(r"""a"""), [CallExpr(Id(r"""f3"""), [CallExpr(Id(r"""f2"""), [Id(r"""n""")])])]))))
        self.assertTrue(TestChecker.test(testcase, expect, 449))

    # def test_type_cannot_be_inferred_deep_lhs(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         Var: m[2];
    #         m[m[m[m[m[m[0]]]]]] = m[0];
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #     EndBody.
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id(r"""m"""), [ArrayCell(Id(r"""m"""), [ArrayCell(Id(r"""m"""), [ArrayCell(Id(r"""m"""), [ArrayCell(Id(r"""m"""), [ArrayCell(Id(r"""m"""), [IntLiteral(0)])])])])])]), ArrayCell(Id(r"""m"""), [IntLiteral(0)]))))
    #     self.assertTrue(TestChecker.test(testcase, expect, 450))

    def test_type_mismatch_in_stmt_assign_diff_type(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            a = main();
            b = c;
            printStrLn(string_of_int(foo(x, a, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id(r"""main"""), [])))
        self.assertTrue(TestChecker.test(testcase, expect, 467))

    def test_type_mismatch_in_stmt_if(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If x Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(If([(Id(r"""x"""), [], [For(Id(r"""x"""), IntLiteral(0), BinaryOp(r"""<""", BinaryOp('\\', Id(r"""x"""), IntLiteral(2)), BinaryOp(r"""*""", IntLiteral(10), IntLiteral(10))), BinaryOp(r"""+""", BinaryOp(r"""-""", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), ([], [If([(BinaryOp(r"""==""", Id(r"""x"""), Id(r"""y""")), [], [Continue()])], ([], [Break()]))]))]), (BinaryOp(r"""=/=""", FloatLiteral(1.0), FloatLiteral(1.0)), [], [While(BinaryOp(r"""!=""", Id(r"""x"""), IntLiteral(1)), ([], [If([(BinaryOp(r"""==""", BinaryOp(r"""%""", Id(r"""x"""), IntLiteral(2)), IntLiteral(1)), [], [Assign(Id(r"""x"""), BinaryOp(r"""+""", BinaryOp(r"""*""", Id(r"""x"""), IntLiteral(3)), IntLiteral(1)))])], ([], [Assign(Id(r"""x"""), BinaryOp('\\', Id(r"""x"""), IntLiteral(2)))]))]))]), (CallExpr(Id(r"""bool_of_string"""), [StringLiteral(r"""True""")]), [], [Dowhile(([], [Assign(ArrayCell(Id(r"""z"""), [IntLiteral(0)]), CallExpr(Id(r"""string_of_float"""), [BinaryOp(r"""*.""", CallExpr(Id(r"""float_of_string"""), [ArrayCell(Id(r"""z"""), [IntLiteral(0)])]), FloatLiteral(3.1415))]))]), UnaryOp(r"""!""", BinaryOp(r"""=/=""", BinaryOp(r"""\.""", BinaryOp(r"""*.""", FloatLiteral(1.0), FloatLiteral(1.0)), FloatLiteral(1.0)), FloatLiteral(1.0))))])], ([], [CallStmt(Id(r"""main"""), [])]))))
        self.assertTrue(TestChecker.test(testcase, expect, 468))

    def test_type_mismatch_in_stmt_elseif(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf z Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(If([(BooleanLiteral(True), [], [For(Id(r"""x"""), IntLiteral(0), BinaryOp(r"""<""", BinaryOp('\\', Id(r"""x"""), IntLiteral(2)), BinaryOp(r"""*""", IntLiteral(10), IntLiteral(10))), BinaryOp(r"""+""", BinaryOp(r"""-""", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), ([], [If([(BinaryOp(r"""==""", Id(r"""x"""), Id(r"""y""")), [], [Continue()])], ([], [Break()]))]))]), (Id(r"""z"""), [], [While(BinaryOp(r"""!=""", Id(r"""x"""), IntLiteral(1)), ([], [If([(BinaryOp(r"""==""", BinaryOp(r"""%""", Id(r"""x"""), IntLiteral(2)), IntLiteral(1)), [], [Assign(Id(r"""x"""), BinaryOp(r"""+""", BinaryOp(r"""*""", Id(r"""x"""), IntLiteral(3)), IntLiteral(1)))])], ([], [Assign(Id(r"""x"""), BinaryOp('\\', Id(r"""x"""), IntLiteral(2)))]))]))]), (CallExpr(Id(r"""bool_of_string"""), [StringLiteral(r"""True""")]), [], [Dowhile(([], [Assign(ArrayCell(Id(r"""z"""), [IntLiteral(0)]), CallExpr(Id(r"""string_of_float"""), [BinaryOp(r"""*.""", CallExpr(Id(r"""float_of_string"""), [ArrayCell(Id(r"""z"""), [IntLiteral(0)])]), FloatLiteral(3.1415))]))]), UnaryOp(r"""!""", BinaryOp(r"""=/=""", BinaryOp(r"""\.""", BinaryOp(r"""*.""", FloatLiteral(1.0), FloatLiteral(1.0)), FloatLiteral(1.0)), FloatLiteral(1.0))))])], ([], [CallStmt(Id(r"""main"""), [])]))))
        self.assertTrue(TestChecker.test(testcase, expect, 469))

    def test_type_mismatch_in_stmt_for_var(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (z = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id(r"""z"""), IntLiteral(0), BinaryOp(r"""<""", BinaryOp('\\', Id(r"""x"""), IntLiteral(2)), BinaryOp(r"""*""", IntLiteral(10), IntLiteral(10))), BinaryOp(r"""+""", BinaryOp(r"""-""", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), ([], [If([(BinaryOp(r"""==""", Id(r"""x"""), Id(r"""y""")), [], [Continue()])], ([], [Break()]))]))))
        self.assertTrue(TestChecker.test(testcase, expect, 470))

    def test_type_mismatch_in_stmt_for_expr2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(For(Id(r"""x"""), IntLiteral(0), BinaryOp('\\', Id(r"""x"""), IntLiteral(2)), BinaryOp(r"""+""", BinaryOp(r"""-""", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), ([], [If([(BinaryOp(r"""==""", Id(r"""x"""), Id(r"""y""")), [], [Continue()])], ([], [Break()]))]))))
        self.assertTrue(TestChecker.test(testcase, expect, 472))

    def test_type_mismatch_in_stmt_while(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While b Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(While(Id(r"""b"""), ([], [If([(BinaryOp(r"""==""", BinaryOp(r"""%""", Id(r"""x"""), IntLiteral(2)), IntLiteral(1)), [], [Assign(Id(r"""x"""), BinaryOp(r"""+""", BinaryOp(r"""*""", Id(r"""x"""), IntLiteral(3)), IntLiteral(1)))])], ([], [Assign(Id(r"""x"""), BinaryOp('\\', Id(r"""x"""), IntLiteral(2)))]))]))))
        self.assertTrue(TestChecker.test(testcase, expect, 474))

    def test_type_mismatch_in_stmt_do_while(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While main()
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id(r"""main"""), [])))
        self.assertTrue(TestChecker.test(testcase, expect, 475))

    def test_type_mismatch_in_stmt_call_too_many_arg(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main(0);
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id(r"""main"""), [IntLiteral(0)])))
        self.assertTrue(TestChecker.test(testcase, expect, 476))

    def test_type_mismatch_in_stmt_call_too_few_arg(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            foo(x, z);
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id(r"""foo"""), [Id(r"""x"""), Id(r"""z""")])))
        self.assertTrue(TestChecker.test(testcase, expect, 477))

    def test_type_mismatch_in_stmt_call_diff_arg_type(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            foo(x, z, b);
            foo(x, x, b);
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id(r"""foo"""), [Id(r"""x"""), Id(r"""x"""), Id(r"""b""")])))
        self.assertTrue(TestChecker.test(testcase, expect, 479))

    def test_type_mismatch_in_stmt_call_diff_ret_type(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            foo(x, z, b);
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id(r"""foo"""), [Id(r"""x"""), Id(r"""z"""), Id(r"""b""")])))
        self.assertTrue(TestChecker.test(testcase, expect, 480))

    def test_type_mismatch_in_stmt_return(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Return 2;
                    Else
                        Return 1;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id(r"""main"""), [])))
        self.assertTrue(TestChecker.test(testcase, expect, 482))

    def test_type_mismatch_in_expr_call_too_many_arg(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b, x)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id(r"""foo"""), [Id(r"""x"""), Id(r"""z"""), Id(r"""b"""), Id(r"""x""")])))
        self.assertTrue(TestChecker.test(testcase, expect, 483))

    def test_type_mismatch_in_expr_call_diff_arg_type(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(True, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(BinaryOp(r"""+""", Id(r"""i"""), BinaryOp(r"""*""", CallExpr(Id(r"""int_of_string"""), [ArrayCell(Id(r"""j"""), [IntLiteral(0)])]), CallExpr(Id(r"""int_of_float"""), [ArrayCell(Id(r"""k"""), [IntLiteral(0), IntLiteral(0)])])))))
        self.assertTrue(TestChecker.test(testcase, expect, 486))

    def test_type_mismatch_in_expr_call_ret_type(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_float(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Return(BinaryOp(r"""+""", Id(r"""i"""), BinaryOp(r"""*""", CallExpr(Id(r"""int_of_string"""), [ArrayCell(Id(r"""j"""), [IntLiteral(0)])]), CallExpr(Id(r"""int_of_float"""), [ArrayCell(Id(r"""k"""), [IntLiteral(0), IntLiteral(0)])]))))))
        self.assertTrue(TestChecker.test(testcase, expect, 489))

    # def test_type_mismatch_in_expr_idx_too_few_dim(self):
        # testcase = r"""
        # Var: x;
        # Var: y = 0;
        # Var: z[1];
        # Var: a[1] = {"1"};
        # Var: b[1][1];
        # Var: c[1][1] = {{0.0}};

        # Function: main
        # Body:
        #     Var: m[1][1] = {{0}};
        #     Var: n[1];
        #     n = m[0];
        #     x = y;
        #     z = a;
        #     b = c;
        #     printStrLn(string_of_int(foo(x, z, b)));
        #     If True Then
        #         For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
        #             If x == y Then
        #                 Continue;
        #             Else
        #                 Break;
        #             EndIf.
        #         EndFor.
        #     ElseIf 1. =/= 1. Then
        #         While x != 1 Do
        #             If x % 2 == 1 Then
        #                 x = x * 3 + 1;
        #             Else
        #                 x = x \ 2;
        #             EndIf.
        #         EndWhile.
        #     ElseIf bool_of_string("True") Then
        #         Do
        #             z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
        #         While !(1. *. 1. \. 1. =/= 1.)
        #         EndDo.
        #     Else
        #         main();
        #     EndIf.
        # EndBody.

        # Function: foo
        # Parameter: m, n[1], p[1][1]
        # Body:
        #     Var: i, j[1], k[1][1];
        #     i = m;
        #     j = n;
        #     k = p;
        #     Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        # EndBody.
        # """
        # expect = str(TypeMismatchInExpression(ArrayCell(Id(r"""m"""), [IntLiteral(0)])))
        # self.assertTrue(TestChecker.test(testcase, expect, 491))

    def test_type_mismatch_in_expr_idx_not_array(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x[0], z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id(r"""x"""), [IntLiteral(0)])))
        self.assertTrue(TestChecker.test(testcase, expect, 492))

    def test_type_mismatch_in_expr_op(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While -(1. *. 1. \. 1. =/= 1.) == 0
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(UnaryOp(r"""-""", BinaryOp(r"""=/=""", BinaryOp(r"""\.""", BinaryOp(r"""*.""", FloatLiteral(1.0), FloatLiteral(1.0)), FloatLiteral(1.0)), FloatLiteral(1.0)))))
        self.assertTrue(TestChecker.test(testcase, expect, 497))

    def test_no_entry_point(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: foo
        Body:
            Var: i, j[1], k[1][1];
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(testcase, expect, 498))

    def test_not_in_loop_break_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
            Break;
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(NotInLoop(Break()))
        self.assertTrue(TestChecker.test(testcase, expect, 500))

    def test_not_in_loop_break_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
                Break;
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(NotInLoop(Break()))
        self.assertTrue(TestChecker.test(testcase, expect, 501))

    def test_not_in_loop_break_3(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                While True Do
                    While True Do
                        Break;
                    EndWhile.
                    Break;
                EndWhile.
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 502))

    def test_not_in_loop_break_4(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                Do
                    While True Do
                        For (x = 0, True, 0) Do
                            Break;
                        EndFor.
                        Break;
                    EndWhile.
                    Break;
                While True
                EndDo.
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 503))

    def test_not_in_loop_continue_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
            Continue;
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(NotInLoop(Continue()))
        self.assertTrue(TestChecker.test(testcase, expect, 504))

    def test_not_in_loop_continue_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
                Continue;
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(NotInLoop(Continue()))
        self.assertTrue(TestChecker.test(testcase, expect, 505))

    def test_not_in_loop_continue_3(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                While True Do
                    While True Do
                        Continue;
                    EndWhile.
                    Continue;
                EndWhile.
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 506))

    def test_not_in_loop_continue_4(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                Do
                    While True Do
                        For (x = 0, True, 0) Do
                            Continue;
                        EndFor.
                        Continue;
                    EndWhile.
                    Continue;
                While True
                EndDo.
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 507))

    # def test_invalid_arr_lit_1(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         Var: m[0];
    #         m[y] = 0;
    #         m = {};
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(testcase, expect, 508))

    # def test_invalid_arr_lit_2(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         Var: m[0][1][2];
    #         m[y][y][y] = 0;
    #         m = {};
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(testcase, expect, 509))

    def test_invalid_arr_lit_3(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            Var: m[2] = {1, 1.0};
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([IntLiteral(1), FloatLiteral(1.0)])))
        self.assertTrue(TestChecker.test(testcase, expect, 510))

    def test_invalid_arr_lit_4(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            Var: m[2] = {1.0, 1.0};
            m = {1.0, True};
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([FloatLiteral(1.0), BooleanLiteral(True)])))
        self.assertTrue(TestChecker.test(testcase, expect, 511))

    def test_invalid_arr_lit_5(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            Var: m[2] = {1, 1};
            m = {1, {1}};
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(1)])])))
        self.assertTrue(TestChecker.test(testcase, expect, 512))

    def test_invalid_arr_lit_6(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            Var: m[2][2] = {{1, 1}, {1, 1}};
            m = {{1, 1}, {1, 1, 1}};
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(1)]), ArrayLiteral([IntLiteral(1), IntLiteral(1), IntLiteral(1)])])))
        self.assertTrue(TestChecker.test(testcase, expect, 513))

    def test_invalid_arr_lit_7(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            Var: m[2][2][2] = {{{0, 0}, {0, 0}}, {{0, 0}, {0, 0}}};
            m = {{{0, 0}, {0, 0}}, {{"True", False}, {0, 0}}};
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(InvalidArrayLiteral(ArrayLiteral([StringLiteral(r"""True"""), BooleanLiteral(False)])))
        self.assertTrue(TestChecker.test(testcase, expect, 514))

    def test_func_not_return_at_all(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
        EndBody.
        """
        expect = str(FunctionNotReturn(r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 515))

    def test_func_not_return_if_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            If True Then
                Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
            EndIf.
        EndBody.
        """
        expect = str(FunctionNotReturn(r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 516))

    def test_func_not_return_if_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            If True Then
                Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
            Else
                Return 0;
            EndIf.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 517))

    def test_func_not_return_if_3(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            If True Then
                Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
            ElseIf True Then
                Return i;
            EndIf.
        EndBody.
        """
        expect = str(FunctionNotReturn(r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 518))

    def test_func_not_return_if_4(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            If True Then
                Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
            ElseIf True Then
                Return 0;
            Else
                Return 1;
            EndIf.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 519))

    def test_func_not_return_if_5(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            If True Then
                Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
            ElseIf True Then
                i = 0;
            Else
                Return 1;
            EndIf.
        EndBody.
        """
        expect = str(FunctionNotReturn(r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 520))

    # def test_func_not_return_for_1(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         For (m = 0, m <= m, 0) Do
    #             Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #         EndFor.
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(testcase, expect, 521))

    def test_func_not_return_for_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            For (m = 0, m <= m, 0) Do
                If True Then
                    Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
                EndIf.
            EndFor.
        EndBody.
        """
        expect = str(FunctionNotReturn(r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 522))

    # def test_func_not_return_for_3(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         For (m = 0, m <= m, 0) Do
    #             If True Then
    #                 Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #             Else
    #                 Return 0;
    #             EndIf.
    #         EndFor.
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(testcase, expect, 523))

    def test_func_not_return_for_4(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            For (m = 0, m <= m, 0) Do
                If True Then
                    Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
                ElseIf True Then
                Else
                    Return 0;
                EndIf.
            EndFor.
        EndBody.
        """
        expect = str(FunctionNotReturn(r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 524))

    # def test_func_not_return_while_1(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         While (m <= m) Do
    #             Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(testcase, expect, 525))

    def test_func_not_return_while_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            While (m <= m) Do
                If True Then
                    Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = str(FunctionNotReturn(r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 526))

    # def test_func_not_return_while_3(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         While (m <= m) Do
    #             If True Then
    #                 Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #             Else
    #                 Return 0;
    #             EndIf.
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(testcase, expect, 527))

    def test_func_not_return_while_4(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            While (m <= m) Do
                If True Then
                    Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
                ElseIf True Then
                Else
                    Return 0;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = str(FunctionNotReturn(r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 528))

    # def test_func_not_return_do_while_1(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Do
    #             Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #         While (m <= m)
    #         EndDo.
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(testcase, expect, 529))

    def test_func_not_return_do_while_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Do
                If True Then
                    Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
                EndIf.
            While (m <= m)
            EndDo.
        EndBody.
        """
        expect = str(FunctionNotReturn(r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 530))

    # def test_func_not_return_do_while_3(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Do
    #             If True Then
    #                 Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #             Else
    #                 Return 0;
    #             EndIf.
    #         While (m <= m)
    #         EndDo.
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(testcase, expect, 531))

    def test_func_not_return_do_while_4(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Do
                If True Then
                    Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
                ElseIf True Then
                Else
                    Return 0;
                EndIf.
            While (m <= m)
            EndDo.
        EndBody.
        """
        expect = str(FunctionNotReturn(r"""foo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 532))

    def test_unreachable_func_no_call(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: goo
        Body:
        EndBody.

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(UnreachableFunction(r"""goo"""))
        self.assertTrue(TestChecker.test(testcase, expect, 533))

    def test_unreachable_func_no_call_main(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 534))

    # def test_unreachable_func_recursive_call(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: goo
    #     Body:
    #         goo();
    #     EndBody.

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #     EndBody.
    #     """
    #     expect = str()
    #     self.assertTrue(TestChecker.test(testcase, expect, 535))
        
    def test_unreachable_func_indirect_recursive_call(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: goo
        Body:
            hoo();
        EndBody.

        Function: hoo
        Body:
            goo();
        EndBody.

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 536))

    def test_unreachable_stmt_if_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                    main();
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(UnreachableStatement(CallStmt(Id(r"""main"""), [])))
        self.assertTrue(TestChecker.test(testcase, expect, 537))

    def test_unreachable_stmt_if_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                    EndIf.
                    main();
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 538))

    def test_unreachable_stmt_for_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
                main();
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 539))

    def test_unreachable_stmt_for_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Return;
                    EndIf.
                EndFor.
                main();
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 540))

    # def test_unreachable_stmt_for_3(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Return;
    #                 Else
    #                     Return;
    #                 EndIf.
    #             EndFor.
    #             main();
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(CallStmt(Id(r"""main"""), [])))
    #     self.assertTrue(TestChecker.test(testcase, expect, 541))

    # def test_unreachable_stmt_for_4(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 Return;
    #             EndFor.
    #             main();
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(CallStmt(Id(r"""main"""), [])))
    #     self.assertTrue(TestChecker.test(testcase, expect, 542))

    def test_unreachable_stmt_while_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Return;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                    Break;
                EndWhile.
                main();
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 543))

    def test_unreachable_stmt_while_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Return;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                        Continue;
                    Else
                        x = x \ 2;
                        Break;
                    EndIf.
                EndWhile.
                main();
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 544))

    def test_unreachable_stmt_while_3(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Return;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                        Continue;
                    Else
                        x = x \ 2;
                        Return;
                    EndIf.
                EndWhile.
                main();
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 545))

    # def test_unreachable_stmt_while_4(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Return;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                     Return;
    #                 Else
    #                     x = x \ 2;
    #                     Return;
    #                 EndIf.
    #             EndWhile.
    #             main();
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(CallStmt(Id(r"""main"""), [])))
    #     self.assertTrue(TestChecker.test(testcase, expect, 546))

    def test_unreachable_stmt_do_while_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Return;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                    Continue;
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
                main();
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 547))

    def test_unreachable_stmt_do_while_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Return;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                        Break;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                    If True Then
                        Continue;
                    ElseIf False Then
                        Break;
                    Else
                    EndIf.
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
                main();
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 548))

    def test_unreachable_stmt_do_while_3(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Return;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                    If True Then
                        Continue;
                    ElseIf False Then
                        Break;
                    Else
                        Return;
                    EndIf.
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
                main();
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 549))

    # def test_unreachable_stmt_do_while_4(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Return;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #                 If True Then
    #                     Return;
    #                 ElseIf False Then
    #                     Return;
    #                 Else
    #                     Return;
    #                 EndIf.
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #             main();
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(CallStmt(Id(r"""main"""), [])))
    #     self.assertTrue(TestChecker.test(testcase, expect, 550))

    # def test_unreachable_stmt_return(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Return;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #             EndWhile.
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #         foo(m, n, p);
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(CallStmt(Id(r"""foo"""), [Id(r"""m"""), Id(r"""n"""), Id(r"""p""")])))
    #     self.assertTrue(TestChecker.test(testcase, expect, 551))

    # def test_index_out_of_range_negative_1(self):
    #     testcase = r"""
    #     Var: x;
    #     Var: y = 0;
    #     Var: z[1];
    #     Var: a[1] = {"1"};
    #     Var: b[1][1];
    #     Var: c[1][1] = {{0.0}};

    #     Function: main
    #     Body:
    #         x = y;
    #         z = a;
    #         b = c;
    #         printStrLn(string_of_int(foo(x, z, b)));
    #         If True Then
    #             For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
    #                 If x == y Then
    #                     Continue;
    #                 Else
    #                     Break;
    #                 EndIf.
    #             EndFor.
    #         ElseIf 1. =/= 1. Then
    #             While x != 1 Do
    #                 If x % 2 == 1 Then
    #                     x = x * 3 + 1;
    #                 Else
    #                     x = x \ 2;
    #                 EndIf.
    #                 Return;
    #             EndWhile.
    #             main();
    #         ElseIf bool_of_string("True") Then
    #             Do
    #                 z[-1%-2] = string_of_float(float_of_string(z[0]) *. 3.1);
    #             While !(1. *. 1. \. 1. =/= 1.)
    #             EndDo.
    #         Else
    #             main();
    #         EndIf.
    #     EndBody.

    #     Function: foo
    #     Parameter: m, n[1], p[1][1]
    #     Body:
    #         Var: i, j[1], k[1][1];
    #         i = m;
    #         j = n;
    #         k = p;
    #         Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
    #     EndBody.
    #     """
    #     expect = str(UnreachableStatement(CallStmt(Id(r"""main"""), [])))
    #     self.assertTrue(TestChecker.test(testcase, expect, 552))

    def test_index_out_of_range_negative_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 3.1415);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][-1 \ 2]);
        EndBody.
        """
        expect = str(IndexOutOfRange(ArrayCell(Id(r"""k"""), [IntLiteral(0), BinaryOp('\\', UnaryOp(r"""-""", IntLiteral(1)), IntLiteral(2))])))
        self.assertTrue(TestChecker.test(testcase, expect, 553))
        
    def test_index_out_of_range_negative_3(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 3.1415);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][---1]);
        EndBody.
        """
        expect = str(IndexOutOfRange(ArrayCell(Id(r"""k"""), [IntLiteral(0), UnaryOp(r"""-""", UnaryOp(r"""-""", UnaryOp(r"""-""", IntLiteral(1))))])))
        self.assertTrue(TestChecker.test(testcase, expect, 554))

    def test_index_out_of_range_too_big_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[1 * 3 \ 2]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(IndexOutOfRange(ArrayCell(Id(r"""j"""), [BinaryOp('\\', BinaryOp(r"""*""", IntLiteral(1), IntLiteral(3)), IntLiteral(2))])))
        self.assertTrue(TestChecker.test(testcase, expect, 555))

    def test_index_out_of_range_too_big_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][9 \ 10 * 10]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 556))

    def test_index_out_of_range_too_big_3(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            x = y;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(x, z, b)));
            If True Then
                For (x = 0, x \ 2 < 10 * 10, 1-2+3) Do
                    If x == y Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                EndFor.
            ElseIf 1. =/= 1. Then
                While x != 1 Do
                    If x % 2 == 1 Then
                        x = x * 3 + 1;
                    Else
                        x = x \ 2;
                    EndIf.
                EndWhile.
            ElseIf bool_of_string("True") Then
                Do
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While !(1. *. 1. \. 1. =/= 1.)
                EndDo.
            Else
                main();
            EndIf.
        EndBody.

        Function: foo
        Parameter: m, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_float(k[0][int_of_float(1.0)]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 557))
