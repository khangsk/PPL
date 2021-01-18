;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Tue Jan 05 14:02:41 ICT 2021

.source Test.java
.class public Test
.super java/lang/Object


.method public <init>()V
.limit stack 1
.limit locals 1
.var 0 is this LTest; from Label0 to Label1

Label0:
.line 1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return

.end method

.method public static main([Ljava/lang/String;)V
.limit stack 4
.limit locals 3
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [I from Label2 to Label1
.var 2 is b [I from Label4 to Label1

Label0:
.line 3
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	astore_1
Label2:
.line 4
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	astore_2
Label4:
.line 5
	aload_1
	astore_2
Label1:
.line 7
	return

.end method
