.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	ifgt Label3
	iconst_0
	ifgt Label3
	iconst_0
	goto Label2
Label3:
	iconst_1
Label2:
	ifgt Label5
	iconst_1
	ifgt Label5
	iconst_0
	goto Label4
Label5:
	iconst_1
Label4:
	ifle Label6
	iconst_1
	ifgt Label9
	iconst_0
	ifgt Label9
	iconst_0
	goto Label8
Label9:
	iconst_1
Label8:
	iconst_0
	ifgt Label11
	iconst_1
	ifgt Label11
	iconst_0
	goto Label10
Label11:
	iconst_1
Label10:
	iand
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 23
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
