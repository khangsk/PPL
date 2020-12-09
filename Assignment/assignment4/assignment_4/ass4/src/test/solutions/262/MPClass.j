.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/rettrue()Z
	ifle Label2
	invokestatic MPClass/rettrue()Z
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	invokestatic MPClass/retfalse()Z
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	invokestatic MPClass/rettrue()Z
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBoolLn(Z)V
	invokestatic MPClass/retfalse()Z
	ifgt Label9
	invokestatic MPClass/retfalse()Z
	ifgt Label9
	iconst_0
	goto Label8
Label9:
	iconst_1
Label8:
	ifgt Label11
	invokestatic MPClass/rettrue()Z
	ifgt Label11
	iconst_0
	goto Label10
Label11:
	iconst_1
Label10:
	ifgt Label13
	invokestatic MPClass/retfalse()Z
	ifgt Label13
	iconst_0
	goto Label12
Label13:
	iconst_1
Label12:
	invokestatic io/putBoolLn(Z)V
	invokestatic MPClass/retfalse()Z
	ifgt Label15
	invokestatic MPClass/retfalse()Z
	ifgt Label15
	iconst_0
	goto Label14
Label15:
	iconst_1
Label14:
	ifgt Label17
	invokestatic MPClass/rettrue()Z
	ifgt Label17
	iconst_0
	goto Label16
Label17:
	iconst_1
Label16:
	ifle Label18
	invokestatic MPClass/rettrue()Z
	ifle Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label20
	invokestatic MPClass/retfalse()Z
	ifle Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label22
	invokestatic MPClass/rettrue()Z
	ifle Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 34
.limit locals 1
.end method

.method public static rettrue()Z
Label0:
	ldc "retTrue; "
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_1
	ireturn
Label1:
.limit stack 2
.limit locals 0
.end method

.method public static retfalse()Z
Label0:
	ldc "retFalse; "
	invokestatic io/putString(Ljava/lang/String;)V
	iconst_0
	ireturn
Label1:
.limit stack 2
.limit locals 0
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
