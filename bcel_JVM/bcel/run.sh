#!/usr/bin/env bash

# Compile java source code to java bytecode
javac -g Test.java

# Disassemble bytecode to jasmin
java -cp .:bcel-5.2/bcel-5.2.jar JasminVisitor Test.class

# Remove class file and assemble jasmin to java bytecode
rm Test.class
java -jar jasmin.jar Test.j

# Run bytecode
java Test