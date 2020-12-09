.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static isTrue Z
.field static arr [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is isT Z from Label0 to Label1
.var 2 is isF Z from Label0 to Label1
Label0:
	getstatic MPClass/arr [Z
	iconst_3
	iconst_1
	isub
	iconst_0
	bastore
	getstatic MPClass/arr [Z
	iconst_2
	iconst_1
	isub
	getstatic MPClass/arr [Z
	iconst_3
	iconst_1
	isub
	baload
	bastore
	getstatic MPClass/arr [Z
	iconst_1
	iconst_1
	isub
	getstatic MPClass/arr [Z
	iconst_2
	iconst_1
	isub
	baload
	bastore
	getstatic MPClass/arr [Z
	iconst_1
	iconst_1
	isub
	baload
	ifgt Label3
	iconst_1
	goto Label2
Label3:
	iconst_0
Label2:
	istore_1
	getstatic MPClass/arr [Z
	iconst_2
	iconst_1
	isub
	baload
	ifgt Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	ifgt Label7
	iconst_1
	goto Label6
Label7:
	iconst_0
Label6:
	istore_2
	iload_2
	ifgt Label9
	iconst_1
	goto Label8
Label9:
	iconst_0
Label8:
	ifgt Label11
	iconst_1
	goto Label10
Label11:
	iconst_0
Label10:
	ifgt Label13
	iconst_1
	goto Label12
Label13:
	iconst_0
Label12:
	ifgt Label15
	iconst_1
	goto Label14
Label15:
	iconst_0
Label14:
	ifgt Label17
	iconst_1
	goto Label16
Label17:
	iconst_0
Label16:
	ifgt Label19
	iconst_1
	goto Label18
Label19:
	iconst_0
Label18:
	putstatic MPClass/isTrue Z
	getstatic MPClass/isTrue Z
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 29
.limit locals 3
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
	iconst_4
	newarray boolean
	putstatic MPClass/arr [Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
