.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x [I from Label0 to Label1
Label0:
	iconst_3
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_5
	iastore
	aload_1
	iconst_1
	bipush 7
	iastore
	aload_1
	iconst_2
	bipush 9
	iastore
	iconst_3
	invokestatic MCClass/foo1(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_1
	iaload
	invokestatic MCClass/foo()[I
	iconst_1
	iaload
	invokestatic MCClass/foo1(I)I
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static foo1(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static foo()[I
.var 0 is x [I from Label0 to Label1
Label0:
	iconst_2
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
	areturn
Label1:
.limit stack 5
.limit locals 1
.end method
