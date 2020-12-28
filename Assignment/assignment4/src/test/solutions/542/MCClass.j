.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x [Ljava/lang/String; from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_3
	anewarray java/lang/String
	astore_1
	iconst_0
	istore_2
	aload_1
	iconst_0
	ldc "Hoang"
	aastore
	aload_1
	iconst_1
	ldc "Gia"
	aastore
	aload_1
	iconst_2
	ldc "Khang"
	aastore
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_3
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	aload_1
	iload_2
	aaload
	invokestatic io/print(Ljava/lang/String;)V
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 5
.limit locals 3
.end method
