import random
Comp3 = {1: 'Rock', 2: 'Paper', 3: 'Scissor'}
def rps(user):
    cp = random.randint(1, 3)
    print(f"Computer picked: {cp} ({Comp3[cp]})")
    if (cp == 1 and user == 2) or \
       (cp == 2 and user == 3) or \
       (cp == 3 and user == 1):
        print("You win!")
    elif cp == user:
        print("Tie!")
    else:
        print("You lose!")
print("Welcome to the Rock Paper Scissor game!")
while True:
    user = int(input("Pick one!\n1) Rock\n2) Paper\n3) Scissor\nYour choice: "))
    while user not in [1, 2, 3]:
        print("Invalid input.")
        user = int(input("Your choice: "))
    rps(user)
    retry = input("Do you want to try again? (y/n): ").lower()
    while retry not in ['y', 'n']:
        print("Invalid input.")
        retry = input("Do you want to try again? (y/n): ").lower()
    if retry == 'n':
        print("Thanks for using the program! Hope you enjoyed it!")
        break

