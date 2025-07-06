#!/usr/bin/env python3

passwords=[
    "W4$acxyH7BtQiU3er",
    "Zk7i$F8uo#Aq",
    "L#1npOdATe2rjy",
    "vE@XsLwzKmy",
    "cBa6Hg7@uY3WjR",
    "QpiTcS7Ozlk2"
]

print("Password Reversal Results: ")
for pwd in passwords:
    r_pwd = pwd[::-1]
    print(f"Original: {pwd}")
    print(f"Reversed: {r_pwd}")
    print()
