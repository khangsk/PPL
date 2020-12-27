.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b F
.field static c Z
.field static d Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	ldc ""
	putstatic MCClass/d Ljava/lang/String;
	iconst_1
	putstatic MCClass/c Z
	ldc 1.0
	putstatic MCClass/b F
	iconst_1
	putstatic MCClass/a I
	invokestatic io/printLn()V
	getstatic MCClass/a I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/b F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/c Z
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/d Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method
