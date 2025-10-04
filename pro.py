import random

number = random.randint(1, 100)
attempts = 0
guess = 0

while guess != number and attempts < 12:
    guess = int(input("Enter a number: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")

# after the loop ends, check why
if guess != number:
    print("😢 You used all 12 tries. You lose! The number was", number)



