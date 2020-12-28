.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	invokestatic MCClass/foo()V
	iconst_2
	iconst_3
	invokestatic MCClass/foo1(II)V
	bipush 120
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static foo()V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iconst_2
	istore_1
	iconst_1
	istore_0
	iload_0
	iload_1
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static foo1(II)V
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
