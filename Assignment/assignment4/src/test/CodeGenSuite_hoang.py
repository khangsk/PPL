import unittest
from TestUtils import TestCodeGen


class CheckCodeGenSuite(unittest.TestCase):

    # PART 1: NO INFERENCE

    ##""" Test builtin functions with primitive literals """

    def test_501(self):
        input = r"""
Function: main
    Body:
        printLn();
        print("Hello ");
        printStrLn("World");
    EndBody.
"""
        expect = r"""
Hello World
"""
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_502(self):
        input = r"""
Function: main
    Body:
        printStrLn("\n\t\'\\'"");
    EndBody.
"""
        expect = r"""
	'\"
"""
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_503(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_int(int_of_string("-2147483648")));
        printStrLn(string_of_int(int_of_string("-32768")));
        printStrLn(string_of_int(int_of_string("-128")));
        printStrLn(string_of_int(int_of_string("-1")));
        printStrLn(string_of_int(0));
        printStrLn(string_of_int(5));
        printStrLn(string_of_int(127));
        printStrLn(string_of_int(32767));
        printStrLn(string_of_int(2147483647));
    EndBody.
"""
        expect = r"""
-2147483648
-32768
-128
-1
0
5
127
32767
2147483647
"""
        self.assertTrue(TestCodeGen.test(input, expect, 503))



    def test_504(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_float(float_of_string("-3.4028235E38")));
        printStrLn(string_of_float(float_of_string("-1.4E-45")));
        printStrLn(string_of_float(float_of_string("-1.")));
        printStrLn(string_of_float(0.));
        printStrLn(string_of_float(1.));
        printStrLn(string_of_float(2.));
        printStrLn(string_of_float(1.4E-45));
        printStrLn(string_of_float(3.4028235E38));
    EndBody.
"""
        expect = r"""
-3.4028235E38
-1.4E-45
-1.0
0.0
1.0
2.0
1.4E-45
3.4028235E38
"""
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_505(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(bool_of_string("true")));
        printStrLn(string_of_bool(bool_of_string("false")));
        printStrLn(string_of_bool(True));
        printStrLn(string_of_bool(False));
    EndBody.
"""
        expect = r"""
true
false
true
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_506(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_int(int_of_float(1.)));
        printStrLn(string_of_float(float_to_int(1)));
    EndBody.
"""
        expect = r"""
1
1.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    ##""" Unary expression """

    def test_507(self):
        input = r"""
        Var: a = 10;
        
Function: main
    Body:
        printLn();
        printStrLn(string_of_int(-1));
        printStrLn(string_of_float(-.1.));
        printStrLn(string_of_bool(!True));
    EndBody.
"""
        expect = r"""
-1
-1.0
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    ##""" Arithmetic binary expression """

    def test_508(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_int(1 + 2));
        printStrLn(string_of_int(3 - 4));
        printStrLn(string_of_float(5. +. 6.));
        printStrLn(string_of_float(7. -. 9.));

        printStrLn(string_of_int(1 + -2));
        printStrLn(string_of_int(3 - -4));
        printStrLn(string_of_float(5. +. -.6.));
        printStrLn(string_of_float(7. -. -.9.));

    EndBody.
"""
        expect = r"""
3
-1
11.0
-2.0
-1
7
-1.0
16.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_509(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_int(2 * 5));
        printStrLn(string_of_int(20 \ 3));
        printStrLn(string_of_float(3.14 *. 3.));
        printStrLn(string_of_float(7. \. 8.));

        printStrLn(string_of_int(2 * -5));
        printStrLn(string_of_int(20 \ -3));
        printStrLn(string_of_float(3.14 *. -.3.));
        printStrLn(string_of_float(7. \. -.8.));
    EndBody.
"""
        expect = r"""
10
6
9.42
0.875
-10
-6
-9.42
-0.875
"""
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_510(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_int(20 % 3));
        printStrLn(string_of_int(10 % 5));

        printStrLn(string_of_int(-20 % 3));
        printStrLn(string_of_int(-10 % 5));
    EndBody.
"""
        expect = r"""
2
0
-2
0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    ##""" Relational binary expression with integer """

    def test_511(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(1 == 2));
        printStrLn(string_of_bool(4 == 3));
        printStrLn(string_of_bool(5 == 5));
    EndBody.
"""
        expect = r"""
false
false
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_512(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(1 != 2));
        printStrLn(string_of_bool(4 != 3));
        printStrLn(string_of_bool(5 != 5));
    EndBody.
"""
        expect = r"""
true
true
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_513(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(1 >= 2));
        printStrLn(string_of_bool(4 >= 3));
        printStrLn(string_of_bool(5 >= 5));
    EndBody.
"""
        expect = r"""
false
true
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_514(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(1 > 2));
        printStrLn(string_of_bool(4 > 3));
        printStrLn(string_of_bool(5 > 5));
    EndBody.
"""
        expect = r"""
false
true
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_515(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(1 <= 2));
        printStrLn(string_of_bool(4 <= 3));
        printStrLn(string_of_bool(5 <= 5));
    EndBody.
"""
        expect = r"""
true
false
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_516(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(1 < 2));
        printStrLn(string_of_bool(4 < 3));
        printStrLn(string_of_bool(5 < 5));
    EndBody.
"""
        expect = r"""
true
false
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    ##""" Relational binary expression with float """

    def test_517(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(1. =/= 2.));
        printStrLn(string_of_bool(4. =/= 3.));
        printStrLn(string_of_bool(5. =/= 5.));
    EndBody.
"""
        expect = r"""
true
true
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_518(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(1. >=. 2.));
        printStrLn(string_of_bool(4. >=. 3.));
        printStrLn(string_of_bool(5. >=. 5.));
    EndBody.
"""
        expect = r"""
false
true
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_519(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(1. >. 2.));
        printStrLn(string_of_bool(4. >. 3.));
        printStrLn(string_of_bool(5. >. 5.));
    EndBody.
"""
        expect = r"""
false
true
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_520(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(1. <=. 2.));
        printStrLn(string_of_bool(4. <=. 3.));
        printStrLn(string_of_bool(5. <=. 5.));
    EndBody.
"""
        expect = r"""
true
false
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_521(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(1. <. 2.));
        printStrLn(string_of_bool(4. <. 3.));
        printStrLn(string_of_bool(5. <. 5.));
    EndBody.
"""
        expect = r"""
true
false
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    ##""" Logical binary expression (test value only) """

    def test_522(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(True && True));
        printStrLn(string_of_bool(True && False));
        printStrLn(string_of_bool(False && True));
        printStrLn(string_of_bool(False && False));
    EndBody.
"""
        expect = r"""
true
false
false
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_523(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(True || True));
        printStrLn(string_of_bool(True || False));
        printStrLn(string_of_bool(False || True));
        printStrLn(string_of_bool(False || False));
    EndBody.
"""
        expect = r"""
true
true
true
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    ##""" Variable declaration """

    def test_524(self):
        input = r"""
** Global Variable **

Var: a = 1, b = 1., c = True, d = "";
Function: main
    Body:
        printLn();
        printStrLn(string_of_int(a));
        printStrLn(string_of_float(b));
        printStrLn(string_of_bool(c));
        printStrLn(d);
    EndBody.
"""
        expect = r"""
1
1.0
true

"""
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_525(self):
        input = r"""
** Local Variable **

Function: main
    Body:
        Var: a = 1, b = 1., c = True, d = "";

        printLn();
        printStrLn(string_of_int(a));
        printStrLn(string_of_float(b));
        printStrLn(string_of_bool(c));
        printStrLn(d);
    EndBody.
"""
        expect = r"""
1
1.0
true

"""
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_526(self):
        input = r"""
** Local Variables hide non-local Variables **

Var: a = 1, b = 1., c = True, d = "";

Function: main
    Body:
        Var: b = 2, c = 2., d = False, a = "Hi!";

        printLn();
        printStrLn(string_of_int(b));
        printStrLn(string_of_float(c));
        printStrLn(string_of_bool(d));
        printStrLn(a);
    EndBody.
"""
        expect = r"""
2
2.0
false
Hi!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    #""" Assign statement """

    def test_527(self):
        input = r"""
Var: a = 1, b = 1., c = True, d = "", e = "Hi!";

Function: main
    Body:
        a = a + 1;
        b = b +. 1.;
        c = !c;
        d = e;

        printLn();
        printStrLn(string_of_int(a));
        printStrLn(string_of_float(b));
        printStrLn(string_of_bool(c));
        printStrLn(d);
    EndBody.
"""
        expect = r"""
2
2.0
false
Hi!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    ##""" If statement (test flow) """

    def test_528(self):
        input = r"""
Function: main
    Body:
        printLn();

        If True Then
            printStrLn(string_of_int(1));
        EndIf.
    EndBody.
"""
        expect = r"""
1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_529(self):
        input = r"""
Function: main
    Body:
        printLn();

        If False Then
            printStrLn(string_of_int(1));
        EndIf.

        printStrLn("No else clause");
    EndBody.
"""
        expect = r"""
No else clause
"""
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_530(self):
        input = r"""
Function: main
    Body:
        printLn();

        If True Then
            printStrLn(string_of_int(1));
        Else
            printStrLn(string_of_int(100));
        EndIf.
    EndBody.
"""
        expect = r"""
1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_531(self):
        input = r"""
Function: main
    Body:
        printLn();

        If False Then
            printStrLn(string_of_int(1));
        Else
            printStrLn(string_of_int(100));
        EndIf.
    EndBody.
"""
        expect = r"""
100
"""
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_532(self):
        input = r"""
Function: main
    Body:
        printLn();

        If True Then
            printStrLn(string_of_int(1));
        ElseIf True Then
            printStrLn(string_of_int(2));
        EndIf.
    EndBody.
"""
        expect = r"""
1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_533(self):
        input = r"""
Function: main
    Body:
        printLn();

        If False Then
            printStrLn(string_of_int(1));
        ElseIf True Then
            printStrLn(string_of_int(2));
        EndIf.
    EndBody.
"""
        expect = r"""
2
"""
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_534(self):
        input = r"""
Function: main
    Body:
        printLn();

        If False Then
            printStrLn(string_of_int(1));
        ElseIf False Then
            printStrLn(string_of_int(2));
        ElseIf False Then
            printStrLn(string_of_int(3));
        ElseIf False Then
            printStrLn(string_of_int(4));
        ElseIf False Then
            printStrLn(string_of_int(5));
        ElseIf False Then
            printStrLn(string_of_int(6));
        ElseIf False Then
            printStrLn(string_of_int(7));
        ElseIf False Then
            printStrLn(string_of_int(8));
        ElseIf True Then
            printStrLn(string_of_int(9));
        ElseIf True Then
            printStrLn(string_of_int(10));
        EndIf.
    EndBody.
"""
        expect = r"""
9
"""
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_535(self):
        input = r"""
Function: main
    Body:
        printLn();

        If False Then
            printStrLn(string_of_int(1));
        ElseIf False Then
            printStrLn(string_of_int(2));
        EndIf.

        printStrLn("No else clause");
    EndBody.
"""
        expect = r"""
No else clause
"""
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_536(self):
        input = r"""
Function: main
    Body:
        printLn();

        If True Then
            printStrLn(string_of_int(1));
        ElseIf True Then
            printStrLn(string_of_int(2));
        Else
            printStrLn(string_of_int(100));
        EndIf.
    EndBody.
"""
        expect = r"""
1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_537(self):
        input = r"""
Function: main
    Body:
        printLn();

        If False Then
            printStrLn(string_of_int(1));
        ElseIf True Then
            printStrLn(string_of_int(2));
        Else
            printStrLn(string_of_int(100));
        EndIf.
    EndBody.
"""
        expect = r"""
2
"""
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_538(self):
        input = r"""
Function: main
    Body:
        printLn();

        If False Then
            printStrLn(string_of_int(1));
        ElseIf False Then
            printStrLn(string_of_int(2));
        Else
            printStrLn(string_of_int(100));
        EndIf.
    EndBody.
"""
        expect = r"""
100
"""
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    ##""" If statement (test scope) """

    def test_539(self):
        input = r"""
Var: a = 1, b = "";
Function: main
    Body:
        printLn();

        If True Then
            Var: b = 1;
            printStrLn(string_of_int(a + 1));
            printStrLn(string_of_int(b));
        ElseIf True Then
            Var: b = 1.;
            printStrLn(string_of_int(a + 2));
            printStrLn(string_of_float(b));
        Else
            Var: b = True;
            printStrLn(string_of_int(a + 3));
            printStrLn(string_of_bool(b));
        EndIf.
    EndBody.
"""
        expect = r"""
2
1
"""

        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_540(self):
        input = r"""
Var: a = 1, b = "";
Function: main
    Body:
        printLn();

        If False Then
            Var: b = 1;
            printStrLn(string_of_int(a + 1));
            printStrLn(string_of_int(b));
        ElseIf True Then
            Var: b = 1.;
            printStrLn(string_of_int(a + 2));
            printStrLn(string_of_float(b));
        Else
            Var: b = True;
            printStrLn(string_of_int(a + 3));
            printStrLn(string_of_bool(b));
        EndIf.
    EndBody.
"""
        expect = r"""
3
1.0
"""

        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_541(self):
        input = r"""
Var: a = 1, b = "";
Function: main
    Body:
        printLn();

        If False Then
            Var: b = 1;
            printStrLn(string_of_int(a + 1));
            printStrLn(string_of_int(b));
        ElseIf False Then
            Var: b = 1.;
            printStrLn(string_of_int(a + 2));
            printStrLn(string_of_float(b));
        Else
            Var: b = True;
            printStrLn(string_of_int(a + 3));
            printStrLn(string_of_bool(b));
        EndIf.
    EndBody.
"""
        expect = r"""
4
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    ##""" While (simple) """

    def test_542(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        While i < 5 Do
            print(string_of_int(i));
            i = i + 1;
        EndWhile.
        printLn();
    EndBody.
"""
        expect = r"""
01234
"""
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_543(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        While i < 0 Do
            print(string_of_int(i));
            i = i + 1;
        EndWhile.
        printStrLn("No iteration");
    EndBody.
"""
        expect = r"""
No iteration
"""
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_544(self):
        input = r"""
Function: main
    Body:
        Var: i = 0, a = 100;

        printLn();
        While i < 5 Do
            Var: a = 0;
            print(string_of_int(a));
            a = a + 1;
            i = i + 1;
        EndWhile.
        printLn();
        printStrLn(string_of_int(a));
    EndBody.
"""
        expect = r"""
00000
100
"""
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    ##""" While with Break """

    def test_545(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        While i < 5 Do
            print(string_of_int(i));
            i = i + 1;
            Break;
        EndWhile.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
0
1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_546(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        While i < 5 Do
            print(string_of_int(i));
            i = i + 1;
            If i == 3 Then
                Break;
            EndIf.
        EndWhile.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
012
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    ##""" While with Continue """

    def test_547(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        While i < 5 Do
            print(string_of_int(i));
            i = i + 1;
            Continue;
        EndWhile.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
01234
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_548(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        While i < 5 Do
            i = i + 1;
            If i < 3 Then
                Continue;
            EndIf.
            print(string_of_int(i));
        EndWhile.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
345
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    ##""" Do-While (simple) """

    def test_549(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        Do
            print(string_of_int(i));
            i = i + 1;
        While i < 5 EndDo.
        printLn();
    EndBody.
"""
        expect = r"""
01234
"""
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_550(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        Do
            print(string_of_int(i));
            i = i + 1;
        While i < 0 EndDo.
        printLn();
    EndBody.
"""
        expect = r"""
0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_551(self):
        input = r"""
Function: main
    Body:
        Var: i = 0, a = 100;

        printLn();
        Do
            Var: a = 0;
            print(string_of_int(a));
            a = a + 1;
            i = i + 1;
        While i < 5 EndDo.
        printLn();
        printStrLn(string_of_int(a));
    EndBody.
"""
        expect = r"""
00000
100
"""
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    ##""" Do-While with Break """

    def test_552(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        Do
            print(string_of_int(i));
            i = i + 1;
            Break;
        While i < 5 EndDo.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
0
1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_553(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        Do
            print(string_of_int(i));
            i = i + 1;
            If i == 3 Then
                Break;
            EndIf.
        While i < 5 EndDo.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
012
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    ##""" Do-While with Continue """

    def test_554(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        Do
            print(string_of_int(i));
            i = i + 1;
            Continue;
        While i < 5 EndDo.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
01234
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_555(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;

        printLn();
        Do
            i = i + 1;
            If i < 3 Then
                Continue;
            EndIf.
            print(string_of_int(i));
        While i < 5 EndDo.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
345
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    ##""" For (simple) """

    def test_556(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            print(string_of_int(i));
        EndFor.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
01234
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_557(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 0, 1) Do
            print(string_of_int(i));
        EndFor.
        printStrLn("No iteration");
    EndBody.
"""
        expect = r"""
No iteration
"""
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_558(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            Var: i = 3;
            print(string_of_int(i));
            i = i + 1;
        EndFor.
        printLn();
    EndBody.
"""
        expect = r"""
33333
"""
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_559(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 10, 1) Do
            print(string_of_int(i));
            i = i + 1;
        EndFor.
        printLn();
    EndBody.
"""
        expect = r"""
02468
"""
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_560(self):
        input = r"""
Function: main
    Body:
        Var: i = 0, step = 0;
        printLn();
        For (i = 0, i < 20, step) Do
            printStrLn(string_of_int(i));
            i = i + 1;
            step = step + 1;
        EndFor.
    EndBody.
"""
        expect = r"""
0
2
5
9
14
"""
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    ##""" For with Break """

    def test_561(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            print(string_of_int(i));
            Break;
        EndFor.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
0
0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_562(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            print(string_of_int(i));
            If i == 3 Then
                Break;
            EndIf.
        EndFor.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
0123
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    ##""" For with Continue """

    def test_563(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            print(string_of_int(i));
            Continue;
        EndFor.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
01234
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_564(self):
        input = r"""
Function: main
    Body:
        Var: i = 0;
        printLn();
        For (i = 0, i < 5, 1) Do
            If i < 3 Then
                Continue;
            EndIf.
            print(string_of_int(i));
        EndFor.
        printLn();
        printStrLn(string_of_int(i));
    EndBody.
"""
        expect = r"""
34
5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    #""" Return (simple) """

    def test_565(self):
        input = r"""
Function: main
    Body:
        Var: condition = False;
        printLn();
        If condition Then
            printStrLn("Not return first");
        Else
            printStrLn("Return first");
            Return;
        EndIf.
        printStrLn("This line should not be printed");
    EndBody.
"""
        expect = r"""
Return first
"""
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    ##""" Array declaration """

    def test_566(self):
        input = r"""
Var: a[1] = {1}, b[1] = {1.}, c[1] = {True}, d[1] = {"Hi!"};

Function: main
    Body:
        printLn();
        printStrLn(string_of_int(a[0]));
        printStrLn(string_of_float(b[0]));
        printStrLn(string_of_bool(c[0]));
        printStrLn(d[0]);
    EndBody.
"""
        expect = r"""
1
1.0
true
Hi!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_567(self):
        input = r"""
Var: a[2][2] = {{1,2},{3,4}};
Var: b[2][2] = {{1.,2.},{3.,4.}};
Var: c[2][2] = {{True,False},{False,True}};
Var: d[2][2] = {{"A","B"},{"C","D"}};

Function: main
    Body:
        printLn();
        printStrLn(string_of_int(a[1][1]));
        printStrLn(string_of_float(b[1][1]));
        printStrLn(string_of_bool(c[1][1]));
        printStrLn(d[1][1]);
    EndBody.
"""
        expect = r"""
4
4.0
true
D
"""
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_568(self):
        input = r"""
Var: a[1][1][1][1][1] = {{{{{1}}}}};
Var: b[1][1][1][1][1] = {{{{{1.}}}}};
Var: c[1][1][1][1][1] = {{{{{True}}}}};
Var: d[1][1][1][1][1] = {{{{{"Hi!"}}}}};

Function: main
    Body:
        printLn();
        printStrLn(string_of_int(a[0][0][0][0][0]));
        printStrLn(string_of_float(b[0][0][0][0][0]));
        printStrLn(string_of_bool(c[0][0][0][0][0]));
        printStrLn(d[0][0][0][0][0]);
    EndBody.
"""
        expect = r"""
1
1.0
true
Hi!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    #""" Array store """

    def test_569(self):
        input = r"""
Var: a[1] = {1}, b[1] = {1.}, c[1] = {True}, d[1] = {"Hi!"};

Function: main
    Body:
        a[0] = 2;
        b[0] = 2.;
        c[0] = False;
        d[0] = "Hello!";
        printLn();
        printStrLn(string_of_int(a[0]));
        printStrLn(string_of_float(b[0]));
        printStrLn(string_of_bool(c[0]));
        printStrLn(d[0]);
    EndBody.
"""
        expect = r"""
2
2.0
false
Hello!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_570(self):
        input = r"""
Var: a[2][2] = {{1,2},{3,4}};
Var: b[2][2] = {{1.,2.},{3.,4.}};
Var: c[2][2] = {{True,False},{False,True}};
Var: d[2][2] = {{"A","B"},{"C","D"}};

Function: main
    Body:
        a[1][1] = 5;
        b[1][1] = 5.;
        c[1][1] = False;
        d[1][1] = "Hi!";
        printLn();
        printStrLn(string_of_int(a[1][1]));
        printStrLn(string_of_float(b[1][1]));
        printStrLn(string_of_bool(c[1][1]));
        printStrLn(d[1][1]);
    EndBody.
"""
        expect = r"""
5
5.0
false
Hi!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_571(self):
        input = r"""
Var: a[1][1][1][1][1] = {{{{{1}}}}};
Var: b[1][1][1][1][1] = {{{{{1.}}}}};
Var: c[1][1][1][1][1] = {{{{{True}}}}};
Var: d[1][1][1][1][1] = {{{{{"Hi!"}}}}};

Function: main
    Body:
        a[0][0][0][0][0] = 2;
        b[0][0][0][0][0] = 2.;
        c[0][0][0][0][0] = False;
        d[0][0][0][0][0] = "Hello!";
        printLn();
        printStrLn(string_of_int(a[0][0][0][0][0]));
        printStrLn(string_of_float(b[0][0][0][0][0]));
        printStrLn(string_of_bool(c[0][0][0][0][0]));
        printStrLn(d[0][0][0][0][0]);
    EndBody.
"""
        expect = r"""
2
2.0
false
Hello!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    ##""" Array assign """

    def test_572(self):
        input = r"""
Var: a[1] = {1}, b[1] = {1.}, c[1] = {True}, d[1] = {"Hi!"};

Function: main
    Body:
        a = {2};
        b = {2.};
        c = {False};
        d = {"Hello!"};
        printLn();
        printStrLn(string_of_int(a[0]));
        printStrLn(string_of_float(b[0]));
        printStrLn(string_of_bool(c[0]));
        printStrLn(d[0]);
    EndBody.
"""
        expect = r"""
2
2.0
false
Hello!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_573(self):
        input = r"""
Var: a[2][2] = {{1,2},{3,4}};
Var: b[2][2] = {{1.,2.},{3.,4.}};
Var: c[2][2] = {{True,False},{False,True}};
Var: d[2][2] = {{"A","B"},{"C","D"}};

Function: main
    Body:
        a = {{11,12},{13,14}};
        b = {{11.,12.},{13.,14.}};
        c = {{False,True},{True,False}};
        d = {{"X","Y"},{"Z","T"}};
        printLn();
        printStrLn(string_of_int(a[1][1]));
        printStrLn(string_of_float(b[1][1]));
        printStrLn(string_of_bool(c[1][1]));
        printStrLn(d[1][1]);
    EndBody.
"""
        expect = r"""
14
14.0
false
T
"""
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_574(self):
        input = r"""
Var: a[1][1][1][1][1] = {{{{{1}}}}};
Var: b[1][1][1][1][1] = {{{{{1.}}}}};
Var: c[1][1][1][1][1] = {{{{{True}}}}};
Var: d[1][1][1][1][1] = {{{{{"Hi!"}}}}};

Function: main
    Body:
        a = {{{{{2}}}}};
        b = {{{{{2.}}}}};
        c = {{{{{False}}}}};
        d = {{{{{"Hello!"}}}}};
        printLn();
        printStrLn(string_of_int(a[0][0][0][0][0]));
        printStrLn(string_of_float(b[0][0][0][0][0]));
        printStrLn(string_of_bool(c[0][0][0][0][0]));
        printStrLn(d[0][0][0][0][0]);
    EndBody.
"""
        expect = r"""
2
2.0
false
Hello!
"""
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    ##""" Short circuit """

    def test_575(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(False && (1 \ 0 == 0)));
    EndBody.
"""
        expect = r"""
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_576(self):
        input = r"""
Function: main
    Body:
        printLn();
        printStrLn(string_of_bool(True || (1 \ 0 == 0)));
    EndBody.
"""
        expect = r"""
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    # PART 2: INFERENCE

    # PART 3: COMPLEX PROGRAM

    def test_577(self):
        input = r"""
** Selection sort **

Var: arr[10] = {1, 7, 8, 4, 2, 5, 9, 10, 6, 3};
Function: main
    Body:
        Var: i = 0;
        For (i = 0, i < 10, 1) Do
            Var: j = 0, minIndex = 0, temp = 0;
            ** Find min index **
            minIndex = i;
            For (j = i + 1, j < 10, 1) Do
                If arr[j] < arr[minIndex] Then
                    minIndex = j;
                EndIf.
            EndFor.
            ** Swap **
            temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        EndFor.

        print("\nSorted array:");
        For (i = 0, i < 10, 1) Do
            print(" ");
            print(string_of_int(arr[i]));
        EndFor.
        printLn();
    EndBody.
"""
        expect = r"""
Sorted array: 1 2 3 4 5 6 7 8 9 10
"""
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_578(self):
        input = r"""
** Find prime number **

Function: main
    Body:
        Var: i = 0, n = 50;
        print("\nPrime numbers that less than ");
        print(string_of_int(n));
        print(":");
        For (i = 2, i < n, 1) Do
            Var: isPrime = True, j = 2;
            ** Check if prime **
            For (j = 2, j < i - 1, 1) Do
                ** Early terminate **
                If j * j > i Then
                    Break;
                EndIf.
                If i % j == 0 Then
                    isPrime = False;
                    Break;
                EndIf.
            EndFor.
            ** Print if prime **
            If isPrime Then
                print(" ");
                print(string_of_int(i));
            EndIf.
        EndFor.
        printLn();
    EndBody.
"""
        expect = r"""
Prime numbers that less than 50: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
"""
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_579(self):
        input = r"""
** Find first positive missing value **

Var: arr[15] = {
    0, 3, 4, 100, 2,
    20, 1, 99, 7, 8,
    6, 2, 5, 10, 12
};

Function: main
    Body:
        Var: n = 15, hashTable[15] = {
            False,False,False,False,False,
            False,False,False,False,False,
            False,False,False,False,False
        };
        Var: i = 0, firstMissValue = 0;
        ** Iterate and save to hash table **
        For (i = 0, i < n, 1) Do
            If (arr[i] > n) || (arr[i] <= 0) Then
                Continue;
            EndIf.
            hashTable[arr[i] - 1] = True;
        EndFor.
        ** Find first miss value **
        firstMissValue = 1;
        While (firstMissValue <= n) && hashTable[firstMissValue - 1] Do
            firstMissValue = firstMissValue + 1;
        EndWhile.
        print("\nFirst positive missing value: ");
        printStrLn(string_of_int(firstMissValue));
    EndBody.
"""
        expect = r"""
First positive missing value: 9
"""
        self.assertTrue(TestCodeGen.test(input, expect, 579))