.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static fa F
.field static fb F
.field static fc F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is isTrue Z from Label0 to Label1
.var 2 is isT Z from Label0 to Label1
.var 3 is isF Z from Label0 to Label1
Label0:
	bipush 10
	putstatic MPClass/a I
	getstatic MPClass/a I
	iconst_2
	imul
	putstatic MPClass/b I
	getstatic MPClass/b I
	bipush 7
	idiv
	putstatic MPClass/c I
	getstatic MPClass/a I
	getstatic MPClass/b I
	imul
	getstatic MPClass/c I
	getstatic MPClass/a I
	idiv
	isub
	i2f
	putstatic MPClass/fa F
	getstatic MPClass/a I
	i2f
	getstatic MPClass/fa F
	getstatic MPClass/a I
	i2f
	fadd
	fmul
	getstatic MPClass/c I
	getstatic MPClass/b I
	isub
	i2f
	fmul
	putstatic MPClass/fb F
	getstatic MPClass/fa F
	getstatic MPClass/fb F
	fmul
	getstatic MPClass/c I
	i2f
	fdiv
	putstatic MPClass/fc F
	getstatic MPClass/fa F
	getstatic MPClass/fc F
	fcmpl
	ifge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_2
	getstatic MPClass/fb F
	getstatic MPClass/fa F
	fcmpl
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_3
	iload_2
	iload_3
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	istore_1
	iload_1
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 7
.limit locals 4
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
