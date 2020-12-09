.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
.var 2 is b Z from Label0 to Label1
.var 3 is isTrue Z from Label0 to Label1
.var 4 is arr [Z from Label0 to Label1
Label0:
	iconst_3
	newarray boolean
	astore 4
	iconst_1
	istore_1
	iconst_1
	ifgt Label3
	iconst_1
	goto Label2
Label3:
	iconst_0
Label2:
	istore_2
	aload 4
	iconst_1
	iconst_1
	isub
	iload_1
	ifgt Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	ifgt Label7
	iconst_1
	goto Label6
Label7:
	iconst_0
Label6:
	bastore
	aload 4
	iconst_2
	iconst_1
	isub
	iload_2
	ifgt Label9
	iconst_1
	goto Label8
Label9:
	iconst_0
Label8:
	bastore
	aload 4
	iconst_1
	iconst_1
	isub
	baload
	aload 4
	iconst_2
	iconst_1
	isub
	baload
	ifgt Label11
	iconst_1
	goto Label10
Label11:
	iconst_0
Label10:
	if_icmpeq Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	istore_3
	iload_3
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 20
.limit locals 5
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
