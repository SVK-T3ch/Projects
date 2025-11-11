while True:
 q1 = int(input("Welcome to the multiples printer,This program prints the multiples of a number of user's choice\nPlease enter a number: "))
 if q1%1 == 0:
    n = int(input('Please enter the limit of how many multiples should the program print: '))
    for i in range(1,n+1):
        print(q1*i)
 else:
    print('Please enter a valid input')
 while True:
  q2 = input('Do you wanna try again? [y/n]: ').lower()
  if q2 == 'y':
     break
  elif q2 == 'n':
     print('Thank you for using this program!')
     exit()
  else:
     print('Please enter a valid input')


