.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is a I from Label0 to Label1
.var 4 is b I from Label0 to Label1
Label0:
	iconst_1
	istore_3
	bipush 10
	istore 4
	iload_3
	iload 4
	isub
	istore_1
Label2:
	iload_1
	iload_3
	iload 4
	iadd
	if_icmpgt Label3
	iload_1
	invokestatic io/putInt(I)V
	iload_1
	iconst_1
	iadd
	istore_1
	iload_3
	iconst_1
	isub
	istore_3
	iload 4
	iconst_1
	iadd
	istore 4
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 3
.limit locals 5
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
