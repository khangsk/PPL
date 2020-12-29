.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [I
.field static y [I

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 18
	newarray int
	putstatic MCClass/x [I
	iconst_2
	newarray int
	putstatic MCClass/y [I
	getstatic MCClass/y [I
	iconst_0
	iconst_5
	iastore
	getstatic MCClass/y [I
	iconst_1
	bipush 7
	iastore
	getstatic MCClass/x [I
	iconst_0
	iconst_4
	iastore
	getstatic MCClass/x [I
	iconst_1
	iconst_5
	iastore
	getstatic MCClass/x [I
	iconst_2
	bipush 8
	iastore
	getstatic MCClass/x [I
	iconst_3
	iconst_4
	iastore
	getstatic MCClass/x [I
	iconst_4
	bipush 9
	iastore
	getstatic MCClass/x [I
	iconst_5
	bipush 7
	iastore
	getstatic MCClass/x [I
	bipush 6
	iconst_1
	iastore
	getstatic MCClass/x [I
	bipush 7
	iconst_0
	iastore
	getstatic MCClass/x [I
	bipush 8
	iconst_4
	iastore
	getstatic MCClass/x [I
	bipush 9
	bipush 8
	iastore
	getstatic MCClass/x [I
	bipush 10
	bipush 7
	iastore
	getstatic MCClass/x [I
	bipush 11
	bipush 6
	iastore
	getstatic MCClass/x [I
	bipush 12
	iconst_5
	iastore
	getstatic MCClass/x [I
	bipush 13
	iconst_5
	iastore
	getstatic MCClass/x [I
	bipush 14
	bipush 9
	iastore
	getstatic MCClass/x [I
	bipush 15
	iconst_0
	iastore
	getstatic MCClass/x [I
	bipush 16
	iconst_4
	iastore
	getstatic MCClass/x [I
	bipush 17
	iconst_2
	iastore
	getstatic MCClass/x [I
	iconst_2
	iconst_3
	imul
	iconst_2
	imul
	iconst_1
	iconst_2
	imul
	iadd
	iconst_0
	iadd
	iaload
	getstatic MCClass/y [I
	iconst_0
	iaload
	imul
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
.limit locals 1
.end method
