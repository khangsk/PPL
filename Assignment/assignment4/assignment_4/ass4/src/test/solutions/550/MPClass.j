.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is iNum I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
Label0:
	getstatic MPClass/arr [I
	iconst_1
	iconst_1
	isub
	iconst_0
	iastore
	getstatic MPClass/arr [I
	iconst_2
	iconst_1
	isub
	iconst_1
	iastore
	getstatic MPClass/arr [I
	iconst_3
	iconst_1
	isub
	iconst_2
	iastore
	iconst_3
	putstatic MPClass/a I
	getstatic MPClass/a I
	iconst_2
	iadd
	putstatic MPClass/b I
	getstatic MPClass/b I
	getstatic MPClass/a I
	iadd
	iconst_3
	iadd
	putstatic MPClass/c I
	getstatic MPClass/arr [I
	iconst_1
	iconst_1
	isub
	iaload
	getstatic MPClass/c I
	iadd
	getstatic MPClass/arr [I
	iconst_2
	iconst_1
	isub
	iaload
	getstatic MPClass/b I
	isub
	iadd
	getstatic MPClass/arr [I
	iconst_3
	iconst_1
	isub
	iaload
	getstatic MPClass/arr [I
	iconst_1
	iconst_1
	isub
	iaload
	isub
	isub
	istore_1
	iload_1
	getstatic MPClass/arr [I
	iconst_1
	iconst_1
	isub
	iaload
	isub
	getstatic MPClass/arr [I
	iconst_2
	iconst_1
	isub
	iaload
	iadd
	getstatic MPClass/arr [I
	iconst_3
	iconst_1
	isub
	iaload
	isub
	getstatic MPClass/c I
	isub
	istore_2
	iload_1
	iload_2
	isub
	bipush 11
	iadd
	istore_3
	iload_3
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
	iconst_3
	newarray int
	putstatic MPClass/arr [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
