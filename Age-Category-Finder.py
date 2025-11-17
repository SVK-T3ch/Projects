# M A D E   B Y   SVK-T3CH.
# H O P E  Y O U  E N J O Y  T H E  C O D E!
print('Welcome to the Age category finder!')
print("It is a basic program that tells you your generation and what age group you fall into!")
while True:
 generation = {
    "Gen Alpha": (0, 12),
    "Gen Z": (13, 28),
    "Millennials": (29, 44),
    "Gen X": (45, 60),
    "Boomers": (61, 79),
    "Silent Generation": (80, 97),
    "Greatest Generation": (90, 200)
 }
 age_category = {
    "Child": (0, 12),
    "Teen": (13, 17),
    "Young Adult": (18, 35),
    "Adult": (36, 59),
    "Senior": (60, 200)
 }
 age = int(input('What is your age? (In Years) : '))
 while age <= -1:
    age = int(input('Learn counting bro🥀,try again: '))
 while age >= 200:
     age = int(input('No one is that old😭,try again : '))
 for age_cat,(low,high) in age_category.items():
    if low <= age <= high:
        print('Your age category is:', age_cat)
        break

 for gen,(low,high) in generation.items():
    if low <= age <= high:
        print('Your generation is:', gen)
        break
 while True:
  q = input('Would you like to try again?? (Y/n) : ').lower()
  if q == 'n':
    print('Thank you for your time!')
    exit()
  elif q == 'y':
    break
  else:
    print('PLease type y or n')