.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static z I
.field static b [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is e I from Label0 to Label1
.var 2 is x F from Label0 to Label1
Label0:
	invokestatic MPClass/foo()V
	getstatic MPClass/b [F
	iconst_0
	iconst_0
	isub
	faload
	invokestatic io/putFloatLn(F)V
	getstatic MPClass/b [F
	iconst_1
	iconst_0
	isub
	faload
	invokestatic io/putFloatLn(F)V
	getstatic MPClass/z I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public static foo()V
Label0:
	getstatic MPClass/b [F
	iconst_0
	iconst_0
	isub
	sipush 1000
	i2f
	fastore
	bipush 10
	putstatic MPClass/z I
Label1:
	return
.limit stack 6
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
	iconst_3
	newarray float
	putstatic MPClass/b [F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
