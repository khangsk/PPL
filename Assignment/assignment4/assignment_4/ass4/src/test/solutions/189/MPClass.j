.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_1
Label2:
	iload_1
	iconst_5
	if_icmpgt Label3
	iload_1
	invokestatic io/putInt(I)V
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	iload_1
	invokestatic io/putIntLn(I)V
	iconst_1
	istore_1
Label6:
	iload_1
	iconst_1
	if_icmpgt Label7
	iload_1
	invokestatic io/putInt(I)V
Label8:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label6
Label7:
Label9:
	iload_1
	invokestatic io/putIntLn(I)V
	iconst_5
	istore_1
Label10:
	iload_1
	iconst_1
	if_icmpgt Label11
	iload_1
	invokestatic io/putInt(I)V
Label12:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label10
Label11:
Label13:
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
.limit locals 2
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
