print('Welcome to the Interest Calculator💵💲!')
while True:
 q1 = int(input('Do you wanna calculate Simple Interest or Compound Interest🤔? (1/2): '))
 if q1 == 1:
    p = float(input('Enter the principal: '))
    t =  float(input('Enter the time(in years): '))
    r  = float(input('Enter the rate of interest % : '))
    si = round((p*r*t)/100,2)
    a = round(si+p,2)
    c = input('Enter the currency (eg-USD,INR): ')
    print(f'Your Simple Interest is {si} {c} and Total Amount is {a} {c}')

 elif q1 == 2:
    P = float(input('Enter the principal: '))
    T =  float(input('Enter the time(in years): '))
    R  = float(input('Enter the rate of interest % : '))
    A = round(P*((1+R/100)**T),2)
    CI = round(A - P,2)
    C = input('Enter the currency (eg-USD,INR): ')
    print(f'Your Compound Interest is {CI} {C} and the Total Amount is {A} {C}')
 else:
     print('Please try again')
 while True:
  q2 = input('Do you wanna run the program again? (y/n): ').lower()
  if q2 == 'y':
      break
  elif q2 == 'n':
      print('Thanks for using the program! Hope you enjoyed your time with it!👋')
      exit()
  else:
      print('Please try again')




