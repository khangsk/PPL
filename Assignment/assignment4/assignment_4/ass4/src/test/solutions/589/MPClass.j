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
	iload_2
	bipush 10
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	goto Label17
Label16:
	goto Label13
Label17:
	iload_2
	iconst_2
	irem
	iconst_1
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label20
	goto Label21
Label20:
	goto Label12
Label21:
	iload_3
	iload_2
	iadd
	istore_3
Label12:
	goto Label10
Label11:
Label13:
	iload_1
	iload_2
	irem
	iconst_0
	if_icmpne Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifgt Label24
	goto Label25
Label24:
	goto Label6
Label25:
	iload_1
	iload_2
	iadd
	bipush 40
	if_icmple Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifgt Label28
	goto Label29
Label28:
	goto Label7
Label29:
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
.limit stack 14
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
