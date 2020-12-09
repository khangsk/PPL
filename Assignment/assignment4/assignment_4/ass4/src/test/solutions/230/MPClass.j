.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static x F
.field static y F
.field static u Z
.field static v Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	bipush 10
	invokestatic MPClass/updateha(II)V
	getstatic MPClass/a I
	invokestatic MPClass/ha_i_space(I)V
	getstatic MPClass/b I
	invokestatic MPClass/ha_i_space(I)V
	getstatic MPClass/x F
	invokestatic MPClass/ha_f_space(F)V
	getstatic MPClass/y F
	invokestatic MPClass/ha_f_space(F)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static updateha(II)V
.var 0 is ha1 I from Label0 to Label1
.var 1 is ha2 I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	putstatic MPClass/a I
	iload_0
	iload_1
	isub
	putstatic MPClass/b I
	getstatic MPClass/a I
	getstatic MPClass/b I
	iadd
	i2f
	putstatic MPClass/x F
	getstatic MPClass/a I
	getstatic MPClass/b I
	isub
	i2f
	putstatic MPClass/y F
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static ha_i_space(I)V
.var 0 is ha0852i I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static ha_f_space(F)V
.var 0 is ha0852f F from Label0 to Label1
Label0:
	fload_0
	invokestatic io/putFloat(F)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static ha_b_space(Z)V
.var 0 is ha0852b Z from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putBool(Z)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static ha_str_1()Ljava/lang/String;
Label0:
	ldc "0852 1"
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static ha_str_2()Ljava/lang/String;
Label0:
	ldc "0852 2"
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static ha_str_3()Ljava/lang/String;
Label0:
	ldc "0852 3"
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
