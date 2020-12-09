.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
Label0:
	bipush 100
	i2f
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
	invokestatic MPClass/foo()I
	i2f
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
	invokestatic MPClass/bar()V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static foo()I
Label0:
	bipush 10
	putstatic MPClass/a I
	getstatic MPClass/a I
	iconst_5
	imul
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static bar()V
Label0:
	getstatic MPClass/a I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
.limit locals 0
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
