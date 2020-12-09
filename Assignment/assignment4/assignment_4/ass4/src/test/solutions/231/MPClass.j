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
.var 1 is n I from Label0 to Label1
Label0:
	bipush 10
	istore_1
Label2:
	iconst_1
	ifle Label3
.var 2 is i I from Label6 to Label7
Label6:
	iconst_1
	putstatic MPClass/a I
	iload_1
	putstatic MPClass/b I
	iload_1
	invokestatic MPClass/ha_i_space(I)V
	getstatic MPClass/a I
	istore_2
Label8:
	iload_2
	getstatic MPClass/b I
	if_icmpgt Label9
	getstatic MPClass/a I
	getstatic MPClass/b I
	invokestatic MPClass/mid(II)F
	invokestatic MPClass/ha_f_space(F)V
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label9:
Label11:
	iload_1
	iconst_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	goto Label15
Label14:
	goto Label5
Label15:
Label7:
	iload_1
	iconst_1
	isub
	istore_1
	invokestatic io/putLn()V
Label4:
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 5
.limit locals 3
.end method

.method public static mid(II)F
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	i2f
	iconst_2
	i2f
	fdiv
	freturn
Label1:
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
