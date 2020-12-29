.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is p I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
Label0:
	bipush 6
	newarray int
	putstatic MCClass/arr [I
	iconst_0
	istore_3
	iconst_0
	istore_2
	iconst_1
	istore_1
	getstatic MCClass/arr [I
	iconst_0
	iconst_1
	iastore
	getstatic MCClass/arr [I
	iconst_1
	iconst_2
	iastore
	getstatic MCClass/arr [I
	iconst_2
	iconst_4
	iastore
	getstatic MCClass/arr [I
	iconst_3
	iconst_5
	iastore
	getstatic MCClass/arr [I
	iconst_4
	iconst_3
	iastore
	getstatic MCClass/arr [I
	iconst_5
	iconst_5
	iastore
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
	iconst_0
	istore_3
Label10:
	iload_3
	iconst_2
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label11
	iload_1
	getstatic MCClass/arr [I
	iload_2
	iconst_2
	imul
	iload_3
	iadd
	iaload
	imul
	istore_1
Label12:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label10
Label11:
Label13:
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
.limit stack 10
.limit locals 4
.end method
