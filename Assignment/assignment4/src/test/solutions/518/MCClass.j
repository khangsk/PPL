.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is x Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	ldc 10.12
	ldc 9.5
	fcmpl
	ifeq Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
	ldc 10.5
	ldc 10.0
	fcmpl
	ifle Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label9
	iconst_1
	goto Label8
Label9:
	iconst_0
Label8:
	ifle Label7
	ldc 2.0001
	fneg
	ldc 2.0
	fneg
	fcmpl
	ifge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label7
	iconst_1
	goto Label6
Label7:
	iconst_0
Label6:
	ifle Label5
	ldc 90.1
	ldc 90.1
	fcmpl
	iflt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	ifle Label3
	ldc 12.0
	fneg
	ldc 12.0
	fneg
	fcmpl
	ifgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label3
	iconst_1
	goto Label2
Label3:
	iconst_0
Label2:
	istore_1
	iload_1
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 24
.limit locals 2
.end method
