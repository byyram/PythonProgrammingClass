import random

rand_one = random.randint(1,1001)

while rand_one != 0:

    guess = int(input("Guess my number between 1 and 1000 with the fewest guesses:"))

    if guess < rand_one:
        print("Too low. Try again.")

    if guess > rand_one:
        print("Too high. Try again.")

    if guess == rand_one:
        print("Congratulations. You guessed the number!")
        break
