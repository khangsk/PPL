.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/str_ha_1()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	invokestatic MPClass/str_ha_2()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	invokestatic MPClass/str_ha_3()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	invokestatic MPClass/str_ha_4()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	invokestatic MPClass/str_ha_5()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static str_ha_1()Ljava/lang/String;
Label0:
	ldc "Ha 1"
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static str_ha_2()Ljava/lang/String;
Label0:
	ldc "Ha 2"
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static str_ha_3()Ljava/lang/String;
Label0:
	ldc "Ha 3"
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static str_ha_4()Ljava/lang/String;
Label0:
	ldc "Ha 4"
	areturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static str_ha_5()Ljava/lang/String;
Label0:
	ldc "Ha 5"
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
