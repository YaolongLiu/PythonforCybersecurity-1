#!/usr/bin/env python3

first_name=float(input("What is the first number: "))
activity = input("What activity? ( + - * / )")
second_num = float(input("What is the second number: "))

if activity == "+":
    print(first_name + second_num)  
if activity == "-":
    print(first_name - second_num)
if activity == "*":
    print(first_name * second_num)
if activity == "/":
    print(first_name / second_num)