.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is a I from Label0 to Label1
Label0:
	bipush 100
	istore_2
	iconst_0
	istore_1
	invokestatic io/printLn()V
Label4:
.var 3 is a I from Label0 to Label1
	iconst_0
	istore_3
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_3
	iconst_1
	iadd
	istore_3
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
	iload_1
	iconst_5
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
Label5:
Label7:
	invokestatic io/printLn()V
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
.limit locals 4
.end method
