.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "True"
	invokestatic io/bool_of_string(Ljava/lang/String;)Z
	ifle Label3
	ldc "Dung roi"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label3:
	ldc "Sai roi"
	invokestatic io/print(Ljava/lang/String;)V
Label2:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
