import random
aiNumber = random.randint(1, 100); playerGuess = 0; playerAttempts = 1;
print("I guessed a number between 1 and 100, try to guess it")
while True:
    try:
        playerGuess = int(input("Guess my number (-1234 to quit): "))
    except ValueError:
        print("Thats not a proper answer dude ;-;")
        continue
        if playerGuess == -1234:
            print(f"Thanks for playing! My number was {aiNumber}, and you had {playerAttempts} attempts!"); break
        if playerGuess < aiNumber:
            print("Its higher than that."); playerAttempts += 1
        if playerGuess > aiNumber:
            print("Its lower than that."); playerAttempts += 1
        if playerGuess == aiNumber and playerAttempts == 0:
            print(f"OMG YOU GOT MY NUMBER {aiNumber} IN ONE ATTEMPT??? GET THE CAMERA THIS ACTUALLY IS VERY LUCKY OMG :O"); break
        if playerGuess == aiNumber:
            print(f"You got my number! It was {aiNumber}, and you had {playerAttempts} attempts!")
