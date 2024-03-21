#Problem 1:Sum of Numbers
#Write a program to find the sum of all numbers from 1 to a given number.

num = input('enter a number: ')
num = int(num) + 1
result = 0
for i in range(num):
  result += i
print(result)
