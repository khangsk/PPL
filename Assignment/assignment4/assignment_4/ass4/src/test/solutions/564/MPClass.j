.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [Z from Label0 to Label1
.var 2 is a Z from Label0 to Label1
.var 3 is isTrue Z from Label0 to Label1
Label0:
	iconst_2
	newarray boolean
	astore_1
	iconst_0
	istore_2
	aload_1
	iconst_1
	iconst_1
	isub
	iload_2
	ifgt Label3
	iconst_1
	goto Label2
Label3:
	iconst_0
Label2:
	bastore
	aload_1
	iconst_1
	iconst_1
	isub
	baload
	iload_2
	ifgt Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	istore_3
	iload_3
	invokestatic io/putBoolLn(Z)V
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
