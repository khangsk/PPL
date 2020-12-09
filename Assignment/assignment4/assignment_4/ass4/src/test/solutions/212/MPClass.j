.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is l I from Label0 to Label1
.var 4 is r I from Label0 to Label1
Label0:
	bipush 11
	newarray int
	astore_1
	ldc 1000000000
	istore_3
	ldc 1000000010
	istore 4
	iload_3
	istore_2
Label2:
	iload_2
	iload 4
	if_icmpgt Label3
	aload_1
	iload_2
	ldc 1000000000
	isub
	iload_2
	iconst_1
	iadd
	iastore
	aload_1
	iload_2
	ldc 1000000000
	isub
	iaload
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	invokestatic io/putLn()V
	iload_3
	istore_2
Label6:
	iload_2
	iload 4
	if_icmpgt Label7
	iload_2
	invokestatic io/putInt(I)V
	ldc ": "
	invokestatic io/putString(Ljava/lang/String;)V
	aload_1
	iload_2
	ldc 1000000000
	isub
	iaload
	invokestatic io/putIntLn(I)V
Label8:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label7:
Label9:
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
