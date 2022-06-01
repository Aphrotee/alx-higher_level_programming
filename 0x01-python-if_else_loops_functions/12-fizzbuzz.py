#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 61):
        if (i % 3 == 0) and (i % 5 == 0):
            print("Fizzbuzz ", end="")
        elif (i % 3):
            print("Fizz ", end="")
        elif (i % 5):
            print("Buzz ", end="")
