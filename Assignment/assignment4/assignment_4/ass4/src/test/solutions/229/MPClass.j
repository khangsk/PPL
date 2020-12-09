.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/ha_str_func()Ljava/lang/String;
	bipush 9
	invokestatic MPClass/ha_str_proc(Ljava/lang/String;I)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static ha_str_proc(Ljava/lang/String;I)V
.var 0 is ha Ljava/lang/String; from Label0 to Label1
.var 1 is times I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_2
Label2:
	iload_2
	iload_1
	if_icmpgt Label3
	aload_0
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	invokestatic io/putIntLn(I)V
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static ha_str_func()Ljava/lang/String;
Label0:
	ldc "Ha "
	areturn
Label1:
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
