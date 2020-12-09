.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static fNum F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [I from Label0 to Label1
.var 2 is a I from Label0 to Label1
.var 3 is b I from Label0 to Label1
Label0:
	iconst_4
	newarray int
	astore_1
	bipush 10
	istore_3
	iload_3
	istore_2
	aload_1
	iconst_1
	iconst_1
	isub
	iload_2
	iastore
	iload_2
	istore_3
	aload_1
	iconst_1
	iconst_1
	isub
	iload_3
	iastore
	aload_1
	iconst_2
	iconst_1
	isub
	aload_1
	iconst_1
	iconst_1
	isub
	iaload
	iastore
	aload_1
	iconst_1
	iconst_1
	isub
	bipush 18
	iastore
	aload_1
	iconst_1
	iconst_1
	isub
	iaload
	istore_2
	aload_1
	iconst_3
	iconst_1
	isub
	iload_2
	iastore
	aload_1
	iconst_3
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
