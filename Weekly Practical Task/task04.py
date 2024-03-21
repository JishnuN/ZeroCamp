#Problem 4: Factorial Calculation
#Calculate the factorial of a given number using a loop.

print('Fractorial Calculator')
num = input('enter a number: ')
try:
  num = int(num)
except:
  num = -1
if num <1:
  print('enter a valid number')
else:
  a=1
  b=1
  while b <= num:
    a = a*b
    b = b+1
  print('n! = ',a)
