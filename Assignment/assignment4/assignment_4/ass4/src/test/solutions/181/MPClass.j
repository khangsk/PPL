.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
Label0:
	bipush 10
	iconst_5
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_1
	iload_1
	invokestatic io/putBoolLn(Z)V
	invokestatic MPClass/foo()Z
	istore_1
	iload_1
	invokestatic io/putBoolLn(Z)V
	invokestatic MPClass/bar()V
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static foo()Z
Label0:
	bipush 10
	iconst_5
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	putstatic MPClass/a Z
	getstatic MPClass/a Z
	ifgt Label5
	iconst_1
	ifgt Label5
	iconst_0
	goto Label4
Label5:
	iconst_1
Label4:
	ireturn
Label1:
.limit stack 7
.limit locals 0
.end method

.method public static bar()V
Label0:
	getstatic MPClass/a Z
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 1
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
