.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x I

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	bipush 12
	istore_1
	bipush 111
	putstatic MCClass/x I
	bipush 12
	ineg
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass/x I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method
