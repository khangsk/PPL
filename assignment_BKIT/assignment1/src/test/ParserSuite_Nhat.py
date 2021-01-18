import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """
        Var: x;
        Function: main
        Parameter: x
        Body:
            If (a> 0 && b >0) Then
                a= int_of_string();
                b= float_of_int(a) +. 2.0;
            EndIf.
        EndBody.
        """
        expect = "Error on line 6 col 26: >"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_2(self):
        input = """
        Var: x = 1;
        Function: main
        Parameter: x
        Body:
            While(i<5) Do
                For (i = 1 , i<10 ,2) Do
                    a=a+-1;
                EndFor.
            EndWhile.
            For (i=x+7,i<a[2][3], 6) Do
                writeLn(i);
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_3(self):
        input = """
        Var: a;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c,d=6,e,f;
        Var: m,n[10];
        Function: main
        ** This is a 
        
        * multi-line
        * comment.
        **
        Parameter: a[5][7],b
        Body:
            Var: i=0; 
            Do foo(2+x,4. \.  y); While i<100 EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_4(self):
        input = """
        Var: x=120000e-1;
        ** This is a single-line comment. **
        Function: fact
        Body:
            Var: v;
            If n==0 Then 
                Return 1;
            Else
                a[3+foo(2)] = a[b[2][3]] +4;
                Return n*fact(n-1);
            EndIf.
        EndBody.
        
        Function: main
        Body:
            x=10;
            fact (x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_5(self):
        input = """
               Function: compare
                   Parameter: x, y
                   Body:
                       If (x > y) Then
                           Return True ;
                       Else Return False;
                       EndIf.
                   EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_6(self):
        input = """
        Function: main
        Body:
        s = "abc
        EndBody."""
        expect = "abc"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_7(self):
        input = """
            Function: reverseString
                Parameter: num
                Body:
                    For (i = num * 2, i < num * num, i = i + 1) Do
                        If i % 2 == 0 Then
                            writeln(i);
                        EndIf.
                    EndFor.
                EndBody."""
        expect = "Error on line 5 col 55: ="
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_8(self):
        input = """
            Var: arr[5][6]=1.e790,b,c=2;
            Var: x;
            Function: test_8
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_9(self):
        input = """
            Function: tEST_9
                Parameter: x,a[69],b[1][2][3]
                Body:
                    For (i=1, goo(2+a[6]) < i,2>goo(9)) Do
                        If arr[7] >= foo(3) Then
                            Break;
                        EndIf.
                    EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_10(self):
        input = """
            Function: tEST_10
                Body:
                    Var: max={0};
                    For ( i=1,i<n,1) Do
                        If max < a[i] Then
                            max = a[i]
                        EndIf.
                    EndFor.
                    println(max);
                EndBody."""
        expect = "Error on line 8 col 24: EndIf"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_11(self):
        input = """
            Var: i;
            Function: tEST_11
                Body:
                    For(i=100,i<strlen(s1)\\2,2) Do
                        If (s1[i] != s1[strlen(s1)-1-i]) Then
                            Return 0;
                        EndIf.
                        Return 1;
                    EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_12(self):
        input = """
            Var: i = "This is a string \\x and error"
            """
        expect = "This is a string \\x"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_13(self):
        input = """
            Var: x={1, 2,   3}, y;
            Function: tEST_13
                Body:
                    v = a && b > 2 =/= 0;
                EndBody.
                """
        expect = "Error on line 5 col 35: =/="
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_14(self):
        input = """
            Var: x;
            Function: tEST_14
                Body:
                    Var: s;
                    print(s);
                    For(i=0,i<=. size(), i>9) Do
                        If (s[i] >= a) && (s[i] <= z) Then
                            s[i]=s[i]-32;
                            Continue;
                        EndIf.
                    EndFor.
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_15(self):
        input = """
        Var: pascalTr[10][10]; 
        Var: hang,cot; 
        Function: pascal_program
            Body:
            For(hang=0,hang<size,hang+1) Do 
                For(cot=0,cot<size,cot+1) Do
                    pascalTr[hang][cot]=0; 
                    pascalTr[0][0]=1; 
                    pascalTr[1][0]=1; 
                    pascalTr[1][1]=1; 
                EndFor.
            EndFor.
         
            For(hang=2,hang<size,hang+1) Do 
                pascalTr[hang][0]=1; 
                For(cot=1,cot<=hang,cot+1) Do
                    pascalTr[hang][cot]=pascalTr[hang-1][cot-1]+pascalTr[hang-1][cot]; 
                EndFor.                   
            EndFor.   
                 
            For(hang=0,hang<size,hang+1) Do 
                For(cot=0,cot<=hang,cot+1) Do                
                   printf(pascalTr[10][10]); 
                EndFor. 
            println();   
            EndFor.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_16(self):
        input = """
            Var: ajsd_123s = "Nhat", s__12sA[2] = {  "Long" ,    "Nhat"     };
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_17(self):
        input = """
            Var: a[100]={{{{}}}};
            Function: func_17__
                Body:
                    Var: x;
                    print(s);
                    For(i=0,i<=. size(), i>9) Do
                        Var: y=1.;
                        If (s[i] >= a) && (s[i] <= z) Then
                            s[i]=s[i]-32;
                            Continue;
                        EndIf.
                    EndFor.
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_18(self):
        input = """
            Function: name__func0_18
                Body:
                    For(i=0,i<=. size(), i>9) Do
                        Var: y=1.;
                        If (s[i] >= a) && (s[i] <= z) Then
                            Var: y;
                            s[i]=s[i]-32;
                            Continue;
                        EndIf.
                        Var: z={1};
                    EndFor.
                EndBody.
            """
        expect = "Error on line 11 col 24: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_19(self):
        input = """
            Var: x[7][6]={1,"abc",1.};
            Function: test_index_op
                Body:
                    v=123[True];
                    y=123[0[0[False]]];
                    z=a[1[1][1][1][1][1][1][1]];
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test20(self):
        input = """
            Function: foo 
                Body: 
                    a = 1 + 1.23 *. abc \. id[12[123][2][moreid]];
                    b = 1.E-12  =/= foo(123);
                EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test21(self):
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
                        For ( i=2,i<n, i+1 ) Do
                            f0=f1;
                            f1=fn;
                            fn=f0+f1;
                        EndFor.
                    EndIf.
                    Return fn;
                EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test22(self):
        input = """
            Function: isPrimeNumber
            Parameter: n
                Body: 
                    If n<2 Then
                        Return 0;
                    EndIf.
                    squareRoot = int(sqrt(n));
                    Var: i;
                    For (i = 2, i <= squareRoot, 1) Do
                        If (n % i == 0) Then
                            Return 0;
                        EndIf.
                    EndFor.
                    Return 1;
                EndBody.
                """
        expect = "Error on line 9 col 20: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test23(self):
        input = """
            Function: tinhGiaiThua
            Parameter: n
                Body: 
                    Var: i;
                    Var: giai_thua = 1;
                    If ((n == 0) || (n == 1)) Then
                        Return giai_thua;
                    Else
                        For (i = 2, i <= n, i==100) Do
                            giai_thua = giai_thua*i;
                        EndFor.
                    Return giai_thua;
                    EndIf.
                EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test24(self):
        input = """
            Function: convertNumber
            Parameter: n,b
                Body: 
                    Var: i;
                    Var: arr[20];
                    Var: count = 0;
                    Var: m;
                    Var: remainder = 1;
                    if (n < 0 || b < 2 || b > 16 ) Then
                        cout("He co so hoac gia tri chuyen doi khong hop le!");
                        Return 0;
                    }
                EndBody.
                """
        expect = "Error on line 10 col 35: <"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test25(self):
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
                        remainder = remainder \ b;
                    EndWhile.
                    ** This is a comment **
                    For (i = count - 1, i >= 0, i-1) Do
                        printf("%c, arr[i]");
                    EndFor.
                    Return -1;
                EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test26(self):
        input = """
            Function: main
                Body:
                    Var: s;
                    s = "Hello, my name is Long Nhat \\h \'.";
                    println(x__);
                EndBody.
        """
        expect = "Hello, my name is Long Nhat \h"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test27(self):
        input = """
            Function: phanTichSoNguyen
            Parameter: n
                Body:
                Var: i = 2;
                Var: dem = 0;
                Var: a[100];
                ** This is test comment 1 **
                While n <=. 1 Do
                    If (n % i == 0) Then
                        n = n \ i;
                        a[dem+1] = i;
                    Else 
                        i=i+.1.;
                    EndIf.
                EndWhile.
                 ** This is test comment 2 **
                If dem == 0 Then
                    a[dem+1] = n;
                EndIf.
                ** Show result **
                For (i = 0, i < dem - 1, 1) Do
                    printf(a[i]);
                EndFor.
                printf(a[dem - 1]);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test28(self):
        input = """
            Function: main
            Body:
            Var: s[0] = "VietTuts.Vn";  ** initial value of s **
            Var: ch = "t";             ** comment test **
            Var: i = 0;
            Var: count = 0;             
            While s[i] != "0" Do
                If s[i] == ch Then
                    count=count+1;
                EndIf.
            i=i+1;
            EndWhile.
            If count > 0 Then
                printf("Ky tu %c xuat hien %d lan trong chuoi \\n ");
            Else
                printf("Ky tu %c khong co mat trong chuoi \\h");
            EndIf.
            Return 0;
            EndBody.
        """
        expect = "Ky tu %c khong co mat trong chuoi \\h"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test29(self):
        input = """
            Var: str_1 = "Nguyen long nhat \t \\n";
            Var: x__[5][6]={{ }};
            Function: main 
            Body:
            Var: length = 0;
            While s1[length] != "\\\\" Do
                s2[length] = s1[length];
                length=length+1;
            EndWhile.
            s2[length] = "\\'";
            printf("Chuoi s1 = !s \n");
            Return 0;
            EndBody.
        """
        expect = "Chuoi s1 = !s "
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test30(self):
        input = """
            Function: test_comment
            Body:
                Var: x = {};
                ** this is a comment ****
            EndBody.
        """
        expect = ""
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test31(self):
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
            For (j = 1, j <= 10, 100) Do
                Continue;
            EndFor.
            Continue;
            Return 0;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test32(self):
        input = """
            Function: main
            Body:
            Var: i;
            print("In cac so le \\n:");
            For(i = 1, i <= 10, i+1) Do
                If i%2 != 0 Then
                    printf(" %2d\\n", i);
                    Var: x[5]={1};
                EndIf.
            EndFor.
            Return 0;
            EndBody.
        """
        expect = "Error on line 9 col 20: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test33(self):
        input = """
            Function: main
            Parameter: n, i, j
            Body:
            Var: x = 6;
            printf("Chuoi: \\t      ");
            For(i = 0, i <= n, i+1) Do
                For(j = 0, j <= n-i, j+1) Do
                    printf("  ");
                    For(j = 0, j <= i, j+x) Do
                        printf(" %3d", ncr(i, j));
                        printf("\\n");
                    EndFor.
                Return 0;
            EndBody.
        """
        expect = "Error on line 15 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test34(self):
        input = """
            Function: main
            Parameter: n, i, j
            Body:
            Var: x = 6;
            123[True][1][x] = {{}};
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test35(self):
        input = """
            Function: main
            Parameter: n, i, j
            Body:
            Var: x = -6;
            EndBody.
        """
        expect = "Error on line 5 col 21: -"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test36(self):
        input = """
            Function: main
            Body:
                Var: arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
                Var: i, total = 0;
                Var: size = "x";
                For(i = 0, i < size, i+1) Do
                    total = total + arr[i];
                EndFor.
                printf(5+x);
                Return 0;
            EndBody.
            Var: x;
        """
        expect = "Error on line 13 col 12: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test37(self):
        input = """
            Var: string[1] = "Long_Nhat";
            Var: temp;
            Var: i, j;
            Var: size = 000e23;
            Function: test_comment
            Body:
                printf("this is a string \\b");
                For (i = 0, i < size-1, i+1) Do
                    For (j = i+1, j < size, 100) Do
                        If (string[i] > string[j]) Then
                            temp = string[i];
                            string[i] = string[j];
                            string[j] = temp;
                        EndIf.
                    EndFor.
                EndFor.
                printf("string: '" a '" ");
                Return 0;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test38(self):
        input = """
            Var: x= "this is a string: \\K";
        """
        expect = "this is a string: \\K"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test39(self):
        input = """
            Function: func_name
            Parameter: n
            Body:
                Var: a[20];
                Var: dem = 0, i;
                Do
                    a[dem+1] = (n % dEC_10);
                    n = n \ dEC_10;
                While n > 0
                EndDo.
                For (i = 0, i < (dem \ 2), i+1) Do
                    If (a[i] != a[(dem - i - 1)]) Then
                        Return 0;
                    EndIf.
                EndFor.
                Return 1;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test40(self):
        input = """
            Function: main
            Body:
                Var: s1[50];     
                Var: s2[50];
                Var: n = 0;
                Var: flag = 1;
                printf("Nhap chuoi s1: ");
                gets(s1);
                printf("Nhap chuoi s2: ");
                gets(s2);
                ** this is a comment **
                While s1[n] != "\\\\" Do
                    If s1[n] != s2[n] Then
                        flag = 0;
                        Break;
                    EndIf.
                    n=n+1;
                EndWhile.
                If flag == 1 Then
                    printf("Chuoi %s va chuoi %s la giong nhau.", s1,s2);
                Else
                    printf("Chuoi %s va chuoi %s la khac nhau.", s1, s2);
                EndIf.
                Return 0;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test41(self):
        input = """
            Function: main
            Body:
                Var: string[100];
                printf("Nhap chuoi bat ky: ");
                gets(string);
                strupr(string);
                printf("this is a string \r");
                return (0);
        """
        expect = "this is a string "
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test42(self):
        input = """
            Var: x="fifa is my life" ";
        """
        expect = ";"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test43(self):
        input = """
            Var: x={0};
            Function: test_cmt
            Body:
                ** this is a comment *
            EndBody.
        """
        expect = ""
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test44(self):
        input = """
            Function: test
            Body:
                Var: n,i,j,k=1,a[6];
                Var: n = 6;
                printf("Ve tam giac Floyd:\n");
                For(i = 1, i <= n, a[foo()+9]) Do
                    For(j=1,j <= i, j+1) Do
                        printf("%3d", k++);
                    EndFor.
                EndFor.
                printf("\n");
            EndBody.
        """
        expect = "Ve tam giac Floyd:"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test45(self):
        input = """
            Function: main 
            Body:
                printf("Ve tam giac sao vuong can:\\n");
                For(i = 1, i <= n, i+x) Do
                    For(j = 1, j <= i, j+a) Do
                        printf("* ");
                    EndFor.
                printf("\n");
                EndFor.
            Return 0;
        """
        expect = ""
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test46(self):
        input = """
            Function: uSCLN
            Parameter: a,b
            Body:
                If b == 0 Then Return a; EndIf.
                Return uSCLN(b, a % b);
            EndBody.
            **
            * Tim boi so chung nho nhat (BSCNN)
            **
             
            Function: bSCNN
            Parameter: a,b
            Body:
                Return (a * b) \ uSCLN(a, b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test47(self):
        input = """
            **
            * giai phuong trinh bac 2: ax2 + bx + c = 0
            * 
            * @param a: he so bac 2
            * @param b: he so bac 1
            * @param c: so hang tu do
            **
            Function: giaiPTBac2_part_1
            Parameter: a,b,c
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test48(self):
        input = """
            **
            * giai phuong trinh bac 2: ax2 + bx + c = 0
            * 
            * @param a: he so bac 2
            * @param b: he so bac 1
            * @param c: so hang tu do
            **
            Function: giaiPTBac2_part_2
            Parameter: a,b,c
            Body:
                Var: delta = 1;
                Var: float = "x1";
                Var: float = "x2";
                delta = b*b - 4*a*c;
                If (delta > 0) Then
                    x1 = float((-b + sqrt(delta)) \ (2*a));
                    x2 = float((-b - sqrt(delta)) \ (2*a));
                    printf("Phuong trinh co 2 nghiem la: x1 = %f va x2 = %f", x1, x2);
                ElseIf delta == 0 Then
                    x1 = (-b \ (2 * a));
                    printf("Phong trinh co nghiem kep: x1 = x2 = %f", x1);
                Else
                    printf("Phuong trinh vo nghiem!");
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test49(self):
        input = """
            Var: s[4][20];
            Var: t[20];
            Var: i, j;
            Var: size = 4;
            Function: test____
            Body:
                printf("\\tNhap 4 chuoi bat ky: \\t");
                For (i = 0, i < size, i+1) Do
                    scanf("%s", s[i]);
                EndFor.
                For (i = 1, i < size, i+1) Do
                    For (j = 1, j < size, j+1) Do
                        If (strcmp(s[j - 1], s[j]) > 0) Then
                            strcpy(t, s[j - 1]);
                            strcpy(s[j - 1], s[j]);
                            strcpy(s[j], t);
                        EndIf.
                    EndFor.             
                EndFor.
            return(0);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test50(self):
        input = """
            Function: main
            Body:
                Var: n;
                printf("Nhap so nguyen duong = ");
                scanf("%d", n__0);
                printf("Cac so fibonacci nho hon %d va la so nguyen to: ", n);
                Var: i = 0;
            EndBody.
        """
        expect = "Error on line 8 col 16: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test51(self):
        input = """
            Function: main
            Body:
                Var: n, t;
                Var: sum = 0;
                For (i = 1, i <= n, i+1) Do
                    readln(a[i],b[i]);
                    sum = sum +- a[i];
                    EndFor.
                print(a[i]);
                For ( i = 1, i <= t, 1) Do
                    For (k = 1, k <= n, k+1) Do
                        If (a[k] > 0) Then
                            a[k] = -b[k];
                        EndIf.
                    EndFor.
                    For (j = 1, j <= n, j+1) Do
                        If (a[j] >= 0) Then
                            sum = sum + a[j];
                        EndIf.
                    EndFor.		
                    println(sum);
                EndFor.
            Return 0;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test52(self):
        input = """
            Function: prc
            Parameter: n
            Body:
                For ( y = 1, y < a, y+1) Do
                    x = a \ (y + 1) - y \ 2;
                    If ((y + 1)*(x + float(y) \ 2) == a) Then
                        print("a\\n");
                        For (j = x, j < x + y, j+1) Do
                            print("a\\t");
                        EndFor.
                        println(x + y, "this is a string\n");
                        Return 1;
                    EndIf.
                EndFor.
                Return x;
            EndBody.
        """
        expect = "this is a string"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test53(self):
        input = """
            Var: a[10][10],b[10][10],c[10][10];
            Var: i,j,m,n;
            Function: main
            Body:
                printf("nhap so hang m=");
                printf("nhap so cot n="); 
                printf("nhap vao ma tran:\\f");
                For(i=0,i<m,i+a[foo(2)]) Do
                    For(j=0,j<n,j+a[1]) Do
                        scanf("%d",a[i][j]);
                    EndFor.
                EndFor.
                For(i=0,i<m,i+1) Do
                    For(j=0,j<n,j+2) Do
                        scanf("%d",b[i][j]);
                    EndFor.
                EndFor.
                For(i=0,i<m,i+3) Do
                    For(j=0,j<n,j+4) Do
                        c[i][j]=a[i][j]+b[i][j];
                    EndFor.
                EndFor.
                printf("\\nMa tran sau cong:\\b");
                For(i=0,i<m,j+6) Do    
                    For(j=0,j<n,j+7) Do
                        printf("%5d",c[i][j]);
                    EndFor.
                printf("\\n");
                EndFor.
                getch();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test54(self):
        input = """
            Function: main
            Body:
                Var: kt=0;
                For(i=0,i<n,i+foo()) Do
                    For(j=0,j<n,j+a[5]) Do
                        If(((i==j)&&(a[i][j]!=1))||((i!=j)&&(a[i][j]!=0))) Then
                            kt=1;
                        EndIf.
                    EndFor.
                EndFor.
                If kt==0 Then
                    printf("\\nla ma tran don vi");
                Else        
                    printf("\\'khong phai la ma tran don vi");
                EndIf.
                Return 1+foo();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test55(self):
        input = """
            Function: selectionSort
            Parameter: arr[100],n
            Body:
                Var: i, j, min_idx;
                ****
                For (i = 1+foo(2), i < n-1, i+1) Do
                    **.**
                    min_idx = i;
                    For (j = i+1, j < n, j+2) Do
                        If (arr[j] < arr[min_idx]) Then
                            min_idx = j;
                        EndIf. 
                        **@**
                    EndFor.
                    swap(arr[min_idx], arr[i]);
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test56(self):
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
                arr[1] = {64, 25, 12, 22, 11};
                n = sizeof(arr)\sizeof(arr[0]);
                selectionSort(arr, n);
                printf("Sorted array: n");
                printArray(arr, n);
                Return 0;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test57(self):
        input = """
            Function: main
            Body:
                Var: n = 9, i;
                2[2] = {1, 5, 2, 7, 3, 4, 4, 1, 5};
                counting_sort(input, n);
                printf("Sorted Array : \r");
                For(i = 0, i < n, i+2) Do
                    Printf("%d ", input[i]);
                EndFor.
                Return 0;
            EndBody.
        """
        expect = "Sorted Array : "
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test58(self):
        input = """
            Function: partition
            Parameter: arr[1], low, high
            Body:
                Var: pivot = {"Center"};    ** pivot **
                Var: left = "low \\t";
                Var: right = 1;
                While True Do
                    While(left <= right) && (arr[left] < pivot) Do left=left+1; EndWhile.  ** Tim phan tu >= arr[pivot] **
                    While(right >= left) && (arr[right] > pivot) Do right=right-1; EndWhile. ** Tim phan tu <= arr[pivot] **
                        If (left >= right) Then Break; EndIf. **  **
                        swap(arr[left], arr[right]); ** . **
                        left=left+1; ** % **
                        right=right-1; ********
                        swap(arr[left], arr[high]);
                    Return left; **  ******
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test59(self):
        input = """
            Function: partition
            Parameter: arr[1], low, high
            Body:
                ** this is a comment_1 * * **
                ** this is a comment_2 * *
            EndBody.
        """
        expect = ""
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test60(self):
        input = """
            Function: partition
            Parameter: arr[1], low, high
            Body:
                Var: 
                ** this is a comment ******
            EndBody.
        """
        expect = "Error on line 7 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test61(self):
        input = """
            Function: nhapMaTran
            Parameter: a[1][2], n
            Body:
                Do
                    printf("\\nNhap n: ");
                    scanf("%d", n);
                    If (n < 1) || (n > max) Then
                        printf("\\\\So phan tu khong hop le. Xin kiem tra lai !");
                    EndIf.
                While (n < 1) || (n > max) EndDo.
                For(i = 0, i < n, i+1) Do
                    For(j = 0, j < n, j+go()) Do
                        printf("\\bNhap vao a[%d][%d] = ", i, j);
                        scanf("%d", a[i][j]);
                    EndFor.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test62(self):
        input = """
            Function: main
            Body:
                Var: a[100][100], n;
                nhapMaTran(a,n);
                xuatMaTran(a,n);
                dem1 = demSoChanMaTranTamGiacTrenDuongCheoChinh(a, n);
                printf("\\\\nSo luong so chan ma tran tam giac tren duong cheo chinh = %d", dem);
                dem2 = demSoChanMaTranTamGiacTrenDuongCheoPhu(a, n);
                printf("\\'So luong so chan ma tran tam giac tren duong cheo phu = %d", dem2);
                getch();
                Return 0;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test63(self):
        input = """
            Function: main
            Body:
                a = " this is a string : '" a'" and '" ";
                Break;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test64(self):
        input = """
            Var: x;
            Function: main
            Body:
                a = " this is a string : '" a'" and '" ";
            EndBody.
            x=1;
        """
        expect = "Error on line 7 col 12: x"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test65(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test66(self):
        input = """
            Var: x;
            Function: main
            Body:
                Var: x = "This is a string \t \r";
            EndBody.
        """
        expect = "This is a string \t "
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test67(self):
        input = """
            Function: main
            Body:
                Var: count = 0;
                Var: i;
                print("Liet ke tat ca cac so co 5 chu so:");
                For (i = 10001, i < 99999, i+2)
                    If (isPrimeNumber(i)) Then
                        printf("%d\\n", i);
                        count+1;
                    EndIf.
                EndFor.
                printf("Tong cac so nguyen to co 5 chu so la: %d", count);
            EndBody.
        """
        expect = "Error on line 8 col 20: If"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test68(self):
        input = """
            Function: main
            Body:
                Var: arr[0] = {      "he",        "she", "          hers", "his   "};
                Var: text = "ahishers\\'";
                k = sizeof(arr)\sizeof(arr[0]);
                searchWords(arr, k, text);
                Return 0;
                Continue;
                Break;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test69(self):
        input = """
            Function: searchWords
            Parameter: arr[100], k, text
            ** Preprocess patterns. **
            ** Build machine with goto, failure and output functions **
            Body:
            ** Initialize current state ******
            Var: currentState = 0;
            buildMatchingMachine(arr, k);
            For (i = 0, i < size(), 1+i) Do
                currentState = findNextState(currentState, text[i]);
                If (out[currentState] == 0) Then
                    Continue;
                EndIf.
                For (j = 0, j < k, 100+j) Do
                    If (out[currentState] && (1 < j)) Then
                    EndIf.
                EndFor.
            EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test70(self):
        input = """
            Function: main
            Body: 
                Var: txt[12] = "ABABDABACDABABCABAB\t \\n", pat[27] = "ABABCABAB \b \\\\"; 
                KMPSearch(pat, txt); 
                Return 0; 
            EndBody.
        """
        expect = "K"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test71(self):
        input = """
            Function: generate_derangement
            Body:
                Var: s[1]; 
                For (i = 1, i <= x, i+{1}) Do
                    x[i] = i; 
                    push(x[i]); 
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test72(self):
        input = """
            Function: phanTichSoNguyen
            Body:
                Var: i = 2;
                Var: dem = 0;
                Var: a[100];
                While (n > 1) Do
                    If (n % i == 0) Then
                        n = n \ i;
                        a[dem+1] = i;
                    Else
                        i=i+1;
                    EndIf.
                EndWhile.
                ** this is a comment **
                If (dem == 0) Then
                    a[dem+1] = n;
                EndIf.
                ****
                For (i = 0, i < dem - 1, 1) Do
                    printf("%d x ", a[i]);
                EndFor.
                printf("%d", a[dem - 1]);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test73(self):
        input = """
            Function: main
            Body:
                Var: a = 10;
                Do
                    println("Gia tri cua a: ");
                    a=a+1;
                While a < 20.
                Return 0;
            EndBody.
        """
        expect = "Error on line 9 col 16: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test74(self):
        input = """Var: x[0] = {abc};"""
        expect = "Error on line 1 col 13: abc"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test75(self):
        input = """
        Function: main
        Body:
            Var: a = 10;
            While( a < 20 ) Do   
                print("Gia tri cua a: ");
                a=a+{1};
                If( a > 15) Then
                    ** ket thuc vong lap khi a lon hon 15 **
                    Breakk;
                EndIf.
            EndWhile.
        Return 0;
        EndBody.
        """
        expect = "Error on line 10 col 25: k"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test76(self):
        input = """
        Function: main
        Body:
            Var: a = 10;
            Var: x= {        ** this is a comment **    "abc\\n",    **** 1,   2,3,{1,2}};
            Var: x = {{{1,  2 ,2e-124, "avc" , 1 }, {  4 , **erty**  5}  },  {{ 6  ,  7  },{ 8,9}}};
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test77(self):
        input = """
        Function: main
        Body:
            y = 5 +. 4 +. 1;
            y = 1.1 +. 3 -. 1.2 *. 8.0 \\. 9.23;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test78(self):
        input = """
            Function: main
            Body:
                Var: a = 10;
                Do
                    If a == 15 Then
                    a = a + 1;
                    Continue;
                    println( "Gia tri cua a: ");
                    a=a+1;
                While a < 20.
                Return 0;
            EndBody.
        """
        expect = "Error on line 12 col 16: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_79(self):
        input = """
            Var: x[7][6]={1,"abc",               1.};
            Function: test_index_op
                Body:
                    v=123[True];
                    y=123[0[0[False]]];
                    z=a[1[1][1][1][1][1][1][1]];
                EndBody.
                a=foo(1);
            """
        expect = "Error on line 9 col 16: a"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test80(self):
        input = """
            Function: phanTichSoNguyen
            Parameter: n
                Body:
                Var: i = 2;
                Var: dem = 0;
                Var: a[100];
                ** This is test comment 1 **
                While n <=. 1 Do
                    If (n % i == 0) Then
                        n = n \ i;
                        a[dem+1] = i;
                    Else 
                        i=i+.1.;
                    EndIf.
                EndWhile.
                 ** This is test comment 2 ***
                EndBody.
        """
        expect = "Error on line 17 col 45: *"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test81(self):
        input = """
            Function: main
            Body:
                Var: flag = 1;
                printf("Nhap chuoi s1: ");
                gets(s1);
                printf("Nhap chuoi s2: ");
                gets(s2);
                ** this is a comment **
                While s1[n] != "\\s" Do
                    If s1[n] != s2[n] Then
                        flag = 0;
                        Break;
                    EndIf.
                    n=n+1;
                EndWhile.
            EndBody.
        """
        expect = "\s"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test82(self):
        input = """
            Function: func_name
            Parameter: n
            Body:
                Var: a[20];
                Var: dem = 0, i;
                Do
                    a[dem+1] = (n % dEC_10);
                    n = n \ DEC_10;
                While n > 0
                EndDo.
                Return 1;
            EndBody.
        """
        expect = "D"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test83(self):
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
                        remainder = remainder \. Break;
                    EndWhile.
                EndBody.
                """
        expect = "Error on line 19 col 49: Break"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test84(self):
        input = """
            Function: tinhGiaiThua
            Parameter: n
                Body: 
                    Var: i;
                    Var: giai_thua = 1;
                    If ((n == 0) || (n == 1)) Then
                        Return giai_thua;
                    Else
                        For (i = 2, i <= n, i==100) Do
                            giai_thua = giai_thua*i
                        EndFor.
                    Return giai_thua;
                    EndIf.
                EndBody.
                """
        expect = "Error on line 12 col 24: EndFor"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_85(self):
        input = """
        Var: pascalTr[10][10]; 
        Var: hang,cot; 
        Function: pascal_program
            Body:
            For(hang=0,hang<size,hang+1) Do 
                For(cot=0,cot<size,cot+1) Do
                    pascalTr[hang][cot]=0; 
                    pascalTr[0][0]=1; 
                    pascalTr[1][0]=1; 
                    pascalTr[1][1]=1; 
                EndFor.
            EndFor
            EndBody.
            """
        expect = "Error on line 14 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_86(self):
        input = """
            Function: tEST_286
                Parameter: x,a[69],b[1][2][3+1]
                Body:
                    For (i=1, goo(2+a[6]) < i,2>goo(9)) Do
                    EndFor.
                EndBody.
            """
        expect = "Error on line 3 col 44: +"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_87(self):
        input = """
        Function: main
        Body:
            If (a> 0) && (b >0) Then
                a= int_of_string();
                b= float_of_int(a) +. 2.0;
            EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test88(self):
        input = """
            Function: foo 
                Body: 
                    b = 1.E-12  =/= Foo(123);
                EndBody.
                """
        expect = "F"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test89(self):
        input = """
            Function: fibonacci 
                Body: 
                    Var: f0=0,f1=1,fn=1;
                    Var: i;
                    If n<0 Then
                        Return -1;
                    ElseIf (n==0) || (n==1) Then
                        return n;
                    Else 
                    EndIf.
                    Return fn;
                EndBody.
                """
        expect = "Error on line 9 col 31: n"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test90(self):
        input = """
            Function: uSCLN
            Parameter: a,b,a[7+foo(2,7)]
            Body:
                If b == 0 Then Return a; EndIf.
                Return uSCLN(b, a % b);
            EndBody.
            **
            Tim boi so chung nho nhat (BSCNN)
            **
        """
        expect = "Error on line 3 col 30: +"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test91(self):
        input = """
            Var: ;
        """
        expect = "Error on line 2 col 17: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test92(self):
        input = """

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test93(self):
        input = """
            Function: main
            Body:
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test94(self):
        input = """
            Function: main
            Body:
            writeln("In bang cuu chuong rut gon: \'");
            EndBody.
        """
        expect = '''In bang cuu chuong rut gon: '");'''
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test95(self):
        input = """
            Function: main
            Body:
                Var: x= ''' "abc \' def \'\'" '''
            EndBody.
        """
        expect = """'"""
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test96(self):
        input = """
            Function: giaiPTBac2_part_1
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
        expect = "Error on line 3 col 16: If"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test97(self):
        input = """
            Function: main
            Body:
                Var: arr[10] = {1, 2, 3,            4, 5, 6, 7, 8,              9,                    10};
                Var: i, total = 0;
                Var: size = "x \t";
                For(i = 0, i < size, i+1) Do
                    total = total + arr[i];
                EndFor.
                printf(5+x);
                Return 0;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test98(self):
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
                        remainder = remainder / b;
                    EndWhile.
                EndBody.
                """
        expect = "/"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_99(self):
        input = """
            Function: name__func0_99
                Body:
                    For(i=0,i<=. size(), i>9) Do
                        Var: y=1.;
                        If (s[i] >= a) && (s[i] <= z) Then
                            Var: y;
                            s[i]=s[i]-32;
                            Continue;
                        EndIf.
                    EndFor.
                EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test100(self):
        input = """
            Function: main
            Body: 
                Var: txt[12] = "ABABDABACDABABCABAB\t \\n", pat[27] = "ABABCABAB \b \\\\"; 
                kMPSearch(pat, txt); 
                Return 0; 
                x=(1+foo(2))[1];
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test101(self):
        input = """
        Function: main
            Body:
                a = !--.1;
                a = 3----------------1;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 301))

    def test102(self):
        input = """
        Function: main
            Body:
                ** this is a comment *a   **
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 302))

