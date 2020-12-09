.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	invokestatic MPClass/foo(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo(I)V
.var 0 is x I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iload_0
	istore_1
Label6:
	iload_1
	iconst_1
	if_icmplt Label7
	iload_1
	invokestatic io/putIntLn(I)V
	iload_1
	iconst_3
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	goto Label13
Label12:
	return
Label13:
Label8:
	iload_1
	iconst_1
	isub
	istore_1
	goto Label6
Label7:
Label9:
	goto Label5
Label4:
	return
Label5:
	iload_0
	iconst_1
	isub
	invokestatic MPClass/foo(I)V
Label1:
	return
.limit stack 6
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
