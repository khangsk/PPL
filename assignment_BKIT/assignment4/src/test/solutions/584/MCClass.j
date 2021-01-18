.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_4
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_5
	iastore
	aload_1
	iconst_1
	iconst_4
	iastore
	aload_1
	iconst_2
	bipush 8
	iastore
	aload_1
	iconst_3
	bipush 9
	iastore
	aload_1
	iconst_4
	invokestatic MCClass/foo([II)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static foo([II)V
.var 0 is a [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
Label4:
	iload_1
	iconst_0
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_1
	iconst_1
	isub
	istore_1
	aload_0
	iload_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label6:
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 4
.limit locals 2
.end method
