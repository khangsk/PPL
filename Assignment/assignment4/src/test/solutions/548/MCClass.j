.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/foo()[I
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo()[I
Label0:
	iconst_4
	newarray int
	astore_0
	aload_0
	iconst_0
	iconst_1
	iastore
	aload_0
	iconst_1
	iconst_2
	iastore
	aload_0
	iconst_2
	iconst_3
	iastore
	aload_0
	iconst_3
	iconst_4
	iastore
	aload_0
	areturn
Label1:
.limit stack 4
.limit locals 1
.end method
