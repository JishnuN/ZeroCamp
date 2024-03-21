#Problem 8: Multiplication Table
# Print the multiplication table for a given number.

num = input('Enter a Number: ')
num = int(num)
m = 1 
while m <= 10:
  result = m * num
  print( num, 'X', m, '=', result)
  m = m+1
cont = input("continue? y/n : ")
if cont.lower() == 'y':
  m2 = input('upto: ')
  m2 = int(m2)
  while m <= m2:
    result = m * num
    print( num, 'X', m, '=', result)
    m = m+1
  

