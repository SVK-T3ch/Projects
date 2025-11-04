while True:
 q1 = int(input('Which converter do you want to use?\n Years->Months \n Months->Days\nDays->Hours\nHours->Minutes\nMinutes->Seconds\n(1/2/3/4/5)'))
 if q1 == 1:
    hours = float(input('Enter how many hours: '))
    minutes = hours*60
    print(f'That is {minutes} in total')
 if q1 == 4:
    hours = float(input('Enter how many hours: '))
    minutes = hours*60
    print(f'That is {minutes} minutes in total')
 if q1 == 1:
    years = float(input('Enter how many years: '))
    minutes = years*12
    print(f'That is {minutes} months in total')
 if q1 == 2:
    months = float(input('Enter how many months: '))
    minutes = months*30
    print(f'That is{minutes} days in total')
 if q1 == 3:
    days = float(input('Enter how many days: '))
    minutes = days*24
    print(f'That is {minutes} hours in total')
 if q1 == 5:
    hours = float(input('Enter how many minutes: '))
    minutes = hours*60
    print(f'That is {minutes} seconds in total')
 else:
    print('Try again')
 q2 = input('Wanna check again? (y/n): ').lower()
 if q2 == 'y':
     break
 elif q2 == 'n':
     print('Thanks for using the app!')
     exit()
 else:
     continue

