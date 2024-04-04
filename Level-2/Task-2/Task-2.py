import random

def number_guessing(low, high):
    secret_number = random.randint(low, high)
    guess = None
    attempts = 0

    print(f"Guess the number between {low} and {high}.")

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

st = int(input("Enter the starting Sequence to play Game : "))
end = int(input("Enter the Ending Sequence to play Game : "))
number_guessing(st,end)

# Finished