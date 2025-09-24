import random 

def game():
    print(".....You are playing game.....\n")
    score = random.randint(1, 100)
    with open("game.txt") as f:
        highScore = f.read()
        if(highScore != ""):
            highScore = int(highScore)
        else:
            highScore = 0
    print(f"Your score is {score}")
    if(score > highScore):
        with open("game.txt", "w") as f:
            f.write(str(score))
    return score
    
game()