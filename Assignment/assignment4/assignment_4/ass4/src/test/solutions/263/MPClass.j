.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iload_1
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
.var 2 is b I from Label6 to Label7
Label6:
	iload_1
	invokestatic io/putInt(I)V
	iconst_2
	istore_2
	iload_2
	iconst_2
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
.var 3 is b I from Label12 to Label13
Label12:
	iload_1
	invokestatic io/putInt(I)V
	iconst_4
	istore_3
Label13:
	goto Label11
Label10:
.var 3 is a I from Label14 to Label15
Label14:
	iload_2
	invokestatic io/putInt(I)V
	iconst_3
	istore_3
Label15:
Label11:
Label7:
Label5:
Label1:
	return
.limit stack 5
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
