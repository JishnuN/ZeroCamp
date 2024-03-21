#Problem 9: FizzBuzz
#Print numbers from 1 to a given number. For multiples of 3, print "Fizz," for multiples of 5, print "Buzz," and for numbers that are multiples of both 3 and 5, print "FizzBuzz."

num = 30
a = 1
while a <= num:
  if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
  elif a % 3 == 0:
    print('Fizz')
  elif a % 5 == 0:
    print('Buzz')
  else:
    print(a)
  a = a+1

