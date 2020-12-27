.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	ldc ""
	putstatic MCClass/b Ljava/lang/String;
	iconst_1
	putstatic MCClass/a I
	invokestatic io/printLn()V
	iconst_0
	ifle Label3
.var 1 is b I from Label0 to Label1
	iconst_1
	istore_1
	getstatic MCClass/a I
	iconst_1
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label3:
	iconst_0
	ifle Label4
.var 2 is b F from Label0 to Label1
	ldc 1.0
	fstore_2
	getstatic MCClass/a I
	iconst_2
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	fload_2
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label4:
.var 3 is b Z from Label0 to Label1
	iconst_1
	istore_3
	getstatic MCClass/a I
	iconst_3
	iadd
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iload_3
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label2:
Label1:
	return
.limit stack 5
.limit locals 4
.end method
