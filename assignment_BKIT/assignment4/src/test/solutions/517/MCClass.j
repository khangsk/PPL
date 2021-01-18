.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_3
	iconst_3
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	bipush 10
	bipush 9
	if_icmpeq Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label11
	iconst_1
	goto Label10
Label11:
	iconst_0
Label10:
	ifle Label9
	bipush 100
	bipush 10
	ineg
	if_icmple Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label9
	iconst_1
	goto Label8
Label9:
	iconst_0
Label8:
	ifle Label7
	iconst_2
	ineg
	iconst_0
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label7
	iconst_1
	goto Label6
Label7:
	iconst_0
Label6:
	ifle Label5
	bipush 90
	bipush 90
	if_icmplt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	ifle Label3
	bipush 12
	ineg
	bipush 12
	ineg
	if_icmpgt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label3
	iconst_1
	goto Label2
Label3:
	iconst_0
Label2:
	istore_1
	iload_1
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 29
.limit locals 2
.end method
