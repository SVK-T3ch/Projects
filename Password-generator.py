import random
import string
print("Welcome to Password Generator")
print("This program generates you a random safe password that can not be brute forced")
input("Press Enter to continue...")
while True:
 length = random.randint(10, 15)
 characters = string.ascii_letters + string.digits + string.punctuation
 password = ''.join(random.choices(characters, k=length))
 print(f'Here is your password: {password}')
 while True:
  again = input('Do wanna generate another password? (y/n): ').lower()
  if again == 'y':
     break
  elif again == 'n':
     print('Thank you for using the Password Generator')
     exit()
  else:
     print('Please enter y or n')



