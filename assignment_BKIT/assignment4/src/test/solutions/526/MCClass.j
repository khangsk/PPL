.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	bipush 10
	istore_1
Label4:
.var 2 is x I from Label0 to Label1
.var 3 is y I from Label0 to Label1
	iconst_5
	istore_2
	iconst_4
	istore_3
	iload_1
	iload_2
	iadd
	iload_3
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
	iconst_1
	isub
	istore_1
Label6:
	iload_1
	iconst_0
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
Label5:
Label7:
Label1:
	return
.limit stack 7
.limit locals 4
.end method
