.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is a I from Label0 to Label1
.var 4 is b I from Label0 to Label1
Label0:
	iconst_1
	istore_3
	bipush 10
	istore 4
	iload_3
	istore_1
Label2:
	iload_1
	iload 4
	if_icmpgt Label3
	iload_1
	invokestatic io/putInt(I)V
	ldc ": "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	istore_2
Label6:
	iload_2
	iload 4
	if_icmpgt Label7
	iload_2
	iload_1
	iadd
	iconst_2
	imul
	iload 4
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	goto Label13
Label12:
	goto Label9
Label13:
	iload_2
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label8:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label7:
Label9:
	iload_1
	iconst_5
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	goto Label17
Label16:
	goto Label4
Label17:
	invokestatic io/putLn()V
	ldc "j = "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	invokestatic io/putIntLn(I)V
	ldc "i = "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	invokestatic io/putIntLn(I)V
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 5
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
