.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is l I from Label0 to Label1
.var 3 is r I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iconst_1
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	istore_1
	iload_1
	invokestatic io/putInt(I)V
	iconst_0
	istore_1
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iconst_1
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	istore_1
	iload_1
	invokestatic io/putInt(I)V
	iconst_1
	istore_1
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iconst_1
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iconst_2
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iaload
	iadd
	istore_1
	iload_1
	invokestatic io/putInt(I)V
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
	getstatic MPClass/a [I
	iconst_0
	iconst_0
	isub
	iaload
	iastore
	getstatic MPClass/a [I
	iconst_1
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
	iconst_1
	istore_1
	getstatic MPClass/a [I
	iconst_0
	iconst_0
	isub
	iconst_1
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iaload
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iaload
	iconst_1
	iadd
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iaload
	iconst_2
	imul
	iconst_1
	iadd
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iaload
	iconst_2
	imul
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	iadd
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iaload
	iconst_2
	imul
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	iconst_3
	imul
	iadd
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iaload
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	imul
	iadd
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iaload
	iastore
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
	iconst_0
	istore_2
	bipush 10
	istore_3
	getstatic MPClass/a [I
	iload_2
	iconst_0
	isub
	iconst_1
	iastore
	getstatic MPClass/a [I
	iload_2
	iconst_1
	iadd
	iconst_0
	isub
	iconst_1
	iastore
	iload_2
	iconst_2
	iadd
	istore_1
Label2:
	iload_1
	iload_3
	if_icmpgt Label3
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iaload
	getstatic MPClass/a [I
	iload_1
	iconst_2
	isub
	iconst_0
	isub
	iaload
	iadd
	iastore
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	getstatic MPClass/a [I
	iload_3
	iconst_0
	isub
	iaload
	invokestatic io/putInt(I)V
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
	bipush 11
	newarray int
	putstatic MPClass/a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
