.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y F from Label0 to Label1
.var 3 is z Z from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_1
	i2f
	fstore_2
	iconst_0
	iconst_1
	ior
	istore_3
	bipush 12
	i2f
	ldc 3.2
	fcmpl
	ifeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBoolLn(Z)V
	bipush 12
	i2f
	ldc 12.0
	fcmpl
	ifeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
	bipush 12
	bipush 12
	if_icmpeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBoolLn(Z)V
	bipush 12
	i2f
	ldc 12.0
	fcmpl
	iflt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/putBoolLn(Z)V
	bipush 12
	bipush 12
	if_icmplt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/putBoolLn(Z)V
	iload_1
	iconst_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/putBoolLn(Z)V
	fload_2
	iconst_1
	i2f
	fcmpl
	ifne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	invokestatic io/putBoolLn(Z)V
	fload_2
	ldc 0.0
	fcmpl
	ifne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	invokestatic io/putBoolLn(Z)V
	iload_3
	ifgt Label19
	iconst_1
	goto Label18
Label19:
	iconst_0
Label18:
	iconst_1
	ifgt Label21
	iconst_1
	goto Label20
Label21:
	iconst_0
Label20:
	iand
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 27
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
