.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_1
Label2:
	iload_1
	bipush 10
	if_icmpgt Label3
	iload_1
	iconst_4
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	iload_1
	ineg
	invokestatic io/putInt(I)V
	goto Label9
Label8:
	iload_1
	invokestatic io/putInt(I)V
Label9:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 3
.limit locals 2
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
