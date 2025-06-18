#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, -1, -1):
        if i == 0:
            print("Happy New Year!")
        else:
            print(i)

def square_integers(int_list):
    squared_list = []
    for i in int_list:
        squared_list.append(i**2)
    return squared_list
    

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
