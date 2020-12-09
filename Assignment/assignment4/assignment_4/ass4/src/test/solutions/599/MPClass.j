.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [F from Label0 to Label1
Label0:
	iconst_3
	newarray float
	astore_1
	aload_1
	iconst_3
	iconst_1
	isub
	ldc 1.5
	fastore
	aload_1
	iconst_3
	iconst_1
	isub
	aload_1
	invokestatic MPClass/foo([F)[F
	iconst_3
	iconst_1
	isub
	faload
	ldc 1.1
	fadd
	fastore
	aload_1
	iconst_3
	iconst_1
	isub
	faload
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 6
.limit locals 2
.end method

.method public static foo([F)[F
.var 0 is x [F from Label0 to Label1
Label0:
	aload_0
	invokevirtual [F/clone()Ljava/lang/Object;
	checkcast [F
	astore_0
	aload_0
	iconst_3
	iconst_1
	isub
	ldc 5.1
	fastore
	aload_0
	areturn
Label1:
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
