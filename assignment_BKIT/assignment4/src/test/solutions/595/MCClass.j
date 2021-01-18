.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is c [I from Label0 to Label1
	iconst_4
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_4
	iastore
	aload_1
	iconst_1
	iconst_5
	iastore
	aload_1
	iconst_2
	bipush 6
	iastore
	aload_1
	iconst_3
	bipush 7
	iastore
	aload_1
	iconst_1
	iconst_2
	imul
	iconst_0
	iadd
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method
