.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 123
	i2f
	iconst_3
	i2f
	fdiv
	bipush 46
	i2f
	iconst_5
	i2f
	fdiv
	iconst_1
	i2f
	fdiv
	iconst_1
	i2f
	fdiv
	iconst_1
	i2f
	fdiv
	iconst_2
	i2f
	fdiv
	iconst_4
	i2f
	fdiv
	fadd
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 3
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