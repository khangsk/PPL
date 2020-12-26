.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	iconst_5
	istore_1
Label2:
	iload_1
	invokestatic MCClass/check(I)I
	ifle Label3
.var 2 is y F from Label0 to Label1
	ldc 0.0
	fstore_2
	fload_2
	iload_1
	invokestatic io/float_to_int(I)F
	fadd
	fstore_2
	fload_2
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	iconst_1
	isub
	istore_1
Label4:
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static check(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmple Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	iconst_1
	ireturn
	goto Label2
Label5:
Label2:
	iconst_0
	ireturn
Label1:
	return
.limit stack 5
.limit locals 1
.end method
