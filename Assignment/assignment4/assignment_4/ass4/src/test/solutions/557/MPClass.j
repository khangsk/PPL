.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ifgt Label3
	iconst_1
	ifgt Label3
	iconst_0
	goto Label2
Label3:
	iconst_1
Label2:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ifgt Label5
	iconst_0
	ifgt Label5
	iconst_0
	goto Label4
Label5:
	iconst_1
Label4:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	ifgt Label7
	iconst_1
	ifgt Label7
	iconst_0
	goto Label6
Label7:
	iconst_1
Label6:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	ifgt Label9
	iconst_0
	ifgt Label9
	iconst_0
	goto Label8
Label9:
	iconst_1
Label8:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ifle Label10
	iconst_1
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ifle Label12
	iconst_0
	ifle Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	ifle Label14
	iconst_1
	ifle Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	ifle Label16
	iconst_0
	ifle Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 41
.limit locals 1
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
