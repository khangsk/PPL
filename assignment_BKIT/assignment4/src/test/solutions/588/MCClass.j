.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is a___b I from Label0 to Label1
.var 2 is b Z from Label0 to Label1
.var 3 is c F from Label0 to Label1
Label0:
	ldc 123.0
	fstore_3
	iconst_1
	istore_2
	sipush 12345
	istore_1
	iload_2
	ifle Label3
	fload_3
	ldc 1.0
	fadd
	fstore_3
	fload_3
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label3:
	iload_2
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	return
	goto Label2
Label6:
Label2:
	return
Label1:
	return
.limit stack 5
.limit locals 4
.end method
