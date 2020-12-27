.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b F
.field static c Z
.field static d Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c F from Label0 to Label1
.var 3 is d Z from Label0 to Label1
.var 4 is a Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "Hi!"
	astore 4
	iconst_0
	istore_3
	ldc 2.0
	fstore_2
	iconst_2
	istore_1
	invokestatic io/printLn()V
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	fload_2
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iload_3
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	aload 4
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 5
.end method
