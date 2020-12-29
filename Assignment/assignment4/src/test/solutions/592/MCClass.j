.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args Ljava/lang/String; from Label0 to Label1
.var 1 is r F from Label0 to Label1
Label0:
	ldc 10.0
	fstore_1
	ldc "The tich hinh cau ban kinh r = "
	invokestatic io/print(Ljava/lang/String;)V
	fload_1
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc " la: "
	invokestatic io/print(Ljava/lang/String;)V
	fload_1
	invokestatic MCClass/theTich(F)F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static theTich(F)F
.var 0 is r F from Label0 to Label1
Label0:
	ldc 4.0
	ldc 3.0
	fdiv
	ldc 3.14
	fmul
	fload_0
	fmul
	fload_0
	fmul
	fload_0
	fmul
	freturn
Label1:
.limit stack 2
.limit locals 1
.end method
