.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b F
.field static arr [I
.field static isTrue Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MPClass/isTrue Z
	getstatic MPClass/isTrue Z
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 2
.limit locals 1
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
	iconst_5
	newarray int
	putstatic MPClass/arr [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
