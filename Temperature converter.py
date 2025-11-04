while True:
 q1 = float(input('Enter the magnitude of your current temperature: '))
 q2 = input('Enter the unit in which the above temperature is measured in (k/f/c): ')
 while q2 not in ('k', 'f', 'c'):
    q2 = input('Enter the unit in which the above temperature is measured in (k/f/c): ')
 q3 = input('To which unit do you want to convert the above temperature to? (k/f/c)')
 while q3 not in ('k', 'f', 'c'):
    q3 = input('To which unit do you want to convert the above temperature to? (k/f/c)')
 if q2 == q3 == 'c':
    print(f'Your converted temperature is {q1} degrees celsius')
 elif q2 == q3 == 'k':
    print(f'Your converted temperature is {q1} degrees kelvin')
 elif q2 == q3 == 'f':
    print(f'Your converted temperature is {q1} degrees fahrenheit')
 elif q2 == 'k' and q3 == 'f':
    f = (q1-273.15)*(9/5)+32
    print(f'Your converted temperature is {f} degrees fahrenheit')
 elif q2 == 'k' and q3 == 'c':
    c = q1-273.15
    print(f'Your converted temperature is {c} degrees of temperature')
 elif q2 == 'c' and q3 == 'k':
    k = q1+273.15
    print(f'Your converted temperature is {k} degrees of kelvin')
 elif q2 == 'c' and q3 == 'f':
    f = (q1*9/5)+32
    print(f'Your converted temperature is {f} degrees of fahrenheit')
 elif q2 == 'f' and q3 == 'c':
    c = (q1-32)*5/9
    print(f'Your converted temperature is {c} degrees of celsius')
 elif q2 == 'f' and q3 == 'k':
    k = (q1-32)*5/9+273.15
    print(f'Your converted temperature is {k} degrees of kelvin')
 while True:
  q4 = input('Wanna run the program again? (y/n): ')
  if q4 == 'y':
      break
  elif q4 == 'n':
      print('Thanks for using the program!')
      exit()
  else:
      continue
