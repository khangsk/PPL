.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
Label0:
	iconst_2
	i2f
	iconst_0
	invokestatic MPClass/foo(FZ)F
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static foo(FZ)F
.var 0 is a F from Label0 to Label1
.var 1 is b Z from Label0 to Label1
Label0:
	fload_0
	fload_0
	fmul
	fload_0
	fmul
	fload_0
	iconst_2
	i2f
	fdiv
	fadd
	freturn
Label1:
.limit stack 3
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
