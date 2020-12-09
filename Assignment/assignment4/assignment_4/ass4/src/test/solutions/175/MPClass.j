.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/fi()I
	invokestatic io/putIntLn(I)V
	invokestatic MPClass/ff()F
	invokestatic io/putFloatLn(F)V
	invokestatic MPClass/fb()Z
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static fi()I
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static ff()F
Label0:
	ldc 5.0
	freturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static fb()Z
Label0:
	iconst_0
	ireturn
Label1:
.limit stack 2
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
