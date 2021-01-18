import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_2(self):
        input = """Var:x,y,z=10;"""
        expect = Program([VarDecl(Id("x"),[],None), VarDecl(Id("y"),[], None), VarDecl(Id("z"),[],IntLiteral(10))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_3(self):
        input = """Var:x,y=120000e-1,z="this is a string";"""
        expect = Program([VarDecl(Id("x"),[],None), VarDecl(Id("y"),[], FloatLiteral(120000e-1)), VarDecl(Id("z"),[],StringLiteral("this is a string"))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_4(self):
        input = """Var:n,m[10][20];"""
        expect = Program([VarDecl(Id("n"),[],None), VarDecl(Id("m"),[10,20], None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_5(self):
        input = """Var:n,m[10][20] = True;"""
        expect = Program([VarDecl(Id("n"),[],None), VarDecl(Id("m"),[10,20], BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_6(self):
        input = """Var:n,m[10][20] = {1,        2,         3};"""
        expect = Program([VarDecl(Id("n"),[],None), VarDecl(Id("m"),[10,20], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_7(self):
        input = """Var:n,m[10][20] = {1,        {2},         3, {{}}};"""
        expect = Program([VarDecl(Id("n"),[],None), VarDecl(Id("m"),[10,20], ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(2)]), IntLiteral(3), ArrayLiteral([ArrayLiteral([])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_8(self):
        input = """Var: xxxxx[10000] ={{1}, {{            }}};"""
        expect = Program([VarDecl(Id("xxxxx"),[10000], ArrayLiteral([ArrayLiteral([IntLiteral(1)]), ArrayLiteral([ArrayLiteral([])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_9(self):
        input = """Var: y = {{{{      }}}};"""
        expect = Program([VarDecl(Id("y"),[], ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([])])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_10(self):
        input = """
            Var: arr[5][6]=1.e790,b,c=2;
            Var: x={         ****};
        """
        expect = Program([VarDecl(Id("arr"),[5,6], FloatLiteral(1.e790)), VarDecl(Id("b"),[], None), VarDecl(Id("c"), [], IntLiteral(2)), VarDecl(Id("x"), [], ArrayLiteral([]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_11(self):
        input = """
            Var: arr[5][6]=1.e790,b,c=2;
            Function: compare
                   Parameter: x, y
                   Body:
                   EndBody.
        """
        expect = Program([VarDecl(Id("arr"),[5,6], FloatLiteral(1.e790)), VarDecl(Id("b"),[], None), VarDecl(Id("c"), [], IntLiteral(2)), FuncDecl(Id("compare"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)], ([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_12(self):
        input = """
            Function: func_name
                   Parameter: x, y[12][7], z
                   Body:
                   EndBody.
        """
        expect = Program([FuncDecl(Id("func_name"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [12,7], None), VarDecl(Id("z"), [], None)], ([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_13(self):
        input = """
            Function: name
                   Parameter: k[1][2][3]
                   Body:
                        Var: y = {1,      2, "string", True, {   }};
                   EndBody.
        """
        expect = Program([FuncDecl(Id("name"), [VarDecl(Id("k"), [1,2,3], None)], ([VarDecl(Id("y"), [], ArrayLiteral([IntLiteral(1), IntLiteral(2), StringLiteral("string"), BooleanLiteral(True), ArrayLiteral([])]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_14(self):
        input = """
            Function: hihi
                   Body:
                        Var: x;
                        i = (1+2)[1+3] + 1;
                   EndBody.
        """
        expect = Program([FuncDecl(Id("hihi"), [], ([VarDecl(Id("x"), [], None)],[Assign(Id("i"), BinaryOp("+",ArrayCell(BinaryOp("+", IntLiteral(1), IntLiteral(2)), [BinaryOp("+", IntLiteral(1), IntLiteral(3))]),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_15(self):
        input = """
            Function: hihi
                   Body:
                        arr[1+foo(2,3)][1] = foo(2,1+2);
                   EndBody.
        """
        expect = Program([FuncDecl(Id("hihi"), [], ([],[Assign(ArrayCell(Id("arr"), [BinaryOp("+", IntLiteral(1), CallExpr(Id("foo"), [IntLiteral(2), IntLiteral(3)])), IntLiteral(1)]), CallExpr(Id("foo"), [IntLiteral(2), BinaryOp("+", IntLiteral(1), IntLiteral(2))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_16(self):
        input = """
            Function: a
                   Body:
                        If (x > y) Then
                            Return True ;
                       Else 
                            Return False;
                       EndIf.
                   EndBody.
        """
        expect = Program([FuncDecl(Id("a"), [], ([],[If([(BinaryOp(">", Id("x"), Id("y")), [],[Return(BooleanLiteral(True))])],([],[Return(BooleanLiteral(False))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_17(self):
        input = """
            Function: a______999 
                   Body:
                        Var: x[1][2];
                        Var: max={0};
                        For ( i=1,i<n,1) Do
                            If max < a[i] Then
                                max = a[i];
                            EndIf.
                        EndFor.
                   EndBody.
        """
        expect = Program([FuncDecl(Id("a______999"), [], ([VarDecl(Id("x"), [1,2], None), VarDecl(Id("max"), [], ArrayLiteral([IntLiteral(0)]))],[For(Id("i"), IntLiteral(1), BinaryOp("<", Id("i"), Id("n")), IntLiteral(1), ([], [If([(BinaryOp("<", Id("max"), ArrayCell(Id("a"), [Id("i")])), [], [Assign(Id("max"), ArrayCell(Id("a"), [Id("i")]))])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_18(self):
        input = """
            Var: x= " string \\n";
            Function: func 
                   Body:
                        Var: x[1][2];
                        Var: max={0};
                        If max =/= a[i] Then
                            x= !foo(2);
                        ElseIf a[2][3] || {1,2    } Then
                            Var: y[1];
                            Break;
                        Else
                            Continue;
                        EndIf.
                   EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], StringLiteral(" string \\n")),FuncDecl(Id("func"), [], ([VarDecl(Id("x"), [1,2], None), VarDecl(Id("max"), [], ArrayLiteral([IntLiteral(0)]))],[If([(BinaryOp("=/=", Id("max"), ArrayCell(Id("a"),[Id("i")])), [], [Assign(Id("x"), UnaryOp("!", CallExpr(Id("foo"), [IntLiteral(2)])))]), (BinaryOp("||", ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(3)]), ArrayLiteral([IntLiteral(1), IntLiteral(2)])), [VarDecl(Id("y"), [1], None)], [Break()])],([], [Continue()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_19(self):
        input = """
            Function: fibonacci 
                Body: 
                    Var: f0=0,f1=1,fn=1;
                    Var: i;
                    If n<0 Then
                        Return -1;
                    ElseIf (n==0) || (n==1) Then
                        Return n;
                    Else 
                        Var: a[1] = {{         }};
                        For ( i=2,i<n, i+1 ) Do
                            f0=f1;
                            f1=fn;
                            fn=f0+f1;
                        EndFor.
                    EndIf.
                    Return fn;
                EndBody.
        """
        expect = Program([FuncDecl(Id("fibonacci"), [], ([VarDecl(Id("f0"), [], IntLiteral(0)), VarDecl(Id("f1"), [], IntLiteral(1)), VarDecl(Id("fn"), [], IntLiteral(1)), VarDecl(Id("i"), [], None)], [If([(BinaryOp("<", Id("n"), IntLiteral(0)), [], [Return(UnaryOp("-", IntLiteral(1)))]),(BinaryOp("||", BinaryOp("==", Id("n"), IntLiteral(0)), BinaryOp("==", Id("n"), IntLiteral(1))), [], [Return(Id("n"))])], ([VarDecl(Id("a"), [1], ArrayLiteral([ArrayLiteral([])]))],[For(Id("i"), IntLiteral(2), BinaryOp("<", Id("i"), Id("n")), BinaryOp("+", Id("i"), IntLiteral(1)), ([], [Assign(Id("f0"), Id("f1")), Assign(Id("f1"), Id("fn")), Assign(Id("fn"), BinaryOp("+", Id("f0"), Id("f1")))]))])), Return(Id("fn"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_20(self):
        input = """
            Function: fibonacci 
                Body: 
                    Var: f0=0,f1=1,fn=1;
                    Var: i;
                    If n<0 Then
                        Return -1;
                    ElseIf (n==0) || (n==1) Then
                        Return n;
                    Else 
                        Var: a[1] = {{         }};
                        For ( i=2,i<n, i+1 ) Do
                            f0=f1;
                            f1=fn;
                            fn=f0+f1;
                        EndFor.
                    EndIf.
                    Return fn;
                EndBody.
        """
        expect = Program([FuncDecl(Id("fibonacci"), [], ([VarDecl(Id("f0"), [], IntLiteral(0)), VarDecl(Id("f1"), [], IntLiteral(1)), VarDecl(Id("fn"), [], IntLiteral(1)), VarDecl(Id("i"), [], None)], [If([(BinaryOp("<", Id("n"), IntLiteral(0)), [], [Return(UnaryOp("-", IntLiteral(1)))]),(BinaryOp("||", BinaryOp("==", Id("n"), IntLiteral(0)), BinaryOp("==", Id("n"), IntLiteral(1))), [], [Return(Id("n"))])], ([VarDecl(Id("a"), [1], ArrayLiteral([ArrayLiteral([])]))],[For(Id("i"), IntLiteral(2), BinaryOp("<", Id("i"), Id("n")), BinaryOp("+", Id("i"), IntLiteral(1)), ([], [Assign(Id("f0"), Id("f1")), Assign(Id("f1"), Id("fn")), Assign(Id("fn"), BinaryOp("+", Id("f0"), Id("f1")))]))])), Return(Id("fn"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_21(self):
        input = """
            Function: isPrimeNumber
            Parameter: n
                Body: 
                    If n<2 Then
                        Return 0;
                    EndIf.
                    squareRoot = int(sqrt(n));
                EndBody.
        """
        expect = Program([FuncDecl(Id("isPrimeNumber"), [VarDecl(Id("n"), [], None)], ([],[If([(BinaryOp("<", Id("n"), IntLiteral(2)), [], [Return(IntLiteral(0))])], ([],[])), Assign(Id("squareRoot"), CallExpr(Id("int"), [CallExpr(Id("sqrt"), [Id("n")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_22(self):
        input = """
            Function: phanTichSoNguyen
            Parameter: n
                Body:
                While n <=. 1 Do
                    Var: a[100];
                    If (n % i == 0) Then
                        Var: a = {   ****};
                        n = n \ i;
                        a[dem+1] = i;
                    Else 
                        i=i+.1.;
                    EndIf.
                EndWhile.
                EndBody.
        """
        expect = Program([FuncDecl(Id("phanTichSoNguyen"), [VarDecl(Id("n"), [], None)], ([],[While(BinaryOp("<=.", Id("n"), IntLiteral(1)), ([VarDecl(Id("a"), [100], None)],[If([(BinaryOp("==", BinaryOp("%", Id("n"), Id("i")), IntLiteral(0)), [VarDecl(Id("a"),[], ArrayLiteral([]))], [Assign(Id("n"), BinaryOp("\\", Id("n"), Id("i"))), Assign(ArrayCell(Id("a"), [BinaryOp("+", Id("dem"), IntLiteral(1))]), Id("i"))])], ([],[Assign(Id("i"), BinaryOp("+.", Id("i"), FloatLiteral(1.)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_23(self):
        input = """
            Var: str_1 = "Nguyen long nhat \t \\n";
            Var: x__[5][6]={{  1}};
            Function: main 
            Body:
            Var: length = 0;
            While s1[length] != "\\\\" Do
                s2[length] = s1[length];
                length=length+1;
            EndWhile.
            printf("Chuoi s1 = !s \\n");
            Return ;
            EndBody.
        """
        expect = Program([VarDecl(Id("str_1"), [], StringLiteral("Nguyen long nhat \t \\n")), VarDecl(Id("x__"), [5,6], ArrayLiteral([ArrayLiteral([IntLiteral(1)])])), FuncDecl(Id("main"),[],([VarDecl(Id("length"), [], IntLiteral(0))],[While(BinaryOp("!=", ArrayCell(Id("s1"), [Id("length")]), StringLiteral("\\\\")), ([],[Assign(ArrayCell(Id("s2"), [Id("length")]), ArrayCell(Id("s1"), [Id("length")])), Assign(Id("length"), BinaryOp("+", Id("length"), IntLiteral(1)))])), CallStmt(Id("printf"), [StringLiteral("Chuoi s1 = !s \\n")]), Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_24(self):
        input = """
            Function: main 
            Parameter: a[1][2][3]
            Body:
            EndBody.
            
            Function: sub_main
            Body:
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [1,2,3], None)], ([],[])), FuncDecl(Id("sub_main"), [], ([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_25(self):
        input = """
            Function: main
            Body:
            Var: i, j, count;
            Var: start = 2, end = 10;
            writeln("In bang cuu chuong rut gon:");
            For (i = start, i <=. end, 1) Do
                count = i;
                Break;
            EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("i"), [], None), VarDecl(Id("j"), [], None), VarDecl(Id("count"), [], None), VarDecl(Id("start"), [], IntLiteral(2)), VarDecl(Id("end"), [], IntLiteral(10))],[CallStmt(Id("writeln"), [StringLiteral("In bang cuu chuong rut gon:")]), For(Id("i"), Id("start"), BinaryOp("<=.", Id("i"), Id("end")), IntLiteral(1), ([],[Assign(Id("count"), Id("i")), Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_26(self):
        input = """
            Function: main
            Parameter: n, i, j
            Body:
            Var: x = 6;
            123[True][1][x] = {{}};
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("n"), [], None), VarDecl(Id("i"), [], None), VarDecl(Id("j"), [], None)], ([VarDecl(Id("x"), [], IntLiteral(6))],[Assign(ArrayCell(IntLiteral(123), [BooleanLiteral(True), IntLiteral(1), Id("x")]), ArrayLiteral([ArrayLiteral([])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_27(self):
        input = """
            Function: uSCLN
            Parameter: a,b
            Body:
                If b == 0 Then Return a; EndIf.
                Return uSCLN(b, a % b);
            EndBody.
        """
        expect = Program([FuncDecl(Id("uSCLN"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)], ([],[If([(BinaryOp("==", Id("b"), IntLiteral(0)), [], [Return(Id("a"))])], ([],[])), Return(CallExpr(Id("uSCLN"), [Id("b"), BinaryOp("%", Id("a"), Id("b"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_28(self):
        input = """
            Var: s[4][20];
            Function: test____
            Body:
                printf("\\tNhap 4 chuoi bat ky: \\t");
                For (i = 0, i < size, i+1) Do
                EndFor.
                return(0);
            EndBody.
        """
        expect = Program([VarDecl(Id("s"), [4,20], None), FuncDecl(Id("test____"), [], ([], [CallStmt(Id("printf"), [StringLiteral("\\tNhap 4 chuoi bat ky: \\t")]), For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), Id("size")), BinaryOp("+", Id("i"), IntLiteral(1)), ([],[])), CallStmt(Id("return"), [IntLiteral(0)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_29(self):
        input = """
            Function: nhapMaTran
            Parameter: a[1][2], n
            Body:
                Do
                    scanf("%d", n);
                While (n < 1) || (n > max) EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("nhapMaTran"), [VarDecl(Id("a"), [1,2], None), VarDecl(Id("n"), [], None)], ([],[Dowhile(([],[CallStmt(Id("scanf"), [StringLiteral("%d"), Id("n")])]), BinaryOp("||", BinaryOp("<", Id("n"), IntLiteral(1)), BinaryOp(">", Id("n"), Id("max"))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_30(self):
        input = """
            Var: x = { 1,    1.,   "", True};
            Function: test
            Body:
                Do
                While False EndDo.
            EndBody.
        """
        expect = Program([VarDecl(Id("x"),[] ,ArrayLiteral([IntLiteral(1), FloatLiteral(1.), StringLiteral(""), BooleanLiteral(True)])), FuncDecl(Id("test"), [], ([],[Dowhile(([],[]), BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_31(self):
        input = """
            Function: main
            Body:
                a = " this is a string : '" a'" and '" ";
                Break;
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[Assign(Id("a"), StringLiteral(""" this is a string : '" a'" and '" """)), Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_32(self):
        input = """
            Var: x;
            Function: main
            Body:
                Continue;
                Break;
                Break;
                Continue;
                Continue;
                1[True][False]={ {           {}}};
            EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], None), FuncDecl(Id("main"), [], ([],[Continue(), Break(), Break(), Continue(), Continue(), Assign(ArrayCell(IntLiteral(1), [BooleanLiteral(True), BooleanLiteral(False)]), ArrayLiteral([ArrayLiteral([ArrayLiteral([])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_33(self):
        input = """
            Function: main
            Body:
                Var: arr[0] = {      "he",        "she", "          hers", "his   "};
                Var: text = "ahishers\\'";
                k = sizeof(arr)\sizeof(arr[0]);
                searchWords(arr, k, text);
                Return 0;
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("arr"), [0], ArrayLiteral([StringLiteral("he"), StringLiteral("she"), StringLiteral("          hers"), StringLiteral("his   ")])), VarDecl(Id("text"), [], StringLiteral("ahishers\\'"))],[Assign(Id("k"), BinaryOp("\\", CallExpr(Id("sizeof"), [Id("arr")]), CallExpr(Id("sizeof"), [ArrayCell(Id("arr"), [IntLiteral(0)])]))), CallStmt(Id("searchWords"), [Id("arr"), Id("k"), Id("text")]), Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_34(self):
        input = """
            Function: main
            Body:
                For (j = 0, j < k, 100+j) Do
                    If (out[currentState] && (1 < j)) Then
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), Id("k")), BinaryOp("+", IntLiteral(100), Id("j")), ([],[If([(BinaryOp("&&", ArrayCell(Id("out"), [Id("currentState")]), BinaryOp("<", IntLiteral(1), Id("j"))),[],[])], ([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_35(self):
        input = """
            Function: main
        Body:
            Var: a = 10;
            While( a < 20 ) Do   
                Var: x = {};
                a=a+{1};
                If( a > 15) Then
                    ** ket thuc vong lap khi a lon hon 15 **
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], IntLiteral(10))],[While(BinaryOp("<", Id("a"), IntLiteral(20)), ([VarDecl(Id("x"), [], ArrayLiteral([]))],[Assign(Id("a"), BinaryOp("+", Id("a"), ArrayLiteral([IntLiteral(1)]))), If([(BinaryOp(">", Id("a"), IntLiteral(15)), [], [])], ([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_36(self):
        input = """
            Function: test_index_op
                Body:
                    v=123[True];
                    y=123[0[0[False]]];
                EndBody.
        """
        expect = Program([FuncDecl(Id("test_index_op"), [], ([],[Assign(Id("v"), ArrayCell(IntLiteral(123), [BooleanLiteral(True)])), Assign(Id("y"), ArrayCell(IntLiteral(123), [ArrayCell(IntLiteral(0), [ArrayCell(IntLiteral(0), [BooleanLiteral(False)])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_37(self):
        input = """
            Function: func_name
            Parameter: n
            Body:
                Do
                    a[dem+1] = (n % {});
                    n = n \ foo(1[2]);
                While n > 0
                EndDo.
            EndBody.
        """
        expect = Program([FuncDecl(Id("func_name"), [VarDecl(Id("n"), [], None)], ([],[Dowhile(([],[Assign(ArrayCell(Id("a"), [BinaryOp("+", Id("dem"), IntLiteral(1)),]), BinaryOp("%", Id("n"), ArrayLiteral([]))), Assign(Id("n"), BinaryOp("\\", Id("n"), CallExpr(Id("foo"), [ArrayCell(IntLiteral(1), [IntLiteral(2)])])))]), BinaryOp(">", Id("n"), IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_38(self):
        input = """
        """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_39(self):
        input = """
        Function: main
            Body: 
                Var: txt[12] = "ABABDABACDABABCABAB\t \\n", pat[27] = "ABABCABAB \b \\\\"; 
                kMPSearch(pat, txt); 
                Return 0; 
                x=(1+foo(2))[1];
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("txt"), [12], StringLiteral("ABABDABACDABABCABAB\t \\n")), VarDecl(Id("pat"), [27], StringLiteral("ABABCABAB \b \\\\"))],[CallStmt(Id("kMPSearch"), [Id("pat"), Id("txt")]), Return(IntLiteral(0)), Assign(Id("x"), ArrayCell(BinaryOp("+", IntLiteral(1), CallExpr(Id("foo"), [IntLiteral(2)])), [IntLiteral(1)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_40(self):
        input = """
        Function: name__func0_99
                Body:
                    For(i=0,i<=. size(), i>9) Do
                        Var: y=1.;
                        If (s[i] >= a) && (s[i] <= z) Then
                            Var: y;
                        EndIf.
                    EndFor.
                EndBody.
        """
        expect = Program([FuncDecl(Id("name__func0_99"), [], ([],[For(Id("i"), IntLiteral(0), BinaryOp("<=.", Id("i"), CallExpr(Id("size"), [])), BinaryOp(">", Id("i"), IntLiteral(9)), ([VarDecl(Id("y"), [], FloatLiteral(1.))],[If([(BinaryOp("&&", BinaryOp(">=", ArrayCell(Id("s"), [Id("i")]), Id("a")), BinaryOp("<=", ArrayCell(Id("s"), [Id("i")]), Id("z"))), [VarDecl(Id("y"), [], None)],[])], ([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_41(self):
        input = """
        Function: foo
            Parameter: x, y
            Body:
                writeln(foo(2 + x, 4. \. y) * goo());
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None)], ([],[CallStmt(Id("writeln"), [BinaryOp("*", CallExpr(Id("foo"), [BinaryOp("+", IntLiteral(2), Id("x")), BinaryOp("\.", FloatLiteral(4.), Id("y"))]),CallExpr(Id("goo"), [] ))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_42(self):
        input = """
        Function: square_num
            Parameter: x
            Body:
                If x == 1 Then
                    Var: y=1,x[100];
                    Return 1;
                ElseIf y >=. True Then
                    Var: x= { {} }; 
                Else 
                    Var: x = 1;
                    Return sqrt(x + square_num(x - 1));
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("square_num"), [VarDecl(Id("x"), [], None)], ([],[If([(BinaryOp("==", Id("x"), IntLiteral(1)), [VarDecl(Id("y"), [], IntLiteral(1)), VarDecl(Id("x"), [100], None)],[Return(IntLiteral(1))]), (BinaryOp(">=.", Id("y"), BooleanLiteral(True)), [VarDecl(Id("x"), [], ArrayLiteral([ArrayLiteral([])]))], [])],([VarDecl(Id("x"), [], IntLiteral(1))],[Return(CallExpr(Id("sqrt"),[BinaryOp("+", Id("x"), CallExpr(Id("square_num"), [BinaryOp("-", Id("x"), IntLiteral(1))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_43(self):
        input = """
        Function: main
            Body:
                Var: answer, length, jump_max, arr[10], a , j;
                For (i = 1+foo(), i < length, 1) Do
                    arr[i] = input();
                EndFor.
	            writeln(answer);
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("answer"), [], None), VarDecl(Id("length"), [], None), VarDecl(Id("jump_max"), [], None), VarDecl(Id("arr"), [10], None), VarDecl(Id("a"), [], None), VarDecl(Id("j"), [], None)],[For(Id("i"), BinaryOp("+", IntLiteral(1), CallExpr(Id("foo"), [])), BinaryOp("<", Id("i"), Id("length")), IntLiteral(1), ([],[Assign(ArrayCell(Id("arr"), [Id("i")]), CallExpr(Id("input"), []))])), CallStmt(Id("writeln"), [Id("answer")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_44(self):
        input = """
        Function: power_rep
            Body:
                Var: a = 2;
                If (exp == 0) Then
                    Return 1;
                EndIf.
                For (i = 0, i < exp - 1, 1) Do
                    Var: x;
                    base = base * a;
                EndFor.
                Return base;
            EndBody.
        """
        expect = Program([FuncDecl(Id("power_rep"), [], ([VarDecl(Id("a"),[] ,IntLiteral(2))],[If([(BinaryOp("==", Id("exp"), IntLiteral(0)), [], [Return(IntLiteral(1))])], ([],[])), For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), BinaryOp("-", Id("exp"), IntLiteral(1))), IntLiteral(1), ([VarDecl(Id("x"), [], None)],[Assign(Id("base"), BinaryOp("*", Id("base"), Id("a")))])), Return(Id("base"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_45(self):
        input = """
        Function: giaiPTBac2_part_1
                Body:
                If (a == 0) Then
                    If (b == 0) Then
                        printf("Phuong trinh vo nghiem!");
                    Else
                        printf("Phuong trinh co mot nghiem: x = %f", (-c \ b));
                    EndIf.
                EndIf.
            Return;
            EndBody.
        """
        expect = Program([FuncDecl(Id("giaiPTBac2_part_1"), [], ([],[If([(BinaryOp("==", Id("a"), IntLiteral(0)), [], [If([(BinaryOp("==", Id("b"), IntLiteral(0)), [], [CallStmt(Id("printf"), [StringLiteral("Phuong trinh vo nghiem!")])])], ([],[CallStmt(Id("printf"), [StringLiteral("Phuong trinh co mot nghiem: x = %f"), BinaryOp("\\", UnaryOp("-", Id("c")), Id("b"))])]))])], ([],[])), Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_46(self):
        input = """
        Function: printDivivsors
            Parameter: n
            Body:
                For (i = 1, i <= n, 1) Do
                    Var: x[1]={"string"};
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
        expect = Program([FuncDecl(Id("printDivivsors"), [VarDecl(Id("n"), [], None)], ([],[For(Id("i"), IntLiteral(1), BinaryOp("<=", Id("i"), Id("n")), IntLiteral(1), ([VarDecl(Id("x"), [1], ArrayLiteral([StringLiteral("string")]))],[If([(BinaryOp("==", BinaryOp("%", Id("n"), Id("i")), IntLiteral(0)), [], [CallStmt(Id("writeln"), [Id("i")])])], ([],[]))]))])), FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], None)],[CallStmt(Id("input"), [Id("x")]), CallStmt(Id("printDivivsors"), [Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_47(self):
        input = """
        Function: main
            Body:
                For (j = 0, j < length, 1) Do
                    If (a + jump_max >= arr[i]) && (a + jump_max < arr[i + 1]) Then
                        a = arr[i];
                        answer = answer + 1;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), Id("length")), IntLiteral(1), ([],[If([(BinaryOp("&&", BinaryOp(">=", BinaryOp("+", Id("a"), Id("jump_max")), ArrayCell(Id("arr"), [Id("i")])), BinaryOp("<", BinaryOp("+", Id("a"), Id("jump_max")), ArrayCell(Id("arr"), [BinaryOp("+", Id("i"), IntLiteral(1))]))), [], [Assign(Id("a"), ArrayCell(Id("arr"), [Id("i")])), Assign(Id("answer"), BinaryOp("+", Id("answer"), IntLiteral(1)))])], ([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_48(self):
        input = """
        Var: arr[5][6]=1.e790,b,c=2;
            Function: tEST_function_Name_1
                Parameter: x[100]
                Body:
                    Do 
                        Var: x;
                        x=x + foo(267+a[6]+. 1.0);
                    While i<=27 EndDo .
                EndBody.
        """
        expect = Program([VarDecl(Id("arr"), [5,6], FloatLiteral(1.e790)), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], IntLiteral(2)), FuncDecl(Id("tEST_function_Name_1"), [VarDecl(Id("x"), [100], None)], ([],[Dowhile(([VarDecl(Id("x"), [], None)],[Assign(Id("x"), BinaryOp("+", Id("x"), CallExpr(Id("foo"), [BinaryOp("+.", BinaryOp("+", IntLiteral(267), ArrayCell(Id("a"), [IntLiteral(6)])), FloatLiteral(1.0))])))]), BinaryOp("<=", Id("i"), IntLiteral(27)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_49(self):
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
        expect = Program([FuncDecl(Id("tEST_function_Name_2"), [VarDecl(Id("x"), [], None), VarDecl(Id("a"), [69], None), VarDecl(Id("b"), [1,2,3], None)], ([],[For(Id("i"), IntLiteral(1), BinaryOp("<", CallExpr(Id("goo"), [BinaryOp("+", IntLiteral(2), ArrayCell(Id("a"), [IntLiteral(6)]))]), Id("i")), BinaryOp(">", IntLiteral(2), CallExpr(Id("goo"), [IntLiteral(9)])), ([],[If([(BinaryOp(">=", ArrayCell(Id("arr"), [IntLiteral(7)]), CallExpr(Id("foo"), [IntLiteral(3)])), [], [Break()])], ([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_50(self):
        input = """
        Var: a = True, b = {1,2}, c = {{True, False}, {1.e2, 1e3}};
            Function: test
            Parameter: num
            Body:
                Return False;
            EndBody.
        """
        expect = Program([VarDecl(Id("a"), [], BooleanLiteral(True)), VarDecl(Id("b"), [], ArrayLiteral([IntLiteral(1), IntLiteral(2)])), VarDecl(Id("c"), [], ArrayLiteral([ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)]), ArrayLiteral([FloatLiteral(1.e2), FloatLiteral(1e3)])])), FuncDecl(Id("test"), [VarDecl(Id("num"), [], None)], ([],[Return(BooleanLiteral(False))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_51(self):
        input = """
            Function: test_exp
            Body:
                y = 1.1 +. 3 -. 1.2 *. 8.0 \\. 9.23;
            EndBody.
        """
        expect = Program([FuncDecl(Id("test_exp"), [], ([],[Assign(Id("y"), BinaryOp("-.",BinaryOp("+.", FloatLiteral(1.1), IntLiteral(3)),BinaryOp("\.", BinaryOp("*.", FloatLiteral(1.2), FloatLiteral(8.0)), FloatLiteral(9.23))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_52(self):
        input = """
            Function: generate_derangement
            Body:
                Var: s[1]; 
                For (i = 1, i <= x, i+{1}) Do
                    x[i][j] = i; 
                    push(x[i]); 
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("generate_derangement"), [], ([VarDecl(Id("s"), [1], None)],[For(Id("i"), IntLiteral(1), BinaryOp("<=", Id("i"), Id("x")), BinaryOp("+", Id("i"), ArrayLiteral([IntLiteral(1)])), ([],[Assign(ArrayCell(Id("x"), [Id("i"), Id("j")]), Id("i")), CallStmt(Id("push"), [ArrayCell(Id("x"), [Id("i")])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_53(self):
        input = """
            Function: test_exp
            Body:
                Return foo()[2][3];
            EndBody.
        """
        expect = Program([FuncDecl(Id("test_exp"), [], ([],[Return(ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(2), IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_54(self):
        input = """
            Function: test_exp___9
            Body:
                2[3] = foo()[2][1+foo()];
            EndBody.
        """
        expect = Program([FuncDecl(Id("test_exp___9"), [], ([],[Assign(ArrayCell(IntLiteral(2), [IntLiteral(3)]), ArrayCell(CallExpr(Id("foo"), []), [IntLiteral(2), BinaryOp("+", IntLiteral(1), CallExpr(Id("foo"), []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_55(self):
        input = """
            Function: partition
            Parameter: arr[1], low, high
            Body:
                Var: x = False;
                ** this is a comment **
            EndBody.
        """
        expect = Program([FuncDecl(Id("partition"), [VarDecl(Id("arr"), [1], None), VarDecl(Id("low"), [], None), VarDecl(Id("high"), [], None)], ([VarDecl(Id("x"), [], BooleanLiteral(False))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_56(self):
        input = """
            Function: partition
            Body:
                    While(left <= right) && (arr[left] < pivot) Do left=left+1; EndWhile.  ** Tim phan tu >= arr[pivot] **
                    Return left;
            EndBody.
        """
        expect = Program([FuncDecl(Id("partition"), [], ([],[While(BinaryOp("&&", BinaryOp("<=", Id("left"), Id("right")), BinaryOp("<", ArrayCell(Id("arr"), [Id("left")]), Id("pivot"))), ([],[Assign(Id("left"), BinaryOp("+", Id("left"), IntLiteral(1)))])), Return(Id("left"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_57(self):
        input = """
            Function: main
            Body:
                For(i=0,i<m,i+3) Do
                    For(j=0,j<n,j+4) Do
                        Var: x;
                    EndFor.
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), Id("m")), BinaryOp("+", Id("i"), IntLiteral(3)), ([],[For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), Id("n")), BinaryOp("+", Id("j"), IntLiteral(4)), ([VarDecl(Id("x"), [], None)],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_58(self):
        input = """
            Function: main
            Body:
                For(i=0,i<m,i+3) Do
                    For(j=0,j<n,j+4) Do
                        Var: x;
                    EndFor.
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), Id("m")), BinaryOp("+", Id("i"), IntLiteral(3)), ([],[For(Id("j"), IntLiteral(0), BinaryOp("<", Id("j"), Id("n")), BinaryOp("+", Id("j"), IntLiteral(4)), ([VarDecl(Id("x"), [], None)],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_59(self):
        input = """
            Function: main
            Body:
                readln(a[i],b[i]);
                sum = sum +- a[i];
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[CallStmt(Id("readln"), [ArrayCell(Id("a"), [Id("i")]), ArrayCell(Id("b"), [Id("i")])]), Assign(Id("sum"), BinaryOp("+", Id("sum"), UnaryOp("-", ArrayCell(Id("a"), [Id("i")]))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_60(self):
        input = """
            Function: foo 
                Body: 
                    a = 1 + 1.23 *. abc \. id[moreid];
                EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], ([],[Assign(Id("a"), BinaryOp("+", IntLiteral(1),BinaryOp("\.",BinaryOp("*.", FloatLiteral(1.23), Id("abc")), ArrayCell(Id("id"), [Id("moreid")]))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_61(self):
        input = """
            Var: a,b,c=10,d[3]={1,2,3};
        """
        expect = Program([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], IntLiteral(10)), VarDecl(Id("d"), [3], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_62(self):
        input = """
            Var: a[0xA];
        """
        expect = Program([VarDecl(Id("a"), [0xA], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_63(self):
        input = """
            Var: x={1, 2.,   "3"}, y;
            Function: tEST_13
                Body:
                    v = a && b > 2 + 0;
                EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], ArrayLiteral([IntLiteral(1), FloatLiteral(2.), StringLiteral('3')])), VarDecl(Id("y"), [], None), FuncDecl(Id("tEST_13"), [], ([],[Assign(Id("v"), BinaryOp(">", BinaryOp("&&", Id("a"), Id("b")), BinaryOp("+", IntLiteral(2), IntLiteral(0))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_64(self):
        input = """
            Var: x[1][2][0x123FA];
        """
        expect = Program([VarDecl(Id("x"), [1,2,0x123FA], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_65(self):
        input = """
            Var: y[0X1][0O10];
        """
        expect = Program([VarDecl(Id("y"), [0X1, 0O10], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_66(self):
        input = """
            Var: x = {"s", 0x12, 0o1,1      };
        """
        expect = Program([VarDecl(Id("x"), [], ArrayLiteral([StringLiteral("s"), IntLiteral(0x12), IntLiteral(0o1), IntLiteral(1)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_67(self):
        input = """
            Function: main
                Body:
                    (1+2)[foo()] = 0x99 + 1.e79;
                EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[Assign(ArrayCell(BinaryOp("+", IntLiteral(1), IntLiteral(2)), [CallExpr(Id("foo"), [])]), BinaryOp("+", IntLiteral(0x99), FloatLiteral(1.e79)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_68(self):
        input = """
            Function: main
                Body:
                    Var: x = 1, y = 1., z[1]=0X1, k[100][0x1]=0o1;
                EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], IntLiteral(1)), VarDecl(Id("y"), [], FloatLiteral(1.)), VarDecl(Id("z"), [1], IntLiteral(0X1)), VarDecl(Id("k"), [100,0x1], IntLiteral(0o1))],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_69(self):
        input = """
            Var: x={};
            Var: y= "\\\\";
            Function: main
                Body:
                EndBody.
        """
        expect = Program([VarDecl(Id("x"), [], ArrayLiteral([])), VarDecl(Id("y"), [], StringLiteral("\\\\")), FuncDecl(Id("main"), [], ([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_70(self):
        input = """
        """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_71(self):
        input = """
        Function: main
        Body: 
            Do 
                Var: x;
                foo(2+x,4. \.  y); 
            While i<0x1 EndDo.
        EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[Dowhile(([VarDecl(Id("x"), [], None)],[CallStmt(Id("foo"), [BinaryOp("+", IntLiteral(2), Id("x")), BinaryOp("\.", FloatLiteral(4.), Id("y"))])]), BinaryOp("<", Id("i"), IntLiteral(0x1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_72(self):
        input = """
        Function: pascal_program
            Body:
            For(hang=2,hang<size,hang+1) Do 
                Var: x;
                Var: y;
                Var: z;
            EndFor.   
            EndBody.
        """
        expect = Program([FuncDecl(Id("pascal_program"), [], ([],[For(Id("hang"), IntLiteral(2), BinaryOp("<", Id("hang"), Id("size")), BinaryOp("+", Id("hang"), IntLiteral(1)), ([VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_73(self):
        input = """
        Function: sub
            Parameter: a[1][0x1][0O7]
            Body:   
            EndBody.
        """
        expect = Program([FuncDecl(Id("sub"), [VarDecl(Id("a"), [1,0x1,0O7], None)], ([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_74(self):
        input = """
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Var: x[1];
                    Return 1;
                ElseIf foo(2+{1}) Then
                    Var: y=9;
                Else
                    Var: z;
                    Return n * fact(n - 1);
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("fact"), [VarDecl(Id("n"), [], None)], ([],[If([(BinaryOp("==", Id("n"), IntLiteral(0)), [VarDecl(Id("x"), [1], None)], [Return(IntLiteral(1))]), (CallExpr(Id("foo"), [BinaryOp("+", IntLiteral(2), ArrayLiteral([IntLiteral(1)]))]), [VarDecl(Id("y"), [], IntLiteral(9))], [])], ([VarDecl(Id("z"), [], None)],[Return(BinaryOp("*", Id("n"), CallExpr(Id("fact"), [BinaryOp("-", Id("n"), IntLiteral(1))])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_75(self):
        input = """
        Function: foo
            Body:
                For (i = 0, i < length(str), 1) Do
                    If !str[i] Then
                        writeln(str[i]);
                    EndIf.
                EndFor.    
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], ([],[For(Id("i"), IntLiteral(0), BinaryOp("<",Id("i"), CallExpr(Id("length"), [Id("str")])), IntLiteral(1), ([],[If([(UnaryOp("!", ArrayCell(Id("str"), [Id("i")])), [], [CallStmt(Id("writeln"), [ArrayCell(Id("str"), [Id("i")])])])], ([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_76(self):
        input = """
        Function: square_num
            Parameter: x
            Body: 
                Return sqrt(x + square_num(x - 1));
            EndBody.
        Function: main
            Body:
            EndBody.
        """
        expect = Program([FuncDecl(Id("square_num"), [VarDecl(Id("x"), [], None)], ([],[Return(CallExpr(Id("sqrt"), [BinaryOp("+", Id("x"), CallExpr(Id("square_num"), [BinaryOp("-", Id("x"), IntLiteral(1))]))]))])), FuncDecl(Id("main"), [], ([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_77(self):
        input = """
        Function: test
            Body: 
                Return;
                Break;
                Continue;
            EndBody.
        """
        expect = Program([FuncDecl(Id("test"), [], ([],[Return(None), Break(), Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_78(self):
        input = """
        Function: foo
            Body:
                a = -1;
                Return a * 190;
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], ([],[Assign(Id("a"), UnaryOp("-", IntLiteral(1))), Return(BinaryOp("*", Id("a"), IntLiteral(190)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_79(self):
        input = """
        Function: foo
            Body:
                a = !1;
                Return a * 0x1234AF;
                b = !True;
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], ([],[Assign(Id("a"), UnaryOp("!", IntLiteral(1))), Return(BinaryOp("*", Id("a"), IntLiteral(0x1234AF))), Assign(Id("b"), UnaryOp("!", BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_80(self):
        input = """
        Function: foo
            Body:
                a = a * 1;
                b = 12. * 3.e3;
                c = 0X123 \ 3;
                Return;
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], ([],[Assign(Id("a"), BinaryOp("*", Id("a"), IntLiteral(1))), Assign(Id("b"), BinaryOp("*", FloatLiteral(12.), FloatLiteral(3.e3))), Assign(Id("c"), BinaryOp("\\", IntLiteral(0X123), IntLiteral(3))), Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_81(self):
        input = """
        Function: foo
            Body:
                Return (a == b) && (a != c) || (a > b) || (a < c);
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], ([],[Return(BinaryOp("||", BinaryOp("||", BinaryOp("&&", BinaryOp("==", Id("a"), Id("b")), BinaryOp("!=", Id("a"), Id("c"))), BinaryOp(">", Id("a"), Id("b"))), BinaryOp("<", Id("a"), Id("c"))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_82(self):
        input = """
        Function: square
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
                Return v;
            EndBody.
        """
        expect = Program([FuncDecl(Id("square"), [], ([VarDecl(Id("r"), [], FloatLiteral(10.)), VarDecl(Id("v"), [], None)],[Assign(Id("v"), BinaryOp("*.", BinaryOp("*.", BinaryOp("*.", BinaryOp("*.", BinaryOp("\.", FloatLiteral(4.), FloatLiteral(3.)), FloatLiteral(3.14)), Id("r")), Id("r")), Id("r"))), Return(Id("v"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_83(self):
        input = """
        Var: arr[3][2] = {{1, 2}, {4, 5}, {3, 5}};
        """
        expect = Program([VarDecl(Id("arr"), [3,2], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(4), IntLiteral(5)]), ArrayLiteral([IntLiteral(3), IntLiteral(5)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_84(self):
        input = """
        Function: main
            Body:
                Var: s = "this is a string containing tab \t", a = "0XFA1B23";
                s = s + string(a);
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("s"),[], StringLiteral("this is a string containing tab \t")), VarDecl(Id("a"), [], StringLiteral("0XFA1B23"))],[Assign(Id("s"), BinaryOp("+",Id("s"), CallExpr(Id("string"), [Id("a")])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_85(self):
        input = """
        Function: main
            Body:
                Var: a = 0XFA1B23;
                Var: b = 1;
                a = a *- b;
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"),[], IntLiteral(0XFA1B23)), VarDecl(Id("b"), [], IntLiteral(1))],[Assign(Id("a"), BinaryOp("*", Id("a"), UnaryOp("-", Id("b"))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_86(self):
        input = """
        Function: abc
            Body:
                a = !((!b && c) + 1) || check(d);
                Return a;
            EndBody.
        """
        expect = Program([FuncDecl(Id("abc"), [], ([],[Assign(Id("a"), BinaryOp("||", UnaryOp("!", BinaryOp("+", BinaryOp("&&", UnaryOp("!", Id("b")), Id("c")), IntLiteral(1))), CallExpr(Id("check"), [Id("d")]))), Return(Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_87(self):
        input = """
        Function: main
            Body:
                If !(a + b * 10) Then
                    Return True;
                EndIf.
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[If([(UnaryOp("!", BinaryOp("+", Id("a"), BinaryOp("*", Id("b"), IntLiteral(10)))), [],[Return(BooleanLiteral(True))])], ([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_88(self):
        input = """
        Function: main
            Body:
                c = a == b;
                d = c+-1.23*.-3e4;
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[Assign(Id("c"), BinaryOp("==", Id("a"), Id("b"))), Assign(Id("d"), BinaryOp("+", Id("c"), BinaryOp("*.", UnaryOp("-", FloatLiteral(1.23)), UnaryOp("-", FloatLiteral(3e4)))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_89(self):
        input = """
            Var: a = 5;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: c, d = 6, e, f;
        """
        expect = Program([VarDecl(Id("a"), [], IntLiteral(5)), VarDecl(Id("b"), [2,3], ArrayLiteral([ArrayLiteral([IntLiteral(2), IntLiteral(3), IntLiteral(4)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])])), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], IntLiteral(6)), VarDecl(Id("e"), [], None), VarDecl(Id("f"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_90(self):
        input = """
            Function: main
            Body:
                foo(3 + x[i] * y(3,z(4)));
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[CallStmt(Id("foo"), [BinaryOp("+", IntLiteral(3), BinaryOp("*", ArrayCell(Id("x"), [Id("i")]), CallExpr(Id("y"), [IntLiteral(3), CallExpr(Id("z"), [IntLiteral(4)])])))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_91(self):
        input = """
            Var: abc =  0XF123,    x___asdyz = 0xA398;
        """
        expect = Program([VarDecl(Id("abc"), [], IntLiteral(0XF123)), VarDecl(Id("x___asdyz"), [], IntLiteral(0xA398))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_92(self):
        input = """
            Function: foo
            Body:
                For (i = 0, i < 10, 2) Do
                    writeln(a[i] + b);
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], ([],[For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(10)), IntLiteral(2), ([],[CallStmt(Id("writeln"), [BinaryOp("+", ArrayCell(Id("a"), [Id("i")]), Id("b"))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_93(self):
        input = """
            Function: foo
            Body:
                Var: x;
                Break;
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], ([VarDecl(Id("x"), [], None)],[Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_94(self):
        input = """
            Function: foo
            Body:
                Var: y;
                Continue;
            EndBody.
        """
        expect = Program([FuncDecl(Id("foo"), [], ([VarDecl(Id("y"), [], None)],[Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_95(self):
        input = """
            Function: main
            Body:
                Var: x;
                input(x);
                printDivivsors(x);
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("x"), [], None)],[CallStmt(Id("input"), [Id("x")]), CallStmt(Id("printDivivsors"), [Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_96(self):
        input = """
            Function: power_recur
            Parameter: base, exp
            Body:
                If (exp == 0) Then
                    Return 1;
                EndIf.
                Return base * power_recur(base, exp - 1);
            EndBody.
        """
        expect = Program([FuncDecl(Id("power_recur"), [VarDecl(Id("base"), [], None), VarDecl(Id("exp"), [], None)], ([],[If([(BinaryOp("==", Id("exp"), IntLiteral(0)), [],[Return(IntLiteral(1))])], ([],[])), Return(BinaryOp("*", Id("base"), CallExpr(Id("power_recur"), [Id("base"), BinaryOp("-", Id("exp"), IntLiteral(1))])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_97(self):
        input = """
            Function: main
            Parameter: base, exp
            Body:
                base = input();
                writeln(power_rep(base, exp));
            EndBody.
        """
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("base"), [], None), VarDecl(Id("exp"), [], None)], ([],[Assign(Id("base"), CallExpr(Id("input"), [])), CallStmt(Id("writeln"), [CallExpr(Id("power_rep"), [Id("base"), Id("exp")])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_98(self):
        input = """
            **
            * A
            &
            * %\\s
            * 3'
            **
        """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_99(self):
        input = """
            ****
            Var: x;
            ********
        """
        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_100(self):
        input = """
            ****
            Function: main
            Body:
            EndBody.
            ********
        """
        expect = Program([FuncDecl(Id("main"), [], ([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))











