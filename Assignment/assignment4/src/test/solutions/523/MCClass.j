.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic io/printLn()V
	iconst_1
	ifgt Label2
	iconst_1
	ifgt Label2
	iconst_0
	goto Label3
Label2:
	iconst_1
Label3:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iconst_1
	ifgt Label4
	iconst_0
	ifgt Label4
	iconst_0
	goto Label5
Label4:
	iconst_1
Label5:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iconst_0
	ifgt Label6
	iconst_1
	ifgt Label6
	iconst_0
	goto Label7
Label6:
	iconst_1
Label7:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iconst_0
	ifgt Label8
	iconst_0
	ifgt Label8
	iconst_0
	goto Label9
Label8:
	iconst_1
Label9:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 21
.limit locals 1
.end method
