.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_0
	istore_1
Label4:
	iload_1
	bipush 100
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_1
	invokestatic MCClass/prime_number(I)I
	ifle Label9
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label8
Label9:
Label8:
Label6:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static prime_number(I)I
.var 0 is n I from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iload_0
	iconst_2
	if_icmpge Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label5
	iconst_0
	ireturn
	goto Label2
Label5:
Label2:
	iload_0
	iconst_2
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label7
	iload_0
	iconst_3
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label7
	iconst_0
	goto Label8
Label7:
	iconst_1
Label8:
	ifle Label13
	iconst_1
	ireturn
	goto Label6
Label13:
Label6:
	iconst_2
	istore_1
Label16:
	iload_1
	iload_0
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label17
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifle Label23
	iconst_0
	ireturn
	goto Label20
Label23:
Label20:
Label18:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label16
Label17:
Label19:
	iconst_1
	ireturn
Label1:
.limit stack 18
.limit locals 2
.end method
