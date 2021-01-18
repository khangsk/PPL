import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = str(Program([VarDecl(Id("x"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_simple_program2(self):
        input = """Function: abc
                    Body:
                    EndBody."""
        expect = str(Program([FuncDecl(Id("abc"), [], ([], []))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_simple_program3(self):
        input = """Var: x,y,z;
                Var: m,n,o;
                Function: a1
                Body:
                EndBody.
                Function: a2
                Body:
                EndBody."""
        expect = str(Program([
            VarDecl(Id("x"),[], None),
            VarDecl(Id("y"),[], None),
            VarDecl(Id("z"),[], None),
            VarDecl(Id("m"),[], None),
            VarDecl(Id("n"),[], None),
            VarDecl(Id("o"),[], None),
            FuncDecl(Id("a1"), [], ([], [])),
            FuncDecl(Id("a2"), [], ([], []))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_global_variable_declaration(self):
        input = """Var: x = 4;
                Var: x = 4, y, t=900;"""
        expect = str(Program([
            VarDecl(Id("x"),[], IntLiteral(4)),
            VarDecl(Id("x"),[], IntLiteral(4)),
            VarDecl(Id("y"),[], None),
            VarDecl(Id("t"),[], IntLiteral(900)),
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_composite_variable_declaration(self):
        input = """Var: x[3] = {1,2,3};"""
        expect = str(Program([
            VarDecl(Id("x"), [3], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_composite_variable_declaration2(self):
        input = """Var: x[3][5] = 4;
                Var: x[3][5][6][1] = True;"""
        expect = str(Program([
            VarDecl(Id("x"), [3,5], IntLiteral(4)),
            VarDecl(Id("x"), [3,5,6,1], BooleanLiteral(True))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_composite_variable_declaration3(self):
        input = """Var: x[3][5][6][1] [6]   [9] [10     ] [    11];"""
        expect = str(Program([
            VarDecl(Id("x"), [3,5,6,1,6,9,10,11], None)
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_composite_variable_declaration4(self):
        input = """Var: x[3][5][6][1] = 5;
                    Var: y[4][5] = 3, t = 7, z, w, q[3];
                    Var: q,w,e,r;"""
        expect = str(Program([
            VarDecl(Id("x"), [3,5,6,1], IntLiteral(5)),
            VarDecl(Id("y"), [4,5], IntLiteral(3)),
            VarDecl(Id("t"), [], IntLiteral(7)),
            VarDecl(Id("z"), [], None),
            VarDecl(Id("w"), [], None),
            VarDecl(Id("q"), [3], None),
            VarDecl(Id("q"), [], None),
            VarDecl(Id("w"), [], None),
            VarDecl(Id("e"), [], None),
            VarDecl(Id("r"), [], None)
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_function_declaration1(self):
        input = """Function: ert
                    Parameter: i, x, a[4]
                    Body:
                        x = ert(i);
                    EndBody."""
        expect = str(Program([
            FuncDecl(Id("ert"),
            [VarDecl(Id("i"), [], None),
            VarDecl(Id("x"), [], None),
            VarDecl(Id("a"), [4], None)],
            ([],

            [Assign(Id("x"), CallExpr(Id("ert"), [Id("i")]))])
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_array_literal1(self):
        input = """Var: x = {{1,2}, {3,4}};"""
        expect = str(Program([
            VarDecl(Id("x"), [], ArrayLiteral([
                ArrayLiteral([IntLiteral(1), IntLiteral(2)]),
                ArrayLiteral([IntLiteral(3), IntLiteral(4)])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_array_literal2(self):
        input = """Var: x = {1, 1.5, True, {1,2,3,4}, "abcdef"};"""
        expect = str(Program([
            VarDecl(Id("x"), [], ArrayLiteral([
                IntLiteral(1),
                FloatLiteral(1.5),
                BooleanLiteral(True),
                ArrayLiteral([
                    IntLiteral(1),
                    IntLiteral(2),
                    IntLiteral(3),
                    IntLiteral(4)]),
                StringLiteral("abcdef")
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    
    def test_array_literal3(self):
        input = """Var: x = {{1, 5.5}, {1, 9 ,{4}}};"""
        expect = str(Program([
            VarDecl(Id("x"), [], ArrayLiteral([
                ArrayLiteral([IntLiteral(1), FloatLiteral(5.5)]),
                ArrayLiteral([IntLiteral(1), IntLiteral(9), ArrayLiteral([IntLiteral(4)])])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_array_literal4(self):
        input = """Var: x = {{1,2}, {3,4},
                    {4,5},
                    {7,6}
                    , **sldkjf**
                    {1,9}};"""
        expect = str(Program([
            VarDecl(Id("x"), [], ArrayLiteral([
                ArrayLiteral([IntLiteral(1), IntLiteral(2)]),
                ArrayLiteral([IntLiteral(3), IntLiteral(4)]),
                ArrayLiteral([IntLiteral(4), IntLiteral(5)]),
                ArrayLiteral([IntLiteral(7), IntLiteral(6)]),
                ArrayLiteral([IntLiteral(1), IntLiteral(9)])
            ]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_empty_array_literal(self):
        input = """Var: x = {};"""
        expect = str(Program([VarDecl(Id("x"), [],
            ArrayLiteral([])
        )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    
    def test_empty_array_literal2(self):
        input = """Var: x = {{}, {}, {{}, {}}};"""
        expect = str(Program([VarDecl(Id("x"), [],
            ArrayLiteral([
                ArrayLiteral([]),
                ArrayLiteral([]),
                ArrayLiteral([
                    ArrayLiteral([]),
                    ArrayLiteral([])
                ])
            ])
        )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    
    def test_local_variable_declaration1(self):
        input = """Function: abc
                Parameter: x, y, z
                Body:
                    Var: x = 4, y, z = 8;
                    x = 1;
                    y = 7;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"), [], None)],
            ([VarDecl(Id("x"), [], IntLiteral(4)),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"), [], IntLiteral(8))], 
            [Assign(Id("x"), IntLiteral(1)),
            Assign(Id("y"), IntLiteral(7))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_normal_parameter_declaration(self):
        input = """Function: abc
                Parameter: x, y[1][2], z[5]
                Body:
                    Var: x = 4, y, z = 8;
                    z = 6;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [1,2], None),
            VarDecl(Id("z"), [5], None)],
            ([VarDecl(Id("x"), [], IntLiteral(4)),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"), [], IntLiteral(8))], 
            [Assign(Id("z"), IntLiteral(6))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_add_operator(self):
        input = """Function: abc
                Body:
                    x = 5 + 6;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([], 
            [Assign(Id("x"),BinaryOp("+", IntLiteral(5), IntLiteral(6)))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_association(self):
        input = """Function: abc
                Body:
                    x = 5 + 6 + 7;
                    y = 5 +. 4 +. 1;
                    z = True && False || True;
                    w = 4 - 3 - 3;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([], 
            [Assign(Id("x"),BinaryOp("+", BinaryOp("+", IntLiteral(5), IntLiteral(6)), IntLiteral(7))),
            Assign(Id("y"),BinaryOp("+.", BinaryOp("+.", IntLiteral(5), IntLiteral(4)), IntLiteral(1))),
            Assign(Id("z"),BinaryOp("||", BinaryOp("&&", BooleanLiteral(True), BooleanLiteral(False)), BooleanLiteral(True))),
            Assign(Id("w"),BinaryOp("-", BinaryOp("-", IntLiteral(4), IntLiteral(3)), IntLiteral(3)))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_association2(self):
        input = """Function: abc
                Body:
                    x = 1 - 2 + 4 * 5 \\ 6;
                    y = 1.1 +. 3 -. 1.2 *. 8.0 \\. 9.23;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([], 
            [Assign(Id("x"),BinaryOp("+",BinaryOp("-",IntLiteral(1),IntLiteral(2)),BinaryOp("\\",BinaryOp("*",IntLiteral(4),IntLiteral(5)),IntLiteral(6)))),
            Assign(Id("y"),BinaryOp("-.",BinaryOp("+.",FloatLiteral(1.1),IntLiteral(3)),BinaryOp("\\.",BinaryOp("*.",FloatLiteral(1.2),FloatLiteral(8.0)),FloatLiteral(9.23))))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    
    def test_non_association_operator(self):
        input = """Function: abc
                Body:
                    x = 1 != 2;
                    y = 1 == (2 < 3);
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"), BinaryOp("!=", IntLiteral(1), IntLiteral(2))),
            Assign(Id("y"), BinaryOp("==", IntLiteral(1), BinaryOp("<", IntLiteral(2), IntLiteral(3))))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    
    def test_index_operator(self):
        input = """Function: abc
                Body:
                    x = abcdef[5][7][9];
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"), ArrayCell(Id("abcdef"), [IntLiteral(5),IntLiteral(7),IntLiteral(9)]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_index_operator2(self):
        input = """Function: abc
                Body:
                    x[3 + 4 + (5 * 8)] = 5 + 7;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(ArrayCell(Id("x"),[BinaryOp("+",BinaryOp("+",IntLiteral(3),IntLiteral(4)),BinaryOp("*",IntLiteral(5),IntLiteral(8)))]),BinaryOp("+",IntLiteral(5),IntLiteral(7)))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_index_operator3(self):
        input = """Function: abc
                Body:
                    x = {1,2,3,4} [5][7][9];
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),ArrayCell(ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4)]),[IntLiteral(5),IntLiteral(7),IntLiteral(9)]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    
    def test_index_operator4(self):
        input = """Function: abc
                Body:
                    x = 2 + 8 + 4[5][7][9];
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),BinaryOp("+",BinaryOp("+",IntLiteral(2),IntLiteral(8)),ArrayCell(IntLiteral(4),[IntLiteral(5),IntLiteral(7),IntLiteral(9)])))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    
    def test_index_operator5(self):
        input = """Function: abc
                Body:
                    x = ((1 \\ 2 +. 4 - 4)[5][7])[9];
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),ArrayCell(ArrayCell(BinaryOp("-",BinaryOp("+.",BinaryOp("\\",IntLiteral(1),IntLiteral(2)),IntLiteral(4)),IntLiteral(4)),[IntLiteral(5),IntLiteral(7)]),[IntLiteral(9)]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_index_operator6(self):
        input = """Function: abc
                Body:
                    x[3 + 4 + (5 * 8)] = 5 + 7;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(ArrayCell(Id("x"),[BinaryOp("+",BinaryOp("+",IntLiteral(3),IntLiteral(4)),BinaryOp("*",IntLiteral(5),IntLiteral(8)))]),BinaryOp("+",IntLiteral(5),IntLiteral(7)))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_index_operator7(self):
        input = """Function: abc
                Body:
                    x[3 + 2 + foo() + y[1 + 4 + 6]] = y[2 + 3];
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(ArrayCell(Id("x"),[BinaryOp("+",BinaryOp("+",BinaryOp("+",IntLiteral(3),IntLiteral(2)),CallExpr(Id("foo"),[])),ArrayCell(Id("y"),[BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(4)),IntLiteral(6))]))]),ArrayCell(Id("y"),[BinaryOp("+",IntLiteral(2),IntLiteral(3))]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_unary_operator1(self):
        input = """Function: abc
                Body:
                    x = -5 + -7;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),BinaryOp("+",UnaryOp("-",IntLiteral(5)),UnaryOp("-",IntLiteral(7))))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_unary_operator2(self):
        input = """Function: abc
                Body:
                    x = -5 + -7 -!!!-----.- -8 - -9 - ---!-.--.-10;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),BinaryOp("-",BinaryOp("-",BinaryOp("-",BinaryOp("+",UnaryOp("-",IntLiteral(5)),UnaryOp("-",IntLiteral(7))),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-.",UnaryOp("-",UnaryOp("-",IntLiteral(8)))))))))))),UnaryOp("-",IntLiteral(9))),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",UnaryOp("-.",UnaryOp("-",UnaryOp("-.",UnaryOp("-",IntLiteral(10)))))))))))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_unary_operator3(self):
        input = """Function: abc
                Body:
                    x = -5 + -7 - -.7 + -.2 **skdljf** + -(-5 + 4) + -4[5] + (-4)[5];
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("-",BinaryOp("+",UnaryOp("-",IntLiteral(5)),UnaryOp("-",IntLiteral(7))),UnaryOp("-.",IntLiteral(7))),UnaryOp("-.",IntLiteral(2))),UnaryOp("-",BinaryOp("+",UnaryOp("-",IntLiteral(5)),IntLiteral(4)))),UnaryOp("-",ArrayCell(IntLiteral(4),[IntLiteral(5)]))),ArrayCell(UnaryOp("-",IntLiteral(4)),[IntLiteral(5)])))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_unary_operator4(self):
        input = """Function: abc
                Body:
                    x = True && !False || !!a && !!!bsdklf;
                    y = 5.5 -. -.3.3456 -. -.1.2345 +. -.12.e3 +. -.12.;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),BinaryOp("&&",BinaryOp("||",BinaryOp("&&",BooleanLiteral(True),UnaryOp("!",BooleanLiteral(False))),UnaryOp("!",UnaryOp("!",Id("a")))),UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("bsdklf")))))),
            Assign(Id("y"),BinaryOp("+.",BinaryOp("+.",BinaryOp("-.",BinaryOp("-.",FloatLiteral(5.5),UnaryOp("-.",FloatLiteral(3.3456))),UnaryOp("-.",FloatLiteral(1.2345))),UnaryOp("-.",FloatLiteral(12000.0))),UnaryOp("-.",FloatLiteral(12.0))))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    
    def test_unary_operator5(self):
        input = """Function: abc
                Body:
                    x = -5 == -(s[4]) + -8;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),BinaryOp("==",UnaryOp("-",IntLiteral(5)),BinaryOp("+",UnaryOp("-",ArrayCell(Id("s"),[IntLiteral(4)])),UnaryOp("-",IntLiteral(8)))))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_function_call(self):
        input = """Function: abc
                Body:
                    x = foo() + goo() - too();
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),BinaryOp("-",BinaryOp("+",CallExpr(Id("foo"),[]),CallExpr(Id("goo"),[])),CallExpr(Id("too"),[])))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_nested_function_call(self):
        input = """Function: abc
                Body:
                    x = hoo(foo() + goo(too()) - too(goo() + foo() + qoo()));
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),CallExpr(Id("hoo"),[BinaryOp("-",BinaryOp("+",CallExpr(Id("foo"),[]),CallExpr(Id("goo"),[CallExpr(Id("too"),[])])),CallExpr(Id("too"),[BinaryOp("+",BinaryOp("+",CallExpr(Id("goo"),[]),CallExpr(Id("foo"),[])),CallExpr(Id("qoo"),[]))]))]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_nested_function_call2(self):
        input = """Function: abc
                Body:
                    x = hoo(goo[1 + foo()], boo(1 * 4 == hoo({1,2,3}, {1}))) +. 5 -. 1;
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),BinaryOp("-.",BinaryOp("+.",CallExpr(Id("hoo"),[ArrayCell(Id("goo"),[BinaryOp("+",IntLiteral(1),CallExpr(Id("foo"),[]))]),CallExpr(Id("boo"),[BinaryOp("==",BinaryOp("*",IntLiteral(1),IntLiteral(4)),CallExpr(Id("hoo"),[ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(1)])]))])]),IntLiteral(5)),IntLiteral(1)))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_nested_function_call3(self):
        input = """Function: abc
                Body:
                    x = foo(1, {1, 2}) [1 + foo(4, 5 * too())] + yoo("abcdef foo()");
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [],
            ([],
            [Assign(Id("x"),BinaryOp("+",ArrayCell(CallExpr(Id("foo"),[IntLiteral(1),ArrayLiteral([IntLiteral(1),IntLiteral(2)])]),[BinaryOp("+",IntLiteral(1),CallExpr(Id("foo"),[IntLiteral(4),BinaryOp("*",IntLiteral(5),CallExpr(Id("too"),[]))]))]),CallExpr(Id("yoo"),[StringLiteral("abcdef foo()")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_if_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    If 1 + 3 == 5 Then
                        x = 6;
                        t = 7;
                    ElseIf 1 + 3 == 7 Then
                        y = 9;
                        z = 10;
                    Else z = 11;
                    EndIf.
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"),[4,5], None)],
            ([],
            [If([
                (BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(3)),IntLiteral(5)),
                [],
                [Assign(Id("x"),IntLiteral(6)),Assign(Id("t"),IntLiteral(7))]),
                (BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(3)),IntLiteral(7)),
                [],
                [Assign(Id("y"),IntLiteral(9)),Assign(Id("z"),IntLiteral(10))])],
                ([],
                [Assign(Id("z"),IntLiteral(11))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_if_statement2(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    If 1 + 3 == 5 Then
                        x = 6;
                        t = 7;
                    ElseIf 1 + 3 == 7 Then
                        y = 9;
                        z = 10;
                    ElseIf foo() > goo() Then
                        y = 9;
                        z = 10;
                    ElseIf 1 + 3 == 7 Then
                        y = 9;
                        z = 10;
                    Else z = 11;
                    EndIf.
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"),[4,5], None)],
            ([],
            [If([
                (BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(3)),IntLiteral(5)),
                [],
                [Assign(Id("x"),IntLiteral(6)),Assign(Id("t"),IntLiteral(7))]),
                (BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(3)),IntLiteral(7)),
                [],
                [Assign(Id("y"),IntLiteral(9)),Assign(Id("z"),IntLiteral(10))]),
                (BinaryOp(">",CallExpr(Id("foo"),[]),CallExpr(Id("goo"),[])),
                [],
                [Assign(Id("y"),IntLiteral(9)),Assign(Id("z"),IntLiteral(10))]),
                (BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(3)),IntLiteral(7)),
                []
                ,[Assign(Id("y"),IntLiteral(9)),Assign(Id("z"),IntLiteral(10))])],
                ([],[Assign(Id("z"),IntLiteral(11))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_nested_if_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    If 1 + 3 == 5 Then
                        x = 6;
                        t = 7;
                    ElseIf 1 + 3 == 7 Then
                        If 2 + 5 == 6 Then
                        EndIf.
                    ElseIf foo() > goo() Then
                        y = 9;
                        z = 10;
                    Else z = 11;
                    EndIf.
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"),[4,5], None)],
            ([],
            [If([
                (BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(3)),IntLiteral(5)),
                [],
                [Assign(Id("x"),IntLiteral(6)),Assign(Id("t"),IntLiteral(7))]),
                (BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(3)),IntLiteral(7)),
                [],
                [If([(BinaryOp("==",BinaryOp("+",IntLiteral(2),IntLiteral(5)),IntLiteral(6)),[],[])],([],[]))]),
                (BinaryOp(">",CallExpr(Id("foo"),[]),CallExpr(Id("goo"),[])),
                [],
                [Assign(Id("y"),IntLiteral(9)),Assign(Id("z"),IntLiteral(10))])],
                ([],[Assign(Id("z"),IntLiteral(11))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_nested_if_statement2(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    If a Then
                        If b Then
                        EndIf.
                        If c Then
                            If d Then
                            a = b;
                            EndIf.
                        EndIf.
                    EndIf.
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"),[4,5], None)],
            ([],
            [If([(Id("a"),[],[If([(Id("b"),[],[])],([],[])),If([(Id("c"),[],[If([(Id("d"),[],[Assign(Id("a"),Id("b"))])],([],[]))])],([],[]))])],([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
        
    def test_for_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    For (a = 4, a == 10, 1 + 2) Do
                        i = i + 1;
                    EndFor.
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"),[4,5], None)],
            ([],
            [For(Id("a"),
            IntLiteral(4),
            BinaryOp("==",Id("a"),IntLiteral(10)),
            BinaryOp("+",IntLiteral(1),IntLiteral(2)),
            ([],[Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    
    def test_if_statement_in_for_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    For (a = 4, a == 10, 1 + 2) Do
                        If a == 4 Then a = 5;
                        EndIf.
                    EndFor.
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"),[4,5], None)],
            ([],
            [For(Id("a"),
            IntLiteral(4),
            BinaryOp("==",Id("a"),IntLiteral(10)),
            BinaryOp("+",IntLiteral(1),IntLiteral(2)),
            ([],
            [If([(BinaryOp("==",Id("a"),IntLiteral(4)),[],[Assign(Id("a"),IntLiteral(5))])],([],[]))]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_while_statement(self):
        input = """Function: abc
            Parameter: x, y, z[4][5]
            Body:
                While a != 1 Do
                    a = a + 1;
                    a = a + 2;
                EndWhile.
            EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"),[4,5], None)],
            ([],
            [While(BinaryOp("!=",Id("a"),IntLiteral(1)),
            ([],
            [Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),
            Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2)))]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_empty_while_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    While a != 1 Do
                    EndWhile.
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"),[4,5], None)],
            ([],
            [While(BinaryOp("!=",Id("a"),IntLiteral(1)),([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_do_while_statement(self):
        input = """Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    Do
                        a = 1;
                        b = 2;
                        Break;
                        Continue;
                    While 2000 EndDo.
                EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"),[4,5], None)],
            ([],
            [Dowhile(([],[Assign(Id("a"),IntLiteral(1)),
            Assign(Id("b"),IntLiteral(2)),
            Break(),
            Continue()]),IntLiteral(2000))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_nested_variable_declaration(self):
        input = """Var : x, y, z = 5, t = {1,2,{3,4,5,{1,2,3}}};
                Var : y = 10., t = 6.e200;
                Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    Var: x, y;
                    v = 2 + 3 + 4 \\. 5 +. 6.7e-1;
                    If (x + y + z) Then
                        Var: a, b, c;
                        Var: a[4], b[6], r[1];
                        a = 5.6;
                        b = 2[2][3];
                    ElseIf 2 + 3 Then
                        Var: r, t, r[5];
                        Var: q1, w2, e1;
                        q = 5 * 5 + 5;
                    Else a = 3;
                    EndIf.
                EndBody."""
        expect = str(Program([
            VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"), [],IntLiteral(5)),
            VarDecl(Id("t"), [],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(3),IntLiteral(4),IntLiteral(5),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])])])),
            VarDecl(Id("y"), [],FloatLiteral(10.0)),
            VarDecl(Id("t"), [],FloatLiteral(6e+200)),
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"),[4,5], None)],
            ([VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None)],
            [Assign(Id("v"),BinaryOp("+.",BinaryOp("+",BinaryOp("+",IntLiteral(2),IntLiteral(3)),BinaryOp("\\.",IntLiteral(4),IntLiteral(5))),FloatLiteral(0.67))),
            If([(BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("z")),[VarDecl(Id("a"), [], None),VarDecl(Id("b"), [], None),VarDecl(Id("c"), [], None),VarDecl(Id("a"),[4], None),VarDecl(Id("b"),[6], None),VarDecl(Id("r"),[1], None)],[Assign(Id("a"),FloatLiteral(5.6)),Assign(Id("b"),ArrayCell(IntLiteral(2),[IntLiteral(2),IntLiteral(3)]))]),(BinaryOp("+",IntLiteral(2),IntLiteral(3)),[VarDecl(Id("r"), [], None),VarDecl(Id("t"), [], None),VarDecl(Id("r"),[5], None),VarDecl(Id("q1"), [], None),VarDecl(Id("w2"), [], None),VarDecl(Id("e1"), [], None)],[Assign(Id("q"),BinaryOp("+",BinaryOp("*",IntLiteral(5),IntLiteral(5)),IntLiteral(5)))])],([],[Assign(Id("a"),IntLiteral(3))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_nested_variable_declaration2(self):
        input = """Var : x, y, z = 5, t = {1,2,{3,4,5,{1,2,3}}};
                Var : y = 10., t = 6.e200;
                Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    Var: x, y;
                    v = 2 + 3 + 4 \\. 5 +. 6.7e-1;
                    If (x + y + z) Then
                        Var: a, b, c;
                        Var: a[4], b[6], r[1];
                        a = 5.6;
                        For (e = 1, 4, 6) Do
                            Var: d, e, f = 6789;
                            Var: e[4];
                            printf(i);
                            While
                                a + 4
                            Do
                                Var: x = 5, y, qqqq = 6;
                                Break;
                                Continue;
                                print(a);
                                Do
                                    Var: x, xx, xxx, xxxx;
                                    Break;
                                    Continue;
                                    print(abcdef);
                                While 2000
                                EndDo.
                            EndWhile.
                        EndFor.
                        b = 2[2][3];
                    ElseIf 2 + 3 Then
                        Var: r, t, r[5];
                        Var: q1, w2, e1;
                        q = 5 * 5 + 5;
                        writeln(fff);
                    Else a = 3;
                    EndIf.
                EndBody."""
        expect = str(Program([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"), [],IntLiteral(5)),VarDecl(Id("t"), [],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(3),IntLiteral(4),IntLiteral(5),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])])])),VarDecl(Id("y"), [],FloatLiteral(10.0)),VarDecl(Id("t"), [],FloatLiteral(6e+200)),FuncDecl(Id("abc"),[VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"),[4,5], None)],([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None)],[Assign(Id("v"),BinaryOp("+.",BinaryOp("+",BinaryOp("+",IntLiteral(2),IntLiteral(3)),BinaryOp("\\.",IntLiteral(4),IntLiteral(5))),FloatLiteral(0.67))),If([(BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("z")),[VarDecl(Id("a"), [], None),VarDecl(Id("b"), [], None),VarDecl(Id("c"), [], None),VarDecl(Id("a"),[4], None),VarDecl(Id("b"),[6], None),VarDecl(Id("r"),[1], None)],[Assign(Id("a"),FloatLiteral(5.6)),For(Id("e"),IntLiteral(1),IntLiteral(4),IntLiteral(6),([VarDecl(Id("d"), [], None),VarDecl(Id("e"), [], None),VarDecl(Id("f"), [],IntLiteral(6789)),VarDecl(Id("e"),[4], None)],[CallStmt(Id("printf"),[Id("i")]),While(BinaryOp("+",Id("a"),IntLiteral(4)),([VarDecl(Id("x"), [],IntLiteral(5)),VarDecl(Id("y"), [], None),VarDecl(Id("qqqq"), [],IntLiteral(6))],[Break(),Continue(),CallStmt(Id("print"),[Id("a")]),Dowhile(([VarDecl(Id("x"), [], None),VarDecl(Id("xx"), [], None),VarDecl(Id("xxx"), [], None),VarDecl(Id("xxxx"), [], None)],[Break(),Continue(),CallStmt(Id("print"),[Id("abcdef")])]),IntLiteral(2000))]))])),Assign(Id("b"),ArrayCell(IntLiteral(2),[IntLiteral(2),IntLiteral(3)]))]),(BinaryOp("+",IntLiteral(2),IntLiteral(3)),[VarDecl(Id("r"), [], None),VarDecl(Id("t"), [], None),VarDecl(Id("r"),[5], None),VarDecl(Id("q1"), [], None),VarDecl(Id("w2"), [], None),VarDecl(Id("e1"), [], None)],[Assign(Id("q"),BinaryOp("+",BinaryOp("*",IntLiteral(5),IntLiteral(5)),IntLiteral(5))),CallStmt(Id("writeln"),[Id("fff")])])],([],[Assign(Id("a"),IntLiteral(3))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_return_statement(self):
        input="""Var: x, y, z;
            Function: abc
            Parameter: a, x, z[5]
            Body:
                Return ;
                Return 3;
            EndBody."""
        expect = str(Program([
            VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"), [], None),
            FuncDecl(Id("abc"),
            [VarDecl(Id("a"), [], None),
            VarDecl(Id("x"), [], None),
            VarDecl(Id("z"),[5], None)],
            ([],[Return(None),Return(IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_no_white_space(self):
        input = """Function:abc Parameter:x,y,z[4][5]Body:If1+3==5Thenx=6;t=7;ElseIf1+3==7ThenIf2+5==6Then
                    EndIf.ElseIffoo()>goo()Theny=9;z=10;Elsez=11;EndIf.EndBody."""
        expect = str(Program([
            FuncDecl(Id("abc"),
            [VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], None),
            VarDecl(Id("z"),[4,5], None)],
            ([],
            [If([(BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(3)),IntLiteral(5)),
            [],
            [Assign(Id("x"),IntLiteral(6)),Assign(Id("t"),IntLiteral(7))]),
            (BinaryOp("==",BinaryOp("+",IntLiteral(1),IntLiteral(3)),IntLiteral(7)),
            [],
            [If([(BinaryOp("==",BinaryOp("+",IntLiteral(2),IntLiteral(5)),IntLiteral(6)),[],[])],([],[]))]),
            (BinaryOp(">",CallExpr(Id("foo"),[]),CallExpr(Id("goo"),[])),
            [],
            [Assign(Id("y"),IntLiteral(9)),Assign(Id("z"),IntLiteral(10))])],
            ([],[Assign(Id("z"),IntLiteral(11))]))]))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_random(self):
        input = """Function: main
                Body:
                    a = !--.1;
                    a = 3----------------1;
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),UnaryOp("!",UnaryOp("-",UnaryOp("-.",IntLiteral(1))))),Assign(Id("a"),BinaryOp("-",IntLiteral(3),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(1))))))))))))))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_random2(self):
        input = """Var : x, y, z = 5, t = {1,2,{3,4,5,{1,2,3}}};
                Var : y = 10., t = 6.e200, q[1][2] = {2,3,4,5};
                Function: abc
                Parameter: x, y, z[4][5]
                Body:
                    Var: x, y;
                    Continue;
                    Break;Break;Continue;Return;Return 44444;
                    If 4 Then If 5 Then If 6 Then EndIf.EndIf.EndIf.
                EndBody."""
        expect = str(Program([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"), [],IntLiteral(5)),VarDecl(Id("t"), [],ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(3),IntLiteral(4),IntLiteral(5),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])])])),VarDecl(Id("y"), [],FloatLiteral(10.0)),VarDecl(Id("t"), [],FloatLiteral(6e+200)),VarDecl(Id("q"),[1,2],ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),FuncDecl(Id("abc"),[VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"),[4,5], None)],([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None)],[Continue(),Break(),Break(),Continue(),Return(None),Return(IntLiteral(44444)),If([(IntLiteral(4),[],[If([(IntLiteral(5),[],[If([(IntLiteral(6),[],[])],([],[]))])],([],[]))])],([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_nested_statements(self):
        input = """Function: abc
                Body:
                If 4 Then While 4 Do EndWhile.
                For (q = 1, 2, 3) Do Do While 5 EndDo.
                EndFor.
                ElseIf 5 Then 
                    If 1 Then
                    ElseIf 2 Then While 1 Do EndWhile.
                        For (q = 1, 2, 3) Do  Do While 1 Do EndWhile. While 5 EndDo.
                            EndFor.
                        If 3 Then
                        Else
                            For (q = 1, 2, 3) Do
                            Do While 5 EndDo.
                            While 4 Do  Do While 1 Do EndWhile. While 5 EndDo. EndWhile.
                            EndFor.
                        EndIf.
                    ElseIf -4 Then
                    EndIf.
                    While 4 Do  Do While 5 EndDo. EndWhile.
                ElseIf 6 Then
                While 4 Do  Do While 5 EndDo. EndWhile.
                For (q = 1, 2, 3) Do
                EndFor.
                ElseIf 7 Then While 1 Do EndWhile.
                While 4 Do Do While 5 EndDo. EndWhile.
                For (q = 1, 2, 3) Do
                EndFor.
                ElseIf 8 Then While 4 Do While 1 Do EndWhile. Do While 5 EndDo. EndWhile.
                EndIf.
                EndBody."""
        expect = str(Program([FuncDecl(Id("abc"),[],([],[If([(IntLiteral(4),[],[While(IntLiteral(4),([],[])),For(Id("q"),IntLiteral(1),IntLiteral(2),IntLiteral(3),([],[Dowhile(([],[]),IntLiteral(5))]))]),(IntLiteral(5),[],[If([(IntLiteral(1),[],[]),(IntLiteral(2),[],[While(IntLiteral(1),([],[])),For(Id("q"),IntLiteral(1),IntLiteral(2),IntLiteral(3),([],[Dowhile(([],[While(IntLiteral(1),([],[]))]),IntLiteral(5))])),If([(IntLiteral(3),[],[])],([],[For(Id("q"),IntLiteral(1),IntLiteral(2),IntLiteral(3),([],[Dowhile(([],[]),IntLiteral(5)),While(IntLiteral(4),([],[Dowhile(([],[While(IntLiteral(1),([],[]))]),IntLiteral(5))]))]))]))]),(UnaryOp("-",IntLiteral(4)),[],[])],([],[])),While(IntLiteral(4),([],[Dowhile(([],[]),IntLiteral(5))]))]),(IntLiteral(6),[],[While(IntLiteral(4),([],[Dowhile(([],[]),IntLiteral(5))])),For(Id("q"),IntLiteral(1),IntLiteral(2),IntLiteral(3),([],[]))]),(IntLiteral(7),[],[While(IntLiteral(1),([],[])),While(IntLiteral(4),([],[Dowhile(([],[]),IntLiteral(5))])),For(Id("q"),IntLiteral(1),IntLiteral(2),IntLiteral(3),([],[]))]),(IntLiteral(8),[],[While(IntLiteral(4),([],[While(IntLiteral(1),([],[])),Dowhile(([],[]),IntLiteral(5))]))])],([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_assignable_expression(self):
        input = """Function: abc
                Body:
                5[5[5]] = 4;
                EndBody."""
        expect = str(Program([FuncDecl(Id("abc"),[],([],[Assign(ArrayCell(IntLiteral(5),[ArrayCell(IntLiteral(5),[IntLiteral(5)])]),IntLiteral(4))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_assignable_expression2(self):
        input = """Function: abc
                Body:
                (5 + 5 - 4)[(5+ 5)[5 - 4]] = (4 + 4 * 4)[4][3];
                EndBody."""
        expect = str(Program([FuncDecl(Id("abc"),[],([],[Assign(ArrayCell(BinaryOp("-",BinaryOp("+",IntLiteral(5),IntLiteral(5)),IntLiteral(4)),[ArrayCell(BinaryOp("+",IntLiteral(5),IntLiteral(5)),[BinaryOp("-",IntLiteral(5),IntLiteral(4))])]),ArrayCell(BinaryOp("+",IntLiteral(4),BinaryOp("*",IntLiteral(4),IntLiteral(4))),[IntLiteral(4),IntLiteral(3)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_nested_statements3(self):
        input = """Function:abc
                Body:
                DoDoDoDoDoDoDoDoDoDoWhile------------1EndDo.Whilefun(4,5,5,6,{1,2,3,4,6},6)EndDo.While3.4EndDo.While4444EndDo.While"abcdefjlksdj"EndDo.While6EndDo.While7EndDo.While8EndDo.While9EndDo.While000222e-11111EndDo.
                EndBody."""
        expect = str(Program([FuncDecl(Id("abc"),[],([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[Dowhile(([],[]),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",IntLiteral(1))))))))))))))]),CallExpr(Id("fun"),[IntLiteral(4),IntLiteral(5),IntLiteral(5),IntLiteral(6),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(6)]),IntLiteral(6)]))]),FloatLiteral(3.4))]),IntLiteral(4444))]),StringLiteral("abcdefjlksdj"))]),IntLiteral(6))]),IntLiteral(7))]),IntLiteral(8))]),IntLiteral(9))]),FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_index_operator11(self):
        input = """Function:abc
                Body:
                aaaa[112234[1123][123]][2 + 3 + 1][!!!!!-fun()][thisisfun()][nahthisisnotfun(fun,fee,ee,thisisnotthelasttestcaseSS)] = q;
                EndBody."""
        expect = str(Program([FuncDecl(Id("abc"),[],([],[Assign(ArrayCell(Id("aaaa"),[ArrayCell(IntLiteral(112234),[IntLiteral(1123),IntLiteral(123)]),BinaryOp("+",BinaryOp("+",IntLiteral(2),IntLiteral(3)),IntLiteral(1)),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("-",CallExpr(Id("fun"),[]))))))),CallExpr(Id("thisisfun"),[]),CallExpr(Id("nahthisisnotfun"),[Id("fun"),Id("fee"),Id("ee"),Id("thisisnotthelasttestcaseSS")])]),Id("q"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_random3(self):
        input = """Var: x, y, z[5];
                Function:main
                Parameter: a[5]
                Body:
                    x = 3;
                    y = x + 1;
                    x = x * 2;
                    a[4] = a[3] + a[2];
                EndBody.
                Function:main1
                Parameter: a[11]
                Body:
                EndBody."""
        expect = str(Program([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"),[5], None),FuncDecl(Id("main"),[VarDecl(Id("a"),[5], None)],([],[Assign(Id("x"),IntLiteral(3)),Assign(Id("y"),BinaryOp("+",Id("x"),IntLiteral(1))),Assign(Id("x"),BinaryOp("*",Id("x"),IntLiteral(2))),Assign(ArrayCell(Id("a"),[IntLiteral(4)]),BinaryOp("+",ArrayCell(Id("a"),[IntLiteral(3)]),ArrayCell(Id("a"),[IntLiteral(2)])))])),FuncDecl(Id("main1"),[VarDecl(Id("a"),[11], None)],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_random4(self):
        input = """Var: x[1][2] = {{2,4}};
                Var:y[5] = {"a","b","c","d","e"};
                Function: y3
                Parameter: a, b
                Body:
                    b = b + a;
                    a = y[3] + 1;
                    Return a + b;
                EndBody."""
        expect = str(Program([VarDecl(Id("x"),[1,2],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(4)])])),VarDecl(Id("y"),[5],ArrayLiteral([StringLiteral("a"),StringLiteral("b"),StringLiteral("c"),StringLiteral("d"),StringLiteral("e")])),FuncDecl(Id("y3"),[VarDecl(Id("a"), [], None),VarDecl(Id("b"), [], None)],([],[Assign(Id("b"),BinaryOp("+",Id("b"),Id("a"))),Assign(Id("a"),BinaryOp("+",ArrayCell(Id("y"),[IntLiteral(3)]),IntLiteral(1))),Return(BinaryOp("+",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_random5(self):
        input = """Var: x = 4, y = 5;
                Function: factorial
                Parameter: n
                Body:
                    If n > 1 Then Return n * factorial(n - 1);
                    Else Return 1;
                    EndIf.
                EndBody.
                Function: main
                Body:
                    print(factorial(x));
                    print(factorial(y));
                EndBody."""
        expect = str(Program([VarDecl(Id("x"), [],IntLiteral(4)),VarDecl(Id("y"), [],IntLiteral(5)),FuncDecl(Id("factorial"),[VarDecl(Id("n"), [], None)],([],[If([(BinaryOp(">",Id("n"),IntLiteral(1)),[],[Return(BinaryOp("*",Id("n"),CallExpr(Id("factorial"),[BinaryOp("-",Id("n"),IntLiteral(1))])))])],([],[Return(IntLiteral(1))]))])),FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[CallExpr(Id("factorial"),[Id("x")])]),CallStmt(Id("print"),[CallExpr(Id("factorial"),[Id("y")])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))


    def test_fibonacci_function(self):
        input = """Var: x = 0, y = 1;
                Function: fibonacci
                Parameter: n
                Body:
                    If (n == 0) Then Return 0;
                    ElseIf (n == 1) Then Return 1;
                    Else Return fibonacci (n - 1) + fibonacci(n - 2);
                    EndIf.
                EndBody.
                Function: main
                Body:
                    Var: n;
                    print("Hello, please enter a number : ");
                    n = scanln();
                    println("The result number is : " + toStr(fibonacci(n)));
                    println("Bye~");
                    Return;
                EndBody."""
        expect = str(Program([VarDecl(Id("x"), [],IntLiteral(0)),VarDecl(Id("y"), [],IntLiteral(1)),FuncDecl(Id("fibonacci"),[VarDecl(Id("n"), [], None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(0))]),(BinaryOp("==",Id("n"),IntLiteral(1)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("+",CallExpr(Id("fibonacci"),[BinaryOp("-",Id("n"),IntLiteral(1))]),CallExpr(Id("fibonacci"),[BinaryOp("-",Id("n"),IntLiteral(2))])))]))])),FuncDecl(Id("main"),[],([VarDecl(Id("n"), [], None)],[CallStmt(Id("print"),[StringLiteral("Hello, please enter a number : ")]),Assign(Id("n"),CallExpr(Id("scanln"),[])),CallStmt(Id("println"),[BinaryOp("+",StringLiteral("The result number is : "),CallExpr(Id("toStr"),[CallExpr(Id("fibonacci"),[Id("n")])]))]),CallStmt(Id("println"),[StringLiteral("Bye~")]),Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_random6(self):
        input = """Var: x = 1, y = 2, z = 4, t;
                Function: main
                Parameter: a, b
                Body:
                    Var: x, y;
                    Var: z;
                    x = -5;
                    y = -1;
                    z = - 10;
                    t = x + y + z;
                    print(t);
                EndBody."""
        expect = str(Program([VarDecl(Id("x"), [],IntLiteral(1)),VarDecl(Id("y"), [],IntLiteral(2)),VarDecl(Id("z"), [],IntLiteral(4)),VarDecl(Id("t"), [], None),FuncDecl(Id("main"),[VarDecl(Id("a"), [], None),VarDecl(Id("b"), [], None)],([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"), [], None)],[Assign(Id("x"),UnaryOp("-",IntLiteral(5))),Assign(Id("y"),UnaryOp("-",IntLiteral(1))),Assign(Id("z"),UnaryOp("-",IntLiteral(10))),Assign(Id("t"),BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("z"))),CallStmt(Id("print"),[Id("t")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
        
    def test_random7(self):
        input = """Var: x = 1, y = 2, z = 4, t;
                Function: main
                Parameter: a, b
                Body:
                    t = a + b + x;
                    If (t < 20) Then t = t + main(t, x * t);
                    EndIf.
                    print(t);
                EndBody."""
        expect = str(Program([VarDecl(Id("x"), [],IntLiteral(1)),VarDecl(Id("y"), [],IntLiteral(2)),VarDecl(Id("z"), [],IntLiteral(4)),VarDecl(Id("t"), [], None),FuncDecl(Id("main"),[VarDecl(Id("a"), [], None),VarDecl(Id("b"), [], None)],([],[Assign(Id("t"),BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("x"))),If([(BinaryOp("<",Id("t"),IntLiteral(20)),[],[Assign(Id("t"),BinaryOp("+",Id("t"),CallExpr(Id("main"),[Id("t"),BinaryOp("*",Id("x"),Id("t"))])))])],([],[])),CallStmt(Id("print"),[Id("t")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_random8(self):
        input = """Var: x = 1, y = 2;
                Function: main
                Body:
                    For(t = 1, t < 100, x) Do
                    x = x + y;
                    y = y + 1;
                    print(t);
                    EndFor.
                EndBody."""
        expect = str(Program([VarDecl(Id("x"), [],IntLiteral(1)),VarDecl(Id("y"), [],IntLiteral(2)),FuncDecl(Id("main"),[],([],[For(Id("t"),IntLiteral(1),BinaryOp("<",Id("t"),IntLiteral(100)),Id("x"),([],[Assign(Id("x"),BinaryOp("+",Id("x"),Id("y"))),Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(1))),CallStmt(Id("print"),[Id("t")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_random9(self):
        input = """Var: x = 1, y = 1;
                Function: main
                Body:
                    For(t = 1, t < 100, 1) Do
                    print(x + y + t);
                    EndFor.
                    x = x + y;
                    y = y + 3;
                    If (x < 1000) Then main();
                    EndIf.
                EndBody."""
        expect = str(Program([VarDecl(Id("x"), [],IntLiteral(1)),VarDecl(Id("y"), [],IntLiteral(1)),FuncDecl(Id("main"),[],([],[For(Id("t"),IntLiteral(1),BinaryOp("<",Id("t"),IntLiteral(100)),IntLiteral(1),([],[CallStmt(Id("print"),[BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("t"))])])),Assign(Id("x"),BinaryOp("+",Id("x"),Id("y"))),Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(3))),If([(BinaryOp("<",Id("x"),IntLiteral(1000)),[],[CallStmt(Id("main"),[])])],([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_break(self):
        input = """Function: main
                Body:
                    Break;
                    If 5 Then Break;
                    ElseIf 4 Then Break;
                    Else Break;
                    EndIf.
                    For (i = 1, i < 10, 1) Do
                    Break;
                    EndFor.
                    While 4 Do Break; EndWhile.
                    Do Break; While 3 EndDo.
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Break(),If([(IntLiteral(5),[],[Break()]),(IntLiteral(4),[],[Break()])],([],[Break()])),For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[Break()])),While(IntLiteral(4),([],[Break()])),Dowhile(([],[Break()]),IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_continue(self):
        input = """Function: main
                Body:
                    Break;
                    Continue;
                    If 5 Then Break; Continue;
                    While 4 Do Break; Continue; EndWhile.
                    ElseIf 4 Then Break; Continue;
                    While 4 Do Break; Continue; EndWhile.
                    Else Break; Continue;
                    EndIf.
                    For (i = 1, i < 10, 1) Do
                    Break; Continue;
                    EndFor.
                    While 4 Do Break; Continue; EndWhile.
                    Do Break; Continue; While 3 EndDo.
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Break(),Continue(),If([(IntLiteral(5),[],[Break(),Continue(),While(IntLiteral(4),([],[Break(),Continue()]))]),(IntLiteral(4),[],[Break(),Continue(),While(IntLiteral(4),([],[Break(),Continue()]))])],([],[Break(),Continue()])),For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[Break(),Continue()])),While(IntLiteral(4),([],[Break(),Continue()])),Dowhile(([],[Break(),Continue()]),IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_return(self):
        input = """Function: main
                Body:
                    Break;
                    Return;
                    Continue;
                    If 5 Then Break; Continue; Return 4;
                    While 4 Do Break; Return (5 + 6); Continue; EndWhile.
                    ElseIf 4 Then Break; Continue; Return 1;
                    While 4 Do Break; Continue; EndWhile.
                    Else Break; Continue; Return main();
                    EndIf.
                    For (i = 1, i < 10, 1) Do
                    If 5 Then Break; Continue; Return 4;
                    EndIf.
                    Break; Continue; Return 2;
                    EndFor.
                    While 4 Do Break; Continue; EndWhile.
                    Do Break; Continue; Return; While 3 EndDo.
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([],[Break(),Return(None),Continue(),If([(IntLiteral(5),[],[Break(),Continue(),Return(IntLiteral(4)),While(IntLiteral(4),([],[Break(),Return(BinaryOp("+",IntLiteral(5),IntLiteral(6))),Continue()]))]),(IntLiteral(4),[],[Break(),Continue(),Return(IntLiteral(1)),While(IntLiteral(4),([],[Break(),Continue()]))])],([],[Break(),Continue(),Return(CallExpr(Id("main"),[]))])),For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([],[If([(IntLiteral(5),[],[Break(),Continue(),Return(IntLiteral(4))])],([],[])),Break(),Continue(),Return(IntLiteral(2))])),While(IntLiteral(4),([],[Break(),Continue()])),Dowhile(([],[Break(),Continue(),Return(None)]),IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_vardecl(self):
        input = """Var: x, y, z[4][3];
                Function: main
                Body:
                    Var: x, y[5][7];
                    Break;
                    Return;
                    Continue;
                    If 5 Then Var: a; Break; Continue; Return 4;
                    While 4 Do Var: b; Break; Return (5 + 6); Continue; EndWhile.
                    ElseIf 4 Then Var: c; Break; Continue; Return 1;
                    While 4 Do Break; Continue; EndWhile.
                    Else Break; Continue; Return main();
                    EndIf.
                    For (i = 1, i < 10, 1) Do Var: d[5], e[6] = {1,2};
                    If 5 Then Break; Continue; Return 4;
                    EndIf.
                    Break; Continue; Return 2;
                    EndFor.
                    While 4 Do Break; Continue; EndWhile.
                    Do Break; Continue; Return; While 3 EndDo.
                EndBody."""
        expect = str(Program([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"),[4,3], None),FuncDecl(Id("main"),[],([VarDecl(Id("x"), [], None),VarDecl(Id("y"),[5,7], None)],[Break(),Return(None),Continue(),If([(IntLiteral(5),[VarDecl(Id("a"), [], None)],[Break(),Continue(),Return(IntLiteral(4)),While(IntLiteral(4),([VarDecl(Id("b"), [], None)],[Break(),Return(BinaryOp("+",IntLiteral(5),IntLiteral(6))),Continue()]))]),(IntLiteral(4),[VarDecl(Id("c"), [], None)],[Break(),Continue(),Return(IntLiteral(1)),While(IntLiteral(4),([],[Break(),Continue()]))])],([],[Break(),Continue(),Return(CallExpr(Id("main"),[]))])),For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(1),([VarDecl(Id("d"),[5], None),VarDecl(Id("e"),[6],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))],[If([(IntLiteral(5),[],[Break(),Continue(),Return(IntLiteral(4))])],([],[])),Break(),Continue(),Return(IntLiteral(2))])),While(IntLiteral(4),([],[Break(),Continue()])),Dowhile(([],[Break(),Continue(),Return(None)]),IntLiteral(3))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_functions(self):
        input = """Function: func1 Body: EndBody.
                Function: func2 Parameter: a, b Body: EndBody.
                Function: func3 Parameter: c, d Body: Var: a, b; EndBody.
                Function: func4 Parameter: e, f Body: Var: c; Var: d; Return; EndBody."""
        expect = str(Program([FuncDecl(Id("func1"),[],([],[])),FuncDecl(Id("func2"),[VarDecl(Id("a"), [], None),VarDecl(Id("b"), [], None)],([],[])),FuncDecl(Id("func3"),[VarDecl(Id("c"), [], None),VarDecl(Id("d"), [], None)],([VarDecl(Id("a"), [], None),VarDecl(Id("b"), [], None)],[])),FuncDecl(Id("func4"),[VarDecl(Id("e"), [], None),VarDecl(Id("f"), [], None)],([VarDecl(Id("c"), [], None),VarDecl(Id("d"), [], None)],[Return(None)]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_integer(self):
        input = """Var: x = 1000000000000000000000000000000000000;"""
        expect = str(Program([VarDecl(Id("x"), [],IntLiteral(1000000000000000000000000000000000000))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_boolean1(self):
        input = """Var: z = True, y = False;"""
        expect = str(Program([VarDecl(Id("z"), [],BooleanLiteral(True)),VarDecl(Id("y"), [],BooleanLiteral(False))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_boolean2(self):
        input = """Var: z[2][1] = {True, False, {True, False}}, y = False;"""
        expect = str(Program([VarDecl(Id("z"),[2,1],ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False)])])),VarDecl(Id("y"), [],BooleanLiteral(False))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_float1(self):
        input = """Var: x = 4.55e3;"""
        expect = str(Program([VarDecl(Id("x"), [],FloatLiteral(4.55e3))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_float2(self):
        input = """Var: x = 4554.4e-63;"""
        expect = str(Program([VarDecl(Id("x"), [],FloatLiteral(4554.4e-63))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_float3(self):
        input = """Var: x = 455E-6;"""
        expect = str(Program([VarDecl(Id("x"), [],FloatLiteral(455E-6))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_integer2(self):
        input = """Var: a = 0xABCDEFABCED;"""
        expect = str(Program([VarDecl(Id("a"), [],IntLiteral(0xABCDEFABCED))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_integer3(self):
        input = """Var: a = 0X1AB;"""
        expect = str(Program([VarDecl(Id("a"), [],IntLiteral(0X1AB))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_integer4(self):
        input = """Var: a = 0o10213;
                    Var: a = 0O103457;"""
        expect = str(Program([VarDecl(Id("a"), [],IntLiteral(0o10213))
                    ,VarDecl(Id("a"), [],IntLiteral(0O103457))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_random13(self):
        input = """Function: main
                Body:
                Var: x, y, z;
                x = (0.1 >=. 0.2 +. 0.3 +. 0.5 *. (0.1 -. 0.4) \\. 0.1) || (0.2 <=. x *. y -. z);
                Return x;
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"), [], None)],[Assign(Id("x"),BinaryOp("||",BinaryOp(">=.",FloatLiteral(0.1),BinaryOp("+.",BinaryOp("+.",FloatLiteral(0.2),FloatLiteral(0.3)),BinaryOp("\\.",BinaryOp("*.",FloatLiteral(0.5),BinaryOp("-.",FloatLiteral(0.1),FloatLiteral(0.4))),FloatLiteral(0.1)))),BinaryOp("<=.",FloatLiteral(0.2),BinaryOp("-.",BinaryOp("*.",Id("x"),Id("y")),Id("z"))))),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_random14(self):
        input = """Function: main
                Body:
                Var: x, y, z;
                x = (0.1 <. 0.5) && (2 <= 0x4) || !!(4 >= 0X5) && (0.5 <. 0.99) || (63 % 21 > 99);
                Return x;
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"), [], None),VarDecl(Id("y"), [], None),VarDecl(Id("z"), [], None)],[Assign(Id("x"),BinaryOp("||",BinaryOp("&&",BinaryOp("||",BinaryOp("&&",BinaryOp("<.",FloatLiteral(0.1),FloatLiteral(0.5)),BinaryOp("<=",IntLiteral(2),IntLiteral(4))),UnaryOp("!",UnaryOp("!",BinaryOp(">=",IntLiteral(4),IntLiteral(5))))),BinaryOp("<.",FloatLiteral(0.5),FloatLiteral(0.99))),BinaryOp(">",BinaryOp("%",IntLiteral(63),IntLiteral(21)),IntLiteral(99)))),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_random15(self):
        input = """Function: main
                Body:
                Var: x;
                x = (y || z) && (1 == 2) || (z != 0o3) && (0.3 =/= 0.45e1) || False;
                Return x;
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"), [], None)],[Assign(Id("x"),BinaryOp("||",BinaryOp("&&",BinaryOp("||",BinaryOp("&&",BinaryOp("||",Id("y"),Id("z")),BinaryOp("==",IntLiteral(1),IntLiteral(2))),BinaryOp("!=",Id("z"),IntLiteral(3))),BinaryOp("=/=",FloatLiteral(0.3),FloatLiteral(4.5))),BooleanLiteral(False))),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_random16(self):
        input = """Function: main
                Body:
                Var: x;
                x = float_of_int(1 + int_of_float(2.4)) +. float_of_int(4 * int_of_float(2.3 +. 3.4));
                Return x;
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"), [], None)],[Assign(Id("x"),BinaryOp("+.",CallExpr(Id("float_of_int"),[BinaryOp("+",IntLiteral(1),CallExpr(Id("int_of_float"),[FloatLiteral(2.4)]))]),CallExpr(Id("float_of_int"),[BinaryOp("*",IntLiteral(4),CallExpr(Id("int_of_float"),[BinaryOp("+.",FloatLiteral(2.3),FloatLiteral(3.4))]))]))),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_random17(self):
        input = """Function: main
                Body:
                Var: x;
                x = 5 < (6 && 7 < 0o1234);
                Return x;
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"), [], None)],[Assign(Id("x"),BinaryOp("<",IntLiteral(5),BinaryOp("<",BinaryOp("&&",IntLiteral(6),IntLiteral(7)),IntLiteral(668)))),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_random18(self):
        input = """Function: main
                Body:
                Var: x;
                x = 5 && 6 + 7 && 8;
                Return x;
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"), [], None)],[Assign(Id("x"),BinaryOp("&&",BinaryOp("&&",IntLiteral(5),BinaryOp("+",IntLiteral(6),IntLiteral(7))),IntLiteral(8))),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_random19(self):
        input = """Function: main
                Body:
                Var: x;
                x = 5 + 6 && 7 + 8;
                Return x;
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("x"), [], None)],[Assign(Id("x"),BinaryOp("&&",BinaryOp("+",IntLiteral(5),IntLiteral(6)),BinaryOp("+",IntLiteral(7),IntLiteral(8)))),Return(Id("x"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
        
    def test_random20(self):
        input = """Function: mian
                Parameter: x
                Body:
                If 4 && (x > 0) Then 
                x = x - 1;
                mian(x);
                Else x = 100;
                EndIf.
                EndBody."""
        expect = str(Program([FuncDecl(Id("mian"),[VarDecl(Id("x"), [], None)],([],[If([(BinaryOp("&&",IntLiteral(4),BinaryOp(">",Id("x"),IntLiteral(0))),[],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),CallStmt(Id("mian"),[Id("x")])])],([],[Assign(Id("x"),IntLiteral(100))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_random21(self):
        input = """Function: main
                Body:
                    Var: a[100];
                    For (i = 0, i < 100, 1) Do
                        a[i] = i;
                    EndFor.
                    For (i = 0, i < 100, 2) Do
                        print(a[i] + a[i+1]);
                    EndFor.
                EndBody."""
        expect = str(Program([FuncDecl(Id("main"),[],([VarDecl(Id("a"),[100], None)],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(100)),IntLiteral(1),([],[Assign(ArrayCell(Id("a"),[Id("i")]),Id("i"))])),For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(100)),IntLiteral(2),([],[CallStmt(Id("print"),[BinaryOp("+",ArrayCell(Id("a"),[Id("i")]),ArrayCell(Id("a"),[BinaryOp("+",Id("i"),IntLiteral(1))]))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
        
    def test_random22(self):
        input = """Function: printArray
                Parameter: a[100], i
                Body:
                    If (i > 100) || (i < 0) Then
                    Return;
                    EndIf.
                    printArray(a, i + 1);
                EndBody."""
        expect = str(Program([FuncDecl(Id("printArray"),[VarDecl(Id("a"),[100], None),VarDecl(Id("i"), [], None)],([],[If([(BinaryOp("||",BinaryOp(">",Id("i"),IntLiteral(100)),BinaryOp("<",Id("i"),IntLiteral(0))),[],[Return(None)])],([],[])),CallStmt(Id("printArray"),[Id("a"),BinaryOp("+",Id("i"),IntLiteral(1))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_random23(self):
        input = """Function: printArrayDoubleSide
                Parameter: a[100], i
                Body:
                    If (i > (100 - i)) || (i < 0) || (i > 100) Then
                    Return;
                    EndIf.
                    print(a[i]);
                    print(a[100 - i]);
                    printArrayDoubleSide(a, i + 1);
                EndBody."""
        expect = str(Program([FuncDecl(Id("printArrayDoubleSide"),[VarDecl(Id("a"),[100], None),VarDecl(Id("i"), [], None)],([],[If([(BinaryOp("||",BinaryOp("||",BinaryOp(">",Id("i"),BinaryOp("-",IntLiteral(100),Id("i"))),BinaryOp("<",Id("i"),IntLiteral(0))),BinaryOp(">",Id("i"),IntLiteral(100))),[],[Return(None)])],([],[])),CallStmt(Id("print"),[ArrayCell(Id("a"),[Id("i")])]),CallStmt(Id("print"),[ArrayCell(Id("a"),[BinaryOp("-",IntLiteral(100),Id("i"))])]),CallStmt(Id("printArrayDoubleSide"),[Id("a"),BinaryOp("+",Id("i"),IntLiteral(1))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_random24(self):
        input = """Function: printArray2
                Parameter: a[100][100], i
                Body:
                    If (i > 100) || (i < 0) Then
                    Return;
                    EndIf.
                    printArray(a[i]);
                    printArray2(a, i + 1);
                EndBody."""
        expect = str(Program([FuncDecl(Id("printArray2"),[VarDecl(Id("a"),[100,100], None),VarDecl(Id("i"), [], None)],([],[If([(BinaryOp("||",BinaryOp(">",Id("i"),IntLiteral(100)),BinaryOp("<",Id("i"),IntLiteral(0))),[],[Return(None)])],([],[])),CallStmt(Id("printArray"),[ArrayCell(Id("a"),[Id("i")])]),CallStmt(Id("printArray2"),[Id("a"),BinaryOp("+",Id("i"),IntLiteral(1))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_empty_program(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_deep_array(self):
        input = """Var: x = {{{{{{{{{{{{{{10}}}}}}}}}}}}}};"""
        expect = str(Program([VarDecl(Id("x"), [],ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(10)])])])])])])])])])])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_deep_bracket(self):
        input = """Var: x;
                Function: main
                Body:
                x = (((((((((((((((((((((10)))))))))))))))))))));
                EndBody."""
        expect = str(Program([VarDecl(Id("x"), [], None),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_dot(self):
        input = """Var       : x;
            Function        : main
            Body            :
            EndBody          ."""
        expect = str(Program([VarDecl(Id("x"), [], None),FuncDecl(Id("main"),[],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_string_escape(self):
        input = """Var: x = "ab'"c\\n def";"""
        expect = str(Program([VarDecl(Id("x"), [],StringLiteral("ab\'\"c\\n def"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_string_escape2(self):
        input = """Var: x = "ab'"c\\\\n def";"""
        expect = str(Program([VarDecl(Id("x"), [],StringLiteral("ab\'\"c\\\\n def"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_string_escape3(self):
        input = """Var: x = "ab'"c\\\\n \\t \\b \\r def";"""
        expect = str(Program([VarDecl(Id("x"), [],StringLiteral("ab\'\"c\\\\n \\t \\b \\r def"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_string_escape4(self):
        input = """Var: x = "ab'"c \t \b def";"""
        expect = str(Program([VarDecl(Id("x"), [],StringLiteral("ab\'\"c \t \b def"))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_all(self):
        input = """Var: x = 1, y = 0.5, z = "abcd", w = True;
                    Var: a[5] = {1,2,3,4,5};
                    Var: b[3] = {True, False, True};
                    Function: main
                    Parameter: x[1], y[4][5][6], z
                    Body:
                    Var: t;
                    t = y[1][2][3] + y[4][3][2] + int_of_float(4.45 *. 4.78);
                    If (x > 4) && (y <. 5.7) Then
                    x = 0;
                    ElseIf x < 4 Then
                    Var: e = 44.5E3;
                    For (q = 1, 4, 5 < 6) Do
                        Var: t;
                        Var: c;
                        t = q*q;
                        print(q);
                        If q < 10 Then Break; EndIf.
                        While (q < 10) Do
                            q = q - 1;
                            print(q);
                        EndWhile.
                        Do c = c + 1;
                        If c == 2 Then Continue; EndIf.
                        While c < q EndDo.
                        print(c);
                    EndFor.
                    x = 1;
                    main(x, g, h);
                    Else x = 2;
                    EndIf.
                    EndBody."""
        expect = str(Program([VarDecl(Id("x"), [],IntLiteral(1)),VarDecl(Id("y"), [],FloatLiteral(0.5)),VarDecl(Id("z"), [],StringLiteral("abcd")),VarDecl(Id("w"), [],BooleanLiteral(True)),VarDecl(Id("a"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])),VarDecl(Id("b"),[3],ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False),BooleanLiteral(True)])),FuncDecl(Id("main"),[VarDecl(Id("x"),[1], None),VarDecl(Id("y"),[4,5,6], None),VarDecl(Id("z"), [], None)],([VarDecl(Id("t"), [], None)],[Assign(Id("t"),BinaryOp("+",BinaryOp("+",ArrayCell(Id("y"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayCell(Id("y"),[IntLiteral(4),IntLiteral(3),IntLiteral(2)])),CallExpr(Id("int_of_float"),[BinaryOp("*.",FloatLiteral(4.45),FloatLiteral(4.78))]))),If([(BinaryOp("&&",BinaryOp(">",Id("x"),IntLiteral(4)),BinaryOp("<.",Id("y"),FloatLiteral(5.7))),[],[Assign(Id("x"),IntLiteral(0))]),(BinaryOp("<",Id("x"),IntLiteral(4)),[VarDecl(Id("e"), [],FloatLiteral(44500.0))],[For(Id("q"),IntLiteral(1),IntLiteral(4),BinaryOp("<",IntLiteral(5),IntLiteral(6)),([VarDecl(Id("t"), [], None),VarDecl(Id("c"), [], None)],[Assign(Id("t"),BinaryOp("*",Id("q"),Id("q"))),CallStmt(Id("print"),[Id("q")]),If([(BinaryOp("<",Id("q"),IntLiteral(10)),[],[Break()])],([],[])),While(BinaryOp("<",Id("q"),IntLiteral(10)),([],[Assign(Id("q"),BinaryOp("-",Id("q"),IntLiteral(1))),CallStmt(Id("print"),[Id("q")])])),Dowhile(([],[Assign(Id("c"),BinaryOp("+",Id("c"),IntLiteral(1))),If([(BinaryOp("==",Id("c"),IntLiteral(2)),[],[Continue()])],([],[]))]),BinaryOp("<",Id("c"),Id("q"))),CallStmt(Id("print"),[Id("c")])])),Assign(Id("x"),IntLiteral(1)),CallStmt(Id("main"),[Id("x"),Id("g"),Id("h")])])],([],[Assign(Id("x"),IntLiteral(2))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
