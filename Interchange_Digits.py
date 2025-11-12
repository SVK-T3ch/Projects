print('Welcome!')
print('This program interchanges the digits of a two digit numbers! More updates coming soon!')
while True:
 n = int(input('Enter a number two digit number: '))
 if 10 <= n <= 99:
    print('Noted!')
 while n <= 9:
    n = int(input('Please enter a number between 10 and 99: '))
 while n >= 100:
    n = int(input('Please enter a number between 10 and 99: '))
 a = n // 10
 b = n % 10
 swapped = b * 10 + a
 print('Your number interchanged is: ', swapped)
 while True:
  q = input('Would you like to try again? [Y/n]: ').lower()
  if q == 'n':
     print('Thank you for using this program!')
     exit()
  elif q == 'y':
     break
  else:
     print('Please enter a valid input')