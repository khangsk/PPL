.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
Label0:
	bipush 100
	i2f
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
	invokestatic MPClass/foo()F
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
	invokestatic MPClass/bar()V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static foo()F
Label0:
	bipush 10
	i2f
	putstatic MPClass/a F
	getstatic MPClass/a F
	iconst_5
	i2f
	fmul
	freturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static bar()V
Label0:
	getstatic MPClass/a F
	invokestatic io/putFloatLn(F)V
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
