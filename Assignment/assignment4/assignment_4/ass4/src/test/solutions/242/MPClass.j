.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [F from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	bipush 7
	newarray float
	astore_1
	iconst_4
	istore_2
Label2:
	iload_2
	bipush 10
	if_icmpgt Label3
	aload_1
	iload_2
	iconst_4
	isub
	iload_2
	iload_2
	imul
	i2f
	fastore
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	aload_1
	invokestatic MPClass/foo([F)V
	invokestatic io/putLn()V
	iconst_4
	istore_2
Label6:
	iload_2
	bipush 10
	if_icmpgt Label7
	aload_1
	iload_2
	iconst_4
	isub
	faload
	invokestatic MPClass/ha_f_space(F)V
Label8:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label7:
Label9:
Label1:
	return
.limit stack 6
.limit locals 3
.end method

.method public static foo([F)V
.var 0 is a [F from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	aload_0
	invokevirtual [F/clone()Ljava/lang/Object;
	checkcast [F
	astore_0
	iconst_4
	istore_1
Label2:
	iload_1
	bipush 10
	if_icmpgt Label3
	aload_0
	iload_1
	iconst_4
	isub
	faload
	invokestatic MPClass/ha_f_space(F)V
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	iconst_4
	istore_1
Label6:
	iload_1
	bipush 10
	if_icmpgt Label7
	aload_0
	iload_1
	iconst_4
	isub
	iload_1
	iload_1
	iadd
	i2f
	fastore
Label8:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label6
Label7:
Label9:
	iconst_4
	istore_1
Label10:
	iload_1
	bipush 10
	if_icmpgt Label11
	aload_0
	iload_1
	iconst_4
	isub
	faload
	invokestatic MPClass/ha_f_space(F)V
Label12:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label10
Label11:
Label13:
Label1:
	return
.limit stack 6
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
