.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
Label0:
	bipush 10
	istore_1
	iconst_1
	istore_2
Label2:
	iload_2
	iload_1
	if_icmpgt Label3
	iconst_1
	istore_3
Label6:
	iload_3
	iload_2
	if_icmpgt Label7
	ldc "*"
	invokestatic io/putString(Ljava/lang/String;)V
Label8:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label6
Label7:
Label9:
	invokestatic io/putLn()V
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 2
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
