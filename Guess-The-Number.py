import random

print('Welcome to Guess the Number aka GTN!')
print('In this GTN, you have to guess the secret number. I dare you to do it in less than 3 attempts!')

while True:
    n = random.randint(1, 1000)
    attempts = 0

    while True:
        g = int(input('Guess the Number (0–1000): '))
        attempts += 1

        if g == n:
            print(f'You guessed it in {attempts} attempts! 🔥')
            break
        elif g > n:
            print('Your guess is too high 😤')
        else:
            print('Your guess is too low 😅')

    q2 = input('Wanna try again? [y/n]: ').lower()
    if q2 != 'y':
        print('Thanks for playing, legend ✌️')
        break