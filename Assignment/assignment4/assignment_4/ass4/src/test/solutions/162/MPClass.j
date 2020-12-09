.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ifle Label2
	iconst_0
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	ifle Label4
	iconst_1
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ifle Label6
	iconst_0
	ifle Label8
	iconst_1
	ifle Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ifle Label10
	iconst_0
	ifle Label12
	iconst_1
	ifle Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label14
	iconst_0
	ifle Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ifgt Label17
	iconst_0
	ifgt Label17
	iconst_0
	goto Label16
Label17:
	iconst_1
Label16:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	ifgt Label19
	iconst_1
	ifgt Label19
	iconst_0
	goto Label18
Label19:
	iconst_1
Label18:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ifgt Label21
	iconst_0
	ifgt Label23
	iconst_1
	ifgt Label23
	iconst_0
	goto Label22
Label23:
	iconst_1
Label22:
	ifgt Label21
	iconst_0
	goto Label20
Label21:
	iconst_1
Label20:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	ifgt Label25
	iconst_0
	ifgt Label27
	iconst_1
	ifgt Label27
	iconst_0
	goto Label26
Label27:
	iconst_1
Label26:
	ifgt Label25
	iconst_0
	goto Label24
Label25:
	iconst_1
Label24:
	ifgt Label29
	iconst_0
	ifgt Label29
	iconst_0
	goto Label28
Label29:
	iconst_1
Label28:
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 65
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
