import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    """ Program structure """

    def test_201(self):
        input = """Var: x;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_202(self):
        input = """Var: ;"""
        expect = """Error on line 1 col 5: ;"""
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_203(self):
        input = """Var: hOang = 15;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_204(self):
        input = """Var: h_123 =  0XF123"""
        expect = """Error on line 1 col 20: <EOF>"""
        self.assertTrue(TestParser.checkParser(input, expect, 204))
    def test_205(self):
        input = """Var: h_123 =  123.456"""
        expect = """Error on line 1 col 21: <EOF>"""
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_206(self):
        input = r"""
Var: h, o, a, n,g;
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_207(self):
        input = r"""Var: a, b, ;
"""
        expect = """Error on line 1 col 11: ;"""
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_208(self):
        input = r"""
Var: h[1][2][3][4];
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_209(self):
        input = r"""
Var: a[-1];
"""
        expect = """Error on line 2 col 7: -"""
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_210(self):
        input = r"""
Var: a[1.0];
"""
        expect = """Error on line 2 col 7: 1.0"""
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_211(self):
        input = r"""
Var: a[b];
"""
        expect = """Error on line 2 col 7: b"""
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_212(self):
        input = r"""
Var: a[];
"""
        expect = """Error on line 2 col 7: ]"""
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_213(self):
        input = r"""
Var: a[0];
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_214(self):
        input = r"""
Var: a = -1;
"""
        expect = """Error on line 2 col 9: -"""
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_215(self):
        input = r"""
Var: hoang = h;
"""
        expect = """Error on line 2 col 13: h"""
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_216(self):
        input = r"""
Var: 1 = hoang;
"""
        expect = """Error on line 2 col 5: 1"""
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_217(self):
        input = r"""
Var: a[0o256];
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_218(self):
        input = r"""
Function: main
"""
        expect = """Error on line 3 col 0: <EOF>"""
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_219(self):
        input = r"""
Function:
    Body:
    EndBody.
"""
        expect = """Error on line 3 col 4: Body"""
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_220(self):
        input = r"""
Var: hoang= "tran";
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_221(self):
        input = r"""
Var: hoang[2][3]= {1};
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_222(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_223(self):
        input = r"""
        Var: hoang;
Function: foo
    Body:
        foo();
        Var: a;
    EndBody.
"""
        expect = """Error on line 6 col 8: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_224(self):
        input = r"""
       Var: hoang;
Function: main
    Parameter: a
    Body:
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_225(self):
        input = r"""
        Var: hoang;
        Var: hoang;
        Var: hoang;
        Var: hoang;
Function: main
    Parameter: a, b
    Body:
    EndBody.
    Function: main
    Parameter: a, b
    Body:
    EndBody.
    Function: main
    Parameter: a, b
    Body:
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_226(self):
        input = r"""
         Var: hoang;
Function: main
    Parameter: a, b
    Body:
    EndBody.
    Function: main
    Parameter: a, b
    Body:
    EndBody.
    Function: main
    Parameter: a, b
    Body:
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_227(self):
        input = r"""
        Var: hoang;
Function: main
    Parameter: hoang[1][2]
    Body:
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_228(self):
        input = r"""
        Var: hoang;
Function: main
    Parameter:
    Body:
    EndBody.
"""
        expect = """Error on line 5 col 4: Body"""
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_229(self):
        input = r"""
        Var: hoang;
Function: main
    Parameter: h = 1
    Body:
    EndBody.
"""
        expect = """Error on line 4 col 17: ="""
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_230(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        Function: main
        Body:
        EndBody.
    EndBody.
"""
        expect = """Error on line 5 col 8: Function"""
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    """ If statement """

    def test_231(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_232(self):
        input = r"""
        Var: hoang;
        Function: hoang
    Body:
        If True
        EndIf.
    EndBody.
Function: main
    Body:
        If hoang
        EndIf.
    EndBody.
"""
        expect = """Error on line 6 col 8: EndIf"""
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_233(self):
        input = r"""
        Var: hoang;
        Function: hoang
    Body:
        If True
        EndIf.
    EndBody.
Function: main
    Body:
        If a Then
            Var: a = 1;
        EndIf.
    EndBody.
"""
        expect = """Error on line 6 col 8: EndIf"""
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_234(self):
        input = r"""
        Var: hoang;
        Function: hoang
    Body:
        If True
        EndIf.
    EndBody.
Function: main
    Body:
        If a Then
            foo();
        EndIf.
    EndBody.
"""
        expect = """Error on line 6 col 8: EndIf"""
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_235(self):
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
        **Test comment 
        *Tran
        *danh
        *Hoang
        !!!**
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_236(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        If a Then
            foo();
        ElseIf
            Var: a = 1;
        EndIf.
    EndBody.
"""
        expect = """Error on line 13 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    """ ElseIf """

    def test_237(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        If True Then
        ElseIf True Then
        EndIf.
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_238(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        If True Then
        ElseIf True
        EndIf.
    EndBody.
"""
        expect = """Error on line 12 col 8: EndIf"""
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_239(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        If True Then
        Else If True Then
        EndIf.
    EndBody.
"""
        expect = """Error on line 13 col 4: EndBody"""
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_240(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        If True Then
        ElseIf True Then
        ElseIf True Then
        EndIf.
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_241(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
        Function: foo
            Parameter: a[5], b
            Body:
                For (i = 0, hoang < 10, 15) Do
                    writeln(a[i] + b);
                EndFor.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody."""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_242(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
        Function: testWhileDo
            Parameter: a
            Body:
                Var: hoang_123 = 0;
                **While have no "Do"**
                While (a[i] > b)
                    writeln(a[i]);
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = """Error on line 14 col 20: writeln"""
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_243(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
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
        expect = """Error on line 8 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_244(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: main
            Parameter: a ** = 3 **, b = "error";
            Body:
            EndBody.
        """
        expect = """Error on line 9 col 38: ="""
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_245(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: main
            Body:
                While a > 0 Do
                EndWhile.
                While If a > 0 Then Do
                EndWhile.
            EndBody.
        """
        expect = """Error on line 12 col 22: If"""
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    """ Else """

    def test_246(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: main
            Body:
                Var: a, b = 5;
                input(a);
                If (a > b && a < 10) Then
                    Return True;
                Else
                    Return False;
                EndIf.
            EndBody.
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_247(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: main
            Body:
                Var: a = 0XFA1B23;
                Var: b = 1;
                a = a *+ b;
                writeln(a);
            EndBody.
        """
        expect = """Error on line 12 col 23: +"""
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_248(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        If True Then
        Else
        Else
        EndIf.
    EndBody.
"""
        expect = """Error on line 12 col 8: Else"""
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_249(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        If True Then
        Else Then
        EndIf.
    EndBody.
"""
        expect = """Error on line 11 col 13: Then"""
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_250(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: main
            Return 1;
        """
        expect = """Error on line 9 col 12: Return"""
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_251(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: main
            Body:
                Var: a = b;
            EndBody.
        """
        expect = """Error on line 10 col 25: b"""
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_252(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: main
            Body:
                a = 1!;
            EndBody.
        """
        expect = """Error on line 10 col 21: !"""
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_253(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        If True Then
        Else
            foo();
            Var: a;
        EndIf.
    EndBody.
"""
        expect = """Error on line 13 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    """ While """

    def test_254(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
            EndBody.
        """
        expect = """Error on line 8 col 12: Body"""
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_255(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: foo
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While (i < 5)
                    a[i] = b +. 1.0;
                    i = i + 1;
                EndWhile.
            EndBody.
        """
        expect = """Error on line 13 col 20: a"""
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_256(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: foo
            Body:
                Var: s = "123";
                n = int(s);
                Body:
                    Return True;
                EndBody.
            EndBody.
        """
        expect = """Error on line 12 col 16: Body"""
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_257(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: foo
            Body:
                Var: s = "123";
                n = int(s);
                Function: a
                Body:
                    Return True;
                EndBody.
            EndBody.
        """
        expect = """Error on line 12 col 16: Function"""
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_258(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        While True Do
            foo();
            Var: a;
        EndWhile.
    EndBody.
"""
        expect = """Error on line 12 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_259(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: foo
            Body:
                a = 1 -;
            EndBody.
        """
        expect = """Error on line 10 col 23: ;"""
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_260(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        Do
            Var: a;
        While True
        EndDo.
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_261(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        Do
            foo();
        While True
        EndDo.
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_262(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        Do
            Var: a;
            foo();
        While True
        EndDo.
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_263(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        Do
            foo();
            Var: a;
        While True
        EndDo.
    EndBody.
"""
        expect = """Error on line 12 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 263))


    def test_264(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        For (a = 1 + 1, 1.0, --1) Do
        EndFor.
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_265(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        For (a, a < 10, 1) Do
        EndFor.
    EndBody.
"""
        expect = """Error on line 10 col 14: ,"""
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_266(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        For (Var: a = 1, a < 10, 1) Do
        EndFor.
    EndBody.
"""
        expect = """Error on line 10 col 13: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_267(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        For (a[1] = 1, a < 10, 1) Do
        EndFor.
    EndBody.
"""
        expect = """Error on line 10 col 14: ["""
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_268(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: test
            Parameter: num
            Var: test = 100;
            Body:
                For (i = num * 2, i < num * num, i + 1) Do
                    Var: a = 1;
                    If i % 2 == 0 Then
                        writeln(a * i);
                    EndIf.
                EndFor.
            EndBody."""
        expect = """Error on line 10 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_269(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        For (a = 1, a < 10, 1) Do
            foo();
        EndFor.
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_270(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        For (a = 1, a < 10, 1) Do
            Var: a;
            foo();
        EndFor.
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_271(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        For (a = 1, a < 10, 1) Do
            foo();
            Var: a;
        EndFor.
    EndBody.
"""
        expect = """Error on line 12 col 12: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_272(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        Break;
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    """ Continue """

    def test_273(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        Continue;
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    """ Return """

    def test_274(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
            Function: test
            Parameter: num
            Body:
                For (i = num * 2, i < num * num, i + 1) Do
                    If i % 2 == 0 Then
                        writeln(a * i);
                    EndIf.
                    Var: a = 1;
                EndFor.
            EndBody."""
        expect = """Error on line 15 col 20: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_275(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        Return 1;
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    """ Function call """

    def test_276(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        foo();
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_277(self):
        input = r"""
        
            Var: arr[5][6]=1.e790,b,c=2;
            Var: x;
            Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_278(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        foo(1, a[2], True, "", 1.);
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_279(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        foo(foo(foo()));
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 279))


    def test_280(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_281(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a()[1]=5;
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_282(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a[-1][foo() + a] = 1;
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_283(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
        Function: longest_substr
            Parameter: str
            Body:
                Var: count = 0, check = False;
                For (i = 0, i < length(str), 1) Do
                    For (j = 0, j < length(str), 1) Do
                        **Error is here (!=)**
                        If (str[i] == str[j] && i != j) Then
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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_284(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        1 = 1;
    EndBody.
"""
        expect = """Error on line 10 col 8: 1"""
        self.assertTrue(TestParser.checkParser(input, expect, 284))


    def test_285(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
        Function: power_rep
            Parameter: base, exp
            Body:
                If (exp == 0) Then
                    Return 1;
                EndIf.
                For (i = 0, i < exp - 1, 1) Do
                    base = base * a;
                EndFor.
                Var: a = 2;
                Return base;
            EndBody.
        """
        expect = """Error on line 17 col 16: Var"""
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_286(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = 1;
        a = 1.0;
        a = True;
        a = False;
        a = "Hello World \n";
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_287(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = { 1, 2, 3, 4 };
        a = { 1.0, 2.0, 3.0, 4.0 };
        a = { True, False };
        a = { {1,2}, {3,4} };
        a = {{{{{1}}}}};
        a = {{{{{1}}}}, {1}, 1};
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_288(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = {};
    EndBody.
"""
        expect = """Error on line 10 col 13: }"""
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_289(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = { -1 };
    EndBody.
"""
        expect = """Error on line 10 col 14: -"""
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_290(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = b;
        a = foo();
        a = foo(1,True);
        a = a[1];
        a = foo()[1];
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_291(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = (a);
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_292(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = ();
    EndBody.
"""
        expect = """Error on line 10 col 13: )"""
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_293(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = (((a)));
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_294(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = --1;
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_295(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = +1;
    EndBody.
"""
        expect = """Error on line 10 col 12: +"""
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_296(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = 1++1;
    EndBody.
"""
        expect = """Error on line 10 col 14: +"""
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_297(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = !a > b || c + d * e[2];
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_298(self):
        input = r"""
        Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Body:
        a = !--.1;
        a = 3----------------1;
    EndBody.
"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_299(self):
        input = r"""
       
        Var: hoang;
            Function: main
            Body:
                Var: a = b;
            EndBody.
        """
        expect = """Error on line 6 col 25: b"""
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_300(self):
        input = r"""
        
Var: a, b[1], c[1][1], d = 1, e = 1e1, f = "Hello", g = True, i = {{1,2}};
Var: hoang;
Function: main
    Body:
        If False Then
        EndIf.
    EndBody.
Function: main
    Parameter: a, a[1], a[1][1]
    Body:
        Var: a = 1, b = 1., c = "", d = True;
        Var: sum = 0;
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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    
