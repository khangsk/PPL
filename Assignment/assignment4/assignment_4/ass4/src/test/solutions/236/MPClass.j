.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is l I from Label0 to Label1
.var 3 is r I from Label0 to Label1
Label0:
	ldc 1000000000
	istore_2
	ldc 1000000010
	istore_3
	iload_2
	istore_1
Label2:
	iload_1
	iload_3
	if_icmpgt Label3
	getstatic MPClass/a [I
	iload_1
	ldc 1000000000
	isub
	iload_1
	iconst_1
	iadd
	iastore
	getstatic MPClass/a [I
	iload_1
	ldc 1000000000
	isub
	iaload
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	invokestatic io/putLn()V
	iload_2
	istore_1
Label6:
	iload_1
	iload_3
	if_icmpgt Label7
	iload_1
	invokestatic io/putInt(I)V
	ldc ": "
	invokestatic io/putString(Ljava/lang/String;)V
	getstatic MPClass/a [I
	iload_1
	ldc 1000000000
	isub
	iaload
	invokestatic io/putIntLn(I)V
Label8:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label6
Label7:
Label9:
Label1:
	return
.limit stack 6
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
	bipush 11
	newarray int
	putstatic MPClass/a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
