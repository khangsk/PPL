.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	putstatic MPClass/a I
	bipush 100
	putstatic MPClass/b I
	getstatic MPClass/b I
	i2f
	getstatic MPClass/a I
	i2f
	fdiv
	getstatic MPClass/a I
	getstatic MPClass/b I
	invokestatic MPClass/foo(II)I
	i2f
	fcmpl
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	ldc "aH"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label5
Label4:
	ldc "Ha"
	invokestatic io/putString(Ljava/lang/String;)V
Label5:
	getstatic MPClass/a I
	invokestatic io/putInt(I)V
	getstatic MPClass/b I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static foo(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_2
Label2:
	iload_2
	iload_1
	if_icmpgt Label3
	iload_0
	iload_2
	imul
	iload_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	goto Label9
Label8:
	iconst_1
	ineg
	istore_1
	iload_1
	istore_0
	iload_2
	ireturn
Label9:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	iconst_0
	istore_1
	iload_1
	istore_0
	iconst_1
	ineg
	ireturn
Label1:
.limit stack 3
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
