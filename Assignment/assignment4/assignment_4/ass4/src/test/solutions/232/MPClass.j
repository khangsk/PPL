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
	invokestatic MPClass/ha0852_proc()V
Label1:
	return
.limit stack 0
.limit locals 2
.end method

.method public static ha0852_proc()V
.var 0 is i I from Label0 to Label1
.var 1 is j I from Label0 to Label1
Label0:
	iconst_1
	istore_0
Label2:
	iload_0
	bipush 10
	if_icmpgt Label3
	iconst_1
	istore_1
Label6:
	iload_1
	bipush 10
	if_icmpgt Label7
	iload_0
	bipush 10
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	iload_1
	iconst_5
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label16
	goto Label17
Label16:
	return
Label17:
	iload_0
	invokestatic MPClass/ha_i_space(I)V
Label8:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label6
Label7:
Label9:
Label4:
	iload_0
	iconst_1
	iadd
	istore_0
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 8
.limit locals 2
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
