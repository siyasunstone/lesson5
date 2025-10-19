import random

number = random.randint(1, 100)
attempts = 0
guess = 0

while guess != number and attempts < 3:
    guess = int(input("Enter a number: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")
4
# after the loop ends, check why
if guess != number:
    print("😢 You used all 3 tries. You lose! The number was", number)
















































