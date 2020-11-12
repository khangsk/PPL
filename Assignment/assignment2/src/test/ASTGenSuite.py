import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test2_array_program(self):
        input = """Var:x = 1, y;
        Var: a[2] = 3, b[4];"""
        expect = Program([
            VarDecl(Id("x"),[],IntLiteral(1)),
            VarDecl(Id("y"),[],None),
            VarDecl(Id("a"),[2],IntLiteral(3)),
            VarDecl(Id("b"),[4],None)
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test3_array_program(self):
        input = """Var: abc[1][2][3] = 4;"""
        expect = Program([
            VarDecl(Id("abc"),[1,2,3],IntLiteral(4))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test4_call_stmt(self):
        input = r"""
        Function: fact
        Parameter: b, c[1][2]
        Body:
            Var: a;
            a = 5;
            writeln(a[i], " is smaller than ", b);
        EndBody."""
        expect = Program([
            FuncDecl(
                Id("fact"),
                [
                    VarDecl(Id("b"),[],None),
                    VarDecl(Id("c"),[1,2],None)
                ],
                (
                    [
                        VarDecl(Id("a"),[],None)
                    ],[
                        Assign(Id("a"),IntLiteral(5)),
                        CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is smaller than "),Id("b")])
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test5_only_if_stmt(self):
        input = """
        Function: fact
        Body:
            If a[i] > b Then 
                writeln(a[i], " is larger than ", b);
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("fact"),[],(
                [],
                [
                    If(
                        [
                            (
                                BinaryOp(
                                    ">",
                                    ArrayCell(
                                        Id("a"),
                                        [Id("i")]
                                    ),
                                    Id("b")),
                                [],
                                [
                                    CallStmt(
                                        Id("writeln"),
                                        [
                                            ArrayCell(
                                                Id("a"),
                                                [
                                                    Id("i")]),
                                                    StringLiteral(" is larger than "),
                                                    Id("b")
                                                ]
                                            )
                                        ]
                            )
                        ],
                        []
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test6_if_elseif_stmt(self):
        input = """
        Function: fact
        Body:
            If a[i] > b Then 
                writeln(a[i], " is larger than ", b);
            ElseIf a[i] == b Then 
                writeln(a[i], " equal ", b);
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("fact"),[],(
                [],
                [
                    If(
                        [
                            (
                                BinaryOp(">",ArrayCell(Id("a"),[Id("i")]),Id("b")),
                                [],
                                [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is larger than "),Id("b")])]
                            ),
                            (
                                BinaryOp("==",ArrayCell(Id("a"),[Id("i")]),Id("b")),
                                [],
                                [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" equal "),Id("b")])]
                            )
                        ],
                        []
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test7_if_else_stmt(self):
        input = """
        Function: fact
        Body:
            If a[i] > b Then 
                writeln(a[i], " is larger than ", b);
            Else 
                writeln(a[i], " is smaller than ", b);
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("fact"),[],(
                [],
                [
                    If(
                        [
                            (
                                BinaryOp(">",ArrayCell(Id("a"),[Id("i")]),Id("b")),
                                [],
                                [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is larger than "),Id("b")])]
                            )
                        ],
                        (
                            [],
                            [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is smaller than "),Id("b")])]
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test8_if_stmt(self):
        input = """
        Function: fact
        Body:
            If a[i] > b Then 
                writeln(a[i], " is larger than ", b);
            ElseIf a[i] == b Then 
                writeln(a[i], " equal ", b);
            Else 
                writeln(a[i], " is smaller than ", b);
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("fact"),[],(
                [],
                [
                    If(
                        [
                            (
                                BinaryOp(">",ArrayCell(Id("a"),[Id("i")]),Id("b")),
                                [],
                                [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is larger than "),Id("b")])]
                            ),
                            (
                                BinaryOp("==",ArrayCell(Id("a"),[Id("i")]),Id("b")),
                                [],
                                [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" equal "),Id("b")])]
                            )
                        ],
                        (
                            [],
                            [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is smaller than "),Id("b")])]
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test9_if_stmt(self):
        input = """
        Function: fact
        Body:
            If a[i] > b Then 
                writeln(a[i], " is larger than ", b);
            ElseIf a[i] == b Then 
                writeln(a[i], " equal ", b);
            ElseIf a[i] && b Then 
                writeln(a[i]);
            ElseIf !a[i] Then 
                writeln(b);
            Else 
                writeln(a[i], " is smaller than ", b);
            EndIf.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("fact"),[],(
                [],
                [
                    If(
                        [
                            (
                                BinaryOp(">",ArrayCell(Id("a"),[Id("i")]),Id("b")),
                                [],
                                [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is larger than "),Id("b")])]
                            ),
                            (
                                BinaryOp("==",ArrayCell(Id("a"),[Id("i")]),Id("b")),
                                [],
                                [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" equal "),Id("b")])]
                            ),
                            (
                                BinaryOp("&&",ArrayCell(Id("a"),[Id("i")]),Id("b")),
                                [],
                                [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")])])]
                            ),
                            (
                                UnaryOp("!",ArrayCell(Id("a"),[Id("i")])),
                                [],
                                [CallStmt(Id("writeln"),[Id("b")])]
                            )
                        ],
                        (
                            [],
                            [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is smaller than "),Id("b")])]
                        )
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test10_var_array(self):
        input = """Var: a[3] = {1,0,2};"""
        expect = Program([
            VarDecl(
                Id("a"),
                [3],
                ArrayLiteral([IntLiteral(1),IntLiteral(0),IntLiteral(2)])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test11_var_array(self):
        input = """Var: a[3][2] = {{1,0XAF},{4,0},{0O6543,7}};
        """
        expect = Program([
            VarDecl(
                Id("a"),
                [3,2],
                ArrayLiteral([
                    ArrayLiteral([IntLiteral(1),IntLiteral(175)]),
                    ArrayLiteral([IntLiteral(4),IntLiteral(0)]),
                    ArrayLiteral([IntLiteral(3427),IntLiteral(7)])
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test12_while_stmt(self):
        input = """
        Function: abc
        Body:
            Var: i = 10;
            While (i > 1) Do
                writeln(i);
                i = i - 1;
            EndWhile.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("abc"),
                [],
                (
                    [
                        VarDecl(Id("i"),[],IntLiteral(10))
                    ],
                    [
                        While(
                            BinaryOp(">",Id("i"),IntLiteral(1)),
                            (
                                [],
                                [
                                    CallStmt(Id("writeln"),[Id("i")]),
                                    Assign(
                                        Id("i"),
                                        BinaryOp("-",Id("i"),IntLiteral(1))
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test13_while_stmt(self):
        input = """
        Function: abc
        Body:
            While True Do
            EndWhile.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("abc"),
                [],
                (
                    [],
                    [
                        While(BooleanLiteral(True),([],[]))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test14_do_while_stmt(self):
        input = """
        Function: abc
        Body:
            Do
                Var: abc = False;
                writeln("nothing to print");
            While True EndDo.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("abc"),
                [],
                (
                    [],
                    [
                        Dowhile(
                            (
                                [
                                    VarDecl(Id("abc"),[],BooleanLiteral(False))
                                ],[
                                    CallStmt(Id("writeln"),[StringLiteral("nothing to print")])
                                ]
                            ),
                            BooleanLiteral(True)
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test15_break_stmt(self):
        input = """
        Function: abc
        Body:
            Do
                Var: abc = False;
                Break;
                writeln("nothing to print");
            While True EndDo.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("abc"),[],(
                [],
                [
                    Dowhile(
                        ([
                            VarDecl(Id("abc"),[],BooleanLiteral(False))
                        ],
                        [
                            Break(),
                            CallStmt(Id("writeln"),[StringLiteral("nothing to print")])
                        ]),
                        BooleanLiteral(True)
                    )
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test16_continue_stmt(self):
        input = """
        Function: main
        Body:
            While True Do
                Continue;
                writeln("nothing to print");
            EndWhile.
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],
                ([],
                    [While(
                        BooleanLiteral(True),
                        ([],
                        [
                            Continue(),
                            CallStmt(Id("writeln"),[StringLiteral("nothing to print")])
                        ]
                        )
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test17_return_stmt(self):
        input = """
        Function: main
        Body:
            Var: a = 1;
            a = a + 10;
            Return a;
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],
                ([
                    VarDecl(Id("a"),[],IntLiteral(1))
                ],[
                    Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(10))),
                    Return(Id("a"))
                ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test18_return_stmt(self):
        input = """
        Function: main
        Body:
            Return;
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test19_for_stmt(self):
        input = """
        Function: main
        Parameter: a[10]
        Body:
            For (i = 1, i < 10, 1) Do
                writeln(a[i]);
            EndFor.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("a"),[10],None)],
                (
                    [],
                    [
                        For(
                            Id("i"),
                            IntLiteral(1),
                            BinaryOp("<",Id("i"),IntLiteral(10)),
                            IntLiteral(1),
                            ([],[CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")])])])
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test20_for_stmt(self):
        input = """
        Function: main
        Parameter: a[10]
        Body:
            For (i = 1, i < 10, 1) Do
            EndFor.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("a"),[10],None)],
                (
                    [],
                    [
                        For(
                            Id("i"),
                            IntLiteral(1),
                            BinaryOp("<",Id("i"),IntLiteral(10)),
                            IntLiteral(1),
                            ([],[]))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test21_index_exp(self):
        input = """
        Function: main
        Parameter: a[2][10]
        Body:
            For (i = 0, i < 2, 1) Do
                For (j = 0, j < 10, 1) Do
                    a[i][j] = a[i][j] * 10;
                    writeln(a[i][j]);
                EndFor.
            EndFor.
        EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("a"),[2,10],None)],
                (
                    [],
                    [
                        For(
                            Id("i"),
                            IntLiteral(0),
                            BinaryOp("<",Id("i"),IntLiteral(2)),
                            IntLiteral(1),
                            ([],
                                [
                                    For(
                                        Id("j"),
                                        IntLiteral(0),
                                        BinaryOp("<",Id("j"),IntLiteral(10)),
                                        IntLiteral(1),
                                        ([],[
                                            Assign(ArrayCell(Id("a"),[Id("i"),Id("j")]),BinaryOp("*",ArrayCell(Id("a"),[Id("i"),Id("j")]),IntLiteral(10))),
                                            CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i"),Id("j")])])
                                        ])
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test22_var(self):
        input = r"""
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, z;
        Var: m = 1, n[2] = {   2   ,   3   };"""
        expect = Program([
            VarDecl(Id("a"),[],IntLiteral(5)),
            VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),
            VarDecl(Id("c"),[],None),
            VarDecl(Id("d"),[],IntLiteral(6)),
            VarDecl(Id("e"),[],None),
            VarDecl(Id("z"),[],None),
            VarDecl(Id("m"),[],IntLiteral(1)),
            VarDecl(Id("n"),[2],ArrayLiteral([IntLiteral(2),IntLiteral(3)]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test23_funct_declare_part(self):
        input = r"""
        Var: x;
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact(n - 1);
                EndIf.
            EndBody.
        Function: main
        Body:
            x = 10;
            fact(x);
        EndBody."""
        expect = Program([
            VarDecl(Id("x"),[],None),
            FuncDecl(
                Id("fact"),[VarDecl(Id("n"),[],None)],(
                    [],[
                        If(
                            [(
                                BinaryOp("==",Id("n"),IntLiteral(0)),
                                [],[
                                Return(IntLiteral(1))]
                            )],
                            ([],[
                                Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))
                            ])
                        )
                    ]
                )
            ),
            FuncDecl(
                Id("main"),[],(
                    [],[
                        Assign(Id("x"),IntLiteral(10)),
                        CallStmt(Id("fact"),[Id("x")])
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test24_string_and_comment(self):
        input = r"""
        Var: ajsd_123s = "Khang", u___12sA[2] = {  "Hoang" ,    "Gia"     };
        Var: a, b, c = 3.e3;
        Var: nothing;
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact(n - 1);
                EndIf.
            EndBody.
        **Test comment!!!**
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody."""
        expect = Program([
            VarDecl(Id("ajsd_123s"),[],StringLiteral("Khang")),
            VarDecl(Id("u___12sA"),[2],ArrayLiteral([StringLiteral("Hoang"),StringLiteral("Gia")])),
            VarDecl(Id("a"),[],None),
            VarDecl(Id("b"),[],None),
            VarDecl(Id("c"),[],FloatLiteral(3000.0)),
            VarDecl(Id("nothing"),[],None),
            FuncDecl(
                Id("fact"),
                [VarDecl(Id("n"),[],None)],
                (
                    [],[
                    If(
                        [(
                            BinaryOp("==",Id("n"),IntLiteral(0)),
                            [],
                            [Return(IntLiteral(1))]
                        )],
                        ([],[
                            Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))
                        ])
                    )]
                )
            ),
            FuncDecl(
                Id("main"),[],
                (
                    [],[
                    Assign(Id("x"),IntLiteral(10)),
                    CallStmt(Id("fact"),[Id("x")])
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test25_assign_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While (i < 5) Do
                    a[i] = b +. 1.0;
                    i = i + 1;
                EndWhile.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("foo"),[
                VarDecl(Id("a"),[5],None),
                VarDecl(Id("b"),[],None)],
                (
                    [VarDecl(Id("i"),[],IntLiteral(0))],
                    [
                        While(
                            BinaryOp("<",Id("i"),IntLiteral(5)),
                            ([],[
                                Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral("1.0"))),
                                Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))
                            ])
                        )
                    ]
                )
            ),
            FuncDecl(
                Id("main"),[],([],[
                    Assign(Id("x"),IntLiteral(10)),
                    CallStmt(Id("fact"),[Id("x")])
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test26_for_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[5], b
            Body:
                For (i = 0, i < 10, 2) Do
                    writeln(a[i] + b);
                EndFor.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),[5],None),
                VarDecl(Id("b"),[],None)],
                ([],[
                    For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        IntLiteral(2),
                        ([],
                        [CallStmt(Id("writeln"),[BinaryOp("+",ArrayCell(Id("a"),[Id("i")]),Id("b"))])])
                    )
                ])
            ),
            FuncDecl(Id("main"),[],([],
                [Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("fact"),[Id("x")])
                ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test27_assign_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[5], b
            Body:
                For (i = 0, i < 10, 2) Do
                    a[i] = b;
                EndFor.
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),[5],None),
                VarDecl(Id("b"),[],None)],
                ([],[
                    For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        IntLiteral(2),
                        ([],[Assign(ArrayCell(Id("a"),[Id("i")]),Id("b"))])
                    )
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test28_if_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[2], b
            Body:
                For (i = 0, i < 2, 1) Do
                    If a[i] > b Then writeln(a[i], " is larger than ", b);
                    ElseIf a[i] == b Then writeln(a[i], " equal ", b);
                    Else writeln(a[i], " is smaller than ", b);
                    EndIf.
                EndFor.
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),[2],None),
                VarDecl(Id("b"),[],None)],([],[
                    For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(2)),
                        IntLiteral(1),
                        ([],[
                            If(
                                [(
                                    BinaryOp(">",ArrayCell(Id("a"),[Id("i")]),Id("b")),
                                    [],
                                    [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is larger than "),Id("b")])]
                                ),(
                                    BinaryOp("==",ArrayCell(Id("a"),[Id("i")]),Id("b")),
                                    [],
                                    [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" equal "),Id("b")])]
                                )],([],[
                                    CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is smaller than "),Id("b")])
                                ])
                            )
                        ])
                    )
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test29_while_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[2], b
            Body:
                Var: i = 0;
                While (a[i] > b) Do
                    writeln(a[i]);
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),[2],None),
                VarDecl(Id("b"),[],None)],
                (
                    [VarDecl(Id("i"),[],IntLiteral(0))],
                    [While(
                        BinaryOp(">",ArrayCell(Id("a"),[Id("i")]),Id("b")),
                        ([],[
                            CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")])]),
                            Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))
                        ])
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test30_do_while_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[2], b
            Body:
                Var: i = 0;
                Do 
                    a[i] = a[i] +. 1.;
                While (a[i] > b) EndDo.
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),[2],None),
                VarDecl(Id("b"),[],None)],
                (
                    [VarDecl(Id("i"),[],IntLiteral(0))],
                    [Dowhile(([],[
                        Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",ArrayCell(Id("a"),[Id("i")]),FloatLiteral(1.0)))
                    ]),BinaryOp(">",ArrayCell(Id("a"),[Id("i")]),Id("b"))
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test31_break_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[10]
            Body:
                Var: i;
                For (i = 0, i < 10, 1) Do
                    writeln(a[i]);
                    If (a[10] > 5) Then
                        Break;
                    EndIf.
                EndFor.
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),[10],None)],
                (
                    [VarDecl(Id("i"),[],None)],
                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        IntLiteral(1),
                        ([],[
                            CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")])]),
                            If(
                                [(BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(10)]),IntLiteral(5)),
                                [],
                                [Break()])],
                                []
                            )
                        ])
                    )]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test32_continue_stmt(self):
        input = r"""
        Function: foo
            Parameter: a[10]
            Body:
                Var: i;
                For (i = 0, i < 10, 1) Do
                    writeln(a[i]);
                    If (a[10] > 5) Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),[10],None)],
                ([VarDecl(Id("i"),[],None)],
                [For(
                    Id("i"),
                    IntLiteral(0),
                    BinaryOp("<",Id("i"),IntLiteral(10)),
                    IntLiteral(1),
                    ([],[
                        CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")])]),
                        If(
                            [(
                                BinaryOp(">",ArrayCell(Id("a"),[IntLiteral(10)]),IntLiteral(5)),
                                [],
                                [Continue()]
                            )],
                            []
                        )
                    ])
                )])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test33_call_stmt(self):
        input = r"""
        Function: foo
            Parameter: x, y
            Body:
                writeln(foo(2 + x, 4. \. y) * goo());
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None)],
                ([],[
                    CallStmt(Id("writeln"),[BinaryOp("*",CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("x")),BinaryOp("\.",FloatLiteral(4.0),Id("y"))]),CallExpr(Id("goo"),[]))])
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test34_return_stmt(self):
        input = r"""
        Function: compare
            Parameter: x, y
            Body:
                If (x > y) Then
                    Return True ;
                Else Return False;
                EndIf.
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("compare"),
                [VarDecl(Id("x"),[],None),
                VarDecl(Id("y"),[],None)],([],[
                    If(
                        [(
                            BinaryOp(">",Id("x"),Id("y")),
                            [],
                            [Return(BooleanLiteral(True))]
                        )],
                        ([],[Return(BooleanLiteral(False))])
                    )
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test35_type_coercions(self):
        input = r"""
        Function: compare
            Parameter: a, b
            Body:
                If bool_of_string("True") Then
                    a = int_of_string(read());
                    b = float_of_string(a) +. 2.0;
                EndIf.
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("compare"),
                [VarDecl(Id("a"),[],None),
                VarDecl(Id("b"),[],None)],([],[
                    If(
                        [(
                            CallExpr(Id("bool_of_string"),[StringLiteral("True")]),
                            [],
                            [Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),
                            Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_string"),[Id("a")]),FloatLiteral("2.0")))]
                        )],[]
                    )
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test36_call_stmt(self):
        input = r"""
        Function: printDivivsors
            Parameter: n
            Body:
                For (i = 1, i <= n, 1) Do
                    If (n % i == 0) Then
                        writeln(i);
                    EndIf.
                EndFor.
            EndBody.
        Function: main
            Body:
                Var: x;
                input(x);
                printDivivsors(x);
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("printDivivsors"),
                [VarDecl(Id("n"),[],None)],([],[
                    For(
                        Id("i"),
                        IntLiteral(1),
                        BinaryOp("<=",Id("i"),Id("n")),
                        IntLiteral(1),
                        ([],[
                            If(
                                [(
                                    BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),
                                    [],
                                    [CallStmt(Id("writeln"),[Id("i")])]
                                )],[]
                            )
                        ])
                    )
                ])
            ),
            FuncDecl(
                Id("main"),[],(
                    [VarDecl(Id("x"),[],None)],
                    [CallStmt(Id("input"),[Id("x")]),CallStmt(Id("printDivivsors"),[Id("x")])]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test37(self):
        input = r"""
        Function: power_rep
            Parameter: base, exp
            Body:
                Var: a = 2;
                If (exp == 0) Then
                    Return 1;
                EndIf.
                For (i = 0, i < exp - 1, 1) Do
                    base = base * a;
                EndFor.
                Return base;
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("power_rep"),
                [VarDecl(Id("base"),[],None),
                VarDecl(Id("exp"),[],None)],(
                    [VarDecl(Id("a"),[],IntLiteral(2))],
                    [If(
                        [(
                            BinaryOp("==",Id("exp"),IntLiteral(0)),
                            [],
                            [Return(IntLiteral(1))]
                        )],[]
                    ),
                    For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),BinaryOp("-",Id("exp"),IntLiteral(1))),
                        IntLiteral(1),
                        ([],[Assign(Id("base"),BinaryOp("*",Id("base"),Id("a")))])
                    ),
                    Return(Id("base"))]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test38(self):
        input = r"""
        Function: power_recur
            Parameter: base, exp
            Body:
                If (exp == 0) Then
                    Return 1;
                EndIf.
                Return base * power_recur(base, exp - 1);
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("power_recur"),
                [VarDecl(Id("base"),[],None),
                VarDecl(Id("exp"),[],None)],([],[
                    If(
                        [(
                            BinaryOp("==",Id("exp"),IntLiteral(0)),
                            [],
                            [Return(IntLiteral(1))]
                        )],[]
                    ),
                    Return(BinaryOp("*",Id("base"),CallExpr(Id("power_recur"),[Id("base"),BinaryOp("-",Id("exp"),IntLiteral(1))])))
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test39(self):
        input = r"""
        Function: power_rep
            Parameter: base, exp
            Body:
                Var: a = 2;
                If (exp == 0) Then
                    Return 1;
                EndIf.
                For (i = 0, i < exp - 1, 1) Do
                    base = base * a;
                EndFor.
                Return base;
            EndBody.
        Function: power_recur
            Parameter: base, exp
            Body:
                If (exp == 0) Then
                    Return 1;
                EndIf.
                Return base * power_recur(base, exp - 1);
            EndBody.
        Function: main
            Parameter: base, exp
            Body:
                base = input();
                exp = input();
                writeln(power_rep(base, exp));
                writeln(power_recur(base, exp));
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("power_rep"),
                [VarDecl(Id("base"),[],None),
                VarDecl(Id("exp"),[],None)],
                ([VarDecl(Id("a"),[],IntLiteral(2))],[
                    If(
                        [(
                            BinaryOp("==",Id("exp"),IntLiteral(0)),
                            [],
                            [Return(IntLiteral(1))]
                        )],[]
                    ),
                    For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),BinaryOp("-",Id("exp"),IntLiteral(1))),
                        IntLiteral(1),
                        ([],[Assign(Id("base"),BinaryOp("*",Id("base"),Id("a")))])
                    ),
                    Return(Id("base"))
                ])
            ),
            FuncDecl(
                Id("power_recur"),
                [VarDecl(Id("base"),[],None),
                VarDecl(Id("exp"),[],None)],([],[
                    If(
                        [(
                            BinaryOp("==",Id("exp"),IntLiteral(0)),
                            [],
                            [Return(IntLiteral(1))]
                        )],[]
                    ),
                    Return(BinaryOp("*",Id("base"),CallExpr(Id("power_recur"),[Id("base"),BinaryOp("-",Id("exp"),IntLiteral(1))])))
                ])
            ),
            FuncDecl(
                Id("main"),
                [VarDecl(Id("base"),[],None),
                VarDecl(Id("exp"),[],None)],([],[
                    Assign(Id("base"),CallExpr(Id("input"),[])),
                    Assign(Id("exp"),CallExpr(Id("input"),[])),
                    CallStmt(Id("writeln"),[CallExpr(Id("power_rep"),[Id("base"),Id("exp")])]),
                    CallStmt(Id("writeln"),[CallExpr(Id("power_recur"),[Id("base"),Id("exp")])])
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test40(self):
        input = r"""
        Function: main
            Body:
                Var: answer, length, jump_max, arr[10], a , j;
                For (i = 0, i < length, 1) Do
                    arr[i] = input();
                EndFor.
                For (j = 0, j < length, 1) Do
                    If (a + jump_max >= arr[i]) && (a + jump_max < arr[i + 1]) Then
                        a = arr[i];
                        answer = answer + 1;
                    EndIf.
                EndFor.
                If (j != length - 1) Then
                    answer = -1;
                EndIf.
                If (a + jump_max >= arr[length - 1]) Then
                    answer = answer + 1;
                Else answer = -1;
                EndIf.
	            writeln(answer);
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("main"),[],
                ([VarDecl(Id("answer"),[],None),
                VarDecl(Id("length"),[],None),
                VarDecl(Id("jump_max"),[],None),
                VarDecl(Id("arr"),[10],None),
                VarDecl(Id("a"),[],None),
                VarDecl(Id("j"),[],None)],[
                    For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),Id("length")),
                        IntLiteral(1),
                        ([],[Assign(ArrayCell(Id("arr"),[Id("i")]),CallExpr(Id("input"),[]))])
                    ),
                    For(
                        Id("j"),
                        IntLiteral(0),
                        BinaryOp("<",Id("j"),Id("length")),
                        IntLiteral(1),
                        ([],[
                            If(
                                [(
                                    BinaryOp("&&",BinaryOp(">=",BinaryOp("+",Id("a"),Id("jump_max")),ArrayCell(Id("arr"),[Id("i")])),BinaryOp("<",BinaryOp("+",Id("a"),Id("jump_max")),ArrayCell(Id("arr"),[BinaryOp("+",Id("i"),IntLiteral(1))]))),
                                    [],
                                    [Assign(Id("a"),ArrayCell(Id("arr"),[Id("i")])),
                                    Assign(Id("answer"),BinaryOp("+",Id("answer"),IntLiteral(1)))]
                                )],[]
                            )
                        ])
                    ),
                    If(
                        [(
                            BinaryOp("!=",Id("j"),BinaryOp("-",Id("length"),IntLiteral(1))),
                            [],
                            [Assign(Id("answer"),UnaryOp("-",IntLiteral(1)))]
                        )],[]
                    ),
                    If(
                        [(
                            BinaryOp(">=",BinaryOp("+",Id("a"),Id("jump_max")),ArrayCell(Id("arr"),[BinaryOp("-",Id("length"),IntLiteral(1))])),
                            [],
                            [Assign(Id("answer"),BinaryOp("+",Id("answer"),IntLiteral(1)))]
                        )],([],[Assign(Id("answer"),UnaryOp("-",IntLiteral(1)))])
                    ),
                    CallStmt(Id("writeln"),[Id("answer")])
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test41(self):
        input = r"""
        Function: longest_substr
            Parameter: str
            Body:
                Var: count = 0, check = False;
                For (i = 0, i < length(str), 1) Do
                    For (j = 0, j < length(str), 1) Do
                        If (str[i] == str[j]) && (i != j) Then
                            check = True;
                            Break;
                        EndIf.
                        If (check) Then
                            check = False;
                        EndIf.
                        Continue;
                    EndFor.
                    count = count + 1;
                EndFor.
                Return count;     
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("longest_substr"),
                [VarDecl(Id("str"),[],None)],
                (
                    [VarDecl(Id("count"),[],IntLiteral(0)),
                    VarDecl(Id("check"),[],BooleanLiteral(False))],
                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),CallExpr(Id("length"),[Id("str")])),
                        IntLiteral(1),
                        ([],
                        [For(
                            Id("j"),
                            IntLiteral(0),
                            BinaryOp("<",Id("j"),CallExpr(Id("length"),[Id("str")])),
                            IntLiteral(1),
                            ([],[
                            If(
                                [(
                                    BinaryOp("&&",BinaryOp("==",ArrayCell(Id("str"),[Id("i")]),ArrayCell(Id("str"),[Id("j")])),BinaryOp("!=",Id("i"),Id("j"))),
                                    [],
                                    [Assign(Id("check"),BooleanLiteral(True)),
                                    Break()]
                                )],[]
                            ),
                            If(
                                [(
                                    Id("check"),
                                    [],
                                    [Assign(Id("check"),BooleanLiteral(False))]
                                )],[]
                            ),
                            Continue()])
                        ),
                        Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))
                        ])
                    ),
                    Return(Id("count"))
                    ]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test42(self):
        input = r"""
        Function: foo
            Parameter: str
            Body:
                Var: count = 0, check = False;
                For (i = 0, i < length(str), 1) Do
                    If !str[i] Then
                        count = count + 1;
                        writeln(str[i]);
                    EndIf.
                EndFor.
                Return count;     
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("str"),[],None)],
                ([VarDecl(Id("count"),[],IntLiteral(0)),
                VarDecl(Id("check"),[],BooleanLiteral(False))],
                [For(
                    Id("i"),
                    IntLiteral(0),
                    BinaryOp("<",Id("i"),CallExpr(Id("length"),[Id("str")])),
                    IntLiteral(1),
                    ([],[If(
                        [(
                            UnaryOp("!",ArrayCell(Id("str"),[Id("i")])),
                            [],
                            [Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1))),
                            CallStmt(Id("writeln"),[ArrayCell(Id("str"),[Id("i")])])
                            ]
                        )],[]
                    )])
                ),
                Return(Id("count"))
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test43(self):
        input = r"""
        Function: uoc_chung_lon_nhat
            Parameter: a, b
            Body:
                If (a == b) Then
                    Return a;
                EndIf.
	            If (a > b) Then
		            a = a % b;
                EndIf.
	            If (a == 0) Then
                    Return b;
                EndIf.
	            Return uoc_chung_lon_nhat(b, a);
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("uoc_chung_lon_nhat"),
                [VarDecl(Id("a"),[],None),
                VarDecl(Id("b"),[],None)],
                ([],[
                    If(
                        [(
                            BinaryOp("==",Id("a"),Id("b")),
                            [],
                            [Return(Id("a"))]
                        )],[]
                    ),
                    If(
                        [(
                            BinaryOp(">",Id("a"),Id("b")),
                            [],
                            [Assign(Id("a"),BinaryOp("%",Id("a"),Id("b")))]
                        )],[]
                    ),
                    If(
                        [(
                            BinaryOp("==",Id("a"),IntLiteral(0)),
                            [],
                            [Return(Id("b"))]
                        )],[]
                    ),
                    Return(CallExpr(Id("uoc_chung_lon_nhat"),[Id("b"),Id("a")]))
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test44(self):
        input = r"""
        Function: square_num
            Parameter: x
            Body:
                If x == 1 Then
                    Return 1;
                Else 
                    Return sqrt(x + square_num(x - 1));
                EndIf.
            EndBody.
        Function: main
            Body:
                Var: x = 10;
                writeln(square_num(x));
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("square_num"),
                [VarDecl(Id("x"),[],None)],([],[
                    If(
                        [(
                            BinaryOp("==",Id("x"),IntLiteral(1)),
                            [],
                            [Return(IntLiteral(1))]
                        )],(
                            [],
                            [Return(CallExpr(Id("sqrt"),[BinaryOp("+",Id("x"),CallExpr(Id("square_num"),[BinaryOp("-",Id("x"),IntLiteral(1))]))]))]
                        )
                    )
                ])
            ),
            FuncDecl(
                Id("main"),[],(
                    [VarDecl(Id("x"),[],IntLiteral(10))],
                    [CallStmt(Id("writeln"),[CallExpr(Id("square_num"),[Id("x")])])]
                )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test45(self):
        input = r"""
        Function: reverseString
            Parameter: initialString
            Body:
                If (initialString == nullptr) Then
                    Return;
                EndIf.
                If (strlen(initialString) == 1) Then
                    writeln(initialString[0]);
                    Return;
                EndIf.
                writeln(initialString[strlen(initialString) - 1]);
                initialString[strlen(initialString) - 1] = 0;
                reverseString(initialString);
            EndBody."""
        expect = Program([
            FuncDecl(
                Id("reverseString"),
                [VarDecl(Id("initialString"),[],None)],([],[
                    If(
                        [(
                            BinaryOp("==",Id("initialString"),Id("nullptr")),
                            [],
                            [Return(None)]
                        )],[]
                    ),If(
                        [(
                            BinaryOp("==",CallExpr(Id("strlen"),[Id("initialString")]),IntLiteral(1)),
                            [],
                            [CallStmt(Id("writeln"),[ArrayCell(Id("initialString"),[IntLiteral(0)])]),
                            Return(None)]
                        )],[]
                    ),CallStmt(Id("writeln"),[ArrayCell(Id("initialString"),[BinaryOp("-",CallExpr(Id("strlen"),[Id("initialString")]),IntLiteral(1))])]),
                    Assign(ArrayCell(Id("initialString"),[BinaryOp("-",CallExpr(Id("strlen"),[Id("initialString")]),IntLiteral(1))]),IntLiteral(0)),
                    CallStmt(Id("reverseString"),[Id("initialString")])
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test46(self):
        input = r"""
        Function: reverseString
            Parameter: num
            Body:
                For (i = num * 2, i < num * num, i + 1) Do
                    If i % 2 == 0 Then
                        writeln(i);
                    EndIf.
                EndFor.
            EndBody."""
        expect = Program([
            FuncDecl(Id("reverseString"),
            [VarDecl(Id("num"),[],None)],([],[
                For(
                    Id("i"),
                    BinaryOp("*",Id("num"),IntLiteral(2)),
                    BinaryOp("<",Id("i"),BinaryOp("*",Id("num"),Id("num"))),
                    BinaryOp("+",Id("i"),IntLiteral("1")),
                    ([],
                    [If(
                        [(
                            BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),
                            [],
                            [CallStmt(Id("writeln"),[Id("i")])]
                        )],[]
                    )])
                )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test47(self):
        input = r"""
            Var: arr=1.e790,b,c=2;
            Var: x;
            Function: tEST_function_Name_1
                Parameter: x[100]
                Body:
                    Do 
                        x=x + foo(267+a[6]+. 1.0);
                        x=x%2;
                        If (i>=9) Then
                            writeln(a+7);
                        EndIf.
                    While i<=27 EndDo .
                EndBody."""
        expect = Program([
            VarDecl(Id("arr"),[],FloatLiteral(1e790)),
            VarDecl(Id("b"),[],None),
            VarDecl(Id("c"),[],IntLiteral(2)),
            VarDecl(Id("x"),[],None),
            FuncDecl(
                Id("tEST_function_Name_1"),
                [VarDecl(Id("x"),[100],None)],([],[
                    Dowhile(
                        ([],[
                            Assign(Id("x"),BinaryOp("+",Id("x"),CallExpr(Id("foo"),[BinaryOp("+.",BinaryOp("+",IntLiteral(267),ArrayCell(Id("a"),[IntLiteral(6)])),FloatLiteral(1.0))]))),
                            Assign(Id("x"),BinaryOp("%",Id("x"),IntLiteral(2))),
                            If(
                                [(
                                    BinaryOp(">=",Id("i"),IntLiteral(9)),
                                    [],
                                    [CallStmt(Id("writeln"),[BinaryOp("+",Id("a"),IntLiteral(7))])]
                                )],[]
                        )]),
                        BinaryOp("<=",Id("i"),IntLiteral(27))
                    )
                ])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test48(self):
        input = r"""
            Function: tEST_function_Name_2
                Parameter: x,a[69],b[1][2][3]
                Body:
                    For (i=1, goo(2+a[6]) < i,2>goo(9)) Do
                        If arr[7] >= foo(3) Then
                            Break;
                        EndIf.
                    EndFor.
                EndBody."""
        expect = Program(
            [FuncDecl(Id("tEST_function_Name_2"),
            [VarDecl(Id("x"),[],None),
            VarDecl(Id("a"),[69],None),
            VarDecl(Id("b"),[1,2,3],None)],([],[
                For(
                    Id("i"),
                    IntLiteral(1),
                    BinaryOp("<",CallExpr(Id("goo"),[BinaryOp("+",IntLiteral(2),ArrayCell(Id("a"),[IntLiteral(6)]))]),Id("i")),
                    BinaryOp(">",IntLiteral(2),CallExpr(Id("goo"),[IntLiteral(9)])),
                    ([],[
                        If(
                            [(
                                BinaryOp(">=",ArrayCell(Id("arr"),[IntLiteral(7)]),CallExpr(Id("foo"),[IntLiteral(3)])),
                                [],
                                [Break()]
                            )],[]
                        )
                    ])
                )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test49(self):
        input = r"""
            Function: reverseString
            Parameter: num
            Body:
                For (i = num * 2, i < num * num, i + 1) Do
                    Var: a = 1;
                    If i % 2 == 0 Then
                        writeln(a * i);
                    EndIf.
                EndFor.
            EndBody."""
        expect = Program([
            FuncDecl(Id("reverseString"),
            [VarDecl(Id("num"),[],None)],([],[
                For(
                    Id("i"),
                    BinaryOp("*",Id("num"),IntLiteral(2)),
                    BinaryOp("<",Id("i"),BinaryOp("*",Id("num"),Id("num"))),
                    BinaryOp("+",Id("i"),IntLiteral(1)),
                    ([VarDecl(Id("a"),[],IntLiteral(1))],
                    [If(
                        [(
                            BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),
                            [],
                            [CallStmt(Id("writeln"),[BinaryOp("*",Id("a"),Id("i"))])]
                        )],[]
                    )])
                )
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test50(self):
        input = r"""
            Function: main
            Body:
                Var: arr[10];
                For (i = 0, i < 10, 1) Do
                    For (j = i + 1, j < 10, 1) Do
                        If (arr[i] < arr[j]) Then
                            Var: temp;
                            temp = arr[i];
                            arr[i] = arr[j];
                            arr[j] = temp;
                        EndIf.
                    EndFor.
                EndFor.
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],(
                [VarDecl(Id("arr"),[10],None)],
                [For(
                    Id("i"),
                    IntLiteral(0),
                    BinaryOp("<",Id("i"),IntLiteral(10)),
                    IntLiteral(1),
                    ([],[
                        For(
                            Id("j"),
                            BinaryOp("+",Id("i"),IntLiteral(1)),
                            BinaryOp("<",Id("j"),IntLiteral(10)),
                            IntLiteral(1),
                            ([],[If(
                                [(
                                    BinaryOp("<",ArrayCell(Id("arr"),[Id("i")]),ArrayCell(Id("arr"),[Id("j")])),
                                    [VarDecl(Id("temp"),[],None)],
                                    [Assign(Id("temp"),ArrayCell(Id("arr"),[Id("i")])),
                                    Assign(ArrayCell(Id("arr"),[Id("i")]),ArrayCell(Id("arr"),[Id("j")])),
                                    Assign(ArrayCell(Id("arr"),[Id("j")]),Id("temp"))])],[]
                                )])
                        )]
                    )
                )]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test51(self):
        input = r"""
            Function: main
            Body:
                Var: i, n;
                Do
                    writeln("Input n: ");
                    input(n);
                    If (n <= 0) Then
                        writeln("Input again, N must be larger than 0");
                    EndIf.
                While (n <= 0) EndDo.
                i = 1;
                While (i <= n) Do
                    If (n % i == 0) Then
                        writeln(i);
                        i = i + 1;
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],(
                [VarDecl(Id("i"),[],None),
                VarDecl(Id("n"),[],None)],
                [Dowhile(
                    ([],[CallStmt(Id("writeln"),[StringLiteral("Input n: ")]),
                    CallStmt(Id("input"),[Id("n")]),
                    If(
                        [(
                            BinaryOp("<=",Id("n"),IntLiteral(0)),
                            [],
                            [CallStmt(Id("writeln"),[StringLiteral("Input again, N must be larger than 0")])]
                        )],[])]),
                    BinaryOp("<=",Id("n"),IntLiteral(0))),
                Assign(Id("i"),IntLiteral(1)),
                While(
                    BinaryOp("<=",Id("i"),Id("n")),([],[
                        If(
                            [(
                                BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),
                                [],
                                [CallStmt(Id("writeln"),[Id("i")]),
                                Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]
                            )],[]
                        )]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test52(self):
        input = r"""
            Function: main
            Body:
                For (i = 1, i <= 10, 1) Do
                    For (j = 2, j <= 9, 1) Do
                        writeln(i, j, i * j);
                    EndFor.
                EndFor.
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                For(
                    Id("i"),
                    IntLiteral(1),
                    BinaryOp("<=",Id("i"),
                    IntLiteral(10)),IntLiteral(1),
                    ([],[For(
                        Id("j"),
                        IntLiteral(2),
                        BinaryOp("<=",Id("j"),
                        IntLiteral(9)),
                        IntLiteral(1),
                        ([],[CallStmt(Id("writeln"),[Id("i"),Id("j"),BinaryOp("*",Id("i"),Id("j"))])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test53(self):
        input = """
            Function: prime_number
            Parameter: n
            Body:
                If (n < 2) Then
                    Return False;
                ElseIf (n > 2) Then
                    If (n % 2 == 0) Then
                        Return False;
                    EndIf.
                    For (i = 3, i <= sqrt(n), 2) Do
                        If (n % i == 0) Then
                            Return False;
                        EndIf.
                    EndFor.
                EndIf.
                Return True;
            EndBody.
            Function: main
            Body:
                Var: n;
                input(n);
                If prime_number(n) Then
                    writeln(n, "is prime number");
                Else
                    writeln(n, "is not prime number");
                EndIf.
            EndBody.
        """
        expect = Program([
            FuncDecl(
                Id("prime_number"),
                [VarDecl(Id("n"),[],None)],([],[
                    If(
                        [(
                            BinaryOp("<",Id("n"),IntLiteral(2)),
                            [],
                            [Return(BooleanLiteral(False))]
                        ),(
                            BinaryOp(">",Id("n"),IntLiteral(2)),
                            [],
                            [
                                If(
                                    [(
                                        BinaryOp("==",BinaryOp("%",Id("n"),IntLiteral(2)),IntLiteral(0)),
                                        [],
                                        [Return(BooleanLiteral(False))])],[]),
                                For(
                                    Id("i"),
                                    IntLiteral(3),
                                    BinaryOp("<=",Id("i"),CallExpr(Id("sqrt"),[Id("n")])),
                                    IntLiteral(2),
                                    ([],[
                                        If(
                                            [(
                                                BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),
                                                [],
                                                [Return(BooleanLiteral(False))]
                                            )],[]
                                        )
                                    ]))])],[]),
                    Return(BooleanLiteral(True))
                ])
            ),
            FuncDecl(Id("main"),[],([VarDecl(Id("n"),[],None)],[
                CallStmt(Id("input"),[Id("n")]),
                If(
                    [(
                        CallExpr(Id("prime_number"),[Id("n")]),
                        [],
                        [CallStmt(Id("writeln"),[Id("n"),StringLiteral("is prime number")])]
                    )],([],[CallStmt(Id("writeln"),[Id("n"),StringLiteral("is not prime number")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test54(self):
        input = """
            Function: main
            Body:
                Var: a[10], max;
                For (i = 0, i < 10, 1) Do
                    input(a[i]);
                EndFor.
                max = a[0];
                For (i = 0, i < 10, 1) Do
                    If max < a[i] Then
                        max = a[i];
                    EndIf.
                EndFor.
                writeln("Max number in array is: ", max);
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],(
                [VarDecl(Id("a"),[10],None),
                VarDecl(Id("max"),[],None)],
                [For(
                    Id("i"),
                    IntLiteral(0),
                    BinaryOp("<",Id("i"),IntLiteral(10)),
                    IntLiteral(1),
                    (
                        [],
                        [CallStmt(Id("input"),[ArrayCell(Id("a"),[Id("i")])])]
                    )),
                Assign(Id("max"),ArrayCell(Id("a"),[IntLiteral(0)])),
                For(
                    Id("i"),
                    IntLiteral(0),
                    BinaryOp("<",Id("i"),IntLiteral(10)),
                    IntLiteral(1),
                    ([],[
                        If(
                            [(
                                BinaryOp("<",Id("max"),ArrayCell(Id("a"),[Id("i")])),
                                [],
                                [Assign(Id("max"),ArrayCell(Id("a"),[Id("i")]))])],[])])),
                CallStmt(Id("writeln"),[StringLiteral("Max number in array is: "),Id("max")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test55_complex_exp_test(self):
        input = r"""
        Function: foo 
        Body: 
            a = 1 + 1.23 *. abc \. id[12];
            b = 1.E-12  =/= foo(123);
        EndBody."""
        expect = Program([
            FuncDecl(Id("foo"),[],([],[
                Assign(Id("a"),BinaryOp("+",IntLiteral(1),BinaryOp("\.",BinaryOp("*.",FloatLiteral(1.23),Id("abc")),ArrayCell(Id("id"),[IntLiteral(12)])))),
                Assign(Id("b"),BinaryOp("=/=",FloatLiteral(1e-12),CallExpr(Id("foo"),[IntLiteral(123)])))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test56_sign_operand(self):
        input = r"""
            Function: foo
            Body:
                a = -1;
                Return a * 190;
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("foo"),[],([],[
                Assign(Id("a"),UnaryOp("-",IntLiteral(1))),
                Return(BinaryOp("*",Id("a"),IntLiteral(190)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test57_logical(self):
        input = r"""
            Function: foo
            Body:
                a = !1;
                b = !True;
                Return a * 190;
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("foo"),[],([],[
                Assign(Id("a"),UnaryOp("!",IntLiteral(1))),
                Assign(Id("b"),UnaryOp("!",BooleanLiteral(True))),
                Return(BinaryOp("*",Id("a"),IntLiteral(190)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test58_operators(self):
        input = r"""
            Function: foo
            Body:
                a = a * 1;
                b = 12. * 3.e3;
                c = 0x123 \ 3;
                Return;
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("foo"),[],([],[
                Assign(Id("a"),BinaryOp("*",Id("a"),IntLiteral(1))),
                Assign(Id("b"),BinaryOp("*",FloatLiteral(12.0),FloatLiteral(3000.0))),
                Assign(Id("c"),BinaryOp("\\",IntLiteral(291),IntLiteral(3))),
                Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test59_relational(self):
        input = r"""
            Function: foo
            Body:
                If a =/= b Then
                    Return False;
                ElseIf a >=. b Then
                    Return True;
                ElseIf a <=. b Then
                    Return True;
                EndIf.
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("foo"),[],([],[
                If(
                    [(
                        BinaryOp("=/=",Id("a"),Id("b")),
                        [],
                        [Return(BooleanLiteral(False))]
                    ),(
                        BinaryOp(">=.",Id("a"),Id("b")),
                        [],
                        [Return(BooleanLiteral(True))]
                    ),(
                        BinaryOp("<=.",Id("a"),Id("b")),
                        [],
                        [Return(BooleanLiteral(True))]
                    )],[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    def test60_relational(self):
        input = r"""
            Function: foo
            Body:
                If (a == b) && (a != c) || (a > b) || (a < c)   Then
                    Return True;
                EndIf.
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("foo"),[],([],[
                If(
                    [(
                        BinaryOp("||",BinaryOp("||",BinaryOp("&&",BinaryOp("==",Id("a"),Id("b")),BinaryOp("!=",Id("a"),Id("c"))),BinaryOp(">",Id("a"),Id("b"))),BinaryOp("<",Id("a"),Id("c"))),
                        [],
                        [Return(BooleanLiteral(True))]
                    )],[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test61_relational(self):
        input = r"""
            Function: foo
            Body:
                If (a >. b) && (a <. b) || (a <= d) && (a >= e)  Then
                    Return True;
                EndIf.
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("foo"),[],([],[
                If(
                    [(
                        BinaryOp("&&",BinaryOp("||",BinaryOp("&&",BinaryOp(">.",Id("a"),Id("b")),BinaryOp("<.",Id("a"),Id("b"))),BinaryOp("<=",Id("a"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))),
                        [],
                        [Return(BooleanLiteral(True))])],[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test62_coercions(self):
        input = r"""
            Function: foo
            Body:
                Var: s = "123";
                n = int(s);
                Return n * 10;
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("foo"),[],([VarDecl(Id("s"),[],StringLiteral("123"))],[
                Assign(Id("n"),CallExpr(Id("int"),[Id("s")])),
                Return(BinaryOp("*",Id("n"),IntLiteral(10)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test63(self):
        input = r"""
            Function: test
            Parameter: num
            Body:
                Var: sum = 0;
                For (i = num, i < sqr(num), 2) Do
                    sum = a[1][1][1][1][1][1][1][i];
                EndFor.
                Return sum;
            EndBody."""
        expect = Program([
            FuncDecl(Id("test"),[VarDecl(Id("num"),[],None)],(
                [VarDecl(Id("sum"),[],IntLiteral(0))],[
                    For(
                        Id("i"),
                        Id("num"),
                        BinaryOp("<",Id("i"),CallExpr(Id("sqr"),[Id("num")])),
                        IntLiteral(2),
                        ([],[Assign(Id("sum"),ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(1),IntLiteral(1),IntLiteral(1),IntLiteral(1),IntLiteral(1),IntLiteral(1),Id("i")]))]
                        )),
                    Return(Id("sum"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test64_coercions(self):
        input = r"""
            Var: string[3] = {"1.23", "0.e4", "12e2"};
            Function: test
            Body:
                Var: x[3], sum = 0.;
                For (i = 0, i < 3, 1) Do
                    x[i] = float(string[i]);
                    sum = sum + x[i];
                EndFor.
                Return sum;
            EndBody.
        """
        expect = Program([
            VarDecl(Id("string"),[3],ArrayLiteral([StringLiteral("1.23"),StringLiteral("0.e4"),StringLiteral("12e2")])),
            FuncDecl(Id("test"),[],([VarDecl(Id("x"),[3],None),
            VarDecl(Id("sum"),[],FloatLiteral(0.0))],[
                For(
                    Id("i"),
                    IntLiteral(0),
                    BinaryOp("<",Id("i"),IntLiteral(3)),
                    IntLiteral(1),
                    ([],[Assign(ArrayCell(Id("x"),[Id("i")]),CallExpr(Id("float"),[ArrayCell(Id("string"),[Id("i")])])),
                    Assign(Id("sum"),BinaryOp("+",Id("sum"),ArrayCell(Id("x"),[Id("i")])))])),
                Return(Id("sum"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test65_var_declaration(self):
        input = r"""
            Function: square
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                Return v;
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("square"),[],([
                VarDecl(Id("r"),[],FloatLiteral(10.0)),
                VarDecl(Id("v"),[],None)],[
                    Assign(Id("v"),BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("\\.",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id("r")),Id("r")),Id("r"))),
                    Return(Id("v"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test66_a_operator_p(self):
        input = r"""
            Var: a, b, operator;
            Function: main
            Body:  
                input(a);
                input(b);
                input(operator);
                If operator == "+" Then
                    Return a + b;
                ElseIf operator == "-" Then
                    Return a - b;
                ElseIf operator == "*" Then
                    Return a * b;
                Else
                    Return a \ b;
                EndIf.
            EndBody.
        """
        expect = Program([
            VarDecl(Id("a"),[],None),
            VarDecl(Id("b"),[],None),
            VarDecl(Id("operator"),[],None),
            FuncDecl(Id("main"),[],([],[
                CallStmt(Id("input"),[Id("a")]),
                CallStmt(Id("input"),[Id("b")]),
                CallStmt(Id("input"),[Id("operator")]),
                If(
                    [(
                        BinaryOp("==",Id("operator"),StringLiteral("+")),
                        [],
                        [Return(BinaryOp("+",Id("a"),Id("b")))]
                    ),(
                        BinaryOp("==",Id("operator"),StringLiteral("-")),
                        [],
                        [Return(BinaryOp("-",Id("a"),Id("b")))]
                    ),(
                        BinaryOp("==",Id("operator"),StringLiteral("*")),
                        [],
                        [Return(BinaryOp("*",Id("a"),Id("b")))]
                    )],([],[Return(BinaryOp("\\",Id("a"),Id("b")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    def test67(self):
        input = r"""
            Var: arr[3][2] = {{1, 2}, {4, 5}, {3, 5}};
            Function: main
            Body:
                Var: p = 1;
                For (i = 0, i < 3, 1) Do
                    For (j = 0, j < 2, 1) Do
                        p = p * arr[i][j];
                    EndFor.
                EndFor.
                writeln(p);
            EndBody.
        """
        expect = Program([
            VarDecl(Id("arr"),[3,2],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(4),IntLiteral(5)]),ArrayLiteral([IntLiteral(3),IntLiteral(5)])])),
            FuncDecl(Id("main"),[],([VarDecl(Id("p"),[],IntLiteral(1))],[
                For(
                    Id("i"),
                    IntLiteral(0),
                    BinaryOp("<",Id("i"),IntLiteral(3)),
                    IntLiteral(1),
                    ([],[
                        For(
                            Id("j"),
                            IntLiteral(0),
                            BinaryOp("<",Id("j"),IntLiteral(2)),
                            IntLiteral(1),
                            ([],[Assign(Id("p"),BinaryOp("*",Id("p"),ArrayCell(Id("arr"),[Id("i"),Id("j")])))]))])),
                CallStmt(Id("writeln"),[Id("p")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    def test68_no_stmt_in_body(self):
        input = r"""
            Function: main
            Body:
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test69_coercions(self):
        input = r"""
            Function: main
            Body:
                Var: s = "this is a string containing tab \t", a = "0XFA1B23";
                s = s + string(a);
                writeln(s);
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([VarDecl(Id("s"),[],StringLiteral("this is a string containing tab \\t")),
            VarDecl(Id("a"),[],StringLiteral("0XFA1B23"))],
            [Assign(Id("s"),BinaryOp("+",Id("s"),CallExpr(Id("string"),[Id("a")]))),
            CallStmt(Id("writeln"),[Id("s")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test70_sign_operand(self):
        input = r"""
            Function: main
            Body:
                Var: a = 0XFA1B23;
                Var: b = 1;
                a = a *- b;
                a = a*.-b;
                writeln(a);
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([
                VarDecl(Id("a"),[],IntLiteral(16390947)),
                VarDecl(Id("b"),[],IntLiteral(1))],
                [Assign(Id("a"),BinaryOp("*",Id("a"),UnaryOp("-",Id("b")))),
                Assign(Id("a"),BinaryOp("*.",Id("a"),UnaryOp("-",Id("b")))),
                CallStmt(Id("writeln"),[Id("a")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test71(self):
        input = r"""
            Function: abc
            Body:
                a = !((!b && c) + 1) || check(d);
                Return a;
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("abc"),[],([],[
                Assign(Id("a"),BinaryOp("||",UnaryOp("!",BinaryOp("+",BinaryOp("&&",UnaryOp("!",Id("b")),Id("c")),IntLiteral(1))),CallExpr(Id("check"),[Id("d")]))),
                Return(Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test72_mul_and_add(self):
        input = r"""
            Function: main
            Body:
                Var: a, b = 5;
                input(a);
                If !(a + b * 10) Then
                    Return True;
                Else
                    Return False;
                EndIf.
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([
                VarDecl(Id("a"),[],None),
                VarDecl(Id("b"),[],IntLiteral(5))],[
                    CallStmt(Id("input"),[Id("a")]),
                    If(
                        [(
                            UnaryOp("!",BinaryOp("+",Id("a"),BinaryOp("*",Id("b"),IntLiteral(10)))),
                            [],
                            [Return(BooleanLiteral(True))]
                        )],([],[Return(BooleanLiteral(False))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    def test73_function_call(self):
        input = r"""
            Function: main
            Body:
                Return a(b(c(d(e(f(1123 + True + fo(z(f(f)))))))));
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                Return(CallExpr(Id("a"),[CallExpr(Id("b"),[CallExpr(Id("c"),[CallExpr(Id("d"),[CallExpr(Id("e"),[CallExpr(Id("f"),[BinaryOp("+",BinaryOp("+",IntLiteral(1123),BooleanLiteral(True)),CallExpr(Id("fo"),[CallExpr(Id("z"),[CallExpr(Id("f"),[Id("f")])])]))])])])])])]))]))
            ])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    def test74_coercion_float(self):
        input = r"""
            Function: main
            Body:
                Var: a___b = 12345;
                Var: b = True, c = 123.;
                If b Then
                    c = c +. 1.;
                ElseIf !b Then
                    Return c;
                EndIf.
                Return float(a___b) + c;
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([
            VarDecl(Id("a___b"),[],IntLiteral(12345)),
            VarDecl(Id("b"),[],BooleanLiteral(True)),
            VarDecl(Id("c"),[],FloatLiteral(123.0))],[
                If(
                    [(
                        Id("b"),
                        [],
                        [Assign(Id("c"),BinaryOp("+.",Id("c"),FloatLiteral(1.0)))]
                    ),(
                        UnaryOp("!",Id("b")),
                        [],
                        [Return(Id("c"))]
                    )],[]),
                    Return(BinaryOp("+",CallExpr(Id("float"),[Id("a___b")]),Id("c")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    def test75(self):
        input = r"""
            Var: a = "Hoang Gia Khang";
            Function: check
            Parameter: b
            Body:
                If (a == b) Then
                    Return True;
                EndIf.
                Return False;
            EndBody.
            Function: main
            Body:
                Var: s, k, result;
                input(s);
                input(k);
                result = string(s) + string(k);
                If check(result) Then
                    writeln(result);
                Else
                    writeln("Nothing");
                EndIf.
            EndBody.
        """
        expect = Program([
            VarDecl(Id("a"),[],StringLiteral("Hoang Gia Khang")),
            FuncDecl(Id("check"),[VarDecl(Id("b"),[],None)],([],[
                If(
                    [(
                        BinaryOp("==",Id("a"),Id("b")),
                        [],
                        [Return(BooleanLiteral(True))])],[]),
                Return(BooleanLiteral(False))])),
            FuncDecl(Id("main"),[],([
                VarDecl(Id("s"),[],None),
                VarDecl(Id("k"),[],None),
                VarDecl(Id("result"),[],None)],[
                    CallStmt(Id("input"),[Id("s")]),
                    CallStmt(Id("input"),[Id("k")]),
                    Assign(Id("result"),BinaryOp("+",CallExpr(Id("string"),[Id("s")]),
                    CallExpr(Id("string"),[Id("k")]))),
                    If(
                        [(
                            CallExpr(Id("check"),[Id("result")]),
                            [],
                            [CallStmt(Id("writeln"),[Id("result")])]
                        )],([],[CallStmt(Id("writeln"),[StringLiteral("Nothing")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    def test76_assign_stmt(self):
        input = """
            Function: main
            Body:
                Var: a, b;
                input(a, b);
                c = a == b;
                d = c+-1.23*.-3e4;
                writeln(d);
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([
                VarDecl(Id("a"),[],None),
                VarDecl(Id("b"),[],None)],[
                    CallStmt(Id("input"),[Id("a"),Id("b")]),
                    Assign(Id("c"),BinaryOp("==",Id("a"),Id("b"))),
                    Assign(Id("d"),BinaryOp("+",Id("c"),BinaryOp("*.",UnaryOp("-",FloatLiteral(1.23)),UnaryOp("-",FloatLiteral(30000.0))))),
                    CallStmt(Id("writeln"),[Id("d")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test77_call_stmt(self):
        input = r"""
            Function: main
            Body:
                foo(3 +x[i] * y(3,z(4)));
                If !foo Then
                    Return False;
                EndIf.
                For (i = 0, i < 100, 2) Do
                    writeln(sqrt(i) * test[3][foo(4)]);
                EndFor.
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                CallStmt(Id("foo"),[BinaryOp("+",IntLiteral(3),BinaryOp("*",ArrayCell(Id("x"),[Id("i")]),CallExpr(Id("y"),[IntLiteral(3),CallExpr(Id("z"),[IntLiteral(4)])])))]),
                If(
                    [(
                        UnaryOp("!",Id("foo")),
                        [],
                        [Return(BooleanLiteral(False))]
                    )],[]),
                For(
                    Id("i"),
                    IntLiteral(0),
                    BinaryOp("<",Id("i"),IntLiteral(100)),
                    IntLiteral(2),
                    ([],[CallStmt(Id("writeln"),[BinaryOp("*",CallExpr(Id("sqrt"),[Id("i")]),ArrayCell(Id("test"),[IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(4)])]))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test78_all(self):
        input = r"""
            Function: prime_number
            Parameter: n
            Body:
                If n < 2 Then
                    Return False;
                EndIf.
                If (n == 2) || (n == 3) Then
                    Return True;
                EndIf.
                For (i = 2, i < n, 1) Do
                    If n % i == 0 Then
                        Return False;
                    EndIf.
                EndFor.
                Return True;
            EndBody.
            Function: main
            Body:
                Var: a[100];
                For (i = 0, i < 100, 1) Do
                    input(a[i]);
                    If prime_number(a[i]) && (a[i] % 2 != 0) Then
                        writeln(a[i]);
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("prime_number"),[VarDecl(Id("n"),[],None)],([],[
                If(
                    [(
                        BinaryOp("<",Id("n"),IntLiteral(2)),
                        [],
                        [Return(BooleanLiteral(False))]
                    )],[]),
                If(
                    [(
                        BinaryOp("||",BinaryOp("==",Id("n"),IntLiteral(2)),BinaryOp("==",Id("n"),IntLiteral(3))),
                        [],
                        [Return(BooleanLiteral(True))]
                    )],[]),
                For(
                    Id("i"),
                    IntLiteral(2),
                    BinaryOp("<",Id("i"),Id("n")),
                    IntLiteral(1),
                    ([],[
                        If(
                            [(
                                BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),
                                [],
                                [Return(BooleanLiteral(False))]
                            )],[])])),
                Return(BooleanLiteral(True))])),
            FuncDecl(Id("main"),[],([VarDecl(Id("a"),[100],None)],[
                For(
                    Id("i"),
                    IntLiteral(0),
                    BinaryOp("<",Id("i"),IntLiteral(100)),
                    IntLiteral(1),
                    ([],[CallStmt(Id("input"),[ArrayCell(Id("a"),[Id("i")])]),
                    If(
                        [(
                            BinaryOp("&&",CallExpr(Id("prime_number"),[ArrayCell(Id("a"),[Id("i")])]),BinaryOp("!=",BinaryOp("%",ArrayCell(Id("a"),[Id("i")]),IntLiteral(2)),IntLiteral(0))),
                            [],
                            [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")])])]
                        )],[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test79_all(self):
        input = r"""
            Var: a = 5;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: c, d = 6, e, f;
            Var: m, n[10];
            Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
            EndBody.
            Function: main
            Body:
            ** This is a single-line comment. **
            ** This is a
            * multi-line
            * comment.
            **
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                If bool_of_string ("True") Then
                    a = int_of_string (read ());
                    b = float_of_int (a) +. 2.0;
                EndIf.
                For (i = 0, i < 10, 2) Do
                    writeln(i);
                EndFor.
                x = 10;
                fact (x);
            EndBody.
        """
        expect = Program([
            VarDecl(Id("a"),[],IntLiteral(5)),
            VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),
            VarDecl(Id("c"),[],None),
            VarDecl(Id("d"),[],IntLiteral(6)),
            VarDecl(Id("e"),[],None),
            VarDecl(Id("f"),[],None),
            VarDecl(Id("m"),[],None),
            VarDecl(Id("n"),[10],None),
            FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[
                If(
                    [(
                        BinaryOp("==",Id("n"),IntLiteral(0)),
                        [],
                        [Return(IntLiteral(1))]
                    )],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))
            ])),
            FuncDecl(Id("main"),[],([
                VarDecl(Id("r"),[],FloatLiteral(10.0)),
                VarDecl(Id("v"),[],None)],[
                    Assign(Id("v"),BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("\.",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id("r")),Id("r")),Id("r"))),
                    If(
                        [(
                            CallExpr(Id("bool_of_string"),[StringLiteral("True")]),
                            [],
                            [Assign(Id("a"),
                            CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),
                            Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))])],
                            []),
                    For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        IntLiteral(2),
                        ([],[CallStmt(Id("writeln"),[Id("i")])])),
                    Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test80_var(self):
        input = """
            Var: a[0x1][0x2][0x3][0x4][0x5][0x6][0x7][0x8][0x9];
            Var: b[0xA][0xB][0xC][0xD][0xE][0xF];
            Var: c[0x10000000], d[0XABCDEF];
            Var: e[0x1234], f[0X8765];
        """
        expect = Program([
            VarDecl(Id("a"),[1,2,3,4,5,6,7,8,9],None),
            VarDecl(Id("b"),[10,11,12,13,14,15],None),
            VarDecl(Id("c"),[268435456],None),
            VarDecl(Id("d"),[11259375],None),
            VarDecl(Id("e"),[4660],None),
            VarDecl(Id("f"),[34661],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test81_var(self):
        input = r"""
            Var: a = 1;
            Var: a[1] = {1};
            Var: a[1][2] = {{1}, {2}};
            """
        expect = Program([
            VarDecl(Id("a"),[],IntLiteral(1)),
            VarDecl(Id("a"),[1],ArrayLiteral([IntLiteral(1)])),
            VarDecl(Id("a"),[1,2],ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
    def test82(self):
        input = r"""
            Function: main
            Body:
                Var: sum = 0, a = 1;
                While a < 10 Do
                    Var: b = 1, prod = 1;
                    While b < 10 Do
                        prod = prod * b;
                        b = b + 1;
                    EndWhile.
                    sum = sum + prod;
                    a = a + 1;
                EndWhile.
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([
                VarDecl(Id("sum"),[],IntLiteral(0)),
                VarDecl(Id("a"),[],IntLiteral(1))],[
                    While(
                        BinaryOp("<",Id("a"),IntLiteral(10)),
                        ([VarDecl(Id("b"),[],IntLiteral(1)),
                        VarDecl(Id("prod"),[],IntLiteral(1))],
                        [While(
                            BinaryOp("<",Id("b"),IntLiteral(10)),
                            ([],[Assign(Id("prod"),BinaryOp("*",Id("prod"),Id("b"))),
                            Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))])),
                        Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("prod"))),
                        Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test83(self):
        input = r"""
            Var: a, b = "abc";
            Var: c = 1.;
            Function: main
                Body:
                    While a Do
                        Var: a = True, b;
                        Var: c = {{{1}}};
                        Do
                            Var: a, b;
                            Var: c = {{1}, {2}};
                            For (i = 10, i < 10, --i)
                            Do
                                Var: a = 0, b;
                                Var: c;
                                If c Then
                                    Var: a, b;
                                    Var: c;
                                    foo();
                                ElseIf d Then
                                    Var: a, b;
                                    Var: c;
                                    a = foo()[foo(foo())];
                                Else
                                    Var: a, b;
                                    Var: c;
                                    While abcd Do
                                        Var: a, b = 2;
                                        Var: a[1][2] = {1, 2};
                                        Break;
                                    EndWhile.
                                    Return;
                                EndIf.
                            EndFor.
                            Continue;
                        While b
                        EndDo.
                        Return 1;
                    EndWhile.
                    Return 0;
                EndBody.
            """
        expect = Program([
            VarDecl(Id("a"),[],None),
            VarDecl(Id("b"),[],StringLiteral("abc")),
            VarDecl(Id("c"),[],FloatLiteral(1.0)),
            FuncDecl(
                Id("main"),[],([],[
                    While(
                        Id("a"),
                        ([
                            VarDecl(Id("a"),[],BooleanLiteral(True)),
                            VarDecl(Id("b"),[],None),
                            VarDecl(Id("c"),[],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])]))
                        ],[
                            Dowhile(
                                ([
                                    VarDecl(Id("a"),[],None),
                                    VarDecl(Id("b"),[],None),
                                    VarDecl(Id("c"),[],ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([IntLiteral(2)])]))
                                ],[
                                    For(
                                        Id("i"),
                                        IntLiteral(10),
                                        BinaryOp("<",Id("i"),IntLiteral(10)),
                                        UnaryOp("-",UnaryOp("-",Id("i"))),
                                        ([
                                            VarDecl(Id("a"),[],IntLiteral(0)),
                                            VarDecl(Id("b"),[],None),
                                            VarDecl(Id("c"),[],None)
                                        ],[
                                            If(
                                                [(
                                                    Id("c"),
                                                    [
                                                        VarDecl(Id("a"),[],None),
                                                        VarDecl(Id("b"),[],None),
                                                        VarDecl(Id("c"),[],None)
                                                    ],
                                                    [
                                                        CallStmt(Id("foo"),[])
                                                    ]
                                                ),(
                                                    Id("d"),
                                                    [
                                                        VarDecl(Id("a"),[],None),
                                                        VarDecl(Id("b"),[],None),
                                                        VarDecl(Id("c"),[],None)
                                                    ],[
                                                        Assign(Id("a"),ArrayCell(CallExpr(Id("foo"),[]),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[])])]))
                                                    ]
                                                )],([
                                                    VarDecl(Id("a"),[],None),
                                                    VarDecl(Id("b"),[],None),
                                                    VarDecl(Id("c"),[],None)
                                                ],[
                                                    While(
                                                        Id("abcd"),
                                                        ([
                                                            VarDecl(Id("a"),[],None),
                                                            VarDecl(Id("b"),[],IntLiteral(2)),
                                                            VarDecl(Id("a"),[1,2],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))
                                                        ],[
                                                            Break()
                                                        ])
                                                    ),
                                                    Return(None)
                                                ])
                                            )
                                        ])),
                                    Continue()
                                ]),Id("b")),
                            Return(IntLiteral(1))
                        ])),
                    Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test84(self):
        input = r"""
            Function: main
                Body:
                    a = !a[1] > b || c + foo() * -e[2][abcd] % foo(1)[1] \ True;
                EndBody.
            """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                Assign(Id("a"),BinaryOp(">",UnaryOp("!",ArrayCell(Id("a"),[IntLiteral(1)])),BinaryOp("||",Id("b"),BinaryOp("+",Id("c"),BinaryOp("\\",BinaryOp("%",BinaryOp("*",CallExpr(Id("foo"),[]),UnaryOp("-",ArrayCell(Id("e"),[IntLiteral(2),Id("abcd")]))),ArrayCell(CallExpr(Id("foo"),[IntLiteral(1)]),[IntLiteral(1)])),BooleanLiteral(True))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    def test85(self):
        input = r"""
            Function: main
                Body:
                    a = 1 * 2 * 3;
                    a = 1 *. 2 *. 3;
                    a = 1 \ 2 \ 3;
                    a = 1 \. 2 \. 3;
                    a = 1 % 2 % 3;
                    a = 1 + 2 + 3;
                    a = 1 +. 2 +. 3;
                    a = 1 - 2 - 3;
                    a = 1 -. 2 -. 3;
                    a = 1 && 2 && 3;
                    a = 1 || 2 || 3;
                    a = !!1;
                    a = --1;
                    a = -.-.1;
                EndBody.
            """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                Assign(Id("a"),BinaryOp("*",BinaryOp("*",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),
                Assign(Id("a"),BinaryOp("*.",BinaryOp("*.",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),
                Assign(Id("a"),BinaryOp("\\",BinaryOp("\\",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),
                Assign(Id("a"),BinaryOp("\\.",BinaryOp("\\.",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),
                Assign(Id("a"),BinaryOp("%",BinaryOp("%",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),
                Assign(Id("a"),BinaryOp("+",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),
                Assign(Id("a"),BinaryOp("+.",BinaryOp("+.",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),
                Assign(Id("a"),BinaryOp("-",BinaryOp("-",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),
                Assign(Id("a"),BinaryOp("-.",BinaryOp("-.",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),
                Assign(Id("a"),BinaryOp("&&",BinaryOp("&&",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),
                Assign(Id("a"),BinaryOp("||",BinaryOp("||",IntLiteral(1),IntLiteral(2)),IntLiteral(3))),
                Assign(Id("a"),UnaryOp("!",UnaryOp("!",IntLiteral(1)))),
                Assign(Id("a"),UnaryOp("-",UnaryOp("-",IntLiteral(1)))),
                Assign(Id("a"),UnaryOp("-.",UnaryOp("-.",IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    def test86(self):
        input = r"""
            Function: main
                Body:
                    a = foo()[1];
                    a = foo()[-1];
                    a = foo(1, True, 1., "abcd")[a][b][c];
                EndBody.
            """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                Assign(Id("a"),ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(1)])),
                Assign(Id("a"),ArrayCell(CallExpr(Id("foo"),[]),[UnaryOp("-",IntLiteral(1))])),
                Assign(Id("a"),ArrayCell(CallExpr(Id("foo"),[IntLiteral(1),BooleanLiteral(True),FloatLiteral(1.0),StringLiteral("abcd")]),[Id("a"),Id("b"),Id("c")]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
    def test87(self):
        input = """
        Function: main
            Body:
                a = "abcdef";
                b = "Hello World";
                c = "123: '\" def '\"";
                d = "\\t\\b\\n\\'";
            EndBody."""
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                Assign(Id("a"),StringLiteral("abcdef")),
                Assign(Id("b"),StringLiteral("Hello World")),
                Assign(Id("c"),StringLiteral("123: '\" def '\"")),
                Assign(Id("d"),StringLiteral("\\t\\b\\n\\'"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
    def test88(self):
        input = r"""
            Function: main
                Body:
                    a = 1e+1 + 1.1e+1 + 1.e+1 + 1E+1 + 1.1E+1 + 1.E+1;
                EndBody.
            """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",FloatLiteral(10.0),FloatLiteral(11.0)),FloatLiteral(10.0)),FloatLiteral(10.0)),FloatLiteral(11.0)),FloatLiteral(10.0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    def test89(self):
        input = r"""
            Function: main
                Body:
                    foo()[1] = 1;
                    foo()[-1] = 1;
                    foo(abc, 123)[foo()] = 1;
                    foo(foo())[1] = 1;
                    foo(True, "abc")[a][b][c] = 1;
                EndBody.
            """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                Assign(ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(1)]),IntLiteral(1)),
                Assign(ArrayCell(CallExpr(Id("foo"),[]),[UnaryOp("-",IntLiteral(1))]),IntLiteral(1)),
                Assign(ArrayCell(CallExpr(Id("foo"),[Id("abc"),IntLiteral(123)]),[CallExpr(Id("foo"),[])]),IntLiteral(1)),
                Assign(ArrayCell(CallExpr(Id("foo"),[CallExpr(Id("foo"),[])]),[IntLiteral(1)]),IntLiteral(1)),
                Assign(ArrayCell(CallExpr(Id("foo"),[BooleanLiteral(True),StringLiteral("abc")]),[Id("a"),Id("b"),Id("c")]),IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    def test90(self):
        input = r"""
            Function: main
                Body:
                    If True Then
                    ElseIf True Then
                    ElseIf True Then
                    ElseIf True Then
                    ElseIf True Then
                    ElseIf True Then
                    EndIf.
                EndBody.
            """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                If(
                    [
                        (BooleanLiteral(True),[],[]),
                        (BooleanLiteral(True),[],[]),
                        (BooleanLiteral(True),[],[]),
                        (BooleanLiteral(True),[],[]),
                        (BooleanLiteral(True),[],[]),
                        (BooleanLiteral(True),[],[])
                    ],[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    def test91(self):
        input = r"""
            Function: main
                Body:
                    If a Then
                        Var: a, b;
                        foo1();
                        foo2();
                        a = False;
                        b = True;
                    EndIf.
                EndBody.
            """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                If(
                    [
                        (Id("a"),
                        [VarDecl(Id("a"),[],None),
                        VarDecl(Id("b"),[],None)],
                        [CallStmt(Id("foo1"),[]),
                        CallStmt(Id("foo2"),[]),
                        Assign(Id("a"),BooleanLiteral(False)),
                        Assign(Id("b"),BooleanLiteral(True))])
                    ],[]
        )]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    def test92(self):
        input = """
            Var: a[2][2] = {{0, 0E123}, {0XFFF, 0x12FA}};
            Var: b, c = "nothing";
            Function: main
            Parameter: x
            Body:
                For (i = 0, i < 10, i + 1) Do
                    For (j = i, j < 10, j + 1) Do
                        x = x + a[i][j];
                        writeln(b, c, x);
                    EndFor.
                EndFor.
                Return x;
            EndBody.
        """
        expect = Program([
            VarDecl(Id("a"),[2,2],ArrayLiteral([ArrayLiteral([IntLiteral(0),FloatLiteral(0.0)]),ArrayLiteral([IntLiteral(4095),IntLiteral(4858)])])),
            VarDecl(Id("b"),[],None),
            VarDecl(Id("c"),[],StringLiteral("nothing")),
            FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[
                For(
                    Id("i"),
                    IntLiteral(0),
                    BinaryOp("<",Id("i"),IntLiteral(10)),
                    BinaryOp("+",Id("i"),IntLiteral(1)),
                    ([],[For(
                        Id("j"),
                        Id("i"),
                        BinaryOp("<",Id("j"),IntLiteral(10)),
                        BinaryOp("+",Id("j"),IntLiteral(1)),
                        ([],[
                            Assign(Id("x"),BinaryOp("+",Id("x"),ArrayCell(Id("a"),[Id("i"),Id("j")]))),
                            CallStmt(Id("writeln"),[Id("b"),Id("c"),Id("x")])]))])),
                Return(Id("x"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    def test93(self):
        input = """
            Var: a[2] = {"Hoang", "Gia"};
            Function: main
            Parameter: x
            Body:
                input(x);
                If int(x) == 0 Then
                    writeln(a[int(x)]);
                ElseIf int(x) == 1 Then
                    writeln(a[int(x)] + "Khang");
                Else
                    writeln(a[0] + a[1] + "Khang");
                EndIf.
                Return 0;
            EndBody.
        """
        expect = Program([
            VarDecl(Id("a"),[2],ArrayLiteral([StringLiteral("Hoang"),StringLiteral("Gia")])),
            FuncDecl(Id("main"),[VarDecl(Id("x"),[],None)],([],[
                CallStmt(Id("input"),[Id("x")]),
                If(
                    [(
                        BinaryOp("==",CallExpr(Id("int"),[Id("x")]),IntLiteral(0)),
                        [],
                        [CallStmt(Id("writeln"),[ArrayCell(Id("a"),[CallExpr(Id("int"),[Id("x")])])])]
                    ),(
                        BinaryOp("==",CallExpr(Id("int"),[Id("x")]),IntLiteral(1)),
                        [],
                        [CallStmt(Id("writeln"),[BinaryOp("+",ArrayCell(Id("a"),[CallExpr(Id("int"),[Id("x")])]),StringLiteral("Khang"))])]
                    )],([],[
                        CallStmt(Id("writeln"),[BinaryOp("+",BinaryOp("+",ArrayCell(Id("a"),[IntLiteral(0)]),ArrayCell(Id("a"),[IntLiteral(1)])),StringLiteral("Khang"))])])),
                Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    def test94(self):
        input = """
        Function: main
        Body:
            y = 5 +. 4 +. 1;
            y = 1.1 +. 3 -. 1.2 *. 8.0 \\. 9.23;
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([],[
                Assign(Id("y"),BinaryOp("+.",BinaryOp("+.",IntLiteral(5),IntLiteral(4)),IntLiteral(1))),
                Assign(Id("y"),BinaryOp("-.",BinaryOp("+.",FloatLiteral("1.1"),IntLiteral(3)),BinaryOp("\.",BinaryOp("*.",FloatLiteral("1.2"),FloatLiteral("8.0")),FloatLiteral("9.23"))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    def test95(self):
        input = """
            Function: printArray
            Body:
                Var: i;
                For (i=0, i < size, i+.1.0e0) Do
                    printf("%d ", arr[i]);
                EndFor.
                printf("n");
            EndBody.
 
            Function: main
            Body:
                arr[5] = {64, 25, 12, 22, 11};
                n = sizeof(arr)\sizeof(arr[0]);
                selectionSort(arr, n);
                printf("Sorted array: n");
                printArray(arr, n);
                Return 0;
            EndBody.
        """
        expect = Program([
            FuncDecl(Id("printArray"),[],([
                VarDecl(Id("i"),[],None)],[
                    For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),Id("size")),
                        BinaryOp("+.",Id("i"),FloatLiteral(1.0)),
                        ([],[
                            CallStmt(Id("printf"),[StringLiteral("%d "),ArrayCell(Id("arr"),[Id("i")])])
                        ])),
                    CallStmt(Id("printf"),[StringLiteral("n")])])),
            FuncDecl(Id("main"),[],([],[
                Assign(ArrayCell(Id("arr"),[IntLiteral(5)]),ArrayLiteral([IntLiteral(64),IntLiteral(25),IntLiteral(12),IntLiteral(22),IntLiteral(11)])),
                Assign(Id("n"),BinaryOp("\\",CallExpr(Id("sizeof"),[Id("arr")]),CallExpr(Id("sizeof"),[ArrayCell(Id("arr"),[IntLiteral(0)])]))),
                CallStmt(Id("selectionSort"),[Id("arr"),Id("n")]),
                CallStmt(Id("printf"),[StringLiteral("Sorted array: n")]),
                CallStmt(Id("printArray"),[Id("arr"),Id("n")]),
                Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    def test96_comment(self):
        input = """
        Function: main
        Body:
            Var: a = 10;
            Var: x= {        ** this is a comment **    "abc\\n",    **** 1,   2,3,{1,2}};
            Var: x = {{{1,  2 ,2e-124, "avc" , 1 }, {  4 , **erty**  5}  },  {{ 6  ,  7  },{ 8,9}}};
        EndBody.
        """
        expect = Program([
            FuncDecl(Id("main"),[],([
                VarDecl(Id("a"),[],IntLiteral(10)),
                VarDecl(Id("x"),[],ArrayLiteral([StringLiteral("abc\\n"),IntLiteral(1),IntLiteral(2),IntLiteral(3),ArrayLiteral([IntLiteral(1),IntLiteral(2)])])),
                VarDecl(Id("x"),[],
                ArrayLiteral([
                    ArrayLiteral([
                        ArrayLiteral([IntLiteral(1),IntLiteral(2),FloatLiteral("2e-124"),StringLiteral("avc"),IntLiteral(1)]),
                        ArrayLiteral([IntLiteral(4),IntLiteral(5)])]
                    ),
                    ArrayLiteral([
                        ArrayLiteral([IntLiteral(6),IntLiteral(7)]),
                        ArrayLiteral([IntLiteral(8),IntLiteral(9)])
                    ])
                ]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    def test97_if_else_and_while(self):
        input = """
            Function: convertNumber_continue
            Parameter: x[6][7]
                Body: 
                    While (remainder > 0) Do
                        If (b > 10) Then
                            m = remainder % b;
                            If (m >= 10) Then
                                arr[count] =  char(m + cHAR_55);
                                count = count +1;
                            Else 
                                arr[count] = char(m + cHAR_48);
                                count = count +1;
                            EndIf.
                        Else
                            arr[count] = char((remainder % b) + cHAR_48);
                            count = count +1;
                        EndIf.
                        remainder = remainder \. 3;
                        Break;
                    EndWhile.
                EndBody.
                """
        expect = Program([
            FuncDecl(Id("convertNumber_continue"),[
                VarDecl(Id("x"),[6,7],None)],([],[
                    While(
                        BinaryOp(">",Id("remainder"),IntLiteral(0)),
                        ([],[
                            If(
                                [(
                                    BinaryOp(">",Id("b"),IntLiteral(10)),
                                    [],
                                    [Assign(Id("m"),BinaryOp("%",Id("remainder"),Id("b"))),
                                    If(
                                        [(
                                            BinaryOp(">=",Id("m"),IntLiteral(10)),
                                            [],
                                            [Assign(ArrayCell(Id("arr"),[Id("count")]),CallExpr(Id("char"),[BinaryOp("+",Id("m"),Id("cHAR_55"))])),
                                            Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))]
                                        )],([],[
                                            Assign(ArrayCell(Id("arr"),[Id("count")]),CallExpr(Id("char"),[BinaryOp("+",Id("m"),Id("cHAR_48"))])),
                                            Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))]))
                                    ])],([],[
                                        Assign(ArrayCell(Id("arr"),[Id("count")]),CallExpr(Id("char"),[BinaryOp("+",BinaryOp("%",Id("remainder"),Id("b")),Id("cHAR_48"))])),
                                        Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))])),
                            Assign(Id("remainder"),BinaryOp("\.",Id("remainder"),IntLiteral(3))),
                            Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    def test98_operator_precedence(self):
        input =  r"""Function: function
            Parameter: j, brr[1000]
            Body:
                j = -.-.i +. brrr[5];
            EndBody."""
        expect = Program([
            FuncDecl(Id("function"),[
                VarDecl(Id("j"),[],None),
                VarDecl(Id("brr"),[1000],None)],([],[
                    Assign(Id("j"),BinaryOp("+.",UnaryOp("-.",UnaryOp("-.",Id("i"))),ArrayCell(Id("brrr"),[IntLiteral(5)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    def test99_long_program(self):
        input = r"""
            Var: x = 0, y = 0, z = 0;
            Function: function
                Parameter: j, brr[1000]
                Body:
                    For (j = 0, j < 3, 1) Do
                        If (j == 0) && (j % 3 == 0) Then
                            x = brr[j];
                        ElseIf (j == 1) || (j % 2 == 1) Then
                            y = brr[j];
                            While (y % (j * j) != 0) Do
                                y = y + 1;
                            EndWhile.
                        Else
                            Var: k = 0xFFFFFFFF;
                            k = int_of_string(brr[j]);
                            z = k;
                        EndIf.
                    EndFor.
                EndBody.
                
            Function: super_print
                Parameter: str, n
                Body:
                    For (i = 0, i < n, 1) Do
                        print(str);
                    EndFor.
                EndBody.
                
            Function: main
                Parameter: argv[1000], argc
                Body:
                    function(argc + 1, argv);
                    Do
                        print("\n\r");
                        super_print("Hello World\n");
                    While True EndDo.
                EndBody."""
        expect = Program([
            VarDecl(Id("x"),[],IntLiteral(0)),
            VarDecl(Id("y"),[],IntLiteral(0)),
            VarDecl(Id("z"),[],IntLiteral(0)),
            FuncDecl(
                Id("function"),[
                    VarDecl(Id("j"),[],None),
                    VarDecl(Id("brr"),[1000],None)],([],[
                        For(
                            Id("j"),
                            IntLiteral(0),
                            BinaryOp("<",Id("j"),IntLiteral(3)),
                            IntLiteral(1),
                            ([],[
                                If(
                                    [(
                                        BinaryOp("&&",BinaryOp("==",Id("j"),IntLiteral(0)),BinaryOp("==",BinaryOp("%",Id("j"),IntLiteral(3)),IntLiteral(0))),
                                        [],
                                        [Assign(Id("x"),ArrayCell(Id("brr"),[Id("j")]))]
                                    ),(
                                        BinaryOp("||",BinaryOp("==",Id("j"),IntLiteral(1)),BinaryOp("==",BinaryOp("%",Id("j"),IntLiteral(2)),IntLiteral(1))),
                                        [],
                                        [Assign(Id("y"),ArrayCell(Id("brr"),[Id("j")])),
                                        While(
                                            BinaryOp("!=",BinaryOp("%",Id("y"),BinaryOp("*",Id("j"),Id("j"))),IntLiteral(0)),
                                            ([],[
                                                Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(1)))]))
                                        ])],([
                                            VarDecl(Id("k"),[],IntLiteral(4294967295))],[
                                                Assign(Id("k"),CallExpr(Id("int_of_string"),[ArrayCell(Id("brr"),[Id("j")])])),
                                                Assign(Id("z"),Id("k"))]))]))])),
            FuncDecl(Id("super_print"),[
                VarDecl(Id("str"),[],None),
                VarDecl(Id("n"),[],None)],([],[
                    For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),Id("n")),
                        IntLiteral(1),
                        ([],[CallStmt(Id("print"),[Id("str")])]))])),
            FuncDecl(Id("main"),[
                VarDecl(Id("argv"),[1000],None),
                VarDecl(Id("argc"),[],None)],([],[
                    CallStmt(Id("function"),[BinaryOp("+",Id("argc"),IntLiteral(1)),Id("argv")]),
                    Dowhile(
                        ([],[
                            CallStmt(Id("print"),[StringLiteral("\\n\\r")]),
                            CallStmt(Id("super_print"),[StringLiteral("Hello World\\n")])]),
                        BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
    def test100_long_program(self):
        input = r"""
            Var: x;
            Var: y;
            Var: z;
            Function: function
                Parameter: j, brr[1000]
                Body:
                    For (j = 0, j < 3, 1) Do
                        If (j == 0) && (j % 3 == 0) Then
                            x = brr[j];
                        ElseIf (j == 1) || (j % 2 == 1) Then
                            y = brr[j];
                            While (y % (j * j) != 0) Do
                                y = y + 1;
                            EndWhile.
                        Else
                            Var: k = 0xFFFFFFFF;
                            k = int_of_string(brr[j]);
                            z = k;
                        EndIf.
                    EndFor.
                EndBody.
                
            Function: main
                Parameter: argv[1000], argc
                Body:
                    function(argc, argv);
                EndBody."""
        expect = Program([
            VarDecl(Id("x"),[],None),
            VarDecl(Id("y"),[],None),
            VarDecl(Id("z"),[],None),
            FuncDecl(
                Id("function"),[
                VarDecl(Id("j"),[],None),
                VarDecl(Id("brr"),[1000],None)],
                ([],[
                    For(
                        Id("j"),
                        IntLiteral(0),
                        BinaryOp("<",Id("j"),IntLiteral(3)),
                        IntLiteral(1),
                        ([],[If(
                            [(
                                BinaryOp("&&",BinaryOp("==",Id("j"),IntLiteral(0)),BinaryOp("==",BinaryOp("%",Id("j"),IntLiteral(3)),IntLiteral(0))),
                                [],
                                [Assign(Id("x"),ArrayCell(Id("brr"),[Id("j")]))]
                            ),(
                                BinaryOp("||",BinaryOp("==",Id("j"),IntLiteral(1)),BinaryOp("==",BinaryOp("%",Id("j"),IntLiteral(2)),IntLiteral(1))),
                                [],
                                [Assign(Id("y"),ArrayCell(Id("brr"),[Id("j")])),
                                While(
                                    BinaryOp("!=",BinaryOp("%",Id("y"),BinaryOp("*",Id("j"),Id("j"))),IntLiteral(0)),
                                    ([],[Assign(Id("y"),BinaryOp("+",Id("y"),IntLiteral(1)))])
                                )]
                            )],([VarDecl(Id("k"),[],IntLiteral(4294967295))],
                                [Assign(Id("k"),CallExpr(Id("int_of_string"),[ArrayCell(Id("brr"),[Id("j")])])),
                                Assign(Id("z"),Id("k"))])
                            )]
                        )
                    )]
                )
            ),
            FuncDecl(
                Id("main"),
                [VarDecl(Id("argv"),[1000],None),
                VarDecl(Id("argc"),[],None)],
                ([],[CallStmt(Id("function"),[Id("argc"),Id("argv")])])
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,400))