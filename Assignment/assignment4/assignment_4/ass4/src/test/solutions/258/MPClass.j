.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label2 to Label3
.var 2 is j I from Label2 to Label3
.var 3 is k I from Label2 to Label3
.var 4 is a [I from Label2 to Label3
.var 5 is b [I from Label2 to Label3
.var 6 is c [I from Label2 to Label3
Label2:
	ldc 100002
	newarray int
	astore 4
	ldc 100002
	newarray int
	astore 5
	ldc 100002
	newarray int
	astore 6
	iconst_1
	ineg
	istore_1
Label4:
	iload_1
	sipush 1000
	if_icmpgt Label5
	aload 4
	iload_1
	iconst_m1
	isub
	iload_1
	iload_1
	imul
	iload_1
	isub
	sipush 1000
	iload_1
	iload_1
	iload_1
	imul
	iload_1
	imul
	iadd
	iconst_5
	iload_1
	iload_1
	imul
	iconst_4
	iconst_3
	imul
	iadd
	imul
	iload_1
	iload_1
	iadd
	iload_1
	iconst_2
	imul
	iconst_3
	imul
	iconst_4
	imul
	iconst_1
	iconst_2
	iadd
	iconst_3
	iconst_4
	imul
	iconst_5
	irem
	isub
	iconst_1
	iadd
	irem
	isub
	iconst_1
	iadd
	irem
	isub
	iconst_1
	iadd
	irem
	iadd
	iastore
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label5:
Label7:
	iconst_1
	ineg
	istore_1
Label8:
	iload_1
	bipush 50
	if_icmpgt Label9
	aload 4
	iload_1
	iconst_m1
	isub
	iaload
	aload 5
	iload_1
	iconst_m1
	isub
	iaload
	iadd
	invokestatic io/putInt(I)V
Label10:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label9:
Label11:
Label3:
Label1:
	return
.limit stack 11
.limit locals 7
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
