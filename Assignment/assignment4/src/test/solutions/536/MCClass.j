.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	iconst_4
	istore_1
	iload_1
	iconst_3
	iconst_4
	invokestatic MCClass/foo(II)I
	if_icmple Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label5:
	iconst_3
	iconst_5
	invokestatic MCClass/foo(II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label2:
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static foo(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	iconst_4
	iconst_5
	invokestatic MCClass/foo1(II)I
	iadd
	ireturn
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static foo1(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	imul
	ireturn
Label1:
	return
.limit stack 2
.limit locals 2
.end method
