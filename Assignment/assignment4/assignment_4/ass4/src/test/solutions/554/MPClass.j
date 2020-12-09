.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MPClass/arr [I
	iconst_3
	iconst_1
	isub
	iconst_3
	iastore
	getstatic MPClass/arr [I
	iconst_2
	iconst_1
	isub
	getstatic MPClass/arr [I
	iconst_3
	iconst_1
	isub
	iaload
	iastore
	getstatic MPClass/arr [I
	iconst_1
	iconst_1
	isub
	getstatic MPClass/arr [I
	iconst_2
	iconst_1
	isub
	iaload
	iastore
	bipush 10
	getstatic MPClass/arr [I
	iconst_1
	iconst_1
	isub
	iaload
	idiv
	putstatic MPClass/b I
	getstatic MPClass/arr [I
	iconst_3
	iconst_1
	isub
	iaload
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 6
.limit locals 1
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
	iconst_3
	newarray int
	putstatic MPClass/arr [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
