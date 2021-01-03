.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic io/printLn()V
	iconst_0
	ifle Label3
	iconst_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label3:
	iconst_0
	ifle Label4
	iconst_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label4:
	iconst_0
	ifle Label5
	iconst_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label5:
	iconst_0
	ifle Label6
	iconst_4
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label6:
	iconst_0
	ifle Label7
	iconst_5
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label7:
	iconst_0
	ifle Label8
	bipush 6
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label8:
	iconst_0
	ifle Label9
	bipush 7
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label9:
	iconst_0
	ifle Label10
	bipush 8
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label10:
	iconst_1
	ifle Label11
	bipush 9
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label11:
	iconst_1
	ifle Label12
	bipush 10
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label12:
Label2:
Label1:
	return
.limit stack 11
.limit locals 1
.end method
