import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    """ Program structure """
    def test_301(self):
        input = r""" """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_302(self):
        input = r"""
Var: a, b;
Var: c;

Function: foo
    Body:
    EndBody.

Function: main
    Body:
    EndBody.
"""
        expect = Program([
            VarDecl(Id("a"), [], None),
            VarDecl(Id("b"), [], None),
            VarDecl(Id("c"), [], None),
            FuncDecl(Id("foo"), [], ([], [])),
            FuncDecl(Id("main"), [], ([], []))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    """ Variable declaration """

    def test_303(self):
        input = r"""
Var: a;
"""
        expect = Program([VarDecl(Id("a"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_304(self):
        input = r"""
Var: a1;
Var: b1, b2;
Var: c1, c2, c3;
"""
        expect = Program([
            VarDecl(Id("a1"), [], None),
            VarDecl(Id("b1"), [], None),
            VarDecl(Id("b2"), [], None),
            VarDecl(Id("c1"), [], None),
            VarDecl(Id("c2"), [], None),
            VarDecl(Id("c3"), [], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_305(self):
        input = r"""
Var: a1[0];
Var: a1[1], a2[1][2], a3[1][2][3], a4[1][2][3][4];
"""
        expect = Program([
            VarDecl(Id("a1"), [0], None),
            VarDecl(Id("a1"), [1], None),
            VarDecl(Id("a2"), [1, 2], None),
            VarDecl(Id("a3"), [1, 2, 3], None),
            VarDecl(Id("a4"), [1, 2, 3, 4], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_306(self):
        input = r"""
Var: a1[0o1][0o2][0o3][0o4][0o5][0o6][0o7];
Var: a1[0O1][0O2][0O3][0O4][0O5][0O6][0O7];
Var: a1[0o1000000000], a1[0O76543210];
"""
        expect = Program([
            VarDecl(Id("a1"), [1, 2, 3, 4, 5, 6, 7], None),
            VarDecl(Id("a1"), [1, 2, 3, 4, 5, 6, 7], None),
            VarDecl(Id("a1"), [134217728], None),
            VarDecl(Id("a1"), [16434824], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_307(self):
        input = r"""
Var: a[0x1][0x2][0x3][0x4][0x5][0x6][0x7][0x8][0x9];
Var: b[0xA][0xB][0xC][0xD][0xE][0xF];
Var: c[0X1][0X2][0X3][0X4][0X5][0X6][0X7][0X8][0X9];
Var: d[0XA][0XB][0XC][0XD][0XE][0XF];
Var: c[0x10000000], d[0XABCDEF];
Var: e[0x1234], e[0X8765];
"""
        expect = Program([
            VarDecl(Id("a"), [1, 2, 3, 4, 5, 6, 7, 8, 9], None),
            VarDecl(Id("b"), [10, 11, 12, 13, 14, 15], None),
            VarDecl(Id("c"), [1, 2, 3, 4, 5, 6, 7, 8, 9], None),
            VarDecl(Id("d"), [10, 11, 12, 13, 14, 15], None),
            VarDecl(Id("c"), [268435456], None),
            VarDecl(Id("d"), [11259375], None),
            VarDecl(Id("e"), [4660], None),
            VarDecl(Id("e"), [34661], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_308(self):
        input = r"""
Var: a = 1;
Var: a[1] = {1};
Var: a[1][2] = {{1}, {2}};
"""
        expect = Program([
            VarDecl(Id("a"), [], IntLiteral(1)),
            VarDecl(Id("a"), [1], ArrayLiteral([IntLiteral(1)])),
            VarDecl(Id("a"), [1, 2],
                    ArrayLiteral([ArrayLiteral([IntLiteral(1)]),
                                  ArrayLiteral([IntLiteral(2)])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    """ Function declaration """

    def test_309(self):
        input = r"""
Function: main
    Body:
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_310(self):
        input = r"""
Function: main
    Body:
        Var: a;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_311(self):
        input = r"""
Function: main
    Body:
        foo();
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [CallStmt(Id("foo"), [])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_312(self):
        input = r"""
Function: main
    Body:
        Var: a, b;
        foo1();
        foo2();
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([
                VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)
            ], [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_313(self):
        input = r"""
Function: main
    Parameter: a
    Body:
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_314(self):
        input = r"""
Function: main
    Parameter: a, b, c
    Body:
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [
                VarDecl(Id("a"), [], None),
                VarDecl(Id("b"), [], None),
                VarDecl(Id("c"), [], None)
            ], ([], []))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_315(self):
        input = r"""
Function: main
    Parameter: a[0], b[123], c[0xABCDEF][0X123], d[0o7654][0O3210]
    Body:
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [
                VarDecl(Id("a"), [0], None),
                VarDecl(Id("b"), [123], None),
                VarDecl(Id("c"), [11259375, 291], None),
                VarDecl(Id("d"), [4012, 1672], None)
            ], ([], []))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    """ If statement """

    def test_316(self):
        input = r"""
Function: main
    Body:
        If True Then
        EndIf.
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [If([(BooleanLiteral(True), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_317(self):
        input = r"""
Function: main
    Body:
        If a Then
            Var: a;
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [If([(Id("a"), [VarDecl(Id("a"), [], None)], [])], ([], []))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_318(self):
        input = r"""
Function: main
    Body:
        If a Then
            foo();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [If([(Id("a"), [], [CallStmt(Id("foo"), [])])], ([], []))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_319(self):
        input = r"""
Function: main
    Body:
        If a Then
            Var: a, b;
            foo1();
            foo2();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(Id("a"), [VarDecl(Id("a"), [], None),
                               VarDecl(Id("b"), [], None)],
                     [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_320(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []), (BooleanLiteral(True), [], [])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_321(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
        ElseIf True Then
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []), (BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [], [])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_322(self):
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
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []), (BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [], []), (BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [], []), (BooleanLiteral(True), [], [])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_323(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
            Var: a;
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [VarDecl(Id("a"), [], None)], [])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_324(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
            foo();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [], [CallStmt(Id("foo"), [])])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_325(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
            Var: a, b;
            foo1();
            foo2();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []),
                    (BooleanLiteral(True), [VarDecl(Id("a"), [], None),
                                            VarDecl(Id("b"), [], None)],
                     [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_326(self):
        input = r"""
Function: main
    Body:
        If True Then
        ElseIf True Then
        Else
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], []), (BooleanLiteral(True), [], [])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_327(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
        EndIf.
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [If([(BooleanLiteral(True), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_328(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
            Var: a;
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(
                Id("main"), [],
                ([], [If([(BooleanLiteral(True), [], [])], ([VarDecl(Id("a"), [], None)], []))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_329(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
            foo();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [If([(BooleanLiteral(True), [], [])], ([], [CallStmt(Id("foo"), [])]))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_330(self):
        input = r"""
Function: main
    Body:
        If True Then
        Else
            Var: a, b;
            foo1();
            foo2();
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(BooleanLiteral(True), [], [])],
                   ([VarDecl(Id("a"), [], None),
                     VarDecl(Id("b"), [], None)],
                    [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    """ While """

    def test_331(self):
        input = r"""
Function: main
    Body:
        While True Do
        EndWhile.
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [While(BooleanLiteral(True), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_332(self):
        input = r"""
Function: main
    Body:
        While True Do
            Var: a;
        EndWhile.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [While(BooleanLiteral(True), ([VarDecl(Id("a"), [], None)], []))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_333(self):
        input = r"""
Function: main
    Body:
        While True Do
            foo();
        EndWhile.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [While(BooleanLiteral(True), ([], [CallStmt(Id("foo"), [])]))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_334(self):
        input = r"""
Function: main
    Body:
        While True Do
            Var: a, b;
            foo1();
            foo2();
        EndWhile.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                While(
                    BooleanLiteral(True),
                    ([VarDecl(Id("a"), [], None),
                      VarDecl(Id("b"), [], None)],
                     [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    """ Do while """

    def test_335(self):
        input = r"""
Function: main
    Body:
        Do
        While True
        EndDo.
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Dowhile(([], []), BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_336(self):
        input = r"""
Function: main
    Body:
        Do
            Var: a;
        While True
        EndDo.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Dowhile(([VarDecl(Id("a"), [], None)], []), BooleanLiteral(True))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_337(self):
        input = r"""
Function: main
    Body:
        Do
            foo();
        While True
        EndDo.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Dowhile(([], [CallStmt(Id("foo"), [])]), BooleanLiteral(True))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_338(self):
        input = r"""
Function: main
    Body:
        Do
            Var: a, b;
            foo1();
            foo2();
        While True
        EndDo.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Dowhile(
                    ([VarDecl(Id("a"), [], None),
                      VarDecl(Id("b"), [], None)],
                     [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]), BooleanLiteral(True))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    """ For """

    def test_339(self):
        input = r"""
Function: main
    Body:
        For (a = 1, a < 10, 1) Do
        EndFor.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                For(Id("a"), IntLiteral(1), BinaryOp("<", Id("a"), IntLiteral(10)), IntLiteral(1),
                    ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_340(self):
        input = r"""
Function: main
    Body:
        For (a = 1, a < 10, 1) Do
            Var: a;
        EndFor.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                For(Id("a"), IntLiteral(1), BinaryOp("<", Id("a"), IntLiteral(10)), IntLiteral(1),
                    ([VarDecl(Id("a"), [], None)], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_341(self):
        input = r"""
Function: main
    Body:
        For (a = 1, a < 10, 1) Do
            foo();
        EndFor.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                For(Id("a"), IntLiteral(1), BinaryOp("<", Id("a"), IntLiteral(10)), IntLiteral(1),
                    ([], [CallStmt(Id("foo"), [])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_342(self):
        input = r"""
Function: main
    Body:
        For (a = 1, a < 10, 1) Do
            Var: a, b;
            foo();
            foo();
        EndFor.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                For(Id("a"), IntLiteral(1), BinaryOp("<", Id("a"), IntLiteral(10)), IntLiteral(1),
                    ([VarDecl(Id("a"), [], None),
                      VarDecl(Id("b"), [], None)
                      ], [CallStmt(Id("foo"), []), CallStmt(Id("foo"), [])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_343(self):
        input = r"""
Function: main
    Body:
        For (a = 1 + 1, a < 10, 1) Do
        EndFor.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                For(Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(1)),
                    BinaryOp("<", Id("a"), IntLiteral(10)), IntLiteral(1), ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_344(self):
        input = r"""
Function: main
    Body:
        For (a = 10, a > 10, -1) Do
        EndFor.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                For(Id("a"), IntLiteral(10), BinaryOp(">", Id("a"), IntLiteral(10)),
                    UnaryOp("-", IntLiteral(1)), ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    """ Break """

    def test_345(self):
        input = r"""
Function: main
    Body:
        Break;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_346(self):
        input = r"""
Function: main
    Body:
        Continue;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_347(self):
        input = r"""
Function: main
    Body:
        Return 1;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Return(IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_348(self):
        input = r"""
Function: main
    Body:
        Return;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_349(self):
        input = r"""
Function: main
    Body:
        Return a + b;
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Return(BinaryOp("+", Id("a"), Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    """ Funccall """

    def test_350(self):
        input = r"""
Function: main
    Body:
        foo(a);
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [CallStmt(Id("foo"), [Id("a")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_351(self):
        input = r"""
Function: main
    Body:
        foo(1, a[2], True, "", 1.);
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("foo"), [
                    IntLiteral(1),
                    ArrayCell(Id("a"), [IntLiteral(2)]),
                    BooleanLiteral(True),
                    StringLiteral(""),
                    FloatLiteral(1.0)
                ])
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_352(self):
        input = r"""
Function: main
    Body:
        foo(foo(foo()));
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [CallStmt(Id("foo"), [CallExpr(Id("foo"), [CallExpr(Id("foo"), [])])])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    """ Assignment """

    def test_353(self):
        input = r"""
Function: main
    Body:
        a = abcd;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), Id("abcd"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_354(self):
        input = r"""
Function: main
    Body:
        a = 1;
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_355(self):
        input = r"""
Function: main
    Body:
        a[1] = 1;
        a[-1][foo() + 2] = 1;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(ArrayCell(Id("a"), [IntLiteral(1)]), IntLiteral(1)),
                Assign(
                    ArrayCell(Id("a"), [
                        UnaryOp("-", IntLiteral(1)),
                        BinaryOp("+", CallExpr(Id("foo"), []), IntLiteral(2))
                    ]), IntLiteral(1))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_356(self):
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
            FuncDecl(Id("main"), [], ([], [
                Assign(ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(1)]), IntLiteral(1)),
                Assign(ArrayCell(CallExpr(Id("foo"), []), [UnaryOp("-", IntLiteral(1))]),
                       IntLiteral(1)),
                Assign(
                    ArrayCell(CallExpr(Id("foo"), [Id("abc"), IntLiteral(123)]),
                              [CallExpr(Id("foo"), [])]), IntLiteral(1)),
                Assign(ArrayCell(CallExpr(Id("foo"), [CallExpr(Id("foo"), [])]), [IntLiteral(1)]),
                       IntLiteral(1)),
                Assign(
                    ArrayCell(
                        CallExpr(Id("foo"), [BooleanLiteral(True),
                                             StringLiteral(r"""abc""")]),
                        [Id("a"), Id("b"), Id("c")]), IntLiteral(1))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    """ Integer literal """

    def test_357(self):
        input = r"""
Function: main
    Body:
        a = 0;
        a = 123456789;
        a = 999999999;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), IntLiteral(0)),
                Assign(Id("a"), IntLiteral(123456789)),
                Assign(Id("a"), IntLiteral(999999999))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_358(self):
        input = r"""
Function: main
    Body:
        a = -0;
    EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Assign(Id("a"), UnaryOp("-", IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_359(self):
        input = r"""
Function: main
    Body:
        foo(0o1,0o2,0o3,0o4,0o5,0o6,0o7);
        foo(0O1,0O2,0O3,0O4,0O5,0O6,0O7);
        foo(0o1000000000,0O76543210);
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("foo"), [
                    IntLiteral(1),
                    IntLiteral(2),
                    IntLiteral(3),
                    IntLiteral(4),
                    IntLiteral(5),
                    IntLiteral(6),
                    IntLiteral(7)
                ]),
                CallStmt(Id("foo"), [
                    IntLiteral(1),
                    IntLiteral(2),
                    IntLiteral(3),
                    IntLiteral(4),
                    IntLiteral(5),
                    IntLiteral(6),
                    IntLiteral(7)
                ]),
                CallStmt(Id("foo"),
                         [IntLiteral(134217728), IntLiteral(16434824)])
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_360(self):
        input = r"""
Function: main
    Body:
        foo(0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9);
        foo(0xA,0xB,0xC,0xD,0xE,0xF);
        foo(0X1,0X2,0X3,0X4,0X5,0X6,0X7,0X8,0X9);
        foo(0XA,0XB,0XC,0XD,0XE,0XF);
        foo(0x10000000,0XABCDEF);
        foo(0x1234,0X8765);
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("foo"), [
                    IntLiteral(1),
                    IntLiteral(2),
                    IntLiteral(3),
                    IntLiteral(4),
                    IntLiteral(5),
                    IntLiteral(6),
                    IntLiteral(7),
                    IntLiteral(8),
                    IntLiteral(9)
                ]),
                CallStmt(Id("foo"), [
                    IntLiteral(10),
                    IntLiteral(11),
                    IntLiteral(12),
                    IntLiteral(13),
                    IntLiteral(14),
                    IntLiteral(15)
                ]),
                CallStmt(Id("foo"), [
                    IntLiteral(1),
                    IntLiteral(2),
                    IntLiteral(3),
                    IntLiteral(4),
                    IntLiteral(5),
                    IntLiteral(6),
                    IntLiteral(7),
                    IntLiteral(8),
                    IntLiteral(9)
                ]),
                CallStmt(Id("foo"), [
                    IntLiteral(10),
                    IntLiteral(11),
                    IntLiteral(12),
                    IntLiteral(13),
                    IntLiteral(14),
                    IntLiteral(15)
                ]),
                CallStmt(Id("foo"),
                         [IntLiteral(268435456), IntLiteral(11259375)]),
                CallStmt(Id("foo"), [IntLiteral(4660), IntLiteral(34661)])
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_361(self):
        input = r"""
Function: main
    Body:
        a = 0 + 1 + 0x11 + 0o11;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp(
                        "+",
                        BinaryOp("+", BinaryOp("+", IntLiteral(0), IntLiteral(1)), IntLiteral(17)),
                        IntLiteral(9)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    """ Float literal """

    def test_362(self):
        input = r"""
Function: main
    Body:
        a = 1.1 + 1.;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Assign(Id("a"), BinaryOp("+", FloatLiteral(1.1), FloatLiteral(1.0)))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_363(self):
        input = r"""
Function: main
    Body:
        a = 1E1 + 1E+1 + 1E-1 + 1e1 + 1e+1 + 1e-1;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp(
                        "+",
                        BinaryOp(
                            "+",
                            BinaryOp(
                                "+",
                                BinaryOp("+", BinaryOp("+", FloatLiteral(10.0), FloatLiteral(10.0)),
                                         FloatLiteral(0.1)), FloatLiteral(10.0)),
                            FloatLiteral(10.0)), FloatLiteral(0.1)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_364(self):
        input = r"""
Function: main
    Body:
        a = 1e1 + 1.1e1 + 1.e1 + 1E1 + 1.1E1 + 1.E1;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp(
                        "+",
                        BinaryOp(
                            "+",
                            BinaryOp(
                                "+",
                                BinaryOp("+", BinaryOp("+", FloatLiteral(10.0), FloatLiteral(11.0)),
                                         FloatLiteral(10.0)), FloatLiteral(10.0)),
                            FloatLiteral(11.0)), FloatLiteral(10.0)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_365(self):
        input = r"""
Function: main
    Body:
        a = 1e-1 + 1.1e-1 + 1.e-1 + 1E-1 + 1.1E-1 + 1.E-1;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp(
                        "+",
                        BinaryOp(
                            "+",
                            BinaryOp(
                                "+",
                                BinaryOp("+", BinaryOp("+", FloatLiteral(0.1), FloatLiteral(0.11)),
                                         FloatLiteral(0.1)), FloatLiteral(0.1)),
                            FloatLiteral(0.11)), FloatLiteral(0.1)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_366(self):
        input = r"""
Function: main
    Body:
        a = 1e+1 + 1.1e+1 + 1.e+1 + 1E+1 + 1.1E+1 + 1.E+1;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp(
                        "+",
                        BinaryOp(
                            "+",
                            BinaryOp(
                                "+",
                                BinaryOp("+", BinaryOp("+", FloatLiteral(10.0), FloatLiteral(11.0)),
                                         FloatLiteral(10.0)), FloatLiteral(10.0)),
                            FloatLiteral(11.0)), FloatLiteral(10.0)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    """ Boolean literal """

    def test_367(self):
        input = r"""
Function: main
    Body:
        a = True;
        a = False;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), BooleanLiteral(True)),
                Assign(Id("a"), BooleanLiteral(False))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    """ String literal """

    def test_368(self):
        input = r"""
Function: main
    Body:
        a = "abcdef";
        b = "Hello World";
        c = "123: '" def '"";
        d = "\t\b\n\'";
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), StringLiteral(r"""abcdef""")),
                Assign(Id("b"), StringLiteral(r"""Hello World""")),
                Assign(Id("c"), StringLiteral("123: '\" def '\"")),
                Assign(Id("d"), StringLiteral(r"""\t\b\n\'"""))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    """ Array literal """

    def test_369(self):
        input = r"""
Function: main
    Body:
        a = { 1, 2, 3, 4 };
        a = { 1.0, 2.0, 3.0, 4.0 };
        a = { True, False };
        a = { "Hello", "World" };
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"),
                       ArrayLiteral([IntLiteral(1),
                                     IntLiteral(2),
                                     IntLiteral(3),
                                     IntLiteral(4)])),
                Assign(
                    Id("a"),
                    ArrayLiteral([
                        FloatLiteral(1.0),
                        FloatLiteral(2.0),
                        FloatLiteral(3.0),
                        FloatLiteral(4.0)
                    ])),
                Assign(Id("a"), ArrayLiteral([BooleanLiteral(True),
                                              BooleanLiteral(False)])),
                Assign(Id("a"),
                       ArrayLiteral([StringLiteral(r"""Hello"""),
                                     StringLiteral(r"""World""")]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_370(self):
        input = r"""
Function: main
    Body:
        a = { {1, 2}, {3, 4} };
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    ArrayLiteral([
                        ArrayLiteral([IntLiteral(1), IntLiteral(2)]),
                        ArrayLiteral([IntLiteral(3), IntLiteral(4)])
                    ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_371(self):
        input = r"""
Function: main
    Body:
        a = {{{{{{{{{{{1}}}}}}}}}}};
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    ArrayLiteral([
                        ArrayLiteral([
                            ArrayLiteral([
                                ArrayLiteral([
                                    ArrayLiteral([
                                        ArrayLiteral([
                                            ArrayLiteral([
                                                ArrayLiteral([
                                                    ArrayLiteral([
                                                        ArrayLiteral(
                                                            [ArrayLiteral([IntLiteral(1)])])
                                                    ])
                                                ])
                                            ])
                                        ])
                                    ])
                                ])
                            ])
                        ])
                    ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_372(self):
        input = r"""
Function: main
    Body:
        a = {{{{1}}}, {{1}}, {1}, 1};
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    ArrayLiteral([
                        ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])]),
                        ArrayLiteral([ArrayLiteral([IntLiteral(1)])]),
                        ArrayLiteral([IntLiteral(1)]),
                        IntLiteral(1)
                    ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    """ Bracket """

    def test_373(self):
        input = r"""
Function: main
    Body:
        a = (a);
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_374(self):
        input = r"""
Function: main
    Body:
        a = (((a)));
    EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    """ Call expression """

    def test_375(self):
        input = r"""
Function: main
    Body:
        a = foo();
        a = foo(1, True, "", 1.);
        a = foo(foo(foo()));
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), CallExpr(Id("foo"), [])),
                Assign(
                    Id("a"),
                    CallExpr(
                        Id("foo"),
                        [IntLiteral(1),
                         BooleanLiteral(True),
                         StringLiteral(""),
                         FloatLiteral(1.0)])),
                Assign(Id("a"), CallExpr(Id("foo"),
                                         [CallExpr(Id("foo"), [CallExpr(Id("foo"), [])])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    """ Index expression """

    def test_376(self):
        input = r"""
Function: main
    Body:
        a = a[1];
        a = a[-1][a];
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), ArrayCell(Id("a"), [IntLiteral(1)])),
                Assign(Id("a"), ArrayCell(
                    Id("a"), [UnaryOp("-", IntLiteral(1)), Id("a")]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_377(self):
        input = r"""
Function: main
    Body:
        a = foo()[1];
        a = foo()[-1];
        a = foo(1, True, 1., "abcd")[a][b][c];
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(1)])),
                Assign(Id("a"), ArrayCell(CallExpr(Id("foo"), []), [UnaryOp("-", IntLiteral(1))])),
                Assign(
                    Id("a"),
                    ArrayCell(
                        CallExpr(Id("foo"), [
                            IntLiteral(1),
                            BooleanLiteral(True),
                            FloatLiteral(1.0),
                            StringLiteral(r"""abcd""")
                        ]), [Id("a"), Id("b"), Id("c")]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    """ Binary and unary operator """

    def test_378(self):
        input = r"""
Function: main
    Body:
        a = 1 * 2;
        a = 1 *. 2;
        a = 1 \ 2;
        a = 1 \. 2;
        a = 1 % 2;
        a = 1 + 2;
        a = 1 +. 2;
        a = 1 - 2;
        a = 1 -. 2;
        a = 1 && 2;
        a = 1 || 2;
        a = 1 == 2;
        a = 1 != 2;
        a = 1 =/= 2;
        a = 1 < 2;
        a = 1 <. 2;
        a = 1 > 2;
        a = 1 >. 2;
        a = 1 <= 2;
        a = 1 <=. 2;
        a = 1 >= 2;
        a = 1 >=. 2;
        a = !1;
        a = -1;
        a = -.1;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), BinaryOp("*", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("*.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("\\", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("\\.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("%", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("+.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("-", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("-.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("&&", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("||", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("==", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("!=", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("=/=", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("<", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("<.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp(">", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp(">.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("<=", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp("<=.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp(">=", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), BinaryOp(">=.", IntLiteral(1), IntLiteral(2))),
                Assign(Id("a"), UnaryOp("!", IntLiteral(1))),
                Assign(Id("a"), UnaryOp("-", IntLiteral(1))),
                Assign(Id("a"), UnaryOp("-.", IntLiteral(1)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    """ Associative """

    def test_379(self):
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
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"),
                       BinaryOp("*", BinaryOp("*", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("*.", BinaryOp("*.", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("\\", BinaryOp("\\", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(
                    Id("a"),
                    BinaryOp("\\.", BinaryOp("\\.", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("%", BinaryOp("%", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("+", BinaryOp("+", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("+.", BinaryOp("+.", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("-", BinaryOp("-", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("-.", BinaryOp("-.", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("&&", BinaryOp("&&", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"),
                       BinaryOp("||", BinaryOp("||", IntLiteral(1), IntLiteral(2)), IntLiteral(3))),
                Assign(Id("a"), UnaryOp("!", UnaryOp("!", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("-", UnaryOp("-", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("-.", UnaryOp("-.", IntLiteral(1))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    """ Precendence """

    def test_380(self):
        input = r"""
Function: main
    Body:
        a = !-1;
        a = !-.1;
        a = --.1;
        a = -.-1;
        a = !--1;
        a = !-.-.1;
        a = !--.1;
        a = !-.-1;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(Id("a"), UnaryOp("!", UnaryOp("-", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("!", UnaryOp("-.", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("-", UnaryOp("-.", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("-.", UnaryOp("-", IntLiteral(1)))),
                Assign(Id("a"), UnaryOp("!", UnaryOp("-", UnaryOp("-", IntLiteral(1))))),
                Assign(Id("a"), UnaryOp("!", UnaryOp("-.", UnaryOp("-.", IntLiteral(1))))),
                Assign(Id("a"), UnaryOp("!", UnaryOp("-", UnaryOp("-.", IntLiteral(1))))),
                Assign(Id("a"), UnaryOp("!", UnaryOp("-.", UnaryOp("-", IntLiteral(1)))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_381(self):
        input = r"""
Function: main
    Body:
        a = a && b == c || d;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp("==", BinaryOp("&&", Id("a"), Id("b")), BinaryOp(
                        "||", Id("c"), Id("d"))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_382(self):
        input = r"""
Function: main
    Body:
        a = a + b || c - d;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp("||", BinaryOp("+", Id("a"), Id("b")), BinaryOp("-", Id("c"),
                                                                             Id("d"))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_383(self):
        input = r"""
Function: main
    Body:
        a = a * b + c % d;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp("+", BinaryOp("*", Id("a"), Id("b")), BinaryOp("%", Id("c"), Id("d"))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_384(self):
        input = r"""
Function: main
    Body:
        a = - a * b;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Assign(Id("a"), BinaryOp("*", UnaryOp("-", Id("a")), Id("b")))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_385(self):
        input = r"""
Function: main
    Body:
        a = ! a * b;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Assign(Id("a"), BinaryOp("*", UnaryOp("!", Id("a")), Id("b")))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_386(self):
        input = r"""
Function: main
    Body:
        a = -a[b];
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Assign(Id("a"), UnaryOp("-", ArrayCell(Id("a"), [Id("b")])))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_387(self):
        input = r"""
Function: main
    Body:
        a = !a[b];
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Assign(Id("a"), UnaryOp("!", ArrayCell(Id("a"), [Id("b")])))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_388(self):
        input = r"""
Function: main
    Body:
        a = a * b [c];
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Assign(Id("a"), BinaryOp("*", Id("a"), ArrayCell(Id("b"), [Id("c")])))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_389(self):
        input = r"""
Function: main
    Body:
        a = (a < b) && (d >= d);
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp("&&", BinaryOp("<", Id("a"), Id("b")), BinaryOp(
                        ">=", Id("d"), Id("d"))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_390(self):
        input = r"""
Function: main
    Body:
        a = !(a + b);
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [],
                     ([], [Assign(Id("a"), UnaryOp("!", BinaryOp("+", Id("a"), Id("b"))))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_391(self):
        input = r"""
Function: main
    Body:
        a = 1+-1;
    EndBody.
"""
        expect = Program([
            FuncDecl(
                Id("main"), [],
                ([], [Assign(Id("a"), BinaryOp("+", IntLiteral(1), UnaryOp("-", IntLiteral(1))))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_392(self):
        input = r"""
Function: main
    Body:
        a = 1--2--3;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp("-", BinaryOp("-", IntLiteral(1), UnaryOp("-", IntLiteral(2))),
                             UnaryOp("-", IntLiteral(3))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_393(self):
        input = r"""
Function: main
    Body:
        a = !a[1] > b || c + foo() * -e[2][abcd] % foo(1)[1] \ True;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    Id("a"),
                    BinaryOp(
                        ">", UnaryOp("!", ArrayCell(Id("a"), [IntLiteral(1)])),
                        BinaryOp(
                            "||", Id("b"),
                            BinaryOp(
                                "+", Id("c"),
                                BinaryOp(
                                    "\\",
                                    BinaryOp(
                                        "%",
                                        BinaryOp(
                                            "*", CallExpr(Id("foo"), []),
                                            UnaryOp("-",
                                                    ArrayCell(Id("e"), [IntLiteral(2),
                                                                        Id("abcd")]))),
                                        ArrayCell(CallExpr(Id("foo"), [IntLiteral(1)]),
                                                  [IntLiteral(1)])), BooleanLiteral(True))))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    """ Free Style """

    def test_394(self):
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
"""
        expect = Program([
            FuncDecl(Id("foo"), [VarDecl(Id("a"), [5], None),
                                 VarDecl(Id("b"), [], None)],
                     ([VarDecl(Id("i"), [], IntLiteral(0))], [
                         While(BinaryOp("<", Id("i"), IntLiteral(5)), ([], [
                             Assign(ArrayCell(Id("a"), [Id("i")]),
                                    BinaryOp("+.", Id("b"), FloatLiteral(1.0))),
                             Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))
                         ]))
                     ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_395(self):
        input = r"""

Function: main
    Body:
        Var: r = 10., v;
        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    EndBody.
"""
        expect = Program([
            FuncDecl(
                Id("main"),
                [], ([VarDecl(Id("r"), [], FloatLiteral(10.0)),
                      VarDecl(Id("v"), [], None)], [
                          Assign(
                              Id("v"),
                              BinaryOp(
                                  "*.",
                                  BinaryOp(
                                      "*.",
                                      BinaryOp(
                                          "*.",
                                          BinaryOp(
                                              "*.",
                                              BinaryOp("\\.", FloatLiteral(4.0), FloatLiteral(3.0)),
                                              FloatLiteral(3.14)), Id("r")), Id("r")), Id("r")))
                      ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_396(self):
        input = r"""

Function: main
    Body:
        a[3 + foo(2)] = a[b[2][3]] + 4;
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                Assign(
                    ArrayCell(Id("a"),
                              [BinaryOp("+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(2)]))]),
                    BinaryOp(
                        "+", ArrayCell(
                            Id("a"),
                            [ArrayCell(Id("b"), [IntLiteral(2), IntLiteral(3)])]), IntLiteral(4)))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_397(self):
        input = r"""

Function: main
    Body:
        If bool_of_string ("True") Then
            a = int_of_string (read ());
            b = float_of_int (a) +. 2.0;
        EndIf.
    EndBody.
"""
        expect = Program([
            FuncDecl(Id("main"), [], ([], [
                If([(CallExpr(Id("bool_of_string"), [StringLiteral(r"""True""")]), [], [
                    Assign(Id("a"), CallExpr(Id("int_of_string"), [CallExpr(Id("read"), [])])),
                    Assign(
                        Id("b"),
                        BinaryOp("+.", CallExpr(Id("float_of_int"), [Id("a")]), FloatLiteral(2.0)))
                ])], ([], []))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_398(self):
        input = r"""

Function: main
    Body:
        Var: r = 10., v;
        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    EndBody.
"""
        expect = Program([
            FuncDecl(
                Id("main"),
                [], ([VarDecl(Id("r"), [], FloatLiteral(10.0)),
                      VarDecl(Id("v"), [], None)], [
                          Assign(
                              Id("v"),
                              BinaryOp(
                                  "*.",
                                  BinaryOp(
                                      "*.",
                                      BinaryOp(
                                          "*.",
                                          BinaryOp(
                                              "*.",
                                              BinaryOp("\\.", FloatLiteral(4.0), FloatLiteral(3.0)),
                                              FloatLiteral(3.14)), Id("r")), Id("r")), Id("r")))
                      ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_399(self):
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
            VarDecl(Id("a"), [], None),
            VarDecl(Id("b"), [], StringLiteral(r"""abc""")),
            VarDecl(Id("c"), [], FloatLiteral(1.0)),
            FuncDecl(Id("main"), [], ([], [
                While(Id("a"), ([
                    VarDecl(Id("a"), [], BooleanLiteral(True)),
                    VarDecl(Id("b"), [], None),
                    VarDecl(Id("c"), [],
                            ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])]))
                ], [
                    Dowhile(([
                        VarDecl(Id("a"), [], None),
                        VarDecl(Id("b"), [], None),
                        VarDecl(
                            Id("c"), [],
                            ArrayLiteral(
                                [ArrayLiteral([IntLiteral(1)]),
                                 ArrayLiteral([IntLiteral(2)])]))
                    ], [
                        For(Id("i"), IntLiteral(10), BinaryOp("<", Id("i"), IntLiteral(10)),
                            UnaryOp("-", UnaryOp("-", Id("i"))), ([
                                VarDecl(Id("a"), [], IntLiteral(0)),
                                VarDecl(Id("b"), [], None),
                                VarDecl(Id("c"), [], None)
                            ], [
                                If([(Id("c"), [
                                    VarDecl(Id("a"), [], None),
                                    VarDecl(Id("b"), [], None),
                                    VarDecl(Id("c"), [], None)
                                ], [CallStmt(Id("foo"), [])]),
                                    (Id("d"), [
                                        VarDecl(Id("a"), [], None),
                                        VarDecl(Id("b"), [], None),
                                        VarDecl(Id("c"), [], None)
                                    ], [
                                        Assign(
                                            Id("a"),
                                            ArrayCell(
                                                CallExpr(Id("foo"), []),
                                                [CallExpr(Id("foo"), [CallExpr(Id("foo"), [])])]))
                                    ])], ([
                                        VarDecl(Id("a"), [], None),
                                        VarDecl(Id("b"), [], None),
                                        VarDecl(Id("c"), [], None)
                                    ], [
                                        While(Id("abcd"), ([
                                            VarDecl(Id("a"), [], None),
                                            VarDecl(Id("b"), [], IntLiteral(2)),
                                            VarDecl(Id("a"), [1, 2],
                                                    ArrayLiteral([IntLiteral(1),
                                                                  IntLiteral(2)]))
                                        ], [Break()])),
                                        Return(None)
                                    ]))
                            ])),
                        Continue()
                    ]), Id("b")),
                    Return(IntLiteral(1))
                ])),
                Return(IntLiteral(0))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_400(self):
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
            FuncDecl(Id("main"), [], ([
                VarDecl(Id("sum"), [], IntLiteral(0)),
                VarDecl(Id("a"), [], IntLiteral(1))
            ], [
                While(
                    BinaryOp("<", Id("a"), IntLiteral(10)),
                    ([VarDecl(Id("b"), [], IntLiteral(1)),
                      VarDecl(Id("prod"), [], IntLiteral(1))], [
                          While(BinaryOp("<", Id("b"), IntLiteral(10)), ([], [
                              Assign(Id("prod"), BinaryOp("*", Id("prod"), Id("b"))),
                              Assign(Id("b"), BinaryOp("+", Id("b"), IntLiteral(1)))
                          ])),
                          Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("prod"))),
                          Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))
                      ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))
