.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [Z from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	bipush 7
	newarray boolean
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
	iconst_3
	idiv
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label9
	iload_2
	iconst_3
	idiv
	iconst_5
	if_icmple Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label9
	iconst_0
	goto Label8
Label9:
	iconst_1
Label8:
	bastore
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	aload_1
	invokestatic MPClass/foo([Z)V
	invokestatic io/putLn()V
	iconst_4
	istore_2
Label12:
	iload_2
	bipush 10
	if_icmpgt Label13
	aload_1
	iload_2
	iconst_4
	isub
	baload
	invokestatic MPClass/ha_b_space(Z)V
Label14:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label12
Label13:
Label15:
Label1:
	return
.limit stack 13
.limit locals 3
.end method

.method public static foo([Z)V
.var 0 is a [Z from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	aload_0
	invokevirtual [Z/clone()Ljava/lang/Object;
	checkcast [Z
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
	baload
	invokestatic MPClass/ha_b_space(Z)V
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
	iconst_3
	idiv
	iconst_3
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label13
	iload_1
	iconst_3
	idiv
	iconst_5
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label13
	iconst_0
	goto Label12
Label13:
	iconst_1
Label12:
	ifgt Label17
	iconst_1
	goto Label16
Label17:
	iconst_0
Label16:
	bastore
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
Label18:
	iload_1
	bipush 10
	if_icmpgt Label19
	aload_0
	iload_1
	iconst_4
	isub
	baload
	invokestatic MPClass/ha_b_space(Z)V
Label20:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label18
Label19:
Label21:
Label1:
	return
.limit stack 16
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
