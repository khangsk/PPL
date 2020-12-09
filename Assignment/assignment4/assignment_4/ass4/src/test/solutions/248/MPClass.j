.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static n I
.field static m I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	ldc 100001
	newarray int
	astore_1
	sipush 10000
	putstatic MPClass/n I
	ldc 1000000009
	putstatic MPClass/m I
	aload_1
	iconst_0
	iconst_0
	isub
	iconst_1
	iastore
	aload_1
	iconst_1
	iconst_0
	isub
	iconst_2
	iastore
	iconst_2
	istore_2
Label2:
	iload_2
	getstatic MPClass/n I
	if_icmpgt Label3
	aload_1
	iload_2
	iconst_0
	isub
	aload_1
	iload_2
	iconst_1
	isub
	iconst_0
	isub
	iaload
	aload_1
	iload_2
	iconst_2
	isub
	iconst_0
	isub
	iaload
	iadd
	getstatic MPClass/m I
	irem
	iastore
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	aload_1
	sipush 1597
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	sipush 10946
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 1346269
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 165580141
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 784974805
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 337007687
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 807526340
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 147860051
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 274044507
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 203070066
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 150716683
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 992750503
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 453021451
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 941642764
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 163684284
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 564665913
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
	aload_1
	ldc 102915696
	invokestatic MPClass/indexof([II)I
	invokestatic MPClass/ha_i_space(I)V
Label1:
	return
.limit stack 6
.limit locals 3
.end method

.method public static indexof([II)I
.var 0 is a [I from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is i I from Label0 to Label1
Label0:
	aload_0
	invokevirtual [I/clone()Ljava/lang/Object;
	checkcast [I
	astore_0
	iconst_0
	istore_2
Label2:
	iload_2
	getstatic MPClass/n I
	if_icmpgt Label3
	aload_0
	iload_2
	iconst_0
	isub
	iaload
	iload_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	goto Label9
Label8:
	iload_2
	ireturn
Label9:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	iconst_1
	ineg
	ireturn
Label1:
.limit stack 3
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
