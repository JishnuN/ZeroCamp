#Problem 7: Count Vowels and Consonants
#Count the number of vowels and consonants in a given string.

word = input('Word: ')
vowels = {'a':0,'e':0,'i':0,'o':0,'u':0}
consonants = dict()
for w in word:
  if w in vowels:
    vowels[w] = vowels[w] + 1
  else:
    if w not in consonants:
      consonants[w] = 1
    else:
      consonants[w]=consonants[w]+1
    
print('''Vowels: 
      a = {0}
      e = {1}
      i = {2}
      o = {3}
      u = {4}
      '''.format(vowels['a'],vowels['e'],vowels['i'],vowels['o'],vowels['u']))
print('Consonants :',consonants)