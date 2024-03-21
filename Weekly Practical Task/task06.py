#Problem 6: Palindrome Check
#Write a program to check if a given string is a palindrome (reads the same forwards and backward).

word = input("Enter a word: ")
reverse = word[::-1]
print(reverse)
if word == reverse:
  print('its a palindrome')
else:
  print('not a palindrome')