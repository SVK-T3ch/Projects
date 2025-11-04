while True:
 marks=[]
 print('Welcome to grade calculator!\nThis program calculates your percentage and grades it out of A,B,C,D,F\nPlease note that these grades may not be accepted in your country')
 q1 = input('Enter the name of the student: ')
 q2 = int(input('Enter the amount of subjects: '))
 for i in range(1,q2+1):
    while True:
     Marks = float(input(f'Enter the marks of the subject number {i} (0-100): '))
     if 0 <= Marks <= 100:
        marks.append(Marks)
        break
     else:
        print('Please try again.')
 tm = sum(marks)
 P = round((tm/(q2*100))*100,2)
 print(f'{q1} has secured a percentage of {P}')

 if P >= 90:
    grade = "A+"
 elif P >= 80:
    grade = "A"
 elif P >= 70:
    grade = "B"
 elif P >= 60:
    grade = "C"
 elif P >= 50:
    grade = "D"
 elif P >= 40:
    grade = "E"
 else:
    grade = "F"

 print(f"{q1}'s Final Grade is: {grade}")
 while True:
  q3 = input('Wanna try again? (y/n)').lower()
  if q3 == 'y':
    break
  elif q3 == 'n':
      print(f'Thanks for using the program! Hope you had a great time using it {q1}/User:) ')
      exit()
  else:
      print('Please try again')






