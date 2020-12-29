.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is b [F from Label0 to Label1
.var 2 is a [I from Label0 to Label1
.var 3 is i I from Label0 to Label1
Label0:
	bipush 12
	newarray float
	astore_1
	bipush 6
	newarray int
	astore_2
	iconst_0
	istore_3
	aload_2
	iconst_0
	iconst_1
	iastore
	aload_2
	iconst_1
	iconst_2
	iastore
	aload_2
	iconst_2
	iconst_3
	iastore
	aload_2
	iconst_3
	iconst_4
	iastore
	aload_2
	iconst_4
	iconst_5
	iastore
	aload_2
	iconst_5
	bipush 6
	iastore
	aload_1
	iconst_0
	ldc 2.3
	fastore
	aload_1
	iconst_1
	ldc 5.0
	fastore
	aload_1
	iconst_2
	ldc 7.4
	fastore
	aload_1
	iconst_3
	ldc 4.0
	fastore
	aload_1
	iconst_4
	ldc 6.0
	fastore
	aload_1
	iconst_5
	ldc 17.0
	fastore
	aload_1
	bipush 6
	ldc 9.12
	fastore
	aload_1
	bipush 7
	ldc 30.0
	fastore
	aload_1
	bipush 8
	ldc 0.0
	fastore
	aload_1
	bipush 9
	ldc 10.3
	fastore
	aload_1
	bipush 10
	ldc 5.0
	fastore
	aload_1
	bipush 11
	ldc 2.4
	fastore
	aload_2
	iconst_3
	iconst_2
	invokestatic MCClass/foo(I)I
	iadd
	aload_2
	aload_1
	iconst_2
	iconst_4
	imul
	iconst_3
	iadd
	faload
	invokestatic io/int_of_float(F)I
	iaload
	iconst_4
	iadd
	iastore
	iconst_0
	istore_3
Label4:
	iload_3
	bipush 6
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	aload_2
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label6:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 6
.limit locals 4
.end method

.method public static foo(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	isub
	ireturn
Label1:
.limit stack 2
.limit locals 1
.end method
