.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is condition Z from Label0 to Label1
Label0:
	iconst_0
	istore_1
	invokestatic io/printLn()V
	iload_1
	ifle Label3
	ldc "Not return first"
	invokestatic io/printStrLn(Ljava/lang/String;)V
	goto Label2
Label3:
	ldc "Return first"
	invokestatic io/printStrLn(Ljava/lang/String;)V
	return
Label2:
	ldc "This line should not be printed"
	invokestatic io/printStrLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
