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
	bipush 10
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
.var 2 is x I from Label0 to Label1
	bipush 11
	istore_2
	iload_2
	iload_1
	iadd
	iconst_3
	irem
	iconst_0
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label8
Label11:
Label8:
	iload_1
	bipush 8
	if_icmple Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label15
	goto Label7
	goto Label12
Label15:
Label12:
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
.limit stack 8
.limit locals 3
.end method
