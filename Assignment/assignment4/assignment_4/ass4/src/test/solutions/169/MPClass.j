.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is b F from Label0 to Label1
.var 3 is c F from Label0 to Label1
Label0:
	ldc 5.0
	fstore_1
	ldc 2.0
	fstore_2
	fload_1
	fload_2
	iconst_2
	i2f
	fdiv
	fadd
	iconst_1
	i2f
	fadd
	fstore_2
	fload_2
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
	fload_2
	invokestatic io/putFloatLn(F)V
	fload_1
	fload_2
	fadd
	iconst_4
	i2f
	fdiv
	fload_1
	fload_2
	fsub
	iconst_4
	i2f
	fdiv
	iconst_2
	i2f
	fmul
	fadd
	iconst_1
	i2f
	fadd
	fstore_2
	fload_2
	fstore_1
	fload_1
	fstore_3
	fload_1
	invokestatic io/putFloatLn(F)V
	fload_2
	invokestatic io/putFloatLn(F)V
	fload_3
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 3
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
