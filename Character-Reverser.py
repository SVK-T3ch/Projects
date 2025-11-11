print('Welcome to the Character Reverser\nThis app reverses a set of alphabets or numbers.')
while True:
 n = input('Enter a set of characters: ')
 nr = n[::-1]
 print(f'The following is your input reversed - {nr}')
 while True:
  q2 = input('Do you want to try again? [Y/n]: ').lower()
  if q2 == 'n':
      print('Thank you for using the program!')
      exit()
  elif q2 == 'y':
      break
  else:
      print('Thank you for using the program!')