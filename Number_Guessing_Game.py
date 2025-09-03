import random

print("\n-----WELCOME TO A NUMBER GUESSING GAME!-----")

while True:
    guess = int(input("\nPlease Guess a Number between '1' and '100':"))
    random_number = random.randint(1, 100)
    if (guess > random_number):
        print("Your guess is HIGH!")
    elif(guess < random_number):
        print("Your guess is LOW!")
    else:
        print("please guess number between '1' to '100' ")
    print("Correct number is: ", random_number)
    
    choice = input("If you want to quit this game, Enter 'quit'")
    if(choice == 'quit'):
        print("Thanks for playing!")
        break
    
