.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is n I from Label0 to Label1
Label0:
	bipush 50
	istore_2
	iconst_0
	istore_1
	ldc "\nPrime numbers that less than "
	invokestatic io/print(Ljava/lang/String;)V
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ":"
	invokestatic io/print(Ljava/lang/String;)V
	iconst_2
	istore_1
Label4:
	iload_1
	iload_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
.var 3 is isPrime Z from Label0 to Label1
.var 4 is j I from Label0 to Label1
	iconst_1
	istore_3
	iconst_2
	istore 4
	iconst_2
	istore 4
Label10:
	iload 4
	iload_1
	iconst_1
	isub
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label11
	iload 4
	iload 4
	imul
	iload_1
	if_icmple Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
	goto Label13
	goto Label14
Label17:
Label14:
	iload_1
	iload 4
	irem
	iconst_0
	if_icmpne Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label21
	iconst_0
	istore_3
	goto Label13
	goto Label18
Label21:
Label18:
Label12:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label10
Label11:
Label13:
	iload_3
	ifle Label23
	ldc " "
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label22
Label23:
Label22:
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label5:
Label7:
	invokestatic io/printLn()V
Label1:
	return
.limit stack 13
.limit locals 5
.end method
