.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iload_1
	iconst_1
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	goto Label3
Label2:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 2
.end method
