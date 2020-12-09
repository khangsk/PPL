.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_5
	istore_2
	invokestatic io/putLn()V
.var 3 is a F from Label2 to Label3
.var 4 is b F from Label2 to Label3
.var 5 is c F from Label2 to Label3
Label2:
	iconst_2
	i2f
	fstore_3
	bipush 10
	i2f
	fstore 4
	fload_3
	invokestatic io/putFloat(F)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
	fload 4
	invokestatic io/putFloatLn(F)V
Label3:
	iload_1
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 6
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
