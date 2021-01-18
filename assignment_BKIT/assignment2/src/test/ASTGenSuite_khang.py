import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_simple_program_2(self):
        input = """Var:x=0o12,y=2;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(0o12)),VarDecl(Id("y"),[],IntLiteral(2))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_simple_program_3(self):
        input = """Var:x,z[1][2]={12.0e3,12E3,12.e5,12000.,120000e-1};"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("z"),[1,2],ArrayLiteral([FloatLiteral(12000.0),FloatLiteral(12000.0),FloatLiteral(1200000.0),FloatLiteral(12000.0),FloatLiteral(12000.0)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_simple_program_4(self):
        input = """Var:x=True,y="abc";"""
        expect = Program([VarDecl(Id("x"),[],BooleanLiteral(True)),VarDecl(Id("y"),[],StringLiteral("abc"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_simple_program_5(self):
        input = """Var:x={False,{1,"abc"},0x123};"""
        expect = Program([VarDecl(Id("x"),[],ArrayLiteral([BooleanLiteral(False),ArrayLiteral([IntLiteral(1),StringLiteral("abc")]),IntLiteral(0x123)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_simple_program_6(self):
        input = """Var:x[0x22]={};"""
        expect = Program([VarDecl(Id("x"),[0x22],ArrayLiteral([]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_simple_program_7(self):
        input = """Var:x[0O12]="a'"";"""
        expect = Program([VarDecl(Id("x"),[0O12],StringLiteral("a'\""))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_simple_program_8(self):
        input = """Var:x[0]={{}},**khai bao**y="  ";"""
        expect = Program([VarDecl(Id("x"),[0],ArrayLiteral([ArrayLiteral([])])),VarDecl(Id("y"),[],StringLiteral("  "))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_simple_program_9(self):
        input = """Var:x[0o11][0x12]={0.e+4,{True,"a\tb"}};"""
        expect = Program([VarDecl(Id("x"),[0o11,0x12],ArrayLiteral([FloatLiteral(0.0e+4),ArrayLiteral([BooleanLiteral(True),StringLiteral("a\tb")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_simple_program_10(self):
        input = """Var:x,y="a\\nb",z={""},t;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],StringLiteral("a\\nb")),VarDecl(Id("z"),[],ArrayLiteral([StringLiteral("")])),VarDecl(Id("t"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_simple_program_11(self):
        input = """
        Var:x,y[1]={1e-2,"a\\'b"};
        Function:main
        **Parameter:y[0x1],x**
        Body:
            **Var:z[0x2];**
            z[0O1]=y[1+x]+0o3[2];
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],ArrayLiteral([FloatLiteral(1e-2),StringLiteral("a\\'b")])),FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("z"),[IntLiteral(1)]),BinaryOp("+",ArrayCell(Id("y"),[BinaryOp("+",IntLiteral(1),Id("x"))]),ArrayCell(IntLiteral(3),[IntLiteral(2)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_simple_program_12(self):
        input = """
        Var:x[0x24]=0O24;
        Function: main
        Body:
            If a[0o25[333] *- 1.e-5 < 3] >= 2 Then
                print("Exit");
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[0x24],IntLiteral(0O24)),FuncDecl(Id("main"),[],([],[If([(BinaryOp(">=",ArrayCell(Id("a"),[BinaryOp("<",BinaryOp("*",ArrayCell(IntLiteral(0o25),[IntLiteral(333)]),UnaryOp("-",FloatLiteral(1.e-5))),IntLiteral(3))]),IntLiteral(2)),[],[CallStmt(Id("print"),[StringLiteral("Exit")])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_simple_program_13(self):
        input = """
        Var:x={True,**note**123};
        Function: main
        Body:
            If 0[2] == x \ 1E-2 Then
                foo(-.2 % !(x && True));
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],ArrayLiteral([BooleanLiteral(True),IntLiteral(123)])),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",ArrayCell(IntLiteral(0),[IntLiteral(2)]),BinaryOp("\\",Id("x"),FloatLiteral(0.01))),[],[CallStmt(Id("foo"),[BinaryOp("%",UnaryOp("-.",IntLiteral(2)),UnaryOp("!",BinaryOp("&&",Id("x"),BooleanLiteral(True))))])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_simple_program_14(self):
        input = """
        Var:x[0X20]="\\\\";
        Function: main
        Body:
            If foo(1.25["\\r"]) =/= False Then
                Var:x[0O22],y={"a\\'b"};
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[0X20],StringLiteral("\\\\")),FuncDecl(Id("main"),[],([],[If([(BinaryOp("=/=",CallExpr(Id("foo"),[ArrayCell(FloatLiteral(1.25),[StringLiteral("\\r")])]),BooleanLiteral(False)),[VarDecl(Id("x"),[0O22],None),VarDecl(Id("y"),[],ArrayLiteral([StringLiteral("a\\'b")]))],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_simple_program_15(self):
        input = """
        Var:x[2]={{00.00e+000},{00.E-00}};
        Function: foo
        Parameter:x[2],y
        Body:
            If x[0][1.e+0 > 0.0] <= 0[{1,True}] Then
                If {} Then
                    foo()[""] = "'\"";
                EndIf.
            EndIf.
        EndBody.
        Function: main
        Body:
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[2],ArrayLiteral([ArrayLiteral([FloatLiteral(0.0)]),ArrayLiteral([FloatLiteral(0.0)])])),FuncDecl(Id("foo"),[VarDecl(Id("x"),[2],None),VarDecl(Id("y"),[],None)],([],[If([(BinaryOp("<=",ArrayCell(Id("x"),[IntLiteral(0),BinaryOp(">",FloatLiteral(1.0),FloatLiteral(0.0))]),ArrayCell(IntLiteral(0),[ArrayLiteral([IntLiteral(1),BooleanLiteral(True)])])),[],[If([(ArrayLiteral([]),[],[Assign(ArrayCell(CallExpr(Id("foo"),[]),[StringLiteral("")]),StringLiteral("'\""))])],([],[]))])],([],[]))])),FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_simple_program_16(self):
        input = """
        Var:x,y={},z="",t=0.0;
        Function: main
        Parameter: x,y,z,t
        Body:
            If x > y || z Then
                Return {10.E+100,0.E-100};
            ElseIf x <= z && y Then 
                Return 0[z(t)];
            ElseIf ! x == t Then
                Return ({0x1234567891011} + a[-1][t]);
            Else
                Return;
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],ArrayLiteral([])),VarDecl(Id("z"),[],StringLiteral("")),VarDecl(Id("t"),[],FloatLiteral(0.0)),FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("t"),[],None)],([],[If([(BinaryOp(">",Id("x"),BinaryOp("||",Id("y"),Id("z"))),[],[Return(ArrayLiteral([FloatLiteral(10.E+100),FloatLiteral(0.E-100)]))]),(BinaryOp("<=",Id("x"),BinaryOp("&&",Id("z"),Id("y"))),[],[Return(ArrayCell(IntLiteral(0),[CallExpr(Id("z"),[Id("t")])]))]),(BinaryOp("==",UnaryOp("!",Id("x")),Id("t")),[],[Return(BinaryOp("+",ArrayLiteral([IntLiteral(0x1234567891011)]),ArrayCell(Id("a"),[UnaryOp("-",IntLiteral(1)),Id("t")])))])],([],[Return(None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_simple_program_17(self):
        input = """
        Function: main
        Parameter: x,y,z[0x11],t
        Body:
            If x[y > z] > (y <= t[x]) Then
                x[y && z + 2][x(t * {"0", 0})] = -1.000000000000000000000000000000001;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[17],None),VarDecl(Id("t"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("x"),[BinaryOp(">",Id("y"),Id("z"))]),BinaryOp("<=",Id("y"),ArrayCell(Id("t"),[Id("x")]))),[],[Assign(ArrayCell(Id("x"),[BinaryOp("&&",Id("y"),BinaryOp("+",Id("z"),IntLiteral(2))),CallExpr(Id("x"),[BinaryOp("*",Id("t"),ArrayLiteral([StringLiteral("0"),IntLiteral(0)]))])]),UnaryOp("-",FloatLiteral(1.0)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_simple_program_18(self):
        input = """
        Var: b___ = 0e+0;
        Function: main
        Parameter: x[0]
        Body:
            If 1 *. 2 && 3 Then
                1[-2] = 1 > 2[3];
            ElseIf 0 Then
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("b___"),[],FloatLiteral(0.0)),FuncDecl(Id("main"),[VarDecl(Id("x"),[0],None)],([],[If([(BinaryOp("&&",BinaryOp("*.",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),[],[Assign(ArrayCell(IntLiteral(1),[UnaryOp("-",IntLiteral(2))]),BinaryOp(">",IntLiteral(1),ArrayCell(IntLiteral(2),[IntLiteral(3)])))]),(IntLiteral(0),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_simple_program_19(self):
        input = """
        Function: main
        Body:
            If 1 Then
                If 5 Then
                Else
                EndIf.
            ElseIf 2 Then
                If 3 Then
                ElseIf 4 Then
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(IntLiteral(1),[],[If([(IntLiteral(5),[],[])],([],[]))]),(IntLiteral(2),[],[If([(IntLiteral(3),[],[]),(IntLiteral(4),[],[])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_simple_program_20(self):
        input = """
        Function: main
        Body:
            If 0[-1][foo() && 1[2 > -3 + 2]] =/= 1 \. 2[5 || 7] Then
                foo123(x[{1,2.e-3}] % {"Hello"});
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(BinaryOp("=/=",ArrayCell(IntLiteral(0),[UnaryOp("-",IntLiteral(1)),BinaryOp("&&",CallExpr(Id("foo"),[]),ArrayCell(IntLiteral(1),[BinaryOp(">",IntLiteral(2),BinaryOp("+",UnaryOp("-",IntLiteral(3)),IntLiteral(2)))]))]),BinaryOp("\\.",IntLiteral(1),ArrayCell(IntLiteral(2),[BinaryOp("||",IntLiteral(5),IntLiteral(7))]))),[],[CallStmt(Id("foo123"),[BinaryOp("%",ArrayCell(Id("x"),[ArrayLiteral([IntLiteral(1),FloatLiteral(0.002)])]),ArrayLiteral([StringLiteral("Hello")]))])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_simple_program_21(self):
        input = """
        Var: x, y = {}, z;
        Var: t = ** 123 ** "";
        Function: main
        Body:
            For(i = "Start", i =/= {1,2}, "Add") Do
                For(j = ** 123**" **",j,j) Do
                EndFor.
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],ArrayLiteral([])),VarDecl(Id("z"),[],None),VarDecl(Id("t"),[],StringLiteral("")),FuncDecl(Id("main"),[],([],[For(Id("i"),StringLiteral("Start"),BinaryOp("=/=",Id("i"),ArrayLiteral([IntLiteral(1),IntLiteral(2)])),StringLiteral("Add"),([],[For(Id("j"),StringLiteral(" **"),Id("j"),Id("j"),([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_simple_program_22(self):
        input = """
        Var: x[12345678], y=1.2345678E+2, z={True,False};
        Function: main
        Body:
            For (i__ = 0x231, 0, {{{}}}) Do
                writeln(main(0x231[0o211]));
                Break;
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[12345678],None),VarDecl(Id("y"),[],FloatLiteral(123.45678)),VarDecl(Id("z"),[],ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False)])),FuncDecl(Id("main"),[],([],[For(Id("i__"),IntLiteral(561),IntLiteral(0),ArrayLiteral([ArrayLiteral([ArrayLiteral([])])]),([],[CallStmt(Id("writeln"),[CallExpr(Id("main"),[ArrayCell(IntLiteral(561),[IntLiteral(137)])])]),Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_simple_program_23(self):
        input = """
        Var: x={""};
        Function: main
        Body:
            For(i = 1.1 > 2.2[3], {"abc",2}, 1 && 2) Do
                For(j = x +. y, 2 && !j, -.j) Do
                EndFor.
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],ArrayLiteral([StringLiteral("")])),FuncDecl(Id("main"),[],([],[For(Id("i"),BinaryOp(">",FloatLiteral(1.1),ArrayCell(FloatLiteral(2.2),[IntLiteral(3)])),ArrayLiteral([StringLiteral("abc"),IntLiteral(2)]),BinaryOp("&&",IntLiteral(1),IntLiteral(2)),([],[For(Id("j"),BinaryOp("+.",Id("x"),Id("y")),BinaryOp("&&",IntLiteral(2),UnaryOp("!",Id("j"))),UnaryOp("-.",Id("j")),([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_simple_program_24(self):
        input = """
        Var: x;
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
                x = 10;
                fact (x);
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))])),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_simple_program_25(self):
        input = """
        Var: x, y = {}, z;
        Function: main
        Body:
            For(i = bool_of_string ("True"), i + 1.e-2, 5 <= 6) Do
                Var: i = "a\\tb";
                a[3 + foo(2)] = a[b[2][3]] + 4;
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],ArrayLiteral([])),VarDecl(Id("z"),[],None),FuncDecl(Id("main"),[],([],[For(Id("i"),CallExpr(Id("bool_of_string"),[StringLiteral("True")]),BinaryOp("+",Id("i"),FloatLiteral(0.01)),BinaryOp("<=",IntLiteral(5),IntLiteral(6)),([VarDecl(Id("i"),[],StringLiteral("a\\tb"))],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_simple_program_26(self):
        input = """
        Var: tRUE=True, fALSE=False;
        Function: main
        Parameter: tRUE, fALSE
        Body:
            Var: bool;
            0[bool] = bool[1 > 2] < 3;
            For(i = "Start", i =/= {1,2}, "Add") Do
                Var: bool2;
                If i =/= 2 && 8 Then
                    Continue;
                EndIf.
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id("tRUE"),[],BooleanLiteral(True)),VarDecl(Id("fALSE"),[],BooleanLiteral(False)),FuncDecl(Id("main"),[VarDecl(Id("tRUE"),[],None),VarDecl(Id("fALSE"),[],None)],([VarDecl(Id("bool"),[],None)],[Assign(ArrayCell(IntLiteral(0),[Id("bool")]),BinaryOp("<",ArrayCell(Id("bool"),[BinaryOp(">",IntLiteral(1),IntLiteral(2))]),IntLiteral(3))),For(Id("i"),StringLiteral("Start"),BinaryOp("=/=",Id("i"),ArrayLiteral([IntLiteral(1),IntLiteral(2)])),StringLiteral("Add"),([VarDecl(Id("bool2"),[],None)],[If([(BinaryOp("=/=",Id("i"),BinaryOp("&&",IntLiteral(2),IntLiteral(8))),[],[Continue()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_simple_program_27(self):
        input = """
        Function: main
        Body:
            For(i = 12000., foo(0o234), 1[1[1]]) Do
                Do print(x); While True
                EndDo.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[For(Id("i"),FloatLiteral(12000.0),CallExpr(Id("foo"),[IntLiteral(156)]),ArrayCell(IntLiteral(1),[ArrayCell(IntLiteral(1),[IntLiteral(1)])]),([],[Dowhile(([],[CallStmt(Id("print"),[Id("x")])]),BooleanLiteral(True))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_simple_program_28(self):
        input = """
        Var: x = True;
        Function: main
        Body:
            For(x = True +. False, b__({1, 1.}), x *. (y -. z)) Do
                Var: i = 0;
                While i < 5 Do
                    a[i] = b +. 1.0;
                    i = i + 1;
                EndWhile.
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],BooleanLiteral(True)),FuncDecl(Id("main"),[],([],[For(Id("x"),BinaryOp("+.",BooleanLiteral(True),BooleanLiteral(False)),CallExpr(Id("b__"),[ArrayLiteral([IntLiteral(1),FloatLiteral(1.0)])]),BinaryOp("*.",Id("x"),BinaryOp("-.",Id("y"),Id("z"))),([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_simple_program_29(self):
        input = """
        Var: x, y[0x22];
        Function: foo
        Body:
            For(i = 0., i >. 1 \. 2, 1 && 2 <= 2 *. 3) Do
                x = 0[0] == 3 % 2;
                y = ! ! x -. -. y;
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[34],None),FuncDecl(Id("foo"),[],([],[For(Id("i"),FloatLiteral(0.0),BinaryOp(">.",Id("i"),BinaryOp("\.",IntLiteral(1),IntLiteral(2))),BinaryOp("<=",BinaryOp("&&",IntLiteral(1),IntLiteral(2)),BinaryOp("*.",IntLiteral(2),IntLiteral(3))),([],[Assign(Id("x"),BinaryOp("==",ArrayCell(IntLiteral(0),[IntLiteral(0)]),BinaryOp("%",IntLiteral(3),IntLiteral(2)))),Assign(Id("y"),BinaryOp("-.",UnaryOp("!",UnaryOp("!",Id("x"))),UnaryOp("-.",Id("y"))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_simple_program_30(self):
        input = """
        Var: x, y = {1,1.e-1};
        Function: main
        Body:
            For(i = foo()[2], -. x - y, x +. y - z) Do
                For(i = {{1},{"Hi"}}, 0[foo(1*****2)],1 > -1[2]) Do
                    print(2 \.*** ** 3 ** ***. 4);
                EndFor.
            EndFor.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],ArrayLiteral([IntLiteral(1),FloatLiteral(0.1)])),FuncDecl(Id("main"),[],([],[For(Id("i"),ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(2)]),BinaryOp("-",UnaryOp("-.",Id("x")),Id("y")),BinaryOp("-",BinaryOp("+.",Id("x"),Id("y")),Id("z")),([],[For(Id("i"),ArrayLiteral([ArrayLiteral([IntLiteral(1)]),ArrayLiteral([StringLiteral("Hi")])]),ArrayCell(IntLiteral(0),[CallExpr(Id("foo"),[BinaryOp("*",IntLiteral(1),IntLiteral(2))])]),BinaryOp(">",IntLiteral(1),UnaryOp("-",ArrayCell(IntLiteral(1),[IntLiteral(2)]))),([],[CallStmt(Id("print"),[BinaryOp("*.",BinaryOp("\.",IntLiteral(2),IntLiteral(3)),IntLiteral(4))])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_simple_program_31(self):
        input = """
        Var: x, y = 1.2E-2;
        Function: main
        Body:
            While (0 && True) Do
                While 1 + -. 2.0["Hi"] Do
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],FloatLiteral(1.2E-2)),FuncDecl(Id("main"),[],([],[While(BinaryOp("&&",IntLiteral(0),BooleanLiteral(True)),([],[While(BinaryOp("+",IntLiteral(1),UnaryOp("-.",ArrayCell(FloatLiteral(2.0),[StringLiteral("Hi")]))),([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_simple_program_32(self):
        input = """
        Var: x, t = {"True",****"False"};
        Function: main
        Body:
            While x == (1 == 2) && 2 Do
                Do x = ! foo(-1 -. -2); Break; While !(!True >= 2)
                EndDo.
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("t"),[],ArrayLiteral([StringLiteral("True"),StringLiteral("False")])),FuncDecl(Id("main"),[],([],[While(BinaryOp("==",Id("x"),BinaryOp("&&",BinaryOp("==",IntLiteral(1),IntLiteral(2)),IntLiteral(2))),([],[Dowhile(([],[Assign(Id("x"),UnaryOp("!",CallExpr(Id("foo"),[BinaryOp("-.",UnaryOp("-",IntLiteral(1)),UnaryOp("-",IntLiteral(2)))]))),Break()]),UnaryOp("!",BinaryOp(">=",UnaryOp("!",BooleanLiteral(True)),IntLiteral(2))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_simple_program_33(self):
        input = """
        Var: x = 0x1255;
        Function: main
        Body:
            While foo()[foo()] -. ! -. True Do
                a = int_of_string (read ());
                b = float_of_int (a) +. 2.0;
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(4693)),FuncDecl(Id("main"),[],([],[While(BinaryOp("-.",ArrayCell(CallExpr(Id("foo"),[]),[CallExpr(Id("foo"),[])]),UnaryOp("!",UnaryOp("-.",BooleanLiteral(True)))),([],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_simple_program_34(self):
        input = """
        Var: x, y[0x12], z = "Hello!";
        Function: fact
            Parameter: n[0x12]
            Body:
                While -1 Do
                    a1();
                EndWhile.
            EndBody.
        Function: main
            Body:
                x = (1);
                Return z == 3;
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[18],None),VarDecl(Id("z"),[],StringLiteral("Hello!")),FuncDecl(Id("fact"),[VarDecl(Id("n"),[18],None)],([],[While(UnaryOp("-",IntLiteral(1)),([],[CallStmt(Id("a1"),[])]))])),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(1)),Return(BinaryOp("==",Id("z"),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_simple_program_35(self):
        input = """
        Var: x, y = {0xFF};
        Function: main
        Body:
            While 0xABCD * 0o7777 Do
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
            EndWhile.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],ArrayLiteral([IntLiteral(255)])),FuncDecl(Id("main"),[],([],[While(BinaryOp("*",IntLiteral(43981),IntLiteral(4095)),([VarDecl(Id("r"),[],FloatLiteral(10.0)),VarDecl(Id("v"),[],None)],[Assign(Id("v"),BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("\.",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id("r")),Id("r")),Id("r")))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_simple_program_36(self):
        input = """
        Var: x = 0xEEEE;
        Function: main
        Parameter: x[0o1111]
        Body:
            Var: x = 1.E-1000;
            While -. foo({""}) \ {} Do
                If x != 2 Then
                ElseIf x == 2 Then
                EndIf.
            EndWhile. 
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],IntLiteral(61166)),FuncDecl(Id("main"),[VarDecl(Id("x"),[0o1111],None)],([VarDecl(Id("x"),[],FloatLiteral(0.0))],[While(BinaryOp("\\",UnaryOp("-.",CallExpr(Id("foo"),[ArrayLiteral([StringLiteral("")])])),ArrayLiteral([])),([],[If([(BinaryOp("!=",Id("x"),IntLiteral(2)),[],[]),(BinaryOp("==",Id("x"),IntLiteral(2)),[],[])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_simple_program_37(self):
        input = """
        Function: main
        Body:
            While x Do
                Var: x = 0xCCCC;
                x = x != (1 < 2);
                Break;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(Id("x"),([VarDecl(Id("x"),[],IntLiteral(52428))],[Assign(Id("x"),BinaryOp("!=",Id("x"),BinaryOp("<",IntLiteral(1),IntLiteral(2)))),Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_simple_program_38(self):
        input = """
        Function: main
        Body:
            While x Do
                While y Do
                    While z Do
                        z[y[x][t]] = z < 2 - 3;
                    EndWhile.
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(Id("x"),([],[While(Id("y"),([],[While(Id("z"),([],[Assign(ArrayCell(Id("z"),[ArrayCell(Id("y"),[Id("x"),Id("t")])]),BinaryOp("<",Id("z"),BinaryOp("-",IntLiteral(2),IntLiteral(3))))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_simple_program_39(self):
        input = """
        Function: foo
        Body:
            While -. foo(0[0]) Do
                x[0x22] = 12.0[1>2]>3;
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[While(UnaryOp("-.",CallExpr(Id("foo"),[ArrayCell(IntLiteral(0),[IntLiteral(0)])])),([],[Assign(ArrayCell(Id("x"),[IntLiteral(34)]),BinaryOp(">",ArrayCell(FloatLiteral(12.0),[BinaryOp(">",IntLiteral(1),IntLiteral(2))]),IntLiteral(3)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_simple_program_40(self):
        input = """
        Function: main
        Body:
            While "" Do
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(StringLiteral(""),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_simple_program_41(self):
        input = """
        Var: x, y = {0.1234e-1000};
        Function: main
        Body:
            Do
                While 1 + -. 2.0["Hi"] Do
                EndWhile.
            While "abc"[123]
            EndDo.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],ArrayLiteral([FloatLiteral(0.0)])),FuncDecl(Id("main"),[],([],[Dowhile(([],[While(BinaryOp("+",IntLiteral(1),UnaryOp("-.",ArrayCell(FloatLiteral(2.0),[StringLiteral("Hi")]))),([],[]))]),ArrayCell(StringLiteral("abc"),[IntLiteral(123)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_simple_program_42(self):
        input = """
        Function: main
        Body:
            While x == (1 == 2) && 2 Do
                Var: x[0xFFF];
                Do 
                    Continue;
                    While foo()[2] > 0[2] Do
                        foo (2 + x, 4. \. y);
                    EndWhile. 
                While !(!True >= 2)
                EndDo.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[While(BinaryOp("==",Id("x"),BinaryOp("&&",BinaryOp("==",IntLiteral(1),IntLiteral(2)),IntLiteral(2))),([VarDecl(Id("x"),[0xFFF],None)],[Dowhile(([],[Continue(),While(BinaryOp(">",ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(2)]),ArrayCell(IntLiteral(0),[IntLiteral(2)])),([],[CallStmt(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("x")),BinaryOp("\\.",FloatLiteral(4.0),Id("y"))])]))]),UnaryOp("!",BinaryOp(">=",UnaryOp("!",BooleanLiteral(True)),IntLiteral(2))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_simple_program_43(self):
        input = """
        Var: x = {0x1, 0o1, "1", 1, True};
        Function: main
        Body:
            If "True" Then
                foo(x[{1.2e-3}], y[0x12] + 1.);
            Else
                While "False" Do
                    foo(x - {1,"foo"} == 1, 1>0[0]);
                EndWhile.
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],ArrayLiteral([IntLiteral(1),IntLiteral(1),StringLiteral("1"),IntLiteral(1),BooleanLiteral(True)])),FuncDecl(Id("main"),[],([],[If([(StringLiteral("True"),[],[CallStmt(Id("foo"),[ArrayCell(Id("x"),[ArrayLiteral([FloatLiteral(0.0012)])]),BinaryOp("+",ArrayCell(Id("y"),[IntLiteral(18)]),FloatLiteral(1.0))])])],([],[While(StringLiteral("False"),([],[CallStmt(Id("foo"),[BinaryOp("==",BinaryOp("-",Id("x"),ArrayLiteral([IntLiteral(1),StringLiteral("foo")])),IntLiteral(1)),BinaryOp(">",IntLiteral(1),ArrayCell(IntLiteral(0),[IntLiteral(0)]))])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_simple_program_44(self):
        input = """
        Var: x;
        Function: fact
            Parameter: n[0xFFFFFFFF]
            Body:
                Do 
                    foo(x,y,z,t);
                While -2 > -3
                EndDo.
            EndBody.
        Function: main
            Body:
                Return fact() == (3 > 2)[1];
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[0xFFFFFFFF],None)],([],[Dowhile(([],[CallStmt(Id("foo"),[Id("x"),Id("y"),Id("z"),Id("t")])]),BinaryOp(">",UnaryOp("-",IntLiteral(2)),UnaryOp("-",IntLiteral(3))))])),FuncDecl(Id("main"),[],([],[Return(BinaryOp("==",CallExpr(Id("fact"),[]),ArrayCell(BinaryOp(">",IntLiteral(3),IntLiteral(2)),[IntLiteral(1)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_simple_program_45(self):
        input = """
        Function: foo
        Body:
            Var: x = True;
            x = x && (foo(1) || False);
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([VarDecl(Id("x"),[],BooleanLiteral(True))],[Assign(Id("x"),BinaryOp("&&",Id("x"),BinaryOp("||",CallExpr(Id("foo"),[IntLiteral(1)]),BooleanLiteral(False))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_simple_program_46(self):
        input = """
        Function: print
        Parameter: arr[5], vec[5], x
        Body:
            x = !arr[0]; 
            print(arr[vec[1][x]]);
        EndBody.
        """
        expect = Program([FuncDecl(Id("print"),[VarDecl(Id("arr"),[5],None),VarDecl(Id("vec"),[5],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("x"),UnaryOp("!",ArrayCell(Id("arr"),[IntLiteral(0)]))),CallStmt(Id("print"),[ArrayCell(Id("arr"),[ArrayCell(Id("vec"),[IntLiteral(1),Id("x")])])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_simple_program_47(self):
        input = """
        Function: neg
        Parameter: x
        Body: 
            x = --(-x);
            Return -abs(x);
        EndBody.
        """
        expect = Program([FuncDecl(Id("neg"),[VarDecl(Id("x"),[],None)],([],[Assign(Id("x"),UnaryOp("-",UnaryOp("-",UnaryOp("-",Id("x"))))),Return(UnaryOp("-",CallExpr(Id("abs"),[Id("x")])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_simple_program_48(self):
        input = """
        Function: main
        Body: 
            print(foo(2) || 1.0 -. 0.5 == 0.5);
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("print"),[BinaryOp("==",BinaryOp("||",CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("-.",FloatLiteral(1.0),FloatLiteral(0.5))),FloatLiteral(0.5))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_simple_program_49(self):
        input = """
        Function: main
        Body: 
            foo("True")[1.0] = "He asked me: '"Where is John?'"";
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(ArrayCell(CallExpr(Id("foo"),[StringLiteral("True")]),[FloatLiteral(1.0)]),StringLiteral("He asked me: '\"Where is John?'\""))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_simple_program_50(self):
        input = """
        Function: init
        Body: 
            If abs(foo(x))[1][1] =/= -1.e-2 Then
                For (i = 1, i <. 2.5, 1) Do
                    push(array, i);
                EndFor.
            EndIf.
            Return;
        EndBody.
        """
        expect = Program([FuncDecl(Id("init"),[],([],[If([(BinaryOp("=/=",ArrayCell(CallExpr(Id("abs"),[CallExpr(Id("foo"),[Id("x")])]),[IntLiteral(1),IntLiteral(1)]),UnaryOp("-",FloatLiteral(0.01))),[],[For(Id("i"),IntLiteral(1),BinaryOp("<.",Id("i"),FloatLiteral(2.5)),IntLiteral(1),([],[CallStmt(Id("push"),[Id("array"),Id("i")])]))])],([],[])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_simple_program_51(self):
        input = """
        Function: main
        Parameter: a[5]
        Body: 
            For (i = 1 + foo(2), 1.0 <. 2.0, foo(2)[2]) Do
                ** This is a comment
                * multi-line.
                **
                While !1 > 2 Do
                    Iff Then
                        Var: x = {{1}};
                        ** Var declaration **
                    EndIf.
                EndWhile.
            EndFor.            
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("a"),[5],None)],([],[For(Id("i"),BinaryOp("+",IntLiteral(1),CallExpr(Id("foo"),[IntLiteral(2)])),BinaryOp("<.",FloatLiteral(1.0),FloatLiteral(2.0)),ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),[IntLiteral(2)]),([],[While(BinaryOp(">",UnaryOp("!",IntLiteral(1)),IntLiteral(2)),([],[If([(Id("f"),[VarDecl(Id("x"),[],ArrayLiteral([ArrayLiteral([IntLiteral(1)])]))],[])],([],[]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_simple_program_52(self):
        input = """
        Function: square
            Parameter: x
            Body:
                If x == 1 Then
                    Return 1;
                Else 
                    Return sqrt(x + square(x - 1));
                EndIf.
            EndBody.
        Function: main
            Body:
                Var: x = 10;
                writeln(square(x));
            EndBody.
        """
        expect = Program([FuncDecl(Id("square"),[VarDecl(Id("x"),[],None)],([],[If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Return(IntLiteral(1))])],([],[Return(CallExpr(Id("sqrt"),[BinaryOp("+",Id("x"),CallExpr(Id("square"),[BinaryOp("-",Id("x"),IntLiteral(1))]))]))]))])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(10))],[CallStmt(Id("writeln"),[CallExpr(Id("square"),[Id("x")])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_simple_program_53(self):
        input = """
            Function: test
            Parameter: num
            Body:
                Var: sum = 0;
                For (i = num, i < sqr(num), 2) Do
                    sum = 123[1[1][1][1][1][1][1][1]][i];
                EndFor.
                Return sum;
            EndBody."""
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("num"),[],None)],([VarDecl(Id("sum"),[],IntLiteral(0))],[For(Id("i"),Id("num"),BinaryOp("<",Id("i"),CallExpr(Id("sqr"),[Id("num")])),IntLiteral(2),([],[Assign(Id("sum"),ArrayCell(IntLiteral(123),[ArrayCell(IntLiteral(1),[IntLiteral(1),IntLiteral(1),IntLiteral(1),IntLiteral(1),IntLiteral(1),IntLiteral(1),IntLiteral(1)]),Id("i")]))])),Return(Id("sum"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_simple_program_54(self):
        input = """
        Function: foo 
        Body: 
            a = 1 + 1.23 *. abc \. id[12[123][2][moreid]];
            b = 1.E-12  =/= foo(123);
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("a"),BinaryOp("+",IntLiteral(1),BinaryOp("\.",BinaryOp("*.",FloatLiteral(1.23),Id("abc")),ArrayCell(Id("id"),[ArrayCell(IntLiteral(12),[IntLiteral(123),IntLiteral(2),Id("moreid")])])))),Assign(Id("b"),BinaryOp("=/=",FloatLiteral(1e-12),CallExpr(Id("foo"),[IntLiteral(123)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_simple_program_55(self):
        input = """
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
        expect = Program([VarDecl(Id("string"),[3],ArrayLiteral([StringLiteral("1.23"),StringLiteral("0.e4"),StringLiteral("12e2")])),FuncDecl(Id("test"),[],([VarDecl(Id("x"),[3],None),VarDecl(Id("sum"),[],FloatLiteral(0.0))],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(3)),IntLiteral(1),([],[Assign(ArrayCell(Id("x"),[Id("i")]),CallExpr(Id("float"),[ArrayCell(Id("string"),[Id("i")])])),Assign(Id("sum"),BinaryOp("+",Id("sum"),ArrayCell(Id("x"),[Id("i")])))])),Return(Id("sum"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_simple_program_56(self):
        input = """
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
        expect = Program([FuncDecl(Id("main"),[],([],[CallStmt(Id("foo"),[BinaryOp("+",IntLiteral(3),BinaryOp("*",ArrayCell(Id("x"),[Id("i")]),CallExpr(Id("y"),[IntLiteral(3),CallExpr(Id("z"),[IntLiteral(4)])])))]),If([(UnaryOp("!",Id("foo")),[],[Return(BooleanLiteral(False))])],([],[])),For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(100)),IntLiteral(2),([],[CallStmt(Id("writeln"),[BinaryOp("*",CallExpr(Id("sqrt"),[Id("i")]),ArrayCell(Id("test"),[IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(4)])]))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_simple_program_57(self):
        input = """
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
        expect = Program([FuncDecl(Id("prime_number"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("<",Id("n"),IntLiteral(2)),[],[Return(BooleanLiteral(False))])],([],[])),If([(BinaryOp("||",BinaryOp("==",Id("n"),IntLiteral(2)),BinaryOp("==",Id("n"),IntLiteral(3))),[],[Return(BooleanLiteral(True))])],([],[])),For(Id("i"),IntLiteral(2),BinaryOp("<",Id("i"),Id("n")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),[],[Return(BooleanLiteral(False))])],([],[]))])),Return(BooleanLiteral(True))])),FuncDecl(Id("main"),[],([VarDecl(Id("a"),[100],None)],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(100)),IntLiteral(1),([],[CallStmt(Id("input"),[ArrayCell(Id("a"),[Id("i")])]),If([(BinaryOp("&&",CallExpr(Id("prime_number"),[ArrayCell(Id("a"),[Id("i")])]),BinaryOp("!=",BinaryOp("%",ArrayCell(Id("a"),[Id("i")]),IntLiteral(2)),IntLiteral(0))),[],[CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")])])])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_simple_program_58(self):
        input = """
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
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))])),FuncDecl(Id("main"),[],([VarDecl(Id("r"),[],FloatLiteral(10.0)),VarDecl(Id("v"),[],None)],[Assign(Id("v"),BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("\.",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id("r")),Id("r")),Id("r"))),If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))])],([],[])),For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("writeln"),[Id("i")])])),Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_simple_program_59(self):
        input = """
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
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("a___b"),[],IntLiteral(12345)),VarDecl(Id("b"),[],BooleanLiteral(True)),VarDecl(Id("c"),[],FloatLiteral(123.0))],[If([(Id("b"),[],[Assign(Id("c"),BinaryOp("+.",Id("c"),FloatLiteral(1.0)))]),(UnaryOp("!",Id("b")),[],[Return(Id("c"))])],([],[])),Return(BinaryOp("+",CallExpr(Id("float"),[Id("a___b")]),Id("c")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_simple_program_60(self):
        input = """
        Function: main
            Body:
                Return a(b(c(d(e(f(1123 + True + fo(z(f(f)))))))));
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[Return(CallExpr(Id("a"),[CallExpr(Id("b"),[CallExpr(Id("c"),[CallExpr(Id("d"),[CallExpr(Id("e"),[CallExpr(Id("f"),[BinaryOp("+",BinaryOp("+",IntLiteral(1123),BooleanLiteral(True)),CallExpr(Id("fo"),[CallExpr(Id("z"),[CallExpr(Id("f"),[Id("f")])])]))])])])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_simple_program_61(self):
        input = """
    Function: foo 
        Body: 
            Var: a,b = True,c;
            do_something();

            For (it=0, 0, 0) Do
                Var: d,e,f;
                do_something();

                While (abcd) Do
                    Var: g,h,i;
                    do_something();

                    If True Then
                        Var: o,f,f;
                        do_something();
                    ElseIf d Then
                        Var: f,f;
                        do_something();
                    Else
                        Var: d,o,w,n;
                        do_something();
                    EndIf.
                EndWhile.
            EndFor.
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],BooleanLiteral(True)),VarDecl(Id("c"),[],None)],[CallStmt(Id("do_something"),[]),For(Id("it"),IntLiteral(0),IntLiteral(0),IntLiteral(0),([VarDecl(Id("d"),[],None),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None)],[CallStmt(Id("do_something"),[]),While(Id("abcd"),([VarDecl(Id("g"),[],None),VarDecl(Id("h"),[],None),VarDecl(Id("i"),[],None)],[CallStmt(Id("do_something"),[]),If([(BooleanLiteral(True),[VarDecl(Id("o"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("f"),[],None)],[CallStmt(Id("do_something"),[])]),(Id("d"),[VarDecl(Id("f"),[],None),VarDecl(Id("f"),[],None)],[CallStmt(Id("do_something"),[])])],([VarDecl(Id("d"),[],None),VarDecl(Id("o"),[],None),VarDecl(Id("w"),[],None),VarDecl(Id("n"),[],None)],[CallStmt(Id("do_something"),[])]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_simple_program_62(self):
        input = """
        Function: foo
            Body:
                Return;
                Return True;
                For (qbc = 321, (True || False), 123) Do
                    Return;
                    Return (999);
                EndFor.

                While False Do
                    If (abc) Then
                        Return
                        ;
                    ElseIf def Then
                        Return "somes tring"   ;
                    Else Break;
                    EndIf.
                EndWhile.

                Do 
                    Return xas \ a \. h *. c +. n \ "string";
                    Return;
                While True
                EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[],([],[Return(None),Return(BooleanLiteral(True)),For(Id("qbc"),IntLiteral(321),BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)),IntLiteral(123),([],[Return(None),Return(IntLiteral(999))])),While(BooleanLiteral(False),([],[If([(Id("abc"),[],[Return(None)]),(Id("def"),[],[Return(StringLiteral("somes tring"))])],([],[Break()]))])),Dowhile(([],[Return(BinaryOp("+.",BinaryOp("*.",BinaryOp("\.",BinaryOp("\\",Id("xas"),Id("a")),Id("h")),Id("c")),BinaryOp("\\",Id("n"),StringLiteral("string")))),Return(None)]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_simple_program_63(self):
        input = """
            Function: foo
            Body:
                Break;
                Continue;
                For (qbc = 321, (True || False), 123) Do
                    Break;
                    Continue;
                EndFor.

                While False Do
                    If (abc) Then
                        Break
                        ;
                    ElseIf def Then
                        Continue   ;
                    Else Break;
                    EndIf.
                EndWhile.

                Do 
                    Break;
                    Continue;
                While True
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Break(),Continue(),For(Id("qbc"),IntLiteral(321),BinaryOp("||",BooleanLiteral(True),BooleanLiteral(False)),IntLiteral(123),([],[Break(),Continue()])),While(BooleanLiteral(False),([],[If([(Id("abc"),[],[Break()]),(Id("def"),[],[Continue()])],([],[Break()]))])),Dowhile(([],[Break(),Continue()]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_simple_program_64(self):
        input = """
        Function: foo 
        Body: 
            123[9[8][7]] = 123 * 123[abc] + foo() - oo || whoop(a > b[False], c, d);
            arr[123456 *. 654321] = 123 * 123 + foo() - oo || whoop(a > b, c, d);
            more_arr[ foo() || 123456 *. 654321] = 123 * 123 + foo() - oo || whoop(a > b, c, d);
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(ArrayCell(IntLiteral(123),[ArrayCell(IntLiteral(9),[IntLiteral(8),IntLiteral(7)])]),BinaryOp("||",BinaryOp("-",BinaryOp("+",BinaryOp("*",IntLiteral(123),ArrayCell(IntLiteral(123),[Id("abc")])),CallExpr(Id("foo"),[])),Id("oo")),CallExpr(Id("whoop"),[BinaryOp(">",Id("a"),ArrayCell(Id("b"),[BooleanLiteral(False)])),Id("c"),Id("d")]))),Assign(ArrayCell(Id("arr"),[BinaryOp("*.",IntLiteral(123456),IntLiteral(654321))]),BinaryOp("||",BinaryOp("-",BinaryOp("+",BinaryOp("*",IntLiteral(123),IntLiteral(123)),CallExpr(Id("foo"),[])),Id("oo")),CallExpr(Id("whoop"),[BinaryOp(">",Id("a"),Id("b")),Id("c"),Id("d")]))),Assign(ArrayCell(Id("more_arr"),[BinaryOp("||",CallExpr(Id("foo"),[]),BinaryOp("*.",IntLiteral(123456),IntLiteral(654321)))]),BinaryOp("||",BinaryOp("-",BinaryOp("+",BinaryOp("*",IntLiteral(123),IntLiteral(123)),CallExpr(Id("foo"),[])),Id("oo")),CallExpr(Id("whoop"),[BinaryOp(">",Id("a"),Id("b")),Id("c"),Id("d")])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_simple_program_65(self):
        input = """
            Function: foo 
                Parameter: something, more
                Body:
                    While (something > more) Do
                        While (abc + 123 \ 321) Do
                            more = more + something;
                            do_something();
                        EndWhile.
                    EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("something"),[],None),VarDecl(Id("more"),[],None)],([],[While(BinaryOp(">",Id("something"),Id("more")),([],[While(BinaryOp("+",Id("abc"),BinaryOp("\\",IntLiteral(123),IntLiteral(321))),([],[Assign(Id("more"),BinaryOp("+",Id("more"),Id("something"))),CallStmt(Id("do_something"),[])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_simple_program_66(self):
        input = """
            Function: foo
            Parameter: a[2], b
            Body:
                For (i = 0, i < 2, 1) Do
                    If a[i] > b Then writeln(a[i], " is larger than ", b);
                    ElseIf a[i] == b Then writeln(a[i], " equal ", b);
                    Else writeln(a[i], " is smaller than ", b);
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[2],None),VarDecl(Id("b"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(2)),IntLiteral(1),([],[If([(BinaryOp(">",ArrayCell(Id("a"),[Id("i")]),Id("b")),[],[CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is larger than "),Id("b")])]),(BinaryOp("==",ArrayCell(Id("a"),[Id("i")]),Id("b")),[],[CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" equal "),Id("b")])])],([],[CallStmt(Id("writeln"),[ArrayCell(Id("a"),[Id("i")]),StringLiteral(" is smaller than "),Id("b")])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_simple_program_67(self):
        input = """
            Function: foo
            Parameter: x, y
            Body:
                writeln(foo(2 + x, 4. \. y) * goo());
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],([],[CallStmt(Id("writeln"),[BinaryOp("*",CallExpr(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("x")),BinaryOp("\\.",FloatLiteral(4.0),Id("y"))]),CallExpr(Id("goo"),[]))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_simple_program_68(self):
        input = """
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
        expect = Program([FuncDecl(Id("printDivivsors"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),Id("n")),IntLiteral(1),([],[If([(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),[],[CallStmt(Id("writeln"),[Id("i")])])],([],[]))]))])),FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],None)],[CallStmt(Id("input"),[Id("x")]),CallStmt(Id("printDivivsors"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_simple_program_69(self):
        input = """
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
        expect = Program([FuncDecl(Id("power_rep"),[VarDecl(Id("base"),[],None),VarDecl(Id("exp"),[],None)],([VarDecl(Id("a"),[],IntLiteral(2))],[If([(BinaryOp("==",Id("exp"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[])),For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),BinaryOp("-",Id("exp"),IntLiteral(1))),IntLiteral(1),([],[Assign(Id("base"),BinaryOp("*",Id("base"),Id("a")))])),Return(Id("base"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_simple_program_70(self):
        input = """
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
        expect = Program([FuncDecl(Id("power_rep"),[VarDecl(Id("base"),[],None),VarDecl(Id("exp"),[],None)],([VarDecl(Id("a"),[],IntLiteral(2))],[If([(BinaryOp("==",Id("exp"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[])),For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),BinaryOp("-",Id("exp"),IntLiteral(1))),IntLiteral(1),([],[Assign(Id("base"),BinaryOp("*",Id("base"),Id("a")))])),Return(Id("base"))])),FuncDecl(Id("power_recur"),[VarDecl(Id("base"),[],None),VarDecl(Id("exp"),[],None)],([],[If([(BinaryOp("==",Id("exp"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[])),Return(BinaryOp("*",Id("base"),CallExpr(Id("power_recur"),[Id("base"),BinaryOp("-",Id("exp"),IntLiteral(1))])))])),FuncDecl(Id("main"),[VarDecl(Id("base"),[],None),VarDecl(Id("exp"),[],None)],([],[Assign(Id("base"),CallExpr(Id("input"),[])),Assign(Id("exp"),CallExpr(Id("input"),[])),CallStmt(Id("writeln"),[CallExpr(Id("power_rep"),[Id("base"),Id("exp")])]),CallStmt(Id("writeln"),[CallExpr(Id("power_recur"),[Id("base"),Id("exp")])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_simple_program_71(self):
        input = """
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
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("answer"),[],None),VarDecl(Id("length"),[],None),VarDecl(Id("jump_max"),[],None),VarDecl(Id("arr"),[10],None),VarDecl(Id("a"),[],None),VarDecl(Id("j"),[],None)],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),Id("length")),IntLiteral(1),([],[Assign(ArrayCell(Id("arr"),[Id("i")]),CallExpr(Id("input"),[]))])),For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),Id("length")),IntLiteral(1),([],[If([(BinaryOp("&&",BinaryOp(">=",BinaryOp("+",Id("a"),Id("jump_max")),ArrayCell(Id("arr"),[Id("i")])),BinaryOp("<",BinaryOp("+",Id("a"),Id("jump_max")),ArrayCell(Id("arr"),[BinaryOp("+",Id("i"),IntLiteral(1))]))),[],[Assign(Id("a"),ArrayCell(Id("arr"),[Id("i")])),Assign(Id("answer"),BinaryOp("+",Id("answer"),IntLiteral(1)))])],([],[]))])),If([(BinaryOp("!=",Id("j"),BinaryOp("-",Id("length"),IntLiteral(1))),[],[Assign(Id("answer"),UnaryOp("-",IntLiteral(1)))])],([],[])),If([(BinaryOp(">=",BinaryOp("+",Id("a"),Id("jump_max")),ArrayCell(Id("arr"),[BinaryOp("-",Id("length"),IntLiteral(1))])),[],[Assign(Id("answer"),BinaryOp("+",Id("answer"),IntLiteral(1)))])],([],[Assign(Id("answer"),UnaryOp("-",IntLiteral(1)))])),CallStmt(Id("writeln"),[Id("answer")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_simple_program_72(self):
        input = """
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
        expect = Program([FuncDecl(Id("longest_substr"),[VarDecl(Id("str"),[],None)],([VarDecl(Id("count"),[],IntLiteral(0)),VarDecl(Id("check"),[],BooleanLiteral(False))],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),CallExpr(Id("length"),[Id("str")])),IntLiteral(1),([],[For(Id("j"),IntLiteral(0),BinaryOp("<",Id("j"),CallExpr(Id("length"),[Id("str")])),IntLiteral(1),([],[If([(BinaryOp("&&",BinaryOp("==",ArrayCell(Id("str"),[Id("i")]),ArrayCell(Id("str"),[Id("j")])),BinaryOp("!=",Id("i"),Id("j"))),[],[Assign(Id("check"),BooleanLiteral(True)),Break()])],([],[])),If([(Id("check"),[],[Assign(Id("check"),BooleanLiteral(False))])],([],[])),Continue()])),Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))])),Return(Id("count"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_simple_program_73(self):
        input = """
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
            EndBody."""
        expect = Program([FuncDecl(Id("uoc_chung_lon_nhat"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([],[If([(BinaryOp("==",Id("a"),Id("b")),[],[Return(Id("a"))])],([],[])),If([(BinaryOp(">",Id("a"),Id("b")),[],[Assign(Id("a"),BinaryOp("%",Id("a"),Id("b")))])],([],[])),If([(BinaryOp("==",Id("a"),IntLiteral(0)),[],[Return(Id("b"))])],([],[])),Return(CallExpr(Id("uoc_chung_lon_nhat"),[Id("b"),Id("a")]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_simple_program_74(self):
        input = """
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
        expect = Program([FuncDecl(Id("reverseString"),[VarDecl(Id("initialString"),[],None)],([],[If([(BinaryOp("==",Id("initialString"),Id("nullptr")),[],[Return(None)])],([],[])),If([(BinaryOp("==",CallExpr(Id("strlen"),[Id("initialString")]),IntLiteral(1)),[],[CallStmt(Id("writeln"),[ArrayCell(Id("initialString"),[IntLiteral(0)])]),Return(None)])],([],[])),CallStmt(Id("writeln"),[ArrayCell(Id("initialString"),[BinaryOp("-",CallExpr(Id("strlen"),[Id("initialString")]),IntLiteral(1))])]),Assign(ArrayCell(Id("initialString"),[BinaryOp("-",CallExpr(Id("strlen"),[Id("initialString")]),IntLiteral(1))]),IntLiteral(0)),CallStmt(Id("reverseString"),[Id("initialString")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_simple_program_75(self):
        input = """
            Var: arr[5][6]=1.e790,b,c=2;
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
                EndBody.
        """
        expect = Program([VarDecl(Id("arr"),[5,6],FloatLiteral(1.e790)),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],IntLiteral(2)),VarDecl(Id("x"),[],None),FuncDecl(Id("tEST_function_Name_1"),[VarDecl(Id("x"),[100],None)],([],[Dowhile(([],[Assign(Id("x"),BinaryOp("+",Id("x"),CallExpr(Id("foo"),[BinaryOp("+.",BinaryOp("+",IntLiteral(267),ArrayCell(Id("a"),[IntLiteral(6)])),FloatLiteral(1.0))]))),Assign(Id("x"),BinaryOp("%",Id("x"),IntLiteral(2))),If([(BinaryOp(">=",Id("i"),IntLiteral(9)),[],[CallStmt(Id("writeln"),[BinaryOp("+",Id("a"),IntLiteral(7))])])],([],[]))]),BinaryOp("<=",Id("i"),IntLiteral(27)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_simple_program_76(self):
        input = """
            Function: foo 
            Parameter: abc 
            Body: 
            EndBody. 
            Function: foo 
            Body: EndBody.
            Function: goo 
            Parameter: abc 
            Body: 
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("abc"),[],None)],([],[])),FuncDecl(Id("foo"),[],([],[])),FuncDecl(Id("goo"),[VarDecl(Id("abc"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_simple_program_77(self):
        input = """
            Function: tEST_function_Name_2
                Parameter: x,a[69],b[1][2][3]
                Body:
                    For (i=1, goo(2+a[6]) < i,2>goo(9)) Do
                        If arr[7] >= foo(3) Then
                            Break;
                        EndIf.
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("tEST_function_Name_2"),[VarDecl(Id("x"),[],None),VarDecl(Id("a"),[69],None),VarDecl(Id("b"),[1,2,3],None)],([],[For(Id("i"),IntLiteral(1),BinaryOp("<",CallExpr(Id("goo"),[BinaryOp("+",IntLiteral(2),ArrayCell(Id("a"),[IntLiteral(6)]))]),Id("i")),BinaryOp(">",IntLiteral(2),CallExpr(Id("goo"),[IntLiteral(9)])),([],[If([(BinaryOp(">=",ArrayCell(Id("arr"),[IntLiteral(7)]),CallExpr(Id("foo"),[IntLiteral(3)])),[],[Break()])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_simple_program_78(self):
        input = """
            Function: test
            Parameter: num
            Body:
                For (i = num * 2, i < num * num, i + 1) Do
                    If i % 2 == 0 Then
                        writeln(a * i);
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("num"),[],None)],([],[For(Id("i"),BinaryOp("*",Id("num"),IntLiteral(2)),BinaryOp("<",Id("i"),BinaryOp("*",Id("num"),Id("num"))),BinaryOp("+",Id("i"),IntLiteral(1)),([],[If([(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),[],[CallStmt(Id("writeln"),[BinaryOp("*",Id("a"),Id("i"))])])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_simple_program_79(self):
        input = """
            Var: a = True, b = {1,2}, c = {{True, False}, {1.e2, 2e2}};
            Function: test
            Parameter: num
            Body:
                Var: sum = 0;
                For (i = num, i < sqr(num), 2) Do
                    sum = sum + i * i;
                EndFor.
                Return sum;
            EndBody.
        """
        expect = Program([VarDecl(Id("a"),[],BooleanLiteral(True)),VarDecl(Id("b"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("c"),[],ArrayLiteral([ArrayLiteral([BooleanLiteral(True),BooleanLiteral(False)]),ArrayLiteral([FloatLiteral(100.0),FloatLiteral(200.0)])])),FuncDecl(Id("test"),[VarDecl(Id("num"),[],None)],([VarDecl(Id("sum"),[],IntLiteral(0))],[For(Id("i"),Id("num"),BinaryOp("<",Id("i"),CallExpr(Id("sqr"),[Id("num")])),IntLiteral(2),([],[Assign(Id("sum"),BinaryOp("+",Id("sum"),BinaryOp("*",Id("i"),Id("i"))))])),Return(Id("sum"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_simple_program_80(self):
        input = """
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
        expect = Program([FuncDecl(Id("main"),[],([VarDecl(Id("i"),[],None),VarDecl(Id("n"),[],None)],[Dowhile(([],[CallStmt(Id("writeln"),[StringLiteral("Input n: ")]),CallStmt(Id("input"),[Id("n")]),If([(BinaryOp("<=",Id("n"),IntLiteral(0)),[],[CallStmt(Id("writeln"),[StringLiteral("Input again, N must be larger than 0")])])],([],[]))]),BinaryOp("<=",Id("n"),IntLiteral(0))),Assign(Id("i"),IntLiteral(1)),While(BinaryOp("<=",Id("i"),Id("n")),([],[If([(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),[],[CallStmt(Id("writeln"),[Id("i")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_simple_program_81(self):
        input = """
        Var:x,y[1]={1e-2,"a\\'b"};
        Function:main
        Body:
            z[0O1]=y[1+x>2]+o3[2];
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],ArrayLiteral([FloatLiteral(0.01),StringLiteral("a\\'b")])),FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("z"),[IntLiteral(1)]),BinaryOp("+",ArrayCell(Id("y"),[BinaryOp(">",BinaryOp("+",IntLiteral(1),Id("x")),IntLiteral(2))]),ArrayCell(Id("o3"),[IntLiteral(2)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_simple_program_82(self):
        input = """
        Var:x[0x24];
        Function: main
        Body:
            If a[(0o25[333] < 1.e-5) < 3] >= 2 Then
                print("Hello");
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[0x24],None),FuncDecl(Id("main"),[],([],[If([(BinaryOp(">=",ArrayCell(Id("a"),[BinaryOp("<",BinaryOp("<",ArrayCell(IntLiteral(21),[IntLiteral(333)]),FloatLiteral(1e-05)),IntLiteral(3))]),IntLiteral(2)),[],[CallStmt(Id("print"),[StringLiteral("Hello")])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_simple_program_83(self):
        input = """
        Var:x={True};
        Function: main
        Body:
            If 0[2] == 0[1] Then
                foo(!0x12 % -.(x > True));
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],ArrayLiteral([BooleanLiteral(True)])),FuncDecl(Id("main"),[],([],[If([(BinaryOp("==",ArrayCell(IntLiteral(0),[IntLiteral(2)]),ArrayCell(IntLiteral(0),[IntLiteral(1)])),[],[CallStmt(Id("foo"),[BinaryOp("%",UnaryOp("!",IntLiteral(18)),UnaryOp("-.",BinaryOp(">",Id("x"),BooleanLiteral(True))))])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_simple_program_84(self):
        input = """
        Var:x[0X20]="\\f";
        Function: main
        Body:
            If foo(1.25[{1,2}]) =/= False Then
                foo(0["String"] != 2[2]);
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[0x20],StringLiteral("\\f")),FuncDecl(Id("main"),[],([],[If([(BinaryOp("=/=",CallExpr(Id("foo"),[ArrayCell(FloatLiteral(1.25),[ArrayLiteral([IntLiteral(1),IntLiteral(2)])])]),BooleanLiteral(False)),[],[CallStmt(Id("foo"),[BinaryOp("!=",ArrayCell(IntLiteral(0),[StringLiteral("String")]),ArrayCell(IntLiteral(2),[IntLiteral(2)]))])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_simple_program_85(self):
        input = """
        Var:x[0]={{0.000},{000.}};
        Function: foo
        Parameter:x[2],y
        Body:
            If x[0][1.e+1110 >= foo()] =/= 0[{1,True}] Then
                If {} Then
                    print();
                EndIf.
            EndIf.
        EndBody.
        Function: main
        Body:
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[0],ArrayLiteral([ArrayLiteral([FloatLiteral(0.0)]),ArrayLiteral([FloatLiteral(0.0)])])),FuncDecl(Id("foo"),[VarDecl(Id("x"),[2],None),VarDecl(Id("y"),[],None)],([],[If([(BinaryOp("=/=",ArrayCell(Id("x"),[IntLiteral(0),BinaryOp(">=",FloatLiteral(1.e+1110),CallExpr(Id("foo"),[]))]),ArrayCell(IntLiteral(0),[ArrayLiteral([IntLiteral(1),BooleanLiteral(True)])])),[],[If([(ArrayLiteral([]),[],[CallStmt(Id("print"),[])])],([],[]))])],([],[]))])),FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_simple_program_86(self):
        input = """
        Var:x,y={},z="",t=0.0;
        Function: main
        Parameter: x,y,z,t
        Body:
            If x > y || z Then
                Return {"foo",0.E-100};
            ElseIf x <= z Then 
                Return 0[z(t)];
            Else
                Return;
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],ArrayLiteral([])),VarDecl(Id("z"),[],StringLiteral("")),VarDecl(Id("t"),[],FloatLiteral(0.0)),FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("t"),[],None)],([],[If([(BinaryOp(">",Id("x"),BinaryOp("||",Id("y"),Id("z"))),[],[Return(ArrayLiteral([StringLiteral("foo"),FloatLiteral(0.0)]))]),(BinaryOp("<=",Id("x"),Id("z")),[],[Return(ArrayCell(IntLiteral(0),[CallExpr(Id("z"),[Id("t")])]))])],([],[Return(None)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_simple_program_87(self):
        input = """
        Function: main
        Parameter: x,y,z[0x1111],t
        Body:
            If x[y % 2] != (y <= t[x]) Then
                x[y && z +. 2][x(t * {"0", 0})] = -1.000001;
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[4369],None),VarDecl(Id("t"),[],None)],([],[If([(BinaryOp("!=",ArrayCell(Id("x"),[BinaryOp("%",Id("y"),IntLiteral(2))]),BinaryOp("<=",Id("y"),ArrayCell(Id("t"),[Id("x")]))),[],[Assign(ArrayCell(Id("x"),[BinaryOp("&&",Id("y"),BinaryOp("+.",Id("z"),IntLiteral(2))),CallExpr(Id("x"),[BinaryOp("*",Id("t"),ArrayLiteral([StringLiteral("0"),IntLiteral(0)]))])]),UnaryOp("-",FloatLiteral(1.000001)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_simple_program_88(self):
        input = """
        Var: b___b = 0e+0;
        Function: main
        Body:
            If 1 *. 2 && 3 Then
                1[-2.1] = 1 > 2[3];
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("b___b"),[],FloatLiteral(0.0)),FuncDecl(Id("main"),[],([],[If([(BinaryOp("&&",BinaryOp("*.",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),[],[Assign(ArrayCell(IntLiteral(1),[UnaryOp("-",FloatLiteral(2.1))]),BinaryOp(">",IntLiteral(1),ArrayCell(IntLiteral(2),[IntLiteral(3)])))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_simple_program_89(self):
        input = """
        Function: main
        Body:
            If 1 Then
                If 5 Then
                Else
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(IntLiteral(1),[],[If([(IntLiteral(5),[],[])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_simple_program_90(self):
        input = """
        Function: main
        Body:
            If 0[-1][foo() && 1[2 > -3 + 2]] =/= 1 \. 2[5 || 7] Then
                foo123(x[{1,2.e-3}] % {"Hello"} > 1);
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(BinaryOp("=/=",ArrayCell(IntLiteral(0),[UnaryOp("-",IntLiteral(1)),BinaryOp("&&",CallExpr(Id("foo"),[]),ArrayCell(IntLiteral(1),[BinaryOp(">",IntLiteral(2),BinaryOp("+",UnaryOp("-",IntLiteral(3)),IntLiteral(2)))]))]),BinaryOp("\\.",IntLiteral(1),ArrayCell(IntLiteral(2),[BinaryOp("||",IntLiteral(5),IntLiteral(7))]))),[],[CallStmt(Id("foo123"),[BinaryOp(">",BinaryOp("%",ArrayCell(Id("x"),[ArrayLiteral([IntLiteral(1),FloatLiteral(0.002)])]),ArrayLiteral([StringLiteral("Hello")])),IntLiteral(1))])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_simple_program_91(self):
        input = """
        Var:x,y[1]={1e-2,"a\\'b"};
        Function:main
        Body:
            z[0O1]=y[1+x]+0o3[2];
            z[1]=y[0[1]]>0xFF[2];
            z[0xDB]=y[1+x]!=1e3[2];
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1],ArrayLiteral([FloatLiteral(0.01),StringLiteral("a\\'b")])),FuncDecl(Id("main"),[],([],[Assign(ArrayCell(Id("z"),[IntLiteral(1)]),BinaryOp("+",ArrayCell(Id("y"),[BinaryOp("+",IntLiteral(1),Id("x"))]),ArrayCell(IntLiteral(3),[IntLiteral(2)]))),Assign(ArrayCell(Id("z"),[IntLiteral(1)]),BinaryOp(">",ArrayCell(Id("y"),[ArrayCell(IntLiteral(0),[IntLiteral(1)])]),ArrayCell(IntLiteral(255),[IntLiteral(2)]))),Assign(ArrayCell(Id("z"),[IntLiteral(219)]),BinaryOp("!=",ArrayCell(Id("y"),[BinaryOp("+",IntLiteral(1),Id("x"))]),ArrayCell(FloatLiteral(1000.0),[IntLiteral(2)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_simple_program_92(self):
        input = """
        Function: main
        Body:
            If a[0o25[333]] >= 2 Then
                print("Exit");
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(BinaryOp(">=",ArrayCell(Id("a"),[ArrayCell(IntLiteral(21),[IntLiteral(333)])]),IntLiteral(2)),[],[CallStmt(Id("print"),[StringLiteral("Exit")])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_simple_program_93(self):
        input = """
        Var:x={True,**note**123};
        Function: main
        Body:
            If x \ 1E-2 Then
                foo(-.2 % !(x && True));
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],ArrayLiteral([BooleanLiteral(True),IntLiteral(123)])),FuncDecl(Id("main"),[],([],[If([(BinaryOp("\\",Id("x"),FloatLiteral(0.01)),[],[CallStmt(Id("foo"),[BinaryOp("%",UnaryOp("-.",IntLiteral(2)),UnaryOp("!",BinaryOp("&&",Id("x"),BooleanLiteral(True))))])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_simple_program_94(self):
        input = """
        Var:x[0X20]="";
        Function: main
        Body:
            If foo() =/= False Then
                Var:x[0O22],y={"ab"};
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[0X20],StringLiteral("")),FuncDecl(Id("main"),[],([],[If([(BinaryOp("=/=",CallExpr(Id("foo"),[]),BooleanLiteral(False)),[VarDecl(Id("x"),[0O22],None),VarDecl(Id("y"),[],ArrayLiteral([StringLiteral("ab")]))],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_simple_program_95(self):
        input = """
        Var:x[2]={{00.00e+000},{00.E-00}};
        Function: foo
        Parameter:x[2],y
        Body:
            If x[0][1.e+0 > 0.0] <= 0[{1,True}] Then
                Return {};
            EndIf.
        EndBody.
        Function: main
        Body:
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[2],ArrayLiteral([ArrayLiteral([FloatLiteral(0.0)]),ArrayLiteral([FloatLiteral(0.0)])])),FuncDecl(Id("foo"),[VarDecl(Id("x"),[2],None),VarDecl(Id("y"),[],None)],([],[If([(BinaryOp("<=",ArrayCell(Id("x"),[IntLiteral(0),BinaryOp(">",FloatLiteral(1.0),FloatLiteral(0.0))]),ArrayCell(IntLiteral(0),[ArrayLiteral([IntLiteral(1),BooleanLiteral(True)])])),[],[Return(ArrayLiteral([]))])],([],[]))])),FuncDecl(Id("main"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_simple_program_96(self):
        input = """
        Var:x,y={},z="",t=0.0;
        Function: main
        Parameter: x,y,z,t
        Body:
            If x > y || z Then
            ElseIf ! x == t Then
                Return (1 > 2 + a[-1][t]);
            Else
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],ArrayLiteral([])),VarDecl(Id("z"),[],StringLiteral("")),VarDecl(Id("t"),[],FloatLiteral(0.0)),FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None),VarDecl(Id("t"),[],None)],([],[If([(BinaryOp(">",Id("x"),BinaryOp("||",Id("y"),Id("z"))),[],[]),(BinaryOp("==",UnaryOp("!",Id("x")),Id("t")),[],[Return(BinaryOp(">",IntLiteral(1),BinaryOp("+",IntLiteral(2),ArrayCell(Id("a"),[UnaryOp("-",IntLiteral(1)),Id("t")]))))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_simple_program_97(self):
        input = """
        Function: main
        Parameter: x,y,z[0x11],t
        Body:
            If x[y > z] > (y <= t[x]) Then
                x[y && z + 2][x(t * {"0", 0})] = "Hi";
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[17],None),VarDecl(Id("t"),[],None)],([],[If([(BinaryOp(">",ArrayCell(Id("x"),[BinaryOp(">",Id("y"),Id("z"))]),BinaryOp("<=",Id("y"),ArrayCell(Id("t"),[Id("x")]))),[],[Assign(ArrayCell(Id("x"),[BinaryOp("&&",Id("y"),BinaryOp("+",Id("z"),IntLiteral(2))),CallExpr(Id("x"),[BinaryOp("*",Id("t"),ArrayLiteral([StringLiteral("0"),IntLiteral(0)]))])]),StringLiteral("Hi"))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_simple_program_98(self):
        input = """
        Var: b___ = 0e+0;
        Function: main
        Parameter: x[0]
        Body:
            If 1 *. 2 && 3 Then
                1[-2] = 1 > 2[3];
            ElseIf 0 Then
            EndIf.
        EndBody.
        """
        expect = Program([VarDecl(Id("b___"),[],FloatLiteral(0.0)),FuncDecl(Id("main"),[VarDecl(Id("x"),[0],None)],([],[If([(BinaryOp("&&",BinaryOp("*.",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),[],[Assign(ArrayCell(IntLiteral(1),[UnaryOp("-",IntLiteral(2))]),BinaryOp(">",IntLiteral(1),ArrayCell(IntLiteral(2),[IntLiteral(3)])))]),(IntLiteral(0),[],[])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_simple_program_99(self):
        input = """
        Function: main
        Body:
            If 1 Then
                If 5 Then
                Else
                EndIf.
            ElseIf 2 Then
                If 3 Then
                ElseIf 4 Then
                EndIf.
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(IntLiteral(1),[],[If([(IntLiteral(5),[],[])],([],[]))]),(IntLiteral(2),[],[If([(IntLiteral(3),[],[]),(IntLiteral(4),[],[])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_simple_program_100(self):
        input = """
        Function: main
        Body:
            If 0[-1][foo() && 1[2 > -3 + 2]] =/= 1 \. 2[5 || 7] Then
                foo123(x[{1,2.e-3}] % {"Hello"});
            EndIf.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"),[],([],[If([(BinaryOp("=/=",ArrayCell(IntLiteral(0),[UnaryOp("-",IntLiteral(1)),BinaryOp("&&",CallExpr(Id("foo"),[]),ArrayCell(IntLiteral(1),[BinaryOp(">",IntLiteral(2),BinaryOp("+",UnaryOp("-",IntLiteral(3)),IntLiteral(2)))]))]),BinaryOp("\\.",IntLiteral(1),ArrayCell(IntLiteral(2),[BinaryOp("||",IntLiteral(5),IntLiteral(7))]))),[],[CallStmt(Id("foo123"),[BinaryOp("%",ArrayCell(Id("x"),[ArrayLiteral([IntLiteral(1),FloatLiteral(0.002)])]),ArrayLiteral([StringLiteral("Hello")]))])])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,400))