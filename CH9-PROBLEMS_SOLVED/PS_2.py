import random

def game():
    print(" you are playing tha game...")
    score = random.randint(1,50)
    # Fetch the hiscore 
    with open("highscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=" "):
           hiscore = int(hiscore)

        else:
            hiscore = 0

        print(f"your score: {score}")
        if(score>hiscore):

        # write this hiscore to file
          with open("highscore.txt","w") as f:
            f.write(str(score))

        return score

game()



