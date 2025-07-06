#!/usr/bin/env python3
def is_prime(n):
    # less then 2 is not a prime
    if n<2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print("Prime numbers between 1 and 100:")

count = 0
for n in range(2, 101):
    if is_prime(n):
        print(n, end=' ')
#         count+=1
#         if count % 10 == 0:
#             print()
# if count % 10 != 0:
#     print()
print()
