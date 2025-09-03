import random

print("Welcome to the DICE ROLLER!")

while True:
    input("Press enter to roll DICE...")
    dice = random.randint(1, 6)
    print(f"You rolled a DICE {dice}")
    
    choice = input("Rolled again? (y/n)")
    if (choice != 'y'):
        print("Thanks for playing!")
        break
    
    
    