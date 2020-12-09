.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static z I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b [Ljava/lang/String; from Label0 to Label1
.var 2 is e I from Label0 to Label1
.var 3 is x F from Label0 to Label1
.var 4 is z Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	anewarray java/lang/String
	astore_1
	ldc "?? :D ??"
	astore 4
	aload 4
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 5
.end method

.method public static foo()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
