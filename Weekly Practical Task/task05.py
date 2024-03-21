#Problem 5: Reverse a Number
"""Take an integer as input and reverse it. For example, if the input is 123, the output should be 321. Do not convert the number to a string. Perform the task using mathematical operations only."""

number  = 123456789
reverse = 0
while number != 0:
  digit = number % 10
  reverse = reverse *10 + digit
  number = number // 10
print("Reversed Number: ",reverse)