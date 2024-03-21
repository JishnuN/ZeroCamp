#Problem 1:Sum of Numbers
#Write a program to find the sum of all numbers from 1 to a given number.

num = input("enter a number: ")
try :
  number = int(num)
except :
  number = -1
if number <=0:
  print('enter a valid number')
else:
  a = list()
total = 0
while total <= number:
  a.append(total)
  total = total+1
result = sum(a)
print('adding 1 to ',number)
print('total: ',result)
