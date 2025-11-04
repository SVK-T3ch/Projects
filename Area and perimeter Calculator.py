#Area and perimeter calculator

while True:
 print('Welcome to the Area and Perimeter calculator!')
 q = input('Is it a Square, Rectangle, Triangle or Cirle? (s/r/t/c)')
 #Square
 if q == 's':
    q2 = float(input('Enter the length of side: '))
    As = q2*q2
    Ps = q2*4
    print('The area and perimeter of the square are respectively',As,'and',Ps)
 elif q == 'r':
    q3 = float(input('Enter the length: '))
    q4 = float(input('Enter the breath: '))
    Ar = q3*q4
    Pr = q3+q4+q3+q4
    print('The area and perimeter of the Rectangle are respectively',Ar,'and',Pr)
 elif q == 't':
    q5 = float(input('Enter the base: '))
    q6 = float(input('Enter the height: '))
    q7 = float(input('Enter the length of 1st side: '))
    q8 = float(input('Enter the length of 2nd side: '))
    q9 = float(input('Enter the length of 3rd side: '))
    At = 1/2*q5*q6
    Pt = q7 + q8 + q9
    print('The area and perimeter of the Triangle are respectively', At, 'and', Pt)
 elif q == 'c':
    q10 = float(input('Enter the radius: '))
    Ac = 3.1415*q10*q10
    Pc = 3.1415*2*q10
    print('The area and circumference of the Circle are respectively', Ac, 'and', Pc)
 else:
    print('Error,please try again')
 while True:
  q11 = input('Would you like to try it again? (y/n)')
  if q11 == 'y':
     break
  elif q11 == 'n':
      print('Thanks for using the app!')
      exit()
  else:
      print('Try again.')






