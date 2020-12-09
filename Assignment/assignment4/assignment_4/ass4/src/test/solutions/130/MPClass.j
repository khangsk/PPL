.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 123.1
	iconst_5
	i2f
	fdiv
	bipush 123
	i2f
	ldc 5.1
	fdiv
	fadd
	bipush 123
	i2f
	ldc 5.1
	fmul
	ldc 123.1
	iconst_5
	i2f
	fmul
	fadd
	fsub
	bipush 123
	i2f
	bipush 123
	i2f
	bipush 123
	i2f
	fdiv
	bipush 123
	i2f
	fmul
	iconst_1
	i2f
	fadd
	fdiv
	fsub
	ldc 123.123
	ldc 321.213
	fmul
	fsub
	iconst_1
	i2f
	fsub
	invokestatic io/putFloat(F)V
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
