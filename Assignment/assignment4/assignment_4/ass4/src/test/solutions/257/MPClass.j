.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static n I
.field static a [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	bipush 20
	putstatic MPClass/n I
	iconst_1
	istore_1
Label2:
	iload_1
	getstatic MPClass/n I
	if_icmpgt Label3
	getstatic MPClass/a [F
	iload_1
	iconst_0
	isub
	iload_1
	iload_1
	iconst_1
	iadd
	imul
	iload_1
	iconst_2
	iadd
	imul
	i2f
	bipush 6
	i2f
	fdiv
	fastore
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	getstatic MPClass/a [F
	invokestatic MPClass/ha_log_arr([F)V
	getstatic MPClass/a [F
	iconst_3
	bipush 8
	ldc 1.9
	invokestatic MPClass/setrange([FIIF)[F
	iconst_5
	bipush 15
	ldc 4.6
	invokestatic MPClass/setrange([FIIF)[F
	iconst_1
	getstatic MPClass/n I
	iconst_5
	isub
	ldc 1000.00001
	invokestatic MPClass/setrange([FIIF)[F
	invokestatic MPClass/ha_log_arr([F)V
Label1:
	return
.limit stack 6
.limit locals 2
.end method

.method public static setrange([FIIF)[F
.var 0 is a [F from Label0 to Label1
.var 1 is l I from Label0 to Label1
.var 2 is r I from Label0 to Label1
.var 3 is v F from Label0 to Label1
.var 4 is i I from Label0 to Label1
Label0:
	aload_0
	invokevirtual [F/clone()Ljava/lang/Object;
	checkcast [F
	astore_0
	iload_1
	istore 4
Label2:
	iload 4
	iload_2
	if_icmpgt Label3
	aload_0
	iload 4
	iconst_0
	isub
	fload_3
	fastore
Label4:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label2
Label3:
Label5:
	aload_0
	areturn
Label1:
.limit stack 6
.limit locals 5
.end method

.method public static ha_log_arr([F)V
.var 0 is a [F from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	aload_0
	invokevirtual [F/clone()Ljava/lang/Object;
	checkcast [F
	astore_0
	iconst_1
	istore_1
Label2:
	iload_1
	getstatic MPClass/n I
	if_icmpgt Label3
	aload_0
	iload_1
	iconst_0
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
	invokestatic io/putLn()V
Label1:
	return
.limit stack 3
.limit locals 2
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
	ldc 100001
	newarray float
	putstatic MPClass/a [F
Label1:
	return
.limit stack 1
.limit locals 0
.end method
