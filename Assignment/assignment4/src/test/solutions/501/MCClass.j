.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic io/printLn()V
	ldc "Hello "
	invokestatic io/print(Ljava/lang/String;)V
	ldc "World"
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
