.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_4
	anewarray java/lang/String
	astore_1
	aload_1
	iconst_0
	ldc "Hoang"
	aastore
	aload_1
	iconst_1
	ldc "Gia"
	aastore
	aload_1
	iconst_2
	ldc "Khang"
	aastore
	aload_1
	iconst_3
	ldc "CSE"
	aastore
	aload_1
	invokestatic MCClass/foo([Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static foo([Ljava/lang/String;)V
.var 0 is a [Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	iconst_1
	iconst_2
	imul
	iconst_1
	iadd
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method
