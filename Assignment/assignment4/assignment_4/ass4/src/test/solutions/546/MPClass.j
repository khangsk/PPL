.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static gArr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [I from Label0 to Label1
.var 2 is c I from Label0 to Label1
.var 3 is d I from Label0 to Label1
Label0:
	iconst_4
	newarray int
	astore_1
	iconst_1
	putstatic MPClass/a I
	iconst_1
	putstatic MPClass/a I
	getstatic MPClass/a I
	putstatic MPClass/b I
	getstatic MPClass/a I
	istore_2
	getstatic MPClass/b I
	istore_2
	iload_2
	putstatic MPClass/a I
	getstatic MPClass/a I
	putstatic MPClass/b I
	aload_1
	iconst_1
	iconst_1
	isub
	iconst_1
	iastore
	getstatic MPClass/gArr [I
	iconst_1
	iconst_1
	isub
	aload_1
	iconst_1
	iconst_1
	isub
	iaload
	iastore
	getstatic MPClass/gArr [I
	iconst_1
	iconst_1
	isub
	bipush 11
	iastore
	getstatic MPClass/gArr [I
	iconst_2
	iconst_1
	isub
	getstatic MPClass/gArr [I
	iconst_1
	iconst_1
	isub
	iaload
	iastore
	bipush 11
	putstatic MPClass/b I
	getstatic MPClass/gArr [I
	iconst_3
	iconst_1
	isub
	getstatic MPClass/b I
	iastore
	getstatic MPClass/gArr [I
	iconst_3
	iconst_1
	isub
	iaload
	putstatic MPClass/a I
	getstatic MPClass/gArr [I
	iconst_1
	iconst_1
	isub
	getstatic MPClass/a I
	iastore
	aload_1
	iconst_4
	iconst_1
	isub
	getstatic MPClass/gArr [I
	iconst_1
	iconst_1
	isub
	iaload
	iastore
	getstatic MPClass/gArr [I
	iconst_2
	iconst_1
	isub
	aload_1
	iconst_4
	iconst_1
	isub
	iaload
	iastore
	getstatic MPClass/gArr [I
	iconst_2
	iconst_1
	isub
	iaload
	istore_3
	getstatic MPClass/gArr [I
	iconst_2
	iconst_1
	isub
	iaload
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 6
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
	iconst_4
	newarray int
	putstatic MPClass/gArr [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
