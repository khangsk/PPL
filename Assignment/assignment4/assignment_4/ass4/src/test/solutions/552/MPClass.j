.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static arr [I
.field static fa F
.field static fb F
.field static fc F
.field static frr [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is fNum F from Label0 to Label1
Label0:
	getstatic MPClass/arr [I
	iconst_3
	iconst_1
	isub
	iconst_3
	iastore
	getstatic MPClass/arr [I
	iconst_2
	iconst_1
	isub
	getstatic MPClass/arr [I
	iconst_3
	iconst_1
	isub
	iaload
	iastore
	getstatic MPClass/arr [I
	iconst_1
	iconst_1
	isub
	getstatic MPClass/arr [I
	iconst_2
	iconst_1
	isub
	iaload
	iastore
	iconst_3
	iconst_5
	imul
	putstatic MPClass/a I
	getstatic MPClass/a I
	iconst_2
	iadd
	putstatic MPClass/b I
	getstatic MPClass/b I
	getstatic MPClass/a I
	iconst_3
	imul
	iadd
	putstatic MPClass/c I
	getstatic MPClass/a I
	getstatic MPClass/b I
	iadd
	getstatic MPClass/arr [I
	iconst_1
	iconst_1
	isub
	iaload
	iconst_4
	imul
	iadd
	i2f
	fstore_1
	fload_1
	getstatic MPClass/c I
	getstatic MPClass/arr [I
	iconst_1
	iconst_1
	isub
	iaload
	imul
	i2f
	fadd
	putstatic MPClass/fa F
	getstatic MPClass/fa F
	getstatic MPClass/a I
	getstatic MPClass/arr [I
	iconst_2
	iconst_1
	isub
	iaload
	imul
	i2f
	fadd
	putstatic MPClass/fb F
	getstatic MPClass/fb F
	getstatic MPClass/b I
	getstatic MPClass/arr [I
	iconst_3
	iconst_1
	isub
	iaload
	imul
	i2f
	fadd
	fload_1
	getstatic MPClass/a I
	i2f
	fmul
	fadd
	putstatic MPClass/fc F
	getstatic MPClass/frr [F
	iconst_1
	iconst_1
	isub
	getstatic MPClass/fa F
	getstatic MPClass/a I
	i2f
	fmul
	getstatic MPClass/fb F
	getstatic MPClass/b I
	i2f
	fmul
	fadd
	getstatic MPClass/fc F
	getstatic MPClass/c I
	i2f
	fmul
	fadd
	fastore
	getstatic MPClass/frr [F
	iconst_2
	iconst_1
	isub
	getstatic MPClass/frr [F
	iconst_1
	iconst_1
	isub
	faload
	getstatic MPClass/a I
	getstatic MPClass/b I
	imul
	getstatic MPClass/c I
	imul
	i2f
	fadd
	fastore
	getstatic MPClass/frr [F
	iconst_2
	iconst_1
	isub
	faload
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 6
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_3
	newarray int
	putstatic MPClass/arr [I
	iconst_4
	newarray float
	putstatic MPClass/frr [F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
