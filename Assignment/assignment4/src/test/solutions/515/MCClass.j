.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	ifgt Label4
	bipush 10
	iconst_5
	imul
	bipush 60
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label4
	iconst_0
	goto Label5
Label4:
	iconst_1
Label5:
	ifgt Label2
	iconst_3
	iconst_4
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label2
	iconst_0
	goto Label3
Label2:
	iconst_1
Label3:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 12
.limit locals 1
.end method
