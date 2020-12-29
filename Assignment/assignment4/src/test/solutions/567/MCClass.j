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
	iconst_4
	newarray int
	putstatic MCClass/a [I
	iconst_4
	newarray float
	putstatic MCClass/b [F
	iconst_4
	newarray boolean
	putstatic MCClass/c [Z
	iconst_4
	anewarray java/lang/String
	putstatic MCClass/d [Ljava/lang/String;
	getstatic MCClass/d [Ljava/lang/String;
	iconst_0
	ldc "A"
	aastore
	getstatic MCClass/d [Ljava/lang/String;
	iconst_1
	ldc "B"
	aastore
	getstatic MCClass/d [Ljava/lang/String;
	iconst_2
	ldc "C"
	aastore
	getstatic MCClass/d [Ljava/lang/String;
	iconst_3
	ldc "D"
	aastore
	getstatic MCClass/c [Z
	iconst_0
	iconst_1
	bastore
	getstatic MCClass/c [Z
	iconst_1
	iconst_0
	bastore
	getstatic MCClass/c [Z
	iconst_2
	iconst_0
	bastore
	getstatic MCClass/c [Z
	iconst_3
	iconst_1
	bastore
	getstatic MCClass/b [F
	iconst_0
	ldc 1.0
	fastore
	getstatic MCClass/b [F
	iconst_1
	ldc 2.0
	fastore
	getstatic MCClass/b [F
	iconst_2
	ldc 3.0
	fastore
	getstatic MCClass/b [F
	iconst_3
	ldc 4.0
	fastore
	getstatic MCClass/a [I
	iconst_0
	iconst_1
	iastore
	getstatic MCClass/a [I
	iconst_1
	iconst_2
	iastore
	getstatic MCClass/a [I
	iconst_2
	iconst_3
	iastore
	getstatic MCClass/a [I
	iconst_3
	iconst_4
	iastore
	invokestatic io/printLn()V
	getstatic MCClass/a [I
	iconst_1
	iconst_2
	imul
	iconst_1
	iadd
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/b [F
	iconst_1
	iconst_2
	imul
	iconst_1
	iadd
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/c [Z
	iconst_1
	iconst_2
	imul
	iconst_1
	iadd
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/d [Ljava/lang/String;
	iconst_1
	iconst_2
	imul
	iconst_1
	iadd
	aaload
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 9
.limit locals 1
.end method
