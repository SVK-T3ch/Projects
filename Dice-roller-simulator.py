import random
print("Welcome to the dice roller")
while True:
 def roll_dice():
    number = random.randint(1, 6)
    print(f'The number you got is: {number}')
 roll_dice()
 retry = input("Do you want to try again? (y/n): ").lower()
 while retry not in ["y", "n"]:
    retry = input("Please enter y or n.\nDo you want to try again? (y/n): ").lower()
 if retry == "n":
    print("Thank you for using the program!")
    break