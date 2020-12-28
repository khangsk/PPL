.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_4
	newarray float
	astore_1
	aload_1
	iconst_0
	ldc 1.0
	fastore
	aload_1
	iconst_1
	ldc 2.0
	fastore
	aload_1
	iconst_2
	ldc 3.0
	fastore
	aload_1
	iconst_3
	ldc 4.0
	fastore
	aload_1
	invokestatic MCClass/foo([F)V
	ldc "h"
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static foo([F)V
.var 0 is a [F from Label0 to Label1
Label0:
	aload_0
	iconst_3
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method
