.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x [I from Label0 to Label1
Label0:
	bipush 18
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
	bipush 8
	iastore
	aload_1
	iconst_3
	iconst_4
	iastore
	aload_1
	iconst_4
	bipush 9
	iastore
	aload_1
	iconst_5
	bipush 7
	iastore
	aload_1
	bipush 6
	iconst_1
	iastore
	aload_1
	bipush 7
	iconst_0
	iastore
	aload_1
	bipush 8
	iconst_4
	iastore
	aload_1
	bipush 9
	bipush 8
	iastore
	aload_1
	bipush 10
	bipush 7
	iastore
	aload_1
	bipush 11
	bipush 6
	iastore
	aload_1
	bipush 12
	iconst_5
	iastore
	aload_1
	bipush 13
	iconst_5
	iastore
	aload_1
	bipush 14
	bipush 9
	iastore
	aload_1
	bipush 15
	iconst_0
	iastore
	aload_1
	bipush 16
	iconst_4
	iastore
	aload_1
	bipush 17
	iconst_2
	iastore
	aload_1
	bipush 8
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method
