.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
Label0:
	ldc 0.0
	fstore_1
	fload_1
	ldc 5.0
	fadd
	fstore_1
	fload_1
	ldc 10.0
	fsub
	fstore_1
	fload_1
	ldc 2.0
	fneg
	fmul
	fstore_1
	fload_1
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	fload_1
	ldc 1.0
	fadd
	fstore_1
	fload_1
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	fload_1
	ldc 2.0
	fdiv
	fstore_1
	fload_1
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
