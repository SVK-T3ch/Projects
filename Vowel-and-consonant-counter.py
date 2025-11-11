#Code by SVK-T3CH
print('Welcome to the vowel and consonant counter,the program counts the amount of vowels and consonants a sentence has.')
print("Example- The word 'hello' has 2 vowels and 3 consonants. ")
print('Let us start')
while True:
 q = int(input('Would you like to use vowel counter or consonant counter [1/2]: '))
 if q == 1:
  q1 = input('Please a enter a word or sentence: ')
  vowels = 'aeiouAEIOU'
  count = 0
  for characters in q1:
    if characters.isalpha() and characters in vowels:
     count += 1
  print(f'The input you have entered has the following amount of vowels: {count}')
 elif q == 2:
  q1 = input('Please a enter a word or sentence: ')
  vowels = 'aeiouAEIOU'
  count = 0
  for characters in q1:
    if characters.isalpha() and characters not in vowels:
     count += 1
  print(f'The input you have entered has the following amount of consonants: {count}')
 else:
     print('Try again')
 while True:
  q2 = input('Would you like to try again? [Y/n]: ').lower()
  if q2 == 'n':
    print('Thank you for using this program')
    exit()
  elif q2 == 'y':
    break
  else:
    print('Try again')