print('==== Welcome to the HCF and LCM calculator! ====')
while True:
 # numbers
 n1 = int(input('Enter the first number: '))
 n2 = int(input('Enter the second number: '))

 # HCF using Euclid's Algorithm
 a, b = n1, n2
 while b != 0:
    a, b = b, a % b
 hcf = a

 print(f'The HCF of the numbers {n1} and {n2} is {hcf}')

 # LCM
 lcm = (n1 * n2) // hcf
 print(f'The LCM of the numbers {n1} and {n2} is {lcm}')

 # again
 while True:
  again = input('Would you like to try again ? (Y/n): ').lower()
  if again == 'y':
    break
  elif again == 'n':
    print('Thank you for using HCF and LCM calculator!')
    exit()
  else:
    print('Please enter a valid input')


