.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is y F from Label0 to Label1
Label0:
	ldc 0.0
	fstore_1
	ldc 2.0
	fneg
	fstore_1
	fload_1
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method
