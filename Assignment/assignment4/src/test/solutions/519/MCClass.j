.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	iconst_5
	istore_1
	iload_1
	iconst_1
	isub
	istore_1
	iload_1
	iconst_0
	if_icmpge Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	ldc "Nho hon 0"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label5:
	iload_1
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "Bang 0"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label8:
	iload_1
	iconst_1
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	ldc "stop"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label11:
.var 2 is y I from Label0 to Label1
	bipush 100
	istore_2
	iload_1
	iload_2
	iadd
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label2:
Label1:
	return
.limit stack 8
.limit locals 3
.end method
