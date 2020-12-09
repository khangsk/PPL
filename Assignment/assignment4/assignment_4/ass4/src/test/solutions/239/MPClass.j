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
	bipush 20
	ineg
	istore_2
	bipush 20
	istore_3
	getstatic MPClass/a [I
	iload_2
	sipush -10000
	isub
	iconst_1
	iastore
	getstatic MPClass/a [I
	iload_2
	iconst_1
	iadd
	sipush -10000
	isub
	iconst_1
	iastore
	iload_2
	iconst_2
	iadd
	istore_1
Label2:
	iload_1
	iload_3
	if_icmpgt Label3
	getstatic MPClass/a [I
	iload_1
	sipush -10000
	isub
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	sipush -10000
	isub
	iaload
	getstatic MPClass/a [I
	iload_1
	iconst_2
	isub
	sipush -10000
	isub
	iaload
	iadd
	iastore
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	getstatic MPClass/a [I
	iload_3
	sipush -10000
	isub
	iaload
	invokestatic io/putInt(I)V
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
	sipush 20001
	newarray int
	putstatic MPClass/a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
