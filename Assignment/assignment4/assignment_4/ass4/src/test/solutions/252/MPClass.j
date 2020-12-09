.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static x I
.field static n I
.field static m I
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
Label0:
	sipush 10007
	putstatic MPClass/m I
	iconst_1
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	iconst_4
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	bipush 15
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	bipush 27
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	bipush 79
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	sipush 128
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	sipush 9246
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	sipush 14942
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	sipush 29265
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	ldc 667999
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	ldc 1937815
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	ldc 6111917
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	ldc 59684905
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
	ldc 793800323
	ldc 2000000000
	invokestatic MPClass/pow(II)I
	invokestatic MPClass/ha_i_space(I)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static pow(II)I
.var 0 is x I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	iconst_1
	ireturn
Label5:
.var 2 is res I from Label6 to Label7
Label6:
	iload_0
	iload_1
	iconst_2
	idiv
	invokestatic MPClass/pow(II)I
	istore_2
	iload_2
	iload_2
	imul
	getstatic MPClass/m I
	irem
	istore_2
	iload_1
	iconst_2
	irem
	iconst_1
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	iload_2
	iload_0
	imul
	getstatic MPClass/m I
	irem
	istore_2
Label11:
	iload_2
	ireturn
Label7:
Label1:
.limit stack 6
.limit locals 3
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
	newarray int
	putstatic MPClass/a [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
