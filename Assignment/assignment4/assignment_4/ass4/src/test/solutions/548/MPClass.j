.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a Z
.field static b Z
.field static gArr [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [Z from Label0 to Label1
.var 2 is c Z from Label0 to Label1
.var 3 is d Z from Label0 to Label1
Label0:
	iconst_4
	newarray boolean
	astore_1
	iconst_1
	istore_2
	iconst_0
	istore_3
	iload_3
	istore_2
	iload_2
	putstatic MPClass/a Z
	iconst_0
	istore_3
	iload_3
	putstatic MPClass/b Z
	aload_1
	iconst_1
	iconst_1
	isub
	iconst_1
	bastore
	aload_1
	iconst_1
	iconst_1
	isub
	iconst_1
	bastore
	getstatic MPClass/gArr [Z
	iconst_1
	iconst_1
	isub
	aload_1
	iconst_1
	iconst_1
	isub
	baload
	bastore
	aload_1
	iconst_3
	iconst_1
	isub
	iload_3
	bastore
	getstatic MPClass/gArr [Z
	iconst_3
	iconst_1
	isub
	aload_1
	iconst_3
	iconst_1
	isub
	baload
	bastore
	getstatic MPClass/gArr [Z
	iconst_2
	iconst_1
	isub
	getstatic MPClass/gArr [Z
	iconst_3
	iconst_1
	isub
	baload
	bastore
	getstatic MPClass/gArr [Z
	iconst_2
	iconst_1
	isub
	baload
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 11
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
	iconst_4
	newarray boolean
	putstatic MPClass/gArr [Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
