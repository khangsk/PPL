.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is iSum I from Label0 to Label1
Label0:
	iconst_0
	istore_3
	iload_3
	istore_2
	iload_2
	istore_1
Label4:
	iload_1
	bipush 20
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iconst_0
	istore_2
	iload_1
	iconst_1
	iadd
	istore_1
Label10:
	iload_2
	iload_1
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label11
	iload_2
	iconst_1
	iadd
	istore_2
	iload_3
	iload_2
	iadd
	istore_3
Label12:
	goto Label10
Label11:
Label13:
	iload_3
	iload_1
	iadd
	istore_3
Label6:
	goto Label4
Label5:
Label7:
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 6
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
