# Nguyen Khiem - 1810235
import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
#     def test_int(self):
#         """Simple program: int main() {} """
#         input = """Function: main
#                    Body: 
#                         print(string_of_int(120));
#                    EndBody."""
#         expect = "120"
#         self.assertTrue(TestCodeGen.test(input,expect,500))
#     def test_int_ast(self):
#     	input = Program([
#     		FuncDecl(Id("main"),[],([],[
#     			CallStmt(Id("print"),[
#                     CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
#     	expect = "120"
#     	self.assertTrue(TestCodeGen.test(input,expect,501))

#     def test2(self):
#         """Simple program: int main() {} """
#         input = \
# """Function: a
# Parameter: b
# Body: 
#     Return b + 1;
# EndBody.

# Function: main
# Body: 
#     print("abc");
#     print(string_of_int(a(9) + int_of_float(foo2(1.5, {0.5}))));
#     foo(1, {{1,2}});
# EndBody.

# Function: foo
# Parameter: d, e[1][2]
# Body:
#     d = e[0][1];
#     Return;
# EndBody.

# Function: foo2
# Parameter: d, e[1]
# Body: 
#     Return d +. e[0];
# EndBody."""
#         expect = "abc12"
#         self.assertTrue(TestCodeGen.test(input,expect,502))

#     def test3(self):
#         """Simple program: int main() {} """
#         input = \
# """Function: a
# Parameter: b
# Body: 
#     Return b + 1;
# EndBody.

# Function: main
# Body: 
#     print("abc");
#     foo(1, {{1,2}});
# EndBody.

# Function: foo
# Parameter: d, e[1][2]
# Body:
#     d = e[0][1];
#     Return;
# EndBody.

# Function: foo2
# Parameter: d, e[1]
# Body: 
#     Return d +. e[0];
# EndBody."""
#         expect = "abc"
#         self.assertTrue(TestCodeGen.test(input,expect,503))

#     def test4(self):
#         """Test 4"""
#         input = \
# r"""Function: main
# Body: 
#     print("hell'"o");
# EndBody."""
#         expect = "hell\"o"
#         self.assertTrue(TestCodeGen.test(input,expect,504))

#     def test5(self):
#         """Test 5"""
#         input = \
# r"""Var: a = 123;
# Function: main
# Body: 
#     print(string_of_int(a));
# EndBody."""
#         expect = "123"
#         self.assertTrue(TestCodeGen.test(input,expect,505))

#     def test6(self):
#         """Test 6"""
#         input = \
# r"""Function: foo
# Body: 
#     Var: a = 1, b = 1.2;
#     Var: c = True;
#     Return c;
# EndBody.

# Function: main
# Body: 
#     print(string_of_bool(foo()));
# EndBody."""
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,506))

#     def test7(self):
#         """Test 7"""
#         input = \
# r"""Var: a = 123;
# Function: main
# Body:
#     Var: x = "abc";
#     print(x);
# EndBody."""
#         expect = "abc"
#         self.assertTrue(TestCodeGen.test(input,expect,507))


#     def test8(self):
#         """Test 8"""
#         input = \
# r"""Var: a = 123;
# Function: foo
# Body:
#     Var: x = "abc";
#     print(x);
# EndBody.

# Function: main
# Body:
#     foo();
# EndBody."""
#         expect = "abc"
#         self.assertTrue(TestCodeGen.test(input,expect,508))


#     def test9(self):
#         """Test 9"""
#         input = \
# r"""Function: main
# Body:
#     Var: a = True;
#     a = False;
#     print(string_of_bool(a));
# EndBody."""
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,509))

#     def test10(self):
#         """Test 10"""
#         input = \
# r"""Function: foo
# Body: 
#     Var: a = 1, b = 1.2;
#     Var: c = True;
#     Return b;
# EndBody.

# Function: main
# Body: 
#     print(string_of_float(foo()));
# EndBody."""
#         expect = "1.2"
#         self.assertTrue(TestCodeGen.test(input,expect,510))

#     def test11(self):
#         """Test 11"""
#         input = \
# r"""Function: foo
# Body: 
#     Var: a = 1, b = 1.2;
#     Var: c = True;
#     Return c;
# EndBody.

# Function: main
# Body: 
#     print(string_of_bool(foo()));
# EndBody."""
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,511))

#     def test12(self):
#         """Test 12"""
#         input = \
# r"""Function: foo
# Body: 
#     Var: a = 1, b = 1.2;
#     Var: c = True;
#     Return !!!c;
# EndBody.

# Function: main
# Body: 
#     print(string_of_bool(foo()));
# EndBody."""
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,512))

#     def test13(self):
#         """Test 13"""
#         input = \
# r"""Function: foo
# Body: 
#     Var: a = 1, b = 1.2;
#     Var: c = True;
#     Return a < 3;
# EndBody.

# Function: main
# Body: 
#     print(string_of_bool(foo()));
# EndBody."""
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,513))

#     def test14(self):
#         """Test 14"""
#         input = \
# r"""Function: foo
# Body: 
#     Var: a = 1, b = 1.2;
#     Var: c = True;
#     Return b =/= 1.2;
# EndBody.

# Function: main
# Body: 
#     print(string_of_bool(foo()));
# EndBody."""
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,514))

#     def test_515(self):
#         """Testcase number 515:"""
#         input = \
# r"""Function: foo
# Body: 
#     Var: a = 1, b = 1.2;
#     Var: c = True;
#     Return a * 5 - 2 > 999;
# EndBody.

# Function: main
# Body: 
#     print(string_of_bool(foo()));
# EndBody."""
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,515))

#     def test_516(self):
#         """Testcase number 516:"""
#         input = \
# r"""Function: foo
# Body: 
#     Var: a = 1, b = 1.2;
#     Var: c = True;
#     Return b *. 4.4 -. 2.;
# EndBody.

# Function: main
# Body: 
#     print(string_of_float(foo()));
# EndBody."""
#         expect = "3.2800002"
#         self.assertTrue(TestCodeGen.test(input,expect,516))

#     def test_517(self):
#         """Testcase number 517:"""
#         input = \
# r"""Var: a = "init";
# Function: foo
# Body: 
#     a = "foo";
#     Return True;
# EndBody.

# Function: foo1
# Body: 
#     a = "foo1";
#     Return False;
# EndBody.

# Function: main
# Body:
#     Var: b = True;
#     b = b && foo1() && foo();
#     print(string_of_bool(b));
#     print(a);
# EndBody."""
#         expect = "falsefoo1"
#         self.assertTrue(TestCodeGen.test(input,expect,517))

#     def test_518(self):
#         """Testcase number 518:"""
#         input = \
# r"""Var: a = "init";
# Function: foo
# Body: 
#     a = "foo";
#     Return True;
# EndBody.

# Function: foo1
# Body: 
#     a = "foo1";
#     Return False;
# EndBody.

# Function: main
# Body:
#     Var: b = True;
#     b = b && foo1() && False || True || foo();
#     print(string_of_bool(b));
#     print(a);
# EndBody."""
#         expect = "truefoo1"
#         self.assertTrue(TestCodeGen.test(input,expect,518))

#     def test_519(self):
#         """Testcase number 519:"""
#         input = \
# r"""Function: foo
# Parameter: a
# Body: 
#     Return a + 1;
# EndBody.

# Function: main
# Body:
#     print(string_of_int(foo(9)));
# EndBody."""
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,519))

#     def test_520(self):
#         """Testcase number 520:"""
#         input = \
# r"""Function: foo
# Parameter: a
# Body: 
#     Return 3 \ 2;
# EndBody.

# Function: main
# Body:
#     print(string_of_int(foo(9)));
# EndBody."""
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,520))

#     def test_521(self):
#         """Testcase number 521:"""
#         input = \
# r"""
# Function: main
# Body:
#     Var: a = 5;
#     While a > 0 Do
#         a = a - 1;
#         print(string_of_int(a));
#     EndWhile.
#     print(string_of_int(a));
# EndBody."""
#         expect = "432100"
#         self.assertTrue(TestCodeGen.test(input,expect,521))

#     def test_522(self):
#         """Testcase number 522:"""
#         input = \
# r"""
# Function: main
# Body:
#     Var: a = 5;
#     While False Do
#         a = a - 1;
#         print(string_of_int(a));
#     EndWhile.
#     print(string_of_int(a));
# EndBody."""
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,522))

#     def test_523(self):
#         """Testcase number 523:"""
#         input = \
# r"""
# Function: main
# Body:
#     Var: a = 5;
#     Do
#         a = a - 1;
#         print(string_of_int(a));
#     While a > 0 EndDo.
#     print(string_of_int(a));
# EndBody."""
#         expect = "432100"
#         self.assertTrue(TestCodeGen.test(input,expect,523))

#     def test_524(self):
#         """Testcase number 524:"""
#         input = \
# r"""
# Function: main
# Body:
#     Var: a = 5;
#     Do
#         print(string_of_int(a));
#     While False EndDo.
# EndBody."""
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,524))

#     def test_525(self):
#         """Testcase number 525:"""
#         input = \
# r"""Function: main
# Body:
#     While True Do Break; EndWhile.
#     print("broke!");
# EndBody."""
#         expect = "broke!"
#         self.assertTrue(TestCodeGen.test(input,expect,525))

#     def test_526(self):
#         """Testcase number 526:"""
#         input = \
# r"""Function: main
# Body:
#     Var: a = 5;
#     While a > 0 Do
#         a = a - 1;
#         print("exec");
#         Continue;
#         print("this will not be executed!");
#     EndWhile.
#     print("broke!");
# EndBody."""
#         expect = "execexecexecexecexecbroke!"
#         self.assertTrue(TestCodeGen.test(input,expect,526))

#     def test_527(self):
#         """Testcase number 527:"""
#         input = \
# r"""Var: b = 0;
# Function: main
# Body:
#     For (b = 1, b <= 5, 2) Do
#         print("Do!");
#     EndFor.
# EndBody."""
#         expect = "Do!Do!Do!"
#         self.assertTrue(TestCodeGen.test(input,expect,527))

#     def test_528(self):
#         """Testcase number 528:"""
#         input = \
# r"""Var: b = 0;
# Function: main
# Body:
#     Do
#         Var: x = 2;
#         While (b < x) Do
#             b = b + 1;
#             print("do");
#         EndWhile.
#     While False EndDo.
# EndBody."""
#         expect = "dodo"
#         self.assertTrue(TestCodeGen.test(input,expect,528))

#     def test_529(self):
#         """Testcase number 529:"""
#         input = \
# r"""Var: b = 1;
# Function: main
# Body:
#     If b == 0 Then
#         print("if");
#     ElseIf b == 1 Then
#         print("elseif");
#     EndIf.
# EndBody."""
#         expect = "elseif"
#         self.assertTrue(TestCodeGen.test(input,expect,529))

#     def test_530(self):
#         """Testcase number 530:"""
#         input = \
# r"""Var: b = 33;
# Function: main
# Body:
#     If b == 0 Then
#         print("if");
#     ElseIf b == 1 Then
#         print("elseif");
#     Else
#         print("else");
#     EndIf.
# EndBody."""
#         expect = "else"
#         self.assertTrue(TestCodeGen.test(input,expect,530))

#     def test_531(self):
#         """Testcase number 531:"""
#         input = \
# r"""Var: b = 0;
# Function: main
# Body:
#     Var: x = 3;
#     If b == 0 Then
#         Var: x = 1;

#         Do
#             print(string_of_int(x));
#         While False EndDo.

#     ElseIf b == 1 Then
#         print("elseif");
#     EndIf.
#     print(string_of_int(x));
# EndBody."""
#         expect = "13"
#         self.assertTrue(TestCodeGen.test(input,expect,531))

#     def test_532(self):
#         """Testcase number 532:"""
#         input = \
# r"""Var: b = 1;
# Function: main
# Body:
#     Var: x = 3;
#     If b == 0 Then
#         **do nothing**
#     ElseIf b == 1 Then
#         Var: x = 1;

#         print("elseif\n");

#         Do
#             Var: x = 2;
#             print(string_of_int(x));
#         While False EndDo.

#         print(string_of_int(x));
#     Else ** do nothing **
#     EndIf.
#     print(string_of_int(x));
# EndBody."""
#         expect = "elseif\n213"
#         self.assertTrue(TestCodeGen.test(input,expect,532))

#     def test_533(self):
#         """Testcase number 533:"""
#         input = \
# r"""Var: b = 1;
# Function: foo
# Parameter: x
# Body:
#     If x\5 == 1 Then
#         If x * 5 == 5 Then
#         Else
#             Var: x = 5;
#             x = x + 1;
#             print(string_of_int(x));
#         EndIf.
#     EndIf.
#     print(string_of_int(x - 9));
# EndBody.

# Function: main
# Body:
#     foo(9);
# EndBody."""
#         expect = "60"
#         self.assertTrue(TestCodeGen.test(input,expect,533))

#     def test_534(self):
#         """Testcase number 534:"""
#         input = \
# r"""Var: b = 1;
# Function: foo
# Body:
#     For (b = 1, b < 5, b) Do
#         print(string_of_int(b));
#     EndFor.

# EndBody.

# Function: main
# Body:
#     foo();
# EndBody."""
#         expect = "124"
#         self.assertTrue(TestCodeGen.test(input,expect,534))

#     def test_535(self):
#         """Testcase number 535:"""
#         input = \
# r"""Var: b = 1;
# Function: foo
# Body:
#     For (b = 1, b < 5, 1) Do
#         While True Do
#             b = b + 1;
#             print(string_of_int(b));
#             If b == 2 Then Continue; EndIf.
#             Break;
#         EndWhile.
#         print(string_of_int(b));
#     EndFor.
# EndBody.

# Function: main
# Body:
#     foo();
# EndBody."""
#         expect = "23355"
#         self.assertTrue(TestCodeGen.test(input,expect,535))

#     def test_536(self):
#         """Testcase number 536:"""
#         input = \
# r"""Var: inst[3] = {1, 2, 3};
# Var: flost[3] = {1., 2., 3.};
# Var: boost[3][2] = {{True, False}, {True, False}, {False, False}};
# Var: st[2][2] = {{"a", "bc"}, {"3","k"}};

# Function: main
# Body:
#     Var: x[2] = {1, 2};
#     Var: y[2][1] = {{10}, {20}};
#     Var: z[1][1][2] = {{{100, 200}}};
#     print("x");
# EndBody."""
#         expect = "x"
#         self.assertTrue(TestCodeGen.test(input,expect,536))

#     def test_537(self):
#         """Testcase number 537:"""
#         input = \
# r"""Function: foo
# Parameter: x
# Body:
#     x = "def";
# EndBody.

# Function: main
# Body:
#     Var: x = "abc";
#     foo(x);
#     print(x);
# EndBody."""
#         expect = "abc"
#         self.assertTrue(TestCodeGen.test(input,expect,537))

#     def test_538(self):
#         """Testcase number 538:"""
#         input = \
# r"""Function: main
# Body:
#     Var: x[3] = {1, 2, 3}, i = 0;
#     x[0] = x[2];
#     For (i = 0, i < 3, 1) Do
#         print(string_of_int(x[i]));
#     EndFor.
# EndBody."""
#         expect = "323"
#         self.assertTrue(TestCodeGen.test(input,expect,538))

#     def test_539(self):
#         """Testcase number 539:"""
#         input = \
# r"""Var: x[3] = {1, 2, 3}, i = 0;

# Function: main
# Body:
#     x[0] = x[2];
#     For (i = 0, i < 3, 1) Do
#         print(string_of_int(x[i]));
#     EndFor.
# EndBody."""
#         expect = "323"
#         self.assertTrue(TestCodeGen.test(input,expect,539))

#     def test_540(self):
#         """Testcase number 540:"""
#         input = \
# r"""Var: x[3] = {1., 2., 3.}, i = 0;

# Function: main
# Body:
#     Var: fl[3] = {1.5, 2.5, 3.5};
#     fl[2] = x[1];
#     x[2] = fl[1];

#     For (i = 0, i < 3, 1) Do
#         print(string_of_float(x[i]));
#         print(",");
#     EndFor.
#     For (i = 0, i < 3, 1) Do
#         print(string_of_float(fl[i]));
#         print(",");
#     EndFor.
# EndBody."""
#         expect = "1.0,2.0,2.5,1.5,2.5,2.0,"
#         self.assertTrue(TestCodeGen.test(input,expect,540))

#     def test_541(self):
#         """Testcase number 541:"""
#         input = \
# r"""Var: x[3] = {1., 2., 3.}, i = 0;

# Function: main
# Body:
#     x[1] = 1.2;

#     For (i = 0, i < 3, 1) Do
#         print(string_of_float(x[i]));
#         print(",");
#     EndFor.
# EndBody."""
#         expect = "1.0,1.2,3.0,"
#         self.assertTrue(TestCodeGen.test(input,expect,541))

#     def test_542(self):
#         """Testcase number 542:"""
#         input = \
# r"""Var: x[2] = {True, False}, i = 0;

# Function: main
# Body:
#     x[1] = x[0];

#     For (i = 0, i < 2, 1) Do
#         print(string_of_bool(x[i]));
#         print(",");
#     EndFor.
# EndBody."""
#         expect = "true,true,"
#         self.assertTrue(TestCodeGen.test(input,expect,542))

#     def test_543(self):
#         """Testcase number 543:"""
#         input = \
# r"""Function: foo
# Parameter: a, b[2]
# Body:
#     a = a + 1;
#     b[0] = b[0] + 10;
#     b[1] = 10;
# EndBody.

# Function: main
# Body:
#     Var: arr[2] = {1, 2}, x = 5, i = 0;

#     foo(x, arr);
#     For (i = 0, i < 2, 1) Do
#         print(string_of_int(arr[i]));
#         print(",");
#     EndFor.
#     print(string_of_int(x));
# EndBody."""
#         expect = "11,10,5"
#         self.assertTrue(TestCodeGen.test(input,expect,543))

#     def test_544(self):
#         """Testcase number 544:"""
#         input = \
# """Var: z = "abcdef";

# Function: main
# Body:
#     Var: x[6] = {"a", "b", "c", "d", "e", "f"};
#     Var: y = "abcdef";
#     z = x[1];
#     print(z);
# EndBody."""
#         expect = "b"
#         self.assertTrue(TestCodeGen.test(input,expect,544))

#     def test_545(self):
#         """Testcase number 545:"""
#         input = \
# """Var: z = "abcdef";
# Function: riggedswap
# Parameter: x, y
# Body:
#     Var: n = 0;
#     n = x;
#     x = y;
#     y = n;
# EndBody.

# Function: main
# Body:
#     Var: x[6] = {1, 2, 3, 4, 5, 6}, a = 0;
#     riggedswap(x[1], x[2]);
#     For(a = 0, a < 6, 1) Do
#         print(string_of_int(x[a]));
#     EndFor.

# EndBody."""
#         expect = "123456"
#         self.assertTrue(TestCodeGen.test(input,expect,545))

#     def test_546(self):
#         """Testcase number 546:"""
#         input = \
# """ Var: str1[3] = {"12", "34", "56"};

# Function: concatting
# Parameter: str1[3], str2[3]
# Body:
#     Var: rett[6] = {"","","","","",""};
#     rett[0] = str1[0];
#     rett[1] = str1[1];
#     rett[2] = str1[2];
#     rett[3] = str2[0];
#     rett[4] = str2[1];
#     rett[5] = str2[2];
#     Return rett;
# EndBody.

# Function: main
# Body:
#     Var: str2[3] = {"ab", "c", "def"};
#     Var: concat[6] = {"","","","","",""};
#     Var: i = 0;
    
#     concat = concatting(str1, str2);
#     For (i = 0, i < 6, 1) Do
#         printStrLn(concat[i]);
#     EndFor.
# EndBody."""
#         expect = "12\n34\n56\nab\nc\ndef\n"
#         self.assertTrue(TestCodeGen.test(input,expect,546))

#     def test_547(self):
#         """Testcase number 547:"""
#         input = \
# """Function: foo
# Body:
#     Return {"a", "b"};
# EndBody.

# Function: main
# Body:
#     print(foo()[1]);
# EndBody."""
#         expect = "b"
#         self.assertTrue(TestCodeGen.test(input,expect,547))

#     def test_548(self):
#         """Testcase number 548:"""
#         input = \
# """Function: foo
# Body:
#     Return {"a", "b"};
# EndBody.

# Function: main
# Body:
#     Var: x[3][2] = {{0,0},{0,0},{0,0}};
#     x[1234%3][int_of_string("0") + 9\\10] = 1234 * 5;
#     print(string_of_int(x[1234%3][0 + 9\\10]));
# EndBody."""
#         expect = "6170"
#         self.assertTrue(TestCodeGen.test(input,expect,548))

#     def test_549(self):
#         """Testcase number 549:"""
#         input = \
# """Function: main
# Body:
#     print(string_of_int({{{1,2,3}}}[0][0][1]));
# EndBody."""
#         expect = "2"
#         self.assertTrue(TestCodeGen.test(input,expect,549))

#     def test_550(self):
#         """Testcase number 550:"""
#         input = \
# """Function: main
# Body:
#     Var: a[1][2][2][2][3][1] = {{{{{{1},{2},{3}},{{4},{5},{6}}},{{{7},{8},{9}},{{10},{11},{12}}}},
#                             {{{{13},{14},{15}},{{16},{17},{18}}},{{{19},{20},{21}},{{22},{23},{24}}}}}};
#     print(string_of_int(a[0][1][1][0][0][0]));
# EndBody."""
#         expect = "19"
#         self.assertTrue(TestCodeGen.test(input,expect,550))

#     def test_551(self):
#         """Testcase number 551:"""
#         input = \
# """Function: main
# Body:
#     Var: x = 0;
#     For (x = 0, x < 5, 1) Do
#         If x < 2 Then
#             Continue;
#         EndIf.
#         print(string_of_int(x));
#     EndFor.
# EndBody."""
#         expect = "234"
#         self.assertTrue(TestCodeGen.test(input,expect,551))

#     def test_552(self):
#         """Testcase number 552:"""
#         input = \
# """Function: main
# Body:
#     Var: x = 0;
#     For (x = 0, x < 5, 1) Do
#         If x < 2 Then
#             Continue;
#         ElseIf x > 3 Then
#             Break;
#         EndIf.
#         print(string_of_int(x));
#     EndFor.
# EndBody."""
#         expect = "23"
#         self.assertTrue(TestCodeGen.test(input,expect,552))

#     def test_553(self):
#         """Testcase number 553:"""
#         input = \
# """Function: main
# Body:
#     Var: x = 0;
#     While x < 5 Do
#         x = x + 1;
#         If x < 2 Then
#             Continue;**
#         ElseIf x > 3 Then
#             Break;**
#         EndIf.
#         print(string_of_int(x));
#     EndWhile.
# EndBody."""
#         expect = "2345"
#         self.assertTrue(TestCodeGen.test(input,expect,553))

#     def test_554(self):
#         """Testcase number 554:"""
#         input = \
# """Function: main
# Body:
#     Var: x = 0;
#     While x < 5 Do
#         x = x + 1;
#         If x < 2 Then
#             Continue;
#         ElseIf x > 3 Then
#             Break;
#         EndIf.
#         print(string_of_int(x));
#     EndWhile.
# EndBody."""
#         expect = "23"
#         self.assertTrue(TestCodeGen.test(input,expect,554))

#     def test_555(self):
#         """Testcase number 555:"""
#         input = \
# """Var: x = 0;
# Function: foo
# Parameter: x
# Body:
#     x = 5;
#     If True Then
#         Var: x = 1;
#         x = 6;
#     EndIf.
#     print(string_of_int(x));
# EndBody.

# Function: main
# Body:
#     Var: x = 10;
#     foo(2);
# EndBody."""
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,555))

#     def test_556(self):
#         """Testcase number 556:"""
#         input = \
# """Var: a = 10;
# Function: foo
# Parameter: x
# Body:
#     a = x;
#     Return x;
# EndBody.

# Function: main
# Body:
#     print(string_of_int(a + foo(5)));
# EndBody."""
#         expect = "15"
#         self.assertTrue(TestCodeGen.test(input,expect,556))

#     def test_557(self):
#         """Testcase number 557:"""
#         input = \
# """Var: a = 10;
# Function: foo
# Parameter: x
# Body:
#     a = x;
#     Return x;
# EndBody.

# Function: main
# Body:
#     print(string_of_int(foo(5) + a));
# EndBody."""
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,557))

#     def test_558(self):
#         """Testcase number 558:"""
#         input = \
# """Var: a = 9;
# Function: foo
# Parameter: x
# Body:
#     a = x;
#     Return x;
# EndBody.

# Function: main
# Body:
#     print(string_of_int(a + foo(5) * a));
# EndBody."""
#         expect = "34"
#         self.assertTrue(TestCodeGen.test(input,expect,558))

#     def test_559(self):
#         """Testcase number 559:"""
#         input = \
# """Var: a = 9;
# Function: foo
# Parameter: x
# Body:
#     a = x;
#     Return x;
# EndBody.

# Function: main
# Body:
#     print(string_of_int(a * -foo(5)));
# EndBody."""
#         expect = "-45"
#         self.assertTrue(TestCodeGen.test(input,expect,559))

#     def test_560(self):
#         """Testcase number 560:"""
#         input = \
# r"""Var: a = 9;
# Function: foo
# Parameter: x, y
# Body:
#     a = x;
#     Return x < y;
# EndBody.

# Function: foo1
# Parameter: x, y
# Body:
#     a = int_of_float(x \. y);
#     Return x <. y;
# EndBody.

# Function: main
# Body:
#     print(string_of_bool(foo(1, 2) || foo1(2.5, 1.5)));
#     print(string_of_int(a));
# EndBody."""
#         expect = "true1"
#         self.assertTrue(TestCodeGen.test(input,expect,560))

#     def test_561(self):
#         """Testcase number 561:"""
#         input = \
# r"""Var: a = 9;
# Function: foo
# Parameter: x, y
# Body:
#     a = x;
#     Return x < y;
# EndBody.

# Function: foo1
# Parameter: x, y
# Body:
#     a = int_of_float(x \. y);
#     Return x <. y;
# EndBody.

# Function: main
# Body:
#     print(string_of_bool(foo(1, 2) && foo1(2.5, 1.5)));
#     print(string_of_int(a));
# EndBody."""
#         expect = "false1"
#         self.assertTrue(TestCodeGen.test(input,expect,561))

#     def test_562(self):
#         """Testcase number 562:"""
#         input = \
# r"""Var: a = 9;
# Function: foo
# Body:
#     a = 1;
#     Return False;
# EndBody.

# Function: foo1
# Body:
#     a = 2;
#     Return False;
# EndBody.

# Function: foo2
# Body:
#     a = 3;
#     Return False;
# EndBody.

# Function: main
# Body:
#     print(string_of_bool(foo() && foo1() && foo2()));
#     print(string_of_int(a));
# EndBody."""
#         expect = "false1"
#         self.assertTrue(TestCodeGen.test(input,expect,562))

#     def test_563(self):
#         """Testcase number 563:"""
#         input = \
# r"""Var: a = 9;
# Function: foo
# Body:
#     a = 1;
#     Return False;
# EndBody.

# Function: foo1
# Body:
#     a = 2;
#     Return False;
# EndBody.

# Function: foo2
# Body:
#     a = 3;
#     Return True;
# EndBody.

# Function: foo3
# Body:
#     a = 4;
#     Return True;
# EndBody.

# Function: main
# Body:
#     print(string_of_bool(foo() && foo1() || foo2() || foo3()));
#     print(string_of_int(a));
# EndBody."""
#         expect = "true3"
#         self.assertTrue(TestCodeGen.test(input,expect,563))

#     def test_564(self):
#         """Testcase number 564:"""
#         input = \
# r"""Var: a = 9;
# Function: foo
# Body:
#     a = 1;
#     Return False;
# EndBody.

# Function: foo1
# Body:
#     a = 2;
#     Return False;
# EndBody.

# Function: foo2
# Body:
#     a = 3;
#     Return True;
# EndBody.

# Function: foo3
# Body:
#     a = 4;
#     Return True;
# EndBody.

# Function: main
# Body:
#     print(string_of_bool(!foo() || foo1() || foo2() || foo3()));
#     print(string_of_int(a));
# EndBody."""
#         expect = "true1"
#         self.assertTrue(TestCodeGen.test(input,expect,564))

#     def test_565(self):
#         """Testcase number 565:"""
#         input = \
# r"""Function: main
# Body:
#     print(string_of_float(-.1.2E-2));
# EndBody."""
#         expect = "-0.012"
#         self.assertTrue(TestCodeGen.test(input,expect,565))

#     def test_566(self):
#         """Testcase number 566:"""
#         input = \
# r"""Function: main
# Body:
#     print(string_of_float(-.1.2E-30));
# EndBody."""
#         expect = "-0.0"
#         self.assertTrue(TestCodeGen.test(input,expect,566))

#     def test_567(self):
#         """Testcase number 567:"""
#         input = \
# r"""Function: main
# Body:
#     print(string_of_bool(!(-.1.2 *. 2.4 =/= 3.5)));
# EndBody."""
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,567))

#     def test_568(self):
#         """Testcase number 568:"""
#         input = \
# r"""Var: a = 9;
# Function: foo
# Body:
#     a = 1;
#     Return True;
# EndBody.

# Function: foo1
# Body:
#     a = 2;
#     Return True;
# EndBody.

# Function: foo2
# Body:
#     a = 3;
#     Return True;
# EndBody.

# Function: foo3
# Body:
#     a = 4;
#     Return True;
# EndBody.

# Function: main
# Body:
#     print(string_of_bool(foo() || foo1() || foo2() || foo3()));
#     print(string_of_int(a));
# EndBody."""
#         expect = "true1"
#         self.assertTrue(TestCodeGen.test(input,expect,568))

#     def test_569(self):
#         """Testcase number 569:"""
#         input = \
# r"""Function: main
# Body:
#     Var: a = 0;
#     a = int_of_float(float_to_int(1));
#     print(string_of_int(a));
#     printStrLn(string_of_int(int_of_string("123")));
#     print(string_of_float(float_of_string("4.5")));
#     print(string_of_bool(bool_of_string("true")));
# EndBody."""
#         expect = "1123\n4.5true"
#         self.assertTrue(TestCodeGen.test(input,expect,569))

#     def test_570(self):
#         """Testcase number 570:"""
#         input = \
# r"""Function: main
# Body:
#     Var: a = 0;
#     a = 1 + 2 * 3 - 3 % 20 \ 6;
#     print(string_of_int(a));
# EndBody."""
#         expect = "7"
#         self.assertTrue(TestCodeGen.test(input,expect,570))

#     def test_571(self):
#         """Testcase number 571:"""
#         input = \
# r"""Function: main
# Body:
#     Var: a = 0;
#     a = 159 \ 10 \ 2;
#     print(string_of_int(a));
# EndBody."""
#         expect = "7"
#         self.assertTrue(TestCodeGen.test(input,expect,571))

#     def test_572(self):
#         """Testcase number 572:"""
#         input = \
# r"""Function: main
# Body:
#     Var: a = False;
#     a = 19 % 20 \ 3 != 19 % (20 \ 3);
#     print(string_of_bool(a));
# EndBody."""
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,572))

#     def test_573(self):
#         """Testcase number 573:"""
#         input = \
# r"""Function: foo
# Parameter: x
# Body:
#     If x Then
#         Return {{1000}};
#     Else
#         Return {{99}};
#     EndIf.
# EndBody.

# Function: main
# Body:
#     Var: a = 0, b = False;
#     a = foo((2 * 3 > 5) || b)[0][0] - foo(19 % 20 \ 3 == 19 % (20 \ 3))[0][0];
#     print(string_of_int(a));
# EndBody."""
#         expect = "901"
#         self.assertTrue(TestCodeGen.test(input,expect,573))

#     def test_574(self):
#         """Testcase number 574:"""
#         input = \
# r"""Function: foo
# Parameter: x
# Body:
#     If x Then
#         Return {{1000.}};
#     Else
#         Return {{99.}};
#     EndIf.
# EndBody.

# Function: main
# Body:
#     Var: a = 1.0, b = False;
#     a = foo((2. *. 3. >. 5.) || b)[0][0] -. foo(!(19. \. 20. \. 3. =/= 19. \. (20. \. 3.)))[0][0];
#     print(string_of_float(a));
# EndBody."""
#         expect = "901.0"
#         self.assertTrue(TestCodeGen.test(input,expect,574))

#     def test_575(self):
#         """Testcase number 575:"""
#         input = \
# r"""Var: x[1] = {4.7};
# Function: main
# Body:
#     Var: a = 1.0, b = False;
#     b = 2.0 \. 3.0 *. 6e0 =/= 2.0 +. 6.7 -. x[0];
#     print(string_of_bool(b));
# EndBody."""
#         expect = "false"
#         self.assertTrue(TestCodeGen.test(input,expect,575))

#     def test_576(self):
#         """Testcase number 576:"""
#         input = \
# r"""Var: x = 4.7;
# Function: main
# Body:
#     x = (x +. 0.3 -. 2.0 *. 2.0) \. 4.0;
#     print(string_of_float(x));
# EndBody."""
#         expect = "0.25"
#         self.assertTrue(TestCodeGen.test(input,expect,576))

#     def test_577(self):
#         """Testcase number 577:"""
#         input = \
# r"""Var: x = True, y = True, z = True;
# Function: main
# Body:
#     x = (2 > 2) || (2 < 2);
#     y = (2 >= 2) && (2 <= 2);
#     z = (2 == 2) && (2 != 3);
#     print(string_of_bool(x));
#     print(string_of_bool(y && z));
# EndBody."""
#         expect = "falsetrue"
#         self.assertTrue(TestCodeGen.test(input,expect,577))

#     def test_578(self):
#         """Testcase number 578:"""
#         input = \
# r"""Var: x = True, y = True, z = True;
# Function: main
# Body:
#     x = (2.0 >. 2.0) || (2.0 <. 2.0);
#     y = (2.0 >=. 2.0) && (2.0 <=. 2.0);
#     z = (2.0 =/= 2.0);
#     print(string_of_bool(x || z));
#     print(string_of_bool(y));
# EndBody."""
#         expect = "falsetrue"
#         self.assertTrue(TestCodeGen.test(input,expect,578))

#     def test_579(self):
#         """Testcase number 579:"""
#         input = \
# r"""Var: x = True, y = True, z = True;
# Function: main
# Body:
#     x = 0.01 =/= 8.91 -. 8.90;
#     print(string_of_float(8.91 -. 8.90));
#     print(string_of_bool(x));
# EndBody."""
#         expect = "0.010000229true"
#         self.assertTrue(TestCodeGen.test(input,expect,579))

#     def test_580(self):
#         """Testcase number 580:"""
#         input = \
# r"""Var: x = True, y = True, z = True;
# Function: main
# Body:
#     x = 0.125 =/= 8.425 -. 8.4;
#     print(string_of_float(8.425 -. 8.3));
#     print(string_of_bool(x));
# EndBody."""
#         expect = "0.125true"
#         self.assertTrue(TestCodeGen.test(input,expect,580))

#     def test_581(self):
#         """Testcase number 581:"""
#         input = \
# r"""Var: x = True, y = True, z = True;
# Function: main
# Body:
#     x = 0.125 =/= 8.125 -. 8.0;
#     print(string_of_float(8.125 -. 8.0));
#     print(string_of_bool(x));
# EndBody."""
#         expect = "0.125false"
#         self.assertTrue(TestCodeGen.test(input,expect,581))

#     def test_582(self):
#         """Testcase number 582:"""
#         input = \
# r"""Function: main
# Body:
#     Var: x = True, y = True, z = True;
#     x = 0.125 =/= 8.125 -. 8.0;
#     print(string_of_float(8.125 -. 8.0));
#     print(string_of_bool(x));
# EndBody."""
#         expect = "0.125false"
#         self.assertTrue(TestCodeGen.test(input,expect,582))

#     def test_583(self):
#         """Testcase number 583:"""
#         input = \
# r"""Function: main
# Body:
#     Var: x = 0.0;
#     x = 0.125 +. 8.125 -. 8.0;
#     print(string_of_float(x));
# EndBody."""
#         expect = "0.25"
#         self.assertTrue(TestCodeGen.test(input,expect,583))

#     def test_584(self):
#         """Testcase number 584:"""
#         input = \
# r"""Function: main
# Body:
#     Var: x = 0.0;
#     x = 0.0 *. 12.3;
#     print(string_of_float(x));
# EndBody."""
#         expect = "0.0"
#         self.assertTrue(TestCodeGen.test(input,expect,584))

#     def test_585(self):
#         """Testcase number 585:"""
#         input = \
# r"""Var: a = 9;
# Function: foo
# Body:
#     a = 1;
#     Return 0.0;
# EndBody.

# Function: foo1
# Body:
#     a = 2;
#     Return 1.0;
# EndBody.

# Function: foo2
# Body:
#     a = 3;
#     Return 0.0;
# EndBody.

# Function: foo3
# Body:
#     a = 4;
#     Return 1.0;
# EndBody.

# Function: main
# Body:
#     Var: t = 0.0;
#     t = foo() *. foo1() *. foo2() *. foo3();
#     print(string_of_float(t));
#     print(string_of_int(a));
# EndBody."""
#         expect = "0.04"
#         self.assertTrue(TestCodeGen.test(input,expect,585))

#     def test_586(self):
#         """Testcase number 586:"""
#         input = \
# r"""Var: a = 9;
# Function: foo
# Body:
#     a = 1;
#     Return 0;
# EndBody.

# Function: foo1
# Body:
#     a = 2;
#     Return 1;
# EndBody.

# Function: foo2
# Body:
#     a = 3;
#     Return 0;
# EndBody.

# Function: foo3
# Body:
#     a = 4;
#     Return 1;
# EndBody.

# Function: main
# Body:
#     Var: t = 0;
#     t = foo() * foo1() * foo2() * foo3();
#     print(string_of_int(t));
#     print(string_of_int(a));
# EndBody."""
#         expect = "04"
#         self.assertTrue(TestCodeGen.test(input,expect,586))

#     def test_587(self):
#         """Testcase number 587:"""
#         input = \
# r"""Var: a = 9;
# Function: foo
# Body:
#     a = 1;
#     Return 0;
# EndBody.

# Function: foo1
# Body:
#     a = 2;
#     Return 1;
# EndBody.

# Function: foo2
# Body:
#     a = 3;
#     Return 2;
# EndBody.

# Function: foo3
# Body:
#     a = 4;
#     Return 3;
# EndBody.

# Function: main
# Body:
#     Var: t = 0;
#     t = foo() \ foo1() \ foo2() \ foo3();
#     print(string_of_int(t));
#     print(string_of_int(a));
# EndBody."""
#         expect = "04"
#         self.assertTrue(TestCodeGen.test(input,expect,587))

#     def test_588(self):
#         """Testcase number 588:"""
#         input = \
# r"""Function: main
#     Body:
#         Var: h = 5, i = 0, j = 0, k = 0;
#         For (i = 0, i < h, 1) Do
#             If (i == 0) ||(i == h - 1) || (i == (h-1)\2) Then
#                 For (j = 0, j < 5, 1) Do
#                     print("*");
#                 EndFor.
#             Else
#                 For (j = 0, j < 5, 1) Do
#                     If (j == 0) || (j == h-1) || (j == (h-1)\2) Then
#                         print(" ");
#                     Else
#                         print("*");
#                     EndIf.
#                 EndFor.
#             EndIf.
#             printLn();
#         EndFor.
#     EndBody."""
#         expect = \
# r"""*****
#  * * 
# *****
#  * * 
# *****
# """
#         self.assertTrue(TestCodeGen.test(input,expect,588))

#     def test_589(self):
#         """Testcase number 589:"""
#         input = \
# r"""Function: main
#     Body:
#         Var: h = 5, i = 0, j = 0, k = 0;
#         For (i = 0, i < h, 1) Do
#             If (i == 0) ||(i == h - 1) || (i == (h-1)\2) Then
#                 For (j = 0, j < 5, 1) Do
#                     print("*");
#                 EndFor.
#             Else
#                 For (j = 0, j < 5, 1) Do
#                     If (j == 0) || (j == h-1) || (j == (h-1)\2) Then
#                         print("*");
#                     Else
#                         print(" ");
#                     EndIf.
#                 EndFor.
#             EndIf.
#             printLn();
#         EndFor.
#     EndBody."""
#         expect = \
# r"""*****
# * * *
# *****
# * * *
# *****
# """
#         self.assertTrue(TestCodeGen.test(input,expect,589))

#     def test_590(self):
#         """Testcase number 590:"""
#         input = \
# r"""Function: main
#     Body:
#         Var: h = 5, i = 0, j = 0, k = 0;
#         For (i = 0, i < h, 1) Do
#             If (i == 0) ||(i == h - 1) Then
#                 For (j = 0, j < 5, 1) Do
#                     print("*");
#                 EndFor.
#             Else
#                 For (j = 0, j < 5, 1) Do
#                     If (j == 0) || (j == h-1) Then
#                         print("*");
#                     Else
#                         print(" ");
#                     EndIf.
#                 EndFor.
#             EndIf.
#             printLn();
#         EndFor.
#     EndBody."""
#         expect = \
# r"""*****
# *   *
# *   *
# *   *
# *****
# """
#         self.assertTrue(TestCodeGen.test(input,expect,590))

#     def test_591(self):
#         """Testcase number 591:"""
#         input = \
# r"""Function: main
#     Body:
#         Var: h = 5, i = 0, j = 0, k = 0;
#         For (i = 0, i < h, 1) Do
#             For (j = 5 - i, j >= 0, -1) Do
#                 print(" ");
#             EndFor.
#             For (k = i, k >= 0, -1) Do
#                 print("* ");
#             EndFor.
#             printLn();
#         EndFor.
#     EndBody."""
#         expect = \
# r"""      * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
# """
#         self.assertTrue(TestCodeGen.test(input,expect,591))

#     def test_592(self):
#         """Testcase number 592:"""
#         input = \
# r"""Function: main
#     Body:
#         Var: h = 5, i = 0, j = 0, k = 0;
#         For (i = 0, i < h, 1) Do
#             For (j = 5 - i, j > 0, -1) Do
#                 print(" ");
#             EndFor.
#             For (k = i, k < h, 1) Do
#                 print("* ");
#             EndFor.
#             printLn();
#         EndFor.
#     EndBody."""
#         expect = \
# r"""     * * * * * 
#     * * * * 
#    * * * 
#   * * 
#  * 
# """
#         self.assertTrue(TestCodeGen.test(input,expect,592))

#     def test_593(self):
#         """Testcase number 593:"""
#         input = \
# r"""Function: ctof
#     Parameter: c
#     Body:
#         Return (c *. 1.8) +. 32.0;
#     EndBody.

# Function: main
#     Body:
#         Var: c = 37.0, f = 0.0;
#         print("Input Celsius: ");
#         printStrLn(string_of_float(c));

#         f = ctof(c);

#         print("Fahrenheit return: ");
#         print(string_of_float(f));

#     EndBody."""
#         expect = "Input Celsius: 37.0\nFahrenheit return: 98.6"
#         self.assertTrue(TestCodeGen.test(input,expect,593))

#     def test_594(self):
#         """Testcase number 594:"""
#         input = \
# r"""Function: bubble
#     Parameter: arr[5], length
#     Body:
#         Var: i=0, j=0, buffer=0;
#         For (i = 0, i < length - 1, 1) Do
#             For (j = i + 1, j < length, 1) Do
#                 If arr[i] > arr[j] Then
#                     buffer = arr[i];
#                     arr[i] = arr[j];
#                     arr[j] = buffer;
#                 EndIf.
#             EndFor.
#         EndFor.

#         Return arr;
#     EndBody.

# Function: main
#     Body:
#         Var: arr[5] = {5,4,3,2,1}, length=5, i=0;

#         arr = bubble(arr, length);

#         print("Sorted array: ");
#         For (i = 0, i < length, 1) Do
#             print(string_of_int(arr[i]));
#             print(" ");
#         EndFor.
#     EndBody."""
#         expect = "Sorted array: 1 2 3 4 5 "
#         self.assertTrue(TestCodeGen.test(input,expect,594))

#     def test_595(self):
#         """Testcase number 595:"""
#         input = \
# """Function: reduce
# Parameter: n
# Body:
#     If n == 0 Then
#         Return n;
#     Else
#         Return n + reduce(n-1);
#     EndIf.

# EndBody.

# Function: main
# Body:
#     print(string_of_int(reduce(10)));
# EndBody."""
#         expect = "55"
#         self.assertTrue(TestCodeGen.test(input,expect,595))

    def test_596(self):
        """Testcase number 596:"""
        input = \
"""Var: i = 0;

Function: fib
Parameter: n
Body:
    If n <= 1 Then
        Return n;
    EndIf.
    Return fib(n-1) + fib(n-2);
EndBody.

Function: main
Body:
    For (i = 0, i < 7, 1) Do
        print(string_of_int(fib(i)));
    EndFor.
EndBody."""
        expect = "0112358"
        self.assertTrue(TestCodeGen.test(input,expect,596))

#     def test_597(self):
#         """Testcase number 597:"""
#         input = \
# """Function: sort
# Parameter: n[6]
# Body:
#     Var: x = 0;
#     While x < 6 Do
#         Var: y = 0;
#         For (y = x + 1, y < 6, 1) Do
#             If n[x] > n[y] Then
#                 Var: buffer = 0;
#                 buffer = n[x];
#                 n[x] = n[y];
#                 n[y] = buffer;
#             EndIf.
#         EndFor.
#         x = x + 1;
#     EndWhile.
#     Return n;
# EndBody.

# Function: printf
# Parameter: n[6]
# Body:
#     Var: i = 0;
#     While i < 6 Do
#         print(string_of_int(n[i]));
#         i = i + 1;
#     EndWhile.
# EndBody.

# Function: main
# Body:
#     Var: x[6] = {9,5,3,6,7,8}, y[6] = {0,0,0,0,0,0};
#     y = sort(x);
#     printf(x);
#     printLn();
#     printf(y);
# EndBody."""
#         expect = "356789\n356789"
#         self.assertTrue(TestCodeGen.test(input,expect,597))

#     def test_598(self):
#         """Testcase number 598:"""
#         input = \
# r"""Function: foo
# Parameter: x
# Body:
#     If x == 1 Then
#         print(string_of_int(1));
#     Else
#         print(string_of_int(x));
#         foo(x-1);
#     EndIf.
# EndBody.

# Function: main
# Body:
#     foo(9);
# EndBody."""
#         expect = "987654321"
#         self.assertTrue(TestCodeGen.test(input,expect,598))

#     def test_599(self):
#         """Testcase number 599:"""
#         input = \
# r"""Function: isPrime
# Parameter: n
# Body:
#     Var: i = 0, iss = True;
#     For (i = 2, i < n, 1) Do
#         If n % i == 0 Then
#             iss = False;
#             Break;
#         EndIf.
#     EndFor.

#     Return iss;
# EndBody.

# Function: main
# Body:
#     print(string_of_bool(isPrime(97)));
# EndBody."""
#         expect = "true"
#         self.assertTrue(TestCodeGen.test(input,expect,599))