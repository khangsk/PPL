.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
.var 2 is hashTable [Z from Label0 to Label1
.var 3 is i I from Label0 to Label1
.var 4 is firstMissValue I from Label0 to Label1
Label0:
	bipush 15
	newarray int
	putstatic MCClass/arr [I
	bipush 15
	newarray boolean
	astore_2
	iconst_0
	istore 4
	iconst_0
	istore_3
	aload_2
	iconst_0
	iconst_0
	bastore
	aload_2
	iconst_1
	iconst_0
	bastore
	aload_2
	iconst_2
	iconst_0
	bastore
	aload_2
	iconst_3
	iconst_0
	bastore
	aload_2
	iconst_4
	iconst_0
	bastore
	aload_2
	iconst_5
	iconst_0
	bastore
	aload_2
	bipush 6
	iconst_0
	bastore
	aload_2
	bipush 7
	iconst_0
	bastore
	aload_2
	bipush 8
	iconst_0
	bastore
	aload_2
	bipush 9
	iconst_0
	bastore
	aload_2
	bipush 10
	iconst_0
	bastore
	aload_2
	bipush 11
	iconst_0
	bastore
	aload_2
	bipush 12
	iconst_0
	bastore
	aload_2
	bipush 13
	iconst_0
	bastore
	aload_2
	bipush 14
	iconst_0
	bastore
	bipush 15
	istore_1
	getstatic MCClass/arr [I
	iconst_0
	iconst_0
	iastore
	getstatic MCClass/arr [I
	iconst_1
	iconst_3
	iastore
	getstatic MCClass/arr [I
	iconst_2
	iconst_4
	iastore
	getstatic MCClass/arr [I
	iconst_3
	bipush 100
	iastore
	getstatic MCClass/arr [I
	iconst_4
	iconst_2
	iastore
	getstatic MCClass/arr [I
	iconst_5
	bipush 20
	iastore
	getstatic MCClass/arr [I
	bipush 6
	iconst_1
	iastore
	getstatic MCClass/arr [I
	bipush 7
	bipush 99
	iastore
	getstatic MCClass/arr [I
	bipush 8
	bipush 7
	iastore
	getstatic MCClass/arr [I
	bipush 9
	bipush 8
	iastore
	getstatic MCClass/arr [I
	bipush 10
	bipush 6
	iastore
	getstatic MCClass/arr [I
	bipush 11
	iconst_2
	iastore
	getstatic MCClass/arr [I
	bipush 12
	iconst_5
	iastore
	getstatic MCClass/arr [I
	bipush 13
	bipush 10
	iastore
	getstatic MCClass/arr [I
	bipush 14
	bipush 12
	iastore
	iconst_0
	istore_3
Label4:
	iload_3
	iload_1
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	getstatic MCClass/arr [I
	iload_3
	iaload
	iload_1
	if_icmple Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label9
	getstatic MCClass/arr [I
	iload_3
	iaload
	iconst_0
	if_icmpgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifgt Label9
	iconst_0
	goto Label10
Label9:
	iconst_1
Label10:
	ifle Label15
	goto Label6
	goto Label8
Label15:
Label8:
	aload_2
	getstatic MCClass/arr [I
	iload_3
	iaload
	iconst_1
	isub
	iconst_1
	bastore
Label6:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label5:
Label7:
	iconst_1
	istore 4
Label20:
	iload 4
	iload_1
	if_icmpgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label17
	aload_2
	iload 4
	iconst_1
	isub
	baload
	ifle Label17
	iconst_1
	goto Label16
Label17:
	iconst_0
Label16:
	ifle Label21
	iload 4
	iconst_1
	iadd
	istore 4
Label22:
	goto Label20
Label21:
Label23:
	ldc "\nFirst positive missing value: "
	invokestatic io/print(Ljava/lang/String;)V
	iload 4
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 32
.limit locals 5
.end method
