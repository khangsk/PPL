.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
.var 3 is x I from Label0 to Label1
.var 4 is y I from Label0 to Label1
Label0:
	ldc 1.05
	ldc 25.4
	fmul
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
	ldc 2.05
	fload_1
	fadd
	fstore_2
	fload_2
	invokestatic io/putFloatLn(F)V
	fload_1
	bipush 100
	i2f
	fadd
	fload_2
	fsub
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
	sipush 1000
	istore_3
	iconst_1
	istore 4
	iload_3
	iload 4
	sipush 1000
	imul
	iconst_5
	idiv
	iadd
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
	iload 4
	invokestatic io/putIntLn(I)V
	iload_3
	iload 4
	imul
	iload_3
	iconst_2
	imul
	iadd
	iconst_2
	iload_3
	imul
	iadd
	iload 4
	iconst_2
	imul
	isub
	iconst_2
	iload 4
	imul
	iadd
	istore 4
	iload 4
	invokestatic io/putIntLn(I)V
	iload_3
	iload 4
	imul
	iconst_2
	imul
	iconst_5
	imul
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
	fload_1
	fload_2
	fmul
	iload_3
	i2f
	fadd
	iload 4
	i2f
	fdiv
	iload 4
	i2f
	fload_1
	fload_2
	fmul
	iconst_2
	iload_3
	irem
	i2f
	fadd
	fdiv
	fadd
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 5
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
