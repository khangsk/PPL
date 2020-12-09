.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	getstatic MPClass/a [I
	iconst_0
	iconst_0
	isub
	iconst_1
	iastore
	getstatic MPClass/a [I
	iconst_1
	iconst_0
	isub
	iconst_2
	iastore
	getstatic MPClass/a [I
	iconst_0
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
	getstatic MPClass/a [I
	iconst_1
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
	iconst_5
	istore_1
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iconst_5
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
	bipush 6
	istore_1
	getstatic MPClass/a [I
	iload_1
	iconst_1
	iadd
	iconst_0
	isub
	bipush 6
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_1
	iadd
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
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
	bipush 11
	newarray int
	putstatic MPClass/a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
