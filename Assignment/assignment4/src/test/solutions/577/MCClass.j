.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	bipush 10
	newarray int
	putstatic MCClass/arr [I
	iconst_0
	istore_1
	getstatic MCClass/arr [I
	iconst_0
	iconst_1
	iastore
	getstatic MCClass/arr [I
	iconst_1
	bipush 7
	iastore
	getstatic MCClass/arr [I
	iconst_2
	bipush 8
	iastore
	getstatic MCClass/arr [I
	iconst_3
	iconst_4
	iastore
	getstatic MCClass/arr [I
	iconst_4
	iconst_2
	iastore
	getstatic MCClass/arr [I
	iconst_5
	iconst_5
	iastore
	getstatic MCClass/arr [I
	bipush 6
	bipush 9
	iastore
	getstatic MCClass/arr [I
	bipush 7
	bipush 10
	iastore
	getstatic MCClass/arr [I
	bipush 8
	bipush 6
	iastore
	getstatic MCClass/arr [I
	bipush 9
	iconst_3
	iastore
	iconst_0
	istore_1
Label4:
	iload_1
	bipush 10
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
.var 2 is j I from Label0 to Label1
.var 3 is minIndex I from Label0 to Label1
.var 4 is temp I from Label0 to Label1
	iconst_0
	istore_2
	iconst_0
	istore_3
	iconst_0
	istore 4
	iload_1
	istore_3
	iload_1
	iconst_1
	iadd
	istore_2
Label10:
	iload_2
	bipush 10
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label11
	getstatic MCClass/arr [I
	iload_2
	iaload
	getstatic MCClass/arr [I
	iload_3
	iaload
	if_icmpge Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
	iload_2
	istore_3
	goto Label14
Label17:
Label14:
Label12:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label11:
Label13:
	getstatic MCClass/arr [I
	iload_1
	iaload
	istore 4
	getstatic MCClass/arr [I
	iload_1
	getstatic MCClass/arr [I
	iload_3
	iaload
	iastore
	getstatic MCClass/arr [I
	iload_3
	iload 4
	iastore
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label5:
Label7:
	ldc "\nSorted array:"
	invokestatic io/print(Ljava/lang/String;)V
	iconst_0
	istore_1
Label20:
	iload_1
	bipush 10
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label21
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/arr [I
	iload_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label22:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label20
Label21:
Label23:
	invokestatic io/printLn()V
Label1:
	return
.limit stack 12
.limit locals 5
.end method
