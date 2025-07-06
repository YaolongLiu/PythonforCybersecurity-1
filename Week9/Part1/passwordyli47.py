#!/usr/bin/env python3

passwords=[
    "W4$acxyH7BtQiU3er",
    "Zk7i$F8uo#Aq",
    "L#1npOdATe2rjy",
    "vE@XsLwzKmy",
    "cBa6Hg7@uY3WjR",
    "QpiTcS7Ozlk2"
]

for pwd in passwords:
    errors = []

    # check length
    if len(pwd) < 6:
        errors.append("too short (min 6)")
    elif len(pwd) > 16:
        errors.append("too long (max 16)")

    # check lowercase
    if not any(c.islower() for c in pwd):
        errors.append("missing a lowercase letter")

    # check uppercase 
    if not any(c.isupper() for c in pwd):
        errors.append("missing an uppercase letter")

    # check digital
    if not any(c.isdigit() for c in pwd):
        errors.append("missing a digit")

    # check special char
    if not any(c in '$#@' for c in pwd):
        errors.append("missing a special character ($#@)")

    
    print(f"{pwd}: ", end="") # end="" means not change line in the end
    if not errors:
        print("Correct.")
    else:
        print("Incorrect because " + ", ".join(errors)) # use space to list all 