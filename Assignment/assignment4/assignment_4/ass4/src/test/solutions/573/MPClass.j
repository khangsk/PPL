.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y F from Label0 to Label1
.var 3 is z Z from Label0 to Label1
Label0:
	bipush 12
	istore_1
	iload_1
	iload_1
	imul
	i2f
	iload_1
	i2f
	fdiv
	iload_1
	i2f
	fdiv
	fstore_2
	fload_2
	invokestatic io/putFloatLn(F)V
	iload_1
	i2f
	invokestatic io/putFloatLn(F)V
	iload_1
	bipush 7
	ineg
	imul
	bipush 19
	irem
	iconst_2
	idiv
	iconst_4
	irem
	istore_1
	bipush 87
	iload_1
	imul
	bipush 12
	irem
	i2f
	bipush 45
	i2f
	fdiv
	bipush 78
	i2f
	fmul
	bipush 34
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	i2f
	fadd
	fstore_2
	fload_2
	invokestatic io/putFloatLn(F)V
	iload_1
	i2f
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 2
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
