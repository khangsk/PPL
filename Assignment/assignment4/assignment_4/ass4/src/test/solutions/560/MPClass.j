.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static arr [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is isTrue Z from Label0 to Label1
Label0:
	ldc 11.0
	fstore_1
	bipush 11
	istore_2
	fload_1
	iload_2
	i2f
	fcmpl
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_3
	iload_3
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 3
.limit locals 4
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
	iconst_4
	newarray float
	putstatic MPClass/arr [F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
