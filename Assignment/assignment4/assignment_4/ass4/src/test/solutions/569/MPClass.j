.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y F from Label0 to Label1
.var 3 is z Z from Label0 to Label1
Label0:
	bipush 29
	istore_1
	iload_1
	bipush 10
	irem
	invokestatic io/putIntLn(I)V
	bipush 12
	iconst_5
	iadd
	bipush 12
	irem
	invokestatic io/putIntLn(I)V
	bipush 12
	iconst_5
	bipush 12
	irem
	iadd
	invokestatic io/putIntLn(I)V
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
