.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_4
	invokestatic MCClass/foo1(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static foo1(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_5
	invokestatic MCClass/foo(I)I
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static foo(I)I
.var 0 is x I from Label0 to Label1
.var 1 is t I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iload_0
	istore_1
	iload_0
	ireturn
Label1:
.limit stack 1
.limit locals 2
.end method
