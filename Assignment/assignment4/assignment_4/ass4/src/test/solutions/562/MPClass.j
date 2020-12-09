.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static arr [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [F from Label0 to Label1
.var 2 is b F from Label0 to Label1
.var 3 is isTrue Z from Label0 to Label1
Label0:
	iconst_4
	newarray float
	astore_1
	aload_1
	iconst_1
	iconst_1
	isub
	ldc 11.5
	fastore
	aload_1
	iconst_2
	iconst_1
	isub
	aload_1
	iconst_1
	iconst_1
	isub
	faload
	ldc 2.5
	fadd
	fastore
	aload_1
	iconst_2
	iconst_1
	isub
	faload
	ldc 14.0
	fcmpl
	iflt Label2
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
	newarray float
	putstatic MPClass/arr [F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
