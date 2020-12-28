.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_2
	bipush 15
	istore_1
	iconst_0
	istore_2
Label4:
	iload_2
	iload_1
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	iload_2
	invokestatic MCClass/prime(I)I
	ifle Label9
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label8
Label9:
Label8:
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label5:
Label7:
Label1:
	return
.limit stack 5
.limit locals 3
.end method

.method public static prime(I)I
.var 0 is n I from Label0 to Label1
Label0:
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
	iload_0
	iconst_2
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label6
	iload_0
	iconst_3
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label6
	iconst_0
	goto Label7
Label6:
	iconst_1
Label7:
	ifle Label12
	iconst_1
	ireturn
	goto Label2
Label12:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	iconst_2
	istore_1
Label15:
	iload_1
	iload_0
	if_icmpge Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label16
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label22
	iconst_0
	ireturn
	goto Label19
Label22:
Label19:
Label17:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label15
Label16:
Label18:
	iconst_1
	ireturn
Label2:
	iconst_1
	ireturn
Label1:
.limit stack 19
.limit locals 2
.end method
