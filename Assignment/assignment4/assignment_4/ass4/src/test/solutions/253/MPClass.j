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
	iconst_1
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/ha_i_space(I)V
	iconst_1
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/ha_i_space(I)V
	iconst_1
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/ha_i_space(I)V
	iconst_1
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/ha_i_space(I)V
	iconst_1
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/ha_i_space(I)V
	iconst_1
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/inc(I)I
	invokestatic MPClass/ha_i_space(I)V
Label1:
	return
.limit stack 1
.limit locals 3
.end method

.method public static inc(I)I
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 1
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
