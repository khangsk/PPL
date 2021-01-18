.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [I
.field static b [F
.field static c [Z
.field static d [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	newarray int
	putstatic MCClass/a [I
	iconst_1
	newarray float
	putstatic MCClass/b [F
	iconst_1
	newarray boolean
	putstatic MCClass/c [Z
	iconst_1
	anewarray java/lang/String
	putstatic MCClass/d [Ljava/lang/String;
	getstatic MCClass/d [Ljava/lang/String;
	iconst_0
	ldc "Hi!"
	aastore
	getstatic MCClass/c [Z
	iconst_0
	iconst_1
	bastore
	getstatic MCClass/b [F
	iconst_0
	ldc 1.0
	fastore
	getstatic MCClass/a [I
	iconst_0
	iconst_1
	iastore
	invokestatic io/printLn()V
	getstatic MCClass/a [I
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/b [F
	iconst_0
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/c [Z
	iconst_0
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/d [Ljava/lang/String;
	iconst_0
	aaload
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
.limit locals 1
.end method
