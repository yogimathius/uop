#!/bin/bash

# Create bin directory if it doesn't exist
mkdir -p bin

# Compile all Java files in current directory
javac -d bin *.java

# Run the program with the correct package path
java -cp bin cs1102.week3.studentmanagement.Main