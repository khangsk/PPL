.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x [I from Label0 to Label1
Label0:
	bipush 7
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_m1
	isub
	iconst_1
	iastore
	aload_1
	iconst_1
	iconst_m1
	isub
	iconst_2
	iastore
	aload_1
	iconst_3
	iconst_m1
	isub
	iconst_2
	aload_1
	iconst_0
	iconst_m1
	isub
	iaload
	imul
	bipush 10
	aload_1
	iconst_1
	iconst_m1
	isub
	iaload
	imul
	iadd
	iconst_4
	aload_1
	iconst_0
	iconst_m1
	isub
	iaload
	imul
	aload_1
	iconst_1
	iconst_m1
	isub
	iaload
	imul
	isub
	iastore
	aload_1
	iconst_3
	iconst_m1
	isub
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 7
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
