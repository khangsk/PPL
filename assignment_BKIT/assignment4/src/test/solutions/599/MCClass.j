.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is a [F from Label0 to Label1
.var 2 is b F from Label0 to Label1
Label0:
	iconst_5
	newarray float
	astore_1
	ldc 2.0
	fstore_2
	aload_1
	iconst_0
	ldc 0.0
	fastore
	aload_1
	iconst_1
	ldc 0.0
	fastore
	aload_1
	iconst_2
	ldc 0.0
	fastore
	aload_1
	iconst_3
	ldc 0.0
	fastore
	aload_1
	iconst_4
	ldc 0.0
	fastore
	aload_1
	fload_2
	invokestatic MCClass/foo([FF)V
Label1:
	return
.limit stack 5
.limit locals 3
.end method

.method public static foo([FF)V
.var 0 is a [F from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_5
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	aload_0
	iload_2
	fload_1
	ldc 1.0
	fadd
	iload_2
	invokestatic io/float_to_int(I)F
	fadd
	fastore
	iload_2
	iconst_1
	iadd
	istore_2
Label6:
	goto Label4
Label5:
Label7:
	iconst_0
	istore_2
Label10:
	iload_2
	iconst_5
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label11
	aload_0
	iload_2
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_2
	iconst_1
	iadd
	istore_2
Label12:
	goto Label10
Label11:
Label13:
Label1:
	return
.limit stack 7
.limit locals 3
.end method
