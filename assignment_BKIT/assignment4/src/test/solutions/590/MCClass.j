.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static string [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x [F from Label0 to Label1
.var 2 is sum F from Label0 to Label1
.var 3 is i I from Label0 to Label1
Label0:
	iconst_3
	anewarray java/lang/String
	putstatic MCClass/string [Ljava/lang/String;
	iconst_3
	newarray float
	astore_1
	iconst_0
	istore_3
	ldc 0.0
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
	getstatic MCClass/string [Ljava/lang/String;
	iconst_0
	ldc "1.23"
	aastore
	getstatic MCClass/string [Ljava/lang/String;
	iconst_1
	ldc "0.e4"
	aastore
	getstatic MCClass/string [Ljava/lang/String;
	iconst_2
	ldc "12e2"
	aastore
	iconst_0
	istore_3
Label4:
	iload_3
	iconst_3
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	aload_1
	iload_3
	getstatic MCClass/string [Ljava/lang/String;
	iload_3
	aaload
	invokestatic io/float_of_string(Ljava/lang/String;)F
	fastore
	fload_2
	aload_1
	iload_3
	faload
	fadd
	fstore_2
Label6:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label5:
Label7:
	fload_2
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 8
.limit locals 4
.end method
