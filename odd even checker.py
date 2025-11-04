while True:
    a = int(input('Enter a whole number to check if it’s odd or even: '))

    if a % 2 == 0:
        print('Even number')
    else:
        print('Odd number')

    while True:
        q = input('Would you like to use this program again? (y/n): ').lower()
        if q == 'y':
            break  # go back to the main loop
        elif q == 'n':
            print('Thanks for using this program, have a great day!')
            exit()
        else:
            print('Invalid input. Please type y or n.')
