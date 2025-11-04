while True:
 q = int(input('Welcome to BMI Calculator!\nWould you prefer metric system (kg and cm) or Imperial system? (pounds and feet inches)\n (1/2): '))
 if q == 1:
    w = float(input('Enter your weight in Kilograms: '))
    h = float(input('Enter height in cm: '))
    bmi = w/((h/100)**2)
    print('Your BMI is :',bmi)
 elif q == 2:
    W =  float(input('Enter your weight in pounds: '))
    F = int(input('How many feet tall are you?(NOT INCHES,ONLY FEET): '))
    I = float(input('How many inches tall are you in that nth feet?: '))
    i = (F*12)+I
    BMI = (703*W)/(i**2)
    print('Your BMI is :',BMI)
 else:
    print('Try again')
    continue
 while True:
  q2 = input('Would you like to try again? (y/n)')
  if q2 == 'y':
      break
  elif q2 == 'n':
      print('Thanks for using the app :)')
      exit()
  else:
      print('Try again')


