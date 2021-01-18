.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	invokestatic MCClass/fact(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static fact(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label3
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
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MCClass/fact(I)I
	imul
	ireturn
Label1:
.limit stack 5
.limit locals 1
.end method
