.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_5
	invokestatic MCClass/sum(I)I
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static sum(I)I
.var 0 is x I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_5
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_0
	iload_1
	iadd
	istore_0
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label5:
Label7:
	iload_0
	ireturn
Label1:
.limit stack 5
.limit locals 2
.end method
