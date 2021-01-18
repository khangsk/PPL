.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is y F from Label0 to Label1
Label0:
	ldc 4.0
	fstore_2
	iconst_5
	istore_1
	iconst_2
	iload_1
	iadd
	ldc 3.0
	fload_2
	fdiv
	invokestatic MCClass/foo(IF)V
	invokestatic MCClass/goo()V
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public static foo(IF)V
.var 0 is a I from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	iload_0
	invokestatic io/float_to_int(I)F
	fload_1
	fmul
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static goo()V
Label0:
	ldc "Nothing to print!!!"
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 0
.end method
