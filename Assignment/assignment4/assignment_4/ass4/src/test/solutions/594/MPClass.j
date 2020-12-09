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
	iconst_0
	istore_1
Label2:
	iload_1
	bipush 9
	if_icmpgt Label3
	iconst_0
	istore_2
Label6:
	iload_2
	iload_1
	iconst_1
	isub
	if_icmpgt Label7
	iload_1
	iload_2
	iadd
	bipush 17
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	goto Label13
Label12:
	goto Label9
Label13:
	iload_2
	iconst_2
	irem
	iconst_0
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	goto Label17
Label16:
	goto Label8
Label17:
	iload_3
	iload_2
	iadd
	istore_3
Label8:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label7:
Label9:
	iload_3
	bipush 27
	if_icmple Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label20
	goto Label21
Label20:
	goto Label5
Label21:
	iload_1
	iconst_3
	irem
	iconst_0
	if_icmpeq Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifgt Label24
	goto Label25
Label24:
	goto Label4
Label25:
	iload_3
	iload_1
	iadd
	istore_3
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	iload_3
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 10
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
