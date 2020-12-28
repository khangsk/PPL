.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ifle Label3
	iconst_0
	ifle Label3
	iconst_1
	goto Label2
Label3:
	iconst_0
Label2:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iconst_1
	ifle Label5
	iconst_1
	ifle Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iconst_0
	ifle Label7
	iconst_1
	ifle Label7
	iconst_1
	goto Label6
Label7:
	iconst_0
Label6:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 16
.limit locals 1
.end method
