import random

secret_no = random.randint(1, 100)
guess = 1

while guess != secret_no:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    if guess < secret_no:
        print("Too low! Try again.")
    elif guess > secret_no:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number:", secret_no)
        break
