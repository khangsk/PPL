import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):
    def test_redeclared_global_var_vs_global_var(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Var: x;

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
        expect = str(Redeclared(Variable(), r"""x"""))
        self.assertTrue(TestChecker.test(testcase, expect, 400))

    def test_redeclared_global_var_vs_global_var_diff_type_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Var: x[1];

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
        expect = str(Redeclared(Variable(), r"""x"""))
        self.assertTrue(TestChecker.test(testcase, expect, 401))

    def test_redeclared_global_var_vs_global_var_diff_type_2(self):
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

    def test_redeclared_func_vs_func_1(self):
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

    def test_redeclared_func_vs_func_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
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
        expect = str(Redeclared(Function(), r"""main"""))
        self.assertTrue(TestChecker.test(testcase, expect, 407))

    def test_redeclared_param_vs_global_var(self):
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
        Parameter: x, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = x;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 408))

    def test_redeclared_param_vs_func_1(self):
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
        Parameter: main, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = main;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 409))

    def test_redeclared_param_vs_func_2(self):
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
        Parameter: foo, n[1], p[1][1]
        Body:
            Var: i, j[1], k[1][1];
            i = foo;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 410))

    def test_redeclared_param_vs_param(self):
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
        Parameter: m, n[1], p[1][1], m
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Redeclared(Parameter(), r"""m"""))
        self.assertTrue(TestChecker.test(testcase, expect, 411))

    def test_redeclared_param_vs_param_diff_type(self):
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
        Parameter: m, n[1], p[1][1], n
        Body:
            Var: i, j[1], k[1][1];
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Redeclared(Parameter(), r"""n"""))
        self.assertTrue(TestChecker.test(testcase, expect, 412))

    def test_redeclared_func_var_vs_global_var(self):
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
            Var: x, j[1], k[1][1];
            x = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Undeclared(Identifier(), r"""i"""))
        self.assertTrue(TestChecker.test(testcase, expect, 413))

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
            Var: i, j[1], k[1][1], m = 1;
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Redeclared(Variable(), r"""m"""))
        self.assertTrue(TestChecker.test(testcase, expect, 415))

    def test_redeclared_func_var_vs_func_var(self):
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
            Var: i = 1;
            i = m;
            j = n;
            k = p;
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(Redeclared(Variable(), r"""i"""))
        self.assertTrue(TestChecker.test(testcase, expect, 416))

    def test_redeclared_inner_var_vs_func_var(self):
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
                    Var: y;
                    If x == y Then
                        Var: y;
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
        self.assertTrue(TestChecker.test(testcase, expect, 418))

    def test_redeclared_inner_var_vs_inner_var(self):
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
                    Var: x, y;
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
        expect = str(Redeclared(Variable(), r"""y"""))
        self.assertTrue(TestChecker.test(testcase, expect, 419))

    def test_redeclared_inner_var_vs_inner_var_diff_block(self):
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

    def test_undeclared_assign_lhs(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            m = y;
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
        self.assertTrue(TestChecker.test(testcase, expect, 422))

    def test_undeclared_assign_rhs(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = m;
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
        self.assertTrue(TestChecker.test(testcase, expect, 423))

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

    def test_undeclared_rel_expr(self):
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
                For (x = 0, x \ 2 < m, 1-2+3) Do
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
        self.assertTrue(TestChecker.test(testcase, expect, 426))

    def test_undeclared_bool_expr(self):
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
            ElseIf True && m Then
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
        self.assertTrue(TestChecker.test(testcase, expect, 427))

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

    def test_undeclared_call_stmt_arg(self):
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
            printStrLn(m);
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
        self.assertTrue(TestChecker.test(testcase, expect, 429))

    def test_undeclared_method_name_call_expr(self):
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
            printStrLn(str(foo(x, z, b)));
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
        expect = str(Undeclared(Function(), r"""str"""))
        self.assertTrue(TestChecker.test(testcase, expect, 430))

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

    def test_undeclared_method_name_hidden_by_inner_var_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            Var: string_of_int = 1;
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
        self.assertTrue(TestChecker.test(testcase, expect, 432))

    def test_undeclared_method_name_hidden_by_inner_var_2(self):
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

    def test_type_cannot_be_inferred_global_var_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
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
        expect = str(TypeCannotBeInferred(CallStmt(Id(r"""printStrLn"""), [CallExpr(Id(r"""string_of_int"""), [CallExpr(Id(r"""foo"""), [Id(r"""x"""), Id(r"""z"""), Id(r"""b""")])])])))
        self.assertTrue(TestChecker.test(testcase, expect, 434))

    def test_type_cannot_be_inferred_global_var_2(self):
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
            Return x;
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(testcase, expect, 435))

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

    def test_type_cannot_be_inferred_assign_lhs_call_idx_1(self):
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

    def test_type_cannot_be_inferred_assign_lhs_call_idx_2(self):
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
            goo()[0] = z[0];
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
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id(r"""goo"""), []), [IntLiteral(0)]), ArrayCell(Id(r"""z"""), [IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(testcase, expect, 440))

    def test_type_cannot_be_inferred_call_expr_arg(self):
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
        expect = str(TypeCannotBeInferred(CallStmt(Id(r"""printStrLn"""), [CallExpr(Id(r"""string_of_int"""), [CallExpr(Id(r"""foo"""), [Id(r"""x"""), Id(r"""z"""), Id(r"""b""")])])])))
        self.assertTrue(TestChecker.test(testcase, expect, 441))

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

    def test_type_cannot_be_inferred_while(self):
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
                Var: x, y;
                While x != 1 Do
                    x = y;
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
        self.assertTrue(TestChecker.test(testcase, expect, 444))

    def test_type_cannot_be_inferred_do_while(self):
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
                Var: x, y;
                Do
                    x = y;
                    z[0] = string_of_float(float_of_string(z[0]) *. 31415e-4);
                While x == y
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
        expect = str(TypeCannotBeInferred(Assign(Id(r"""x"""), Id(r"""y"""))))
        self.assertTrue(TestChecker.test(testcase, expect, 445))

    def test_type_cannot_be_inferred_for(self):
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
                Var: x;
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
        self.assertTrue(TestChecker.test(testcase, expect, 446))

    def test_type_cannot_be_inferred_if(self):
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
                    Var: x;
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
        self.assertTrue(TestChecker.test(testcase, expect, 447))

    def test_type_cannot_be_inferred_depth_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            Var: m[1];
            m[x] = x;
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
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id(r"""m"""), [Id(r"""x""")]), Id(r"""x"""))))
        self.assertTrue(TestChecker.test(testcase, expect, 448))

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

    def test_type_cannot_be_inferred_deep_lhs(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            Var: m[2];
            m[m[m[m[m[m[0]]]]]] = m[0];
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
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(Id(r"""m"""), [ArrayCell(Id(r"""m"""), [ArrayCell(Id(r"""m"""), [ArrayCell(Id(r"""m"""), [ArrayCell(Id(r"""m"""), [ArrayCell(Id(r"""m"""), [IntLiteral(0)])])])])])]), ArrayCell(Id(r"""m"""), [IntLiteral(0)]))))
        self.assertTrue(TestChecker.test(testcase, expect, 450))

    def test_type_mismatch_in_stmt_assign_diff_type_1(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = 1.0;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(y, z, b)));
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""y"""), FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(testcase, expect, 451))

    def test_type_mismatch_in_stmt_assign_diff_type_2(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = "";
            z = a;
            b = c;
            printStrLn(string_of_int(foo(y, z, b)));
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""y"""), StringLiteral(r""""""))))
        self.assertTrue(TestChecker.test(testcase, expect, 452))

    def test_type_mismatch_in_stmt_assign_diff_type_3(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = True;
            z = a;
            b = c;
            printStrLn(string_of_int(foo(y, z, b)));
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""y"""), BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(testcase, expect, 453))

    def test_type_mismatch_in_stmt_assign_diff_type_4(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = {1};
            z = a;
            b = c;
            printStrLn(string_of_int(foo(y, z, b)));
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""y"""), ArrayLiteral([IntLiteral(1)]))))
        self.assertTrue(TestChecker.test(testcase, expect, 454))

    def test_type_mismatch_in_stmt_assign_diff_type_5(self):
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
            a = {2};
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""a"""), ArrayLiteral([IntLiteral(2)]))))
        self.assertTrue(TestChecker.test(testcase, expect, 455))

    def test_type_mismatch_in_stmt_assign_diff_type_6(self):
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
            a = {True};
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""a"""), ArrayLiteral([BooleanLiteral(True)]))))
        self.assertTrue(TestChecker.test(testcase, expect, 456))

    def test_type_mismatch_in_stmt_assign_diff_type_7(self):
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
            a = {2.e7};
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""a"""), ArrayLiteral([FloatLiteral(20000000.0)]))))
        self.assertTrue(TestChecker.test(testcase, expect, 457))

    def test_type_mismatch_in_stmt_assign_diff_type_8(self):
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
            a = {"1", "2"};
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""a"""), ArrayLiteral([StringLiteral(r"""1"""), StringLiteral(r"""2""")]))))
        self.assertTrue(TestChecker.test(testcase, expect, 458))

    def test_type_mismatch_in_stmt_assign_diff_type_9(self):
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
            a = {{"1"}};
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""a"""), ArrayLiteral([ArrayLiteral([StringLiteral(r"""1""")])]))))
        self.assertTrue(TestChecker.test(testcase, expect, 459))

    def test_type_mismatch_in_stmt_assign_diff_type_10(self):
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
            c = 1;
            printStrLn(string_of_int(foo(x, z, c)));
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""c"""), IntLiteral(1))))
        self.assertTrue(TestChecker.test(testcase, expect, 460))

    def test_type_mismatch_in_stmt_assign_diff_type_11(self):
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
            c = {1.1};
            printStrLn(string_of_int(foo(x, z, c)));
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""c"""), ArrayLiteral([FloatLiteral(1.1)]))))
        self.assertTrue(TestChecker.test(testcase, expect, 461))

    def test_type_mismatch_in_stmt_assign_diff_type_12(self):
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
            c = {0.0, 0.0};
            printStrLn(string_of_int(foo(x, z, c)));
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""c"""), ArrayLiteral([FloatLiteral(0.0), FloatLiteral(0.0)]))))
        self.assertTrue(TestChecker.test(testcase, expect, 462))

    def test_type_mismatch_in_stmt_assign_diff_type_13(self):
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
            c = a;
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""c"""), Id(r"""a"""))))
        self.assertTrue(TestChecker.test(testcase, expect, 463))

    def test_type_mismatch_in_stmt_assign_diff_type_14(self):
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
            a = x;
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""a"""), Id(r"""x"""))))
        self.assertTrue(TestChecker.test(testcase, expect, 464))

    def test_type_mismatch_in_stmt_assign_diff_type_15(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = a;
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
        expect = str(TypeMismatchInStatement(Assign(Id(r"""y"""), Id(r"""a"""))))
        self.assertTrue(TestChecker.test(testcase, expect, 465))

    def test_type_mismatch_in_stmt_assign_diff_type_16(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            y = main();
            z = a;
            b = c;
            printStrLn(string_of_int(foo(y, b, b)));
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
        expect = str(TypeMismatchInExpression(CallExpr(Id(r"""foo"""), [Id(r"""y"""), Id(r"""b"""), Id(r"""b""")])))
        self.assertTrue(TestChecker.test(testcase, expect, 466))

    def test_type_mismatch_in_stmt_assign_diff_type_17(self):
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
        expect = str(TypeMismatchInStatement(If([(Id(r"""x"""), [], [For(Id(r"""x"""), IntLiteral(0), BinaryOp(r"""<""", BinaryOp('\\', Id(r"""x"""), IntLiteral(2)), BinaryOp(r"""*""", IntLiteral(10), IntLiteral(10))), BinaryOp(r"""+""", BinaryOp(r"""-""", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), ([], [If([(BinaryOp(r"""==""", Id(r"""x"""), Id(r"""y""")), [], [Continue()])], ([], [Break()]))]))]), (BinaryOp(r"""=/=""", FloatLiteral(1.0), FloatLiteral(1.0)), [], [While(([], [If([(BinaryOp(r"""==""", BinaryOp(r"""%""", Id(r"""x"""), IntLiteral(2)), IntLiteral(1)), [], [Assign(Id(r"""x"""), BinaryOp(r"""+""", BinaryOp(r"""*""", Id(r"""x"""), IntLiteral(3)), IntLiteral(1)))])], ([], [Assign(Id(r"""x"""), BinaryOp('\\', Id(r"""x"""), IntLiteral(2)))]))]), BinaryOp(r"""!=""", Id(r"""x"""), IntLiteral(1)))]), (CallExpr(Id(r"""bool_of_string"""), [StringLiteral(r"""True""")]), [], [Dowhile(([], [Assign(ArrayCell(Id(r"""z"""), [IntLiteral(0)]), CallExpr(Id(r"""string_of_float"""), [BinaryOp(r"""*.""", CallExpr(Id(r"""float_of_string"""), [ArrayCell(Id(r"""z"""), [IntLiteral(0)])]), FloatLiteral(3.1415))]))]), UnaryOp(r"""!""", BinaryOp(r"""=/=""", BinaryOp(r"""\.""", BinaryOp(r"""*.""", FloatLiteral(1.0), FloatLiteral(1.0)), FloatLiteral(1.0)), FloatLiteral(1.0))))])], ([], [CallStmt(Id(r"""main"""), [])]))))
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
        expect = str(TypeMismatchInStatement(If([(BooleanLiteral(True), [], [For(Id(r"""x"""), IntLiteral(0), BinaryOp(r"""<""", BinaryOp('\\', Id(r"""x"""), IntLiteral(2)), BinaryOp(r"""*""", IntLiteral(10), IntLiteral(10))), BinaryOp(r"""+""", BinaryOp(r"""-""", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), ([], [If([(BinaryOp(r"""==""", Id(r"""x"""), Id(r"""y""")), [], [Continue()])], ([], [Break()]))]))]), (Id(r"""z"""), [], [While(([], [If([(BinaryOp(r"""==""", BinaryOp(r"""%""", Id(r"""x"""), IntLiteral(2)), IntLiteral(1)), [], [Assign(Id(r"""x"""), BinaryOp(r"""+""", BinaryOp(r"""*""", Id(r"""x"""), IntLiteral(3)), IntLiteral(1)))])], ([], [Assign(Id(r"""x"""), BinaryOp('\\', Id(r"""x"""), IntLiteral(2)))]))]), BinaryOp(r"""!=""", Id(r"""x"""), IntLiteral(1)))]), (CallExpr(Id(r"""bool_of_string"""), [StringLiteral(r"""True""")]), [], [Dowhile(([], [Assign(ArrayCell(Id(r"""z"""), [IntLiteral(0)]), CallExpr(Id(r"""string_of_float"""), [BinaryOp(r"""*.""", CallExpr(Id(r"""float_of_string"""), [ArrayCell(Id(r"""z"""), [IntLiteral(0)])]), FloatLiteral(3.1415))]))]), UnaryOp(r"""!""", BinaryOp(r"""=/=""", BinaryOp(r"""\.""", BinaryOp(r"""*.""", FloatLiteral(1.0), FloatLiteral(1.0)), FloatLiteral(1.0)), FloatLiteral(1.0))))])], ([], [CallStmt(Id(r"""main"""), [])]))))
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

    def test_type_mismatch_in_stmt_for_expr1(self):
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
                For (x = 0.0, x \ 2 < 10 * 10, 1-2+3) Do
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
        expect = str(TypeMismatchInStatement(For(Id(r"""x"""), FloatLiteral(0.0), BinaryOp(r"""<""", BinaryOp('\\', Id(r"""x"""), IntLiteral(2)), BinaryOp(r"""*""", IntLiteral(10), IntLiteral(10))), BinaryOp(r"""+""", BinaryOp(r"""-""", IntLiteral(1), IntLiteral(2)), IntLiteral(3)), ([], [If([(BinaryOp(r"""==""", Id(r"""x"""), Id(r"""y""")), [], [Continue()])], ([], [Break()]))]))))
        self.assertTrue(TestChecker.test(testcase, expect, 471))

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

    def test_type_mismatch_in_stmt_for_expr3(self):
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
                For (x = 0, x \ 2 < 10 * 10, x > y) Do
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
        expect = str(TypeMismatchInStatement(For(Id(r"""x"""), IntLiteral(0), BinaryOp(r"""<""", BinaryOp('\\', Id(r"""x"""), IntLiteral(2)), BinaryOp(r"""*""", IntLiteral(10), IntLiteral(10))), BinaryOp(r""">""", Id(r"""x"""), Id(r"""y""")), ([], [If([(BinaryOp(r"""==""", Id(r"""x"""), Id(r"""y""")), [], [Continue()])], ([], [Break()]))]))))
        self.assertTrue(TestChecker.test(testcase, expect, 473))

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
        expect = str(TypeMismatchInStatement(While(([], [If([(BinaryOp(r"""==""", BinaryOp(r"""%""", Id(r"""x"""), IntLiteral(2)), IntLiteral(1)), [], [Assign(Id(r"""x"""), BinaryOp(r"""+""", BinaryOp(r"""*""", Id(r"""x"""), IntLiteral(3)), IntLiteral(1)))])], ([], [Assign(Id(r"""x"""), BinaryOp('\\', Id(r"""x"""), IntLiteral(2)))]))]), Id(r"""b"""))))
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

    def test_type_mismatch_in_stmt_call_diff_arg_type_1(self):
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
            foo(z[0], z, b);
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
        expect = str(TypeMismatchInStatement(CallStmt(Id(r"""foo"""), [ArrayCell(Id(r"""z"""), [IntLiteral(0)]), Id(r"""z"""), Id(r"""b""")])))
        self.assertTrue(TestChecker.test(testcase, expect, 478))

    def test_type_mismatch_in_stmt_call_diff_arg_type_2(self):
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

    def test_type_mismatch_in_stmt_return_1(self):
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
        expect = str(TypeMismatchInStatement(Return(None)))
        self.assertTrue(TestChecker.test(testcase, expect, 481))

    def test_type_mismatch_in_stmt_return_2(self):
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

    def test_type_mismatch_in_expr_call_too_few_arg(self):
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
            printStrLn(string_of_int(foo(x, b)));
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
        expect = str(TypeMismatchInExpression(CallExpr(Id(r"""foo"""), [Id(r"""x"""), Id(r"""b""")])))
        self.assertTrue(TestChecker.test(testcase, expect, 484))

    def test_type_mismatch_in_expr_call_diff_arg_type_1(self):
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
            printStrLn(string_of_int(foo(x, {1}, b)));
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
        expect = str(TypeMismatchInExpression(CallExpr(Id(r"""int_of_string"""), [ArrayCell(Id(r"""j"""), [IntLiteral(0)])])))
        self.assertTrue(TestChecker.test(testcase, expect, 485))

    def test_type_mismatch_in_expr_call_diff_arg_type_2(self):
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
            printStrLn(string_of_int(foo(x, z, b)));
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
        expect = str(TypeMismatchInExpression(CallExpr(Id(r"""string_of_float"""), [CallExpr(Id(r"""foo"""), [Id(r"""x"""), Id(r"""z"""), Id(r"""b""")])])))
        self.assertTrue(TestChecker.test(testcase, expect, 487))

    def test_type_mismatch_in_expr_call_ret_type_1(self):
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
        expect = str(TypeMismatchInExpression(CallExpr(Id(r"""string_of_float"""), [CallExpr(Id(r"""foo"""), [Id(r"""x"""), Id(r"""z"""), Id(r"""b""")])])))
        self.assertTrue(TestChecker.test(testcase, expect, 488))

    def test_type_mismatch_in_expr_call_ret_type_2(self):
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

    def test_type_mismatch_in_expr_idx_too_many_dim(self):
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
            Return i + int_of_string(j[0]) * int_of_float(k[0][0][0]);
        EndBody.
        """
        expect = str(TypeMismatchInExpression(ArrayCell(Id(r"""k"""), [IntLiteral(0), IntLiteral(0), IntLiteral(0)])))
        self.assertTrue(TestChecker.test(testcase, expect, 490))

    def test_type_mismatch_in_expr_idx_too_few_dim(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};

        Function: main
        Body:
            Var: m[1][1] = {{0}};
            Var: n[1];
            n = m[0];
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
        expect = str(TypeMismatchInExpression(ArrayCell(Id(r"""m"""), [IntLiteral(0)])))
        self.assertTrue(TestChecker.test(testcase, expect, 491))

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

    def test_type_mismatch_in_expr_op_1(self):
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
            ElseIf 1. != 1. Then
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
        expect = str(TypeMismatchInExpression(BinaryOp(r"""!=""", FloatLiteral(1.0), FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(testcase, expect, 493))

    def test_type_mismatch_in_expr_op_2(self):
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
                    z[0] = string_of_int(float_of_string(z[0]) * 31415e-4);
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
        expect = str(TypeMismatchInExpression(BinaryOp(r"""*""", CallExpr(Id(r"""float_of_string"""), [ArrayCell(Id(r"""z"""), [IntLiteral(0)])]), FloatLiteral(3.1415))))
        self.assertTrue(TestChecker.test(testcase, expect, 494))

    def test_type_mismatch_in_expr_op_3(self):
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
                While x =/= 1 Do
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
        expect = str(TypeMismatchInExpression(BinaryOp(r"""=/=""", Id(r"""x"""), IntLiteral(1))))
        self.assertTrue(TestChecker.test(testcase, expect, 495))

    def test_type_mismatch_in_expr_op_4(self):
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
            ElseIf 1. == 1. Then
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
        expect = str(TypeMismatchInExpression(BinaryOp(r"""==""", FloatLiteral(1.0), FloatLiteral(1.0))))
        self.assertTrue(TestChecker.test(testcase, expect, 496))

    def test_type_mismatch_in_expr_op_5(self):
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
        Parameter: m, n[1], p[1][1]
        Body:
            Return i + int_of_string(j[0]) * int_of_float(k[0][0]);
        EndBody.
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(testcase, expect, 498))

    def test_no_entry_point_but_with_main_var(self):
        testcase = r"""
        Var: x;
        Var: y = 0;
        Var: z[1];
        Var: a[1] = {"1"};
        Var: b[1][1];
        Var: c[1][1] = {{0.0}};
        Var: main = 0;

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
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(testcase, expect, 499))
