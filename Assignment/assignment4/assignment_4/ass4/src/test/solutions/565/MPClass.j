.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is isTrue Z from Label0 to Label1
.var 4 is arr [I from Label0 to Label1
Label0:
	iconst_2
	newarray int
	astore 4
	bipush 10
	istore_1
	bipush 11
	istore_2
	aload 4
	iconst_1
	iconst_1
	isub
	iload_2
	iload_1
	irem
	iload_1
	iadd
	iastore
	aload 4
	iconst_2
	iconst_1
	isub
	iload_1
	iload_2
	irem
	iload_2
	iadd
	iastore
	aload 4
	iconst_2
	iconst_1
	isub
	iaload
	aload 4
	iconst_1
	iconst_1
	isub
	iaload
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_3
	iload_3
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 6
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