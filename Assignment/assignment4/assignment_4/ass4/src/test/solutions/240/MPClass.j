.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [I from Label0 to Label1
Label0:
	bipush 7
	newarray int
	astore_1
	aload_1
	iconst_5
	iconst_4
	isub
	iconst_5
	iastore
	iconst_4
	aload_1
	invokestatic MPClass/foo(I[I)V
	aload_1
	iconst_5
	iconst_4
	isub
	iaload
	invokestatic MPClass/ha_i_space(I)V
Label1:
	return
.limit stack 6
.limit locals 2
.end method

.method public static foo(I[I)V
.var 0 is i I from Label0 to Label1
.var 1 is a [I from Label0 to Label1
Label0:
	aload_1
	invokevirtual [I/clone()Ljava/lang/Object;
	checkcast [I
	astore_1
	aload_1
	iconst_5
	iconst_4
	isub
	iaload
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	iconst_5
	iconst_4
	isub
	bipush 8
	iastore
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
