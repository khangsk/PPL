.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.5
	iconst_2
	i2f
	fmul
	iconst_2
	i2f
	fadd
	ldc 5.3
	ldc 2.1
	fmul
	fsub
	iconst_3
	iconst_5
	imul
	i2f
	iconst_2
	iconst_3
	imul
	i2f
	iconst_2
	i2f
	fdiv
	fadd
	iconst_4
	i2f
	ldc 7.2
	fmul
	bipush 14
	i2f
	fdiv
	fsub
	iconst_1
	i2f
	fadd
	fsub
	fneg
	invokestatic io/putFloatLn(F)V
	ldc 1.5
	iconst_2
	i2f
	fmul
	iconst_2
	i2f
	fadd
	ldc 5.3
	ldc 2.1
	fmul
	fsub
	fneg
	iconst_3
	iconst_5
	imul
	i2f
	iconst_2
	iconst_3
	imul
	i2f
	iconst_2
	i2f
	fdiv
	fadd
	iconst_4
	i2f
	ldc 7.2
	fmul
	bipush 14
	i2f
	fdiv
	fsub
	iconst_1
	i2f
	fadd
	fsub
	invokestatic io/putFloatLn(F)V
	ldc 1.5
	iconst_2
	i2f
	fmul
	iconst_2
	i2f
	fadd
	ldc 5.3
	ldc 2.1
	fmul
	fsub
	fneg
	fneg
	iconst_3
	iconst_5
	imul
	i2f
	iconst_2
	iconst_3
	imul
	i2f
	iconst_2
	i2f
	fdiv
	fadd
	iconst_4
	i2f
	ldc 7.2
	fmul
	bipush 14
	i2f
	fdiv
	fsub
	iconst_1
	i2f
	fadd
	fneg
	fneg
	fsub
	invokestatic io/putFloatLn(F)V
	ldc 1.5
	iconst_2
	i2f
	fmul
	iconst_2
	i2f
	fadd
	ldc 5.3
	ldc 2.1
	fmul
	fsub
	fneg
	fneg
	fneg
	fneg
	iconst_3
	iconst_5
	imul
	i2f
	iconst_2
	iconst_3
	imul
	i2f
	iconst_2
	i2f
	fdiv
	fadd
	iconst_4
	i2f
	ldc 7.2
	fmul
	bipush 14
	i2f
	fdiv
	fsub
	iconst_1
	i2f
	fadd
	fneg
	fneg
	fneg
	fsub
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 4
.limit locals 1
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
