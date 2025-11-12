N = []
print('Welcome to the program!')
print('This program evaluates and tells what is the highest magnitude number out of the users input')
while True:
  q1 = int(input('Out of how many numbers do you want the program to find the greatest number?: '))
  while q1 >= 2:
     print('Noted!')
     break
  while q1 <= 1:
      print('Please enter a valid input')
      q1 = int(input('Out of how many numbers do you want the program to find the greatest number?: '))
  for i in range(1,q1+1):
     n = float(input(f'Enter number {i}: '))
     N.append(n)
  print('The greatest number out of all the inputs you have entered is:', max(N))
  while True:
   q2 = input('Wanna try again? [Y/n]: ').lower()
   if q2 == 'n':
     print('Thank you for using this program! Hope you had good time using it!')
     exit()
   elif q2 == 'y':
     break
   else:
     print('Please enter a valid input')