import math
print('===== Welcome to the Power and Square Root Finder =====')

while True:
    number = float(input('Enter a number: '))

    choice = input(
        '1) Do you want to find number raised to the nth power?\n'
        '2) Do you want to find the nth root of the number?\n'
        'Your choice [1/2]: '
    )

    # Power calculation
    if choice == '1':
        exponent = float(input(f'Enter the exponent you want to raise {number} to: '))
        output = number ** exponent
        print(f'{number} raised to the power {exponent} is: {output}')

    # Root calculation
    elif choice == '2':
        root = float(input(f'Enter the root you want to find (Example: 2 for square root): '))
        if root == 0:
            print("Root cannot be zero.")
        else:
            output = number ** (1 / root)
            print(f'The {root} root of {number} is: {output}')

    else:
        print('Invalid choice. Please select 1 or 2.')

    # Continue
    while True:
     again = input('Do you want to try again? (y/n): ').lower()
     if again == 'n':
        print('Thank you for using the program!')
        exit()
     elif again == 'y':
         break
     else:
         print('Please enter y/n')
