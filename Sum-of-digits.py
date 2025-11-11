print('Welcome to the Sum of Digits Calculator\nThis program calculates the sum of all the digits of a number\nPlease note that it does not calculate the sum of digits of any decimal number')
while True:
 n = input('enter a number: ')
 sd = 0
 for d in n:
    sd += int(d)
 print(f'The sum of the digits of {n} is {sd}')
 while True:
  q2 = input('Do you want to calculate again? [y/n]: ').lower()
  if q2 == 'y':
    break
  elif q2 == 'n':
    print('Thanks for using this program!')
    exit()
  else:
    print('please enter either y or n')