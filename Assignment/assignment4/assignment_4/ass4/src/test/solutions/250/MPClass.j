.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static n I
.field static m I
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	ldc 50000
	putstatic MPClass/n I
	ldc 1000000009
	putstatic MPClass/m I
	getstatic MPClass/a [I
	iconst_1
	iconst_0
	isub
	iconst_1
	iastore
	getstatic MPClass/a [I
	iconst_2
	iconst_0
	isub
	iconst_2
	iastore
	iconst_3
	istore_1
Label2:
	iload_1
	getstatic MPClass/n I
	if_icmpgt Label3
	getstatic MPClass/a [I
	iload_1
	iconst_0
	isub
	iconst_3
	getstatic MPClass/a [I
	iload_1
	iconst_1
	isub
	iconst_0
	isub
	iaload
	imul
	getstatic MPClass/m I
	irem
	iconst_4
	getstatic MPClass/a [I
	iload_1
	iconst_2
	isub
	iconst_0
	isub
	iaload
	imul
	getstatic MPClass/m I
	irem
	isub
	getstatic MPClass/m I
	iadd
	getstatic MPClass/m I
	irem
	iastore
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	invokestatic MPClass/ha_check_arr()I
	invokestatic MPClass/ha_i_space(I)V
	iconst_1
	getstatic MPClass/n I
	invokestatic MPClass/sort(II)V
	invokestatic MPClass/ha_check_arr()I
	invokestatic MPClass/ha_i_space(I)V
Label1:
	return
.limit stack 7
.limit locals 2
.end method

.method public static sort(II)V
.var 0 is l I from Label0 to Label1
.var 1 is r I from Label0 to Label1
.var 2 is x I from Label0 to Label1
.var 3 is i I from Label0 to Label1
.var 4 is j I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	return
Label5:
	iload_0
	iload_1
	iadd
	iconst_2
	idiv
	istore_2
	iload_0
	istore_3
	iload_1
	istore 4
Label8:
	iload_3
	iload 4
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label9
Label14:
	getstatic MPClass/a [I
	iload_3
	iconst_0
	isub
	iaload
	getstatic MPClass/a [I
	iload_2
	iconst_0
	isub
	iaload
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label15
	iload_3
	iconst_1
	iadd
	istore_3
Label16:
	goto Label14
Label15:
Label17:
Label20:
	getstatic MPClass/a [I
	iload 4
	iconst_0
	isub
	iaload
	getstatic MPClass/a [I
	iload_2
	iconst_0
	isub
	iaload
	if_icmple Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label21
	iload 4
	iconst_1
	isub
	istore 4
Label22:
	goto Label20
Label21:
Label23:
	iload_3
	iload 4
	if_icmpgt Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifgt Label26
	goto Label27
Label26:
.var 5 is tmp I from Label28 to Label29
Label28:
	getstatic MPClass/a [I
	iload_3
	iconst_0
	isub
	iaload
	istore 5
	getstatic MPClass/a [I
	iload_3
	iconst_0
	isub
	getstatic MPClass/a [I
	iload 4
	iconst_0
	isub
	iaload
	iastore
	getstatic MPClass/a [I
	iload 4
	iconst_0
	isub
	iload 5
	iastore
Label29:
	iload_3
	iconst_1
	iadd
	istore_3
	iload 4
	iconst_1
	isub
	istore 4
Label27:
Label10:
	goto Label8
Label9:
Label11:
	iload_0
	iload 4
	invokestatic MPClass/sort(II)V
	iload_3
	iload_1
	invokestatic MPClass/sort(II)V
Label1:
	return
.limit stack 16
.limit locals 6
.end method

.method public static ha_check_arr()I
.var 0 is i I from Label0 to Label1
Label0:
.var 1 is res I from Label2 to Label3
Label2:
	iconst_0
	istore_1
	iconst_1
	istore_0
Label4:
	iload_0
	getstatic MPClass/n I
	if_icmpgt Label5
	iload_1
	getstatic MPClass/a [I
	iload_0
	iconst_0
	isub
	iaload
	iload_0
	imul
	getstatic MPClass/m I
	irem
	iadd
	getstatic MPClass/m I
	irem
	istore_1
Label6:
	iload_0
	iconst_1
	iadd
	istore_0
	goto Label4
Label5:
Label7:
	iload_1
	ireturn
Label3:
Label1:
.limit stack 4
.limit locals 2
.end method

.method public static ha_log_arr()V
.var 0 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_0
Label2:
	iload_0
	getstatic MPClass/n I
	if_icmpgt Label3
	getstatic MPClass/a [I
	iload_0
	iconst_0
	isub
	iaload
	invokestatic MPClass/ha_i_space(I)V
Label4:
	iload_0
	iconst_1
	iadd
	istore_0
	goto Label2
Label3:
Label5:
	invokestatic io/putLn()V
Label1:
	return
.limit stack 3
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
