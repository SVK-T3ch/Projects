#Made by svk-t3ch
print('Welcome to the Basic Login System! ')
Login_Details = []
while True:
 while True:
  q = input('Would you like to login or register? [L/R]: ').lower()
  if q == 'l':
    print("You haven't registered yet ")
    q = input('Would you like to try again? [Y/n]: ').lower()
    if q == 'n':
        print('Thanks for using the app! Hope you enjoyed it!')
        exit()
    elif q == 'y':
        break
  elif q == 'r':
    Username = input('Please enter your username: ')
    Login_Details.append(Username)
    Password = input('Please enter your password: ')
    Login_Details.append(Password)
    Password_recheck = input('Please enter your password again: ')
    if Password == Password_recheck:
        print(f'Welcome, You are successfully logged in {Username} !')
    while Password != Password_recheck:
        Password_recheck = input('Uh oh! Both of them did not match,Please enter your password again: ')
        if Password == Password_recheck:
            print(f'Welcome, You are successfully logged in {Username} !')
    while True:
     q2 = input('Now you can change your password or Logout [P/L] (More Features coming soon!):').lower()
     if q2 == 'p':
        NewPassword = input('Please enter your new password: ')
        Login_Details.remove(Password)
        Login_Details.append(NewPassword)
        print(f'Password changed successfully!')
     elif q2 == 'l':
        print('Thanks for using the app! Hope you enjoyed it!')
        exit()
     else:
        print('Please enter a valid input')



