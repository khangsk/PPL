.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	iconst_1
	istore_1
	iconst_4
	anewarray java/lang/String
	astore_2
	aload_2
	iconst_0
	ldc "Hoang"
	aastore
	aload_2
	iconst_1
	ldc "Gia"
	aastore
	aload_2
	iconst_2
	ldc "Khang"
	aastore
	aload_2
	iconst_3
	ldc "CSE"
	aastore
	aload_2
	invokestatic MCClass/foo([Ljava/lang/String;)V
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static foo([Ljava/lang/String;)V
.var 0 is a [Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	iconst_3
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method
