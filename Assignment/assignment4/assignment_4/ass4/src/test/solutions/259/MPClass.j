.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [Ljava/lang/String; from Label0 to Label1
Label0:
	sipush 2001
	anewarray java/lang/String
	astore_1
.var 2 is a [Ljava/lang/String; from Label2 to Label3
Label2:
	sipush 2001
	anewarray java/lang/String
	astore_2
Label3:
Label1:
	return
.limit stack 1
.limit locals 3
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
	sipush 2001
	anewarray java/lang/String
	putstatic MPClass/a [Ljava/lang/String;
Label1:
	return
.limit stack 1
.limit locals 0
.end method
