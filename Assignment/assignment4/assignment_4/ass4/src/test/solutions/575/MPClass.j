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
.var 1 is arr [I from Label0 to Label1
.var 2 is isTrue Z from Label0 to Label1
.var 3 is isT Z from Label0 to Label1
.var 4 is isF Z from Label0 to Label1
Label0:
	iconst_3
	newarray int
	astore_1
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
	aload_1
	iconst_1
	iconst_1
	isub
	getstatic MPClass/c I
	getstatic MPClass/b I
	iconst_2
	idiv
	iadd
	iastore
	aload_1
	iconst_2
	iconst_1
	isub
	getstatic MPClass/a I
	iconst_2
	idiv
	getstatic MPClass/c I
	iconst_3
	idiv
	iadd
	iastore
	aload_1
	iconst_3
	iconst_1
	isub
	getstatic MPClass/b I
	getstatic MPClass/a I
	imul
	iconst_4
	idiv
	getstatic MPClass/c I
	iconst_4
	idiv
	iadd
	iastore
	aload_1
	iconst_1
	iconst_1
	isub
	iaload
	getstatic MPClass/b I
	imul
	getstatic MPClass/a I
	idiv
	getstatic MPClass/c I
	aload_1
	iconst_3
	iconst_1
	isub
	iaload
	imul
	aload_1
	iconst_2
	iconst_1
	isub
	iaload
	isub
	isub
	i2f
	putstatic MPClass/fa F
	getstatic MPClass/a I
	i2f
	getstatic MPClass/fa F
	aload_1
	iconst_3
	iconst_1
	isub
	iaload
	i2f
	fadd
	fmul
	getstatic MPClass/c I
	aload_1
	iconst_2
	iconst_1
	isub
	iaload
	isub
	i2f
	fmul
	putstatic MPClass/fb F
	getstatic MPClass/fa F
	getstatic MPClass/fb F
	fmul
	aload_1
	iconst_2
	iconst_1
	isub
	iaload
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
	istore_3
	getstatic MPClass/fb F
	getstatic MPClass/fa F
	fcmpl
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore 4
	iload_3
	iload 4
	getstatic MPClass/a I
	iconst_3
	iadd
	bipush 17
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	ior
	getstatic MPClass/a I
	bipush 7
	iadd
	bipush 19
	if_icmpeq Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	aload_1
	iconst_3
	iconst_1
	isub
	iaload
	getstatic MPClass/c I
	iadd
	bipush 11
	if_icmpeq Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	iand
	ior
	istore_2
	aload_1
	iconst_2
	iconst_1
	isub
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 13
.limit locals 5
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
