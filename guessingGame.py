import random
guess=random.randint(1,9)
print ("Welcome to the number guessing game")
chances=0
while chances < 5:
    chances+=1
    number = int(input("Guess a number between 1-9"))
    if guess == number:
        print("CONGRATULATIONS! You got it!", chances)
        break 
    elif guess>number:
        print ("You guessed too low")
    elif guess<number:
        print("Your guess was too high")

if not chances < 5:
    print("YOU LOSE. The number is", number)
