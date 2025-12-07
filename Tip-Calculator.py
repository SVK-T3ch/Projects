print('Welcome to the Tip Calculator!')
print('This program calculates tip out of the total charge')
input("Press Enter to continue...")


def tip():
    while True:
        ba = float(input('Enter the total bill: '))
        q = input('Do you wanna calculate\n1) Tip percentage\n2) Tip amount\nYour choice [1/2] : ')

        if q == '1':
            ta = float(input("Enter the tip amount: "))
            tp = (ta / ba) * 100
            print('Your tip percentage is:', tp)

        elif q == '2':
            tp = float(input("Enter the tip percentage: "))
            ta = ba * (tp / 100)
            print('Your tip amount is:', ta)

        else:
            print('Please enter either 1 or 2!')
            continue

        retry = input('Do you wanna retry again? [Y/n] : ').lower()
        if retry == 'n':
                print("Thank you for using the program!")
                break

        while retry not in ['y','n']:
                print('Please enter a valid input')
                retry = input('Do you wanna retry again? [Y/n] : ')



tip()
