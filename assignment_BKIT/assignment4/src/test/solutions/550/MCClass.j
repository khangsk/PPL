.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/foo()[Ljava/lang/String;
	iconst_2
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo()[Ljava/lang/String;
Label0:
	iconst_3
	anewarray java/lang/String
	astore_0
	aload_0
	iconst_0
	ldc "Hoang"
	aastore
	aload_0
	iconst_1
	ldc "Gia"
	aastore
	aload_0
	iconst_2
	ldc "Khang"
	aastore
	aload_0
	areturn
Label1:
.limit stack 3
.limit locals 1
.end method
