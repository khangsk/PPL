.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MCClass/i I
	iconst_0
	putstatic MCClass/i I
Label4:
	getstatic MCClass/i I
	bipush 7
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	getstatic MCClass/i I
	invokestatic MCClass/fib(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label6:
	getstatic MCClass/i I
	iconst_1
	iadd
	putstatic MCClass/i I
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public static fib(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iconst_0
	putstatic MCClass/i I
	iload_0
	iconst_1
	if_icmpgt Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	iload_0
	ireturn
	goto Label2
Label5:
Label2:
	iload_0
	iconst_1
	isub
	invokestatic MCClass/fib(I)I
	iload_0
	iconst_2
	isub
	invokestatic MCClass/fib(I)I
	iadd
	ireturn
Label1:
.limit stack 5
.limit locals 1
.end method
