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
	getstatic MCClass/a [I
	iconst_0
	bipush 11
	iastore
	getstatic MCClass/a [I
	iconst_1
	bipush 12
	iastore
	getstatic MCClass/a [I
	iconst_2
	bipush 13
	iastore
	getstatic MCClass/a [I
	iconst_3
	bipush 14
	iastore
	getstatic MCClass/b [F
	iconst_0
	ldc 11.0
	fastore
	getstatic MCClass/b [F
	iconst_1
	ldc 12.0
	fastore
	getstatic MCClass/b [F
	iconst_2
	ldc 13.0
	fastore
	getstatic MCClass/b [F
	iconst_3
	ldc 14.0
	fastore
	getstatic MCClass/c [Z
	iconst_0
	iconst_0
	bastore
	getstatic MCClass/c [Z
	iconst_1
	iconst_1
	bastore
	getstatic MCClass/c [Z
	iconst_2
	iconst_1
	bastore
	getstatic MCClass/c [Z
	iconst_3
	iconst_0
	bastore
	getstatic MCClass/d [Ljava/lang/String;
	iconst_0
	ldc "X"
	aastore
	getstatic MCClass/d [Ljava/lang/String;
	iconst_1
	ldc "Y"
	aastore
	getstatic MCClass/d [Ljava/lang/String;
	iconst_2
	ldc "Z"
	aastore
	getstatic MCClass/d [Ljava/lang/String;
	iconst_3
	ldc "T"
	aastore
	invokestatic io/printLn()V
	getstatic MCClass/a [I
	iconst_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/b [F
	iconst_3
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/c [Z
	iconst_3
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass/d [Ljava/lang/String;
	iconst_3
	aaload
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 13
.limit locals 1
.end method
