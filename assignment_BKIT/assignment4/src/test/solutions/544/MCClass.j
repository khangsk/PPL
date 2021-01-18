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
	aload_1
	iconst_1
	iaload
	iconst_3
	iconst_4
	invokestatic MCClass/foo(II)[I
	iconst_0
	iaload
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static foo(II)[I
.var 0 is m I from Label0 to Label1
.var 1 is n I from Label0 to Label1
.var 2 is y [I from Label0 to Label1
Label0:
	iconst_2
	newarray int
	astore_2
	aload_2
	iconst_0
	iconst_1
	iastore
	aload_2
	iconst_1
	iconst_2
	iastore
	iload_0
	iload_1
	imul
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_2
	areturn
Label1:
.limit stack 5
.limit locals 3
.end method
