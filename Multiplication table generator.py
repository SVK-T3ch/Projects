print('Welcome to the multiplication table generator!\nThis program will generate any table you would like to know.')

while True:
    q1 = input('Do you wanna continue? (y/n): ').lower()
    if q1 == 'n':
        print('Thanks for using the table generator!')
        exit()
    elif q1 != 'y':
        print('Please try again.')
        continue

    N = int(input('Enter the number of the table you want: '))
    n = int(input('Enter the number till which you want the table to last for (e.g. 10): '))

    print('\nNoted! Your table is the following:\n')
    for i in range(1, n + 1):
        print(f'{N} × {i} = {N * i}')

    q2 = input('\nWanna try again? (y/n): ').lower()
    if q2 == 'n':
        print('Thanks for using the program! Hope you had a great time :)')
        exit()

