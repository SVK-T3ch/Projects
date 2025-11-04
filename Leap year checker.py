
print('Welcome to the leap year checker!\nThis program checks with a year is a leap year.')
while True:
 q1 = int(input('Please enter the year to check whether it is leap year or not: '))
 if q1 % 4 == 0:
    print('The year you entered is a Leap Year!')
 else:
    print('The year you entered is a Standard year(NOT a Leap Year)')
 q2 = input('Would you like to try it again? (y/n): ').lower()
 while True:
  if q2 == 'y':
    break
  elif q2 == 'n':
    print('Thanks for using the app! Hope you enjoyed your time')
    exit()
  else:
      print('Please Try again')