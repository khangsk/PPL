.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ifle Label5
	iconst_1
	iconst_2
	iadd
	iconst_3
	if_icmplt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	ifle Label3
	iconst_3
	iconst_4
	if_icmpeq Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	iconst_1
	goto Label2
Label3:
	iconst_0
Label2:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 12
.limit locals 1
.end method
