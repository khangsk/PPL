.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static string [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is sum I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_3
	anewarray java/lang/String
	putstatic MCClass/string [Ljava/lang/String;
	iconst_0
	istore_2
	iconst_0
	istore_1
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
	iload_1
	getstatic MCClass/string [Ljava/lang/String;
	iload_2
	aaload
	invokestatic io/float_of_string(Ljava/lang/String;)F
	invokestatic io/int_of_float(F)I
	iadd
	istore_1
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label5:
Label7:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
.limit locals 3
.end method
