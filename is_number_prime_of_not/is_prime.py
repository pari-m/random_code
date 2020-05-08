#Simple program to check if a number is prime or not


import math
print("Enter the number to check if it is prime or not")

a = int(input())

isprime = 0

for test in range(2,int(math.sqrt(a))):
	if a % test == 0:
		isprime = 1
	

if isprime == 1:
	print('number is not  prime')

if isprime == 0:
	print('number is prime')
