q1 = input('Welcome to the prime number checker!\nThis program checks whether a number is prime or not.\nDo you wanna continue? [y/n]: ').lower()

if q1 == 'y':
    while True:
        q2 = int(input('Enter a number: '))
        if q2 <= 1:
            print('not a prime')
        else:
            for i in range(2, q2):
                if q2 % i == 0:
                    print('not a prime')
                    break
            else:
                print('prime')

        q3 = input('Do you wanna try again? [y/n]: ').lower()
        if q3 == 'n':
            print('Thank you for using this program!')
            break
        elif q3 != 'y':
            print('please enter either y or n')
elif q1 == 'n':
    print('Thanks for using this program!')
else:
    print('please enter either y or n')



