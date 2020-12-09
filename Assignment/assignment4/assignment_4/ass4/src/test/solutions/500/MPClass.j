.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MPClass/x I
	getstatic MPClass/x I
	ldc 1.0
	invokestatic MPClass/foo(IF)V
	getstatic MPClass/x I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo(IF)V
.var 0 is i I from Label0 to Label1
.var 1 is f F from Label0 to Label1
.var 2 is bar Z from Label0 to Label1
Label0:
	iconst_1
	istore_2
	iload_2
	invokestatic io/putBool(Z)V
	iconst_2
	istore_0
	iload_0
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 3
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
