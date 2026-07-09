def guess_number():
    secret_number = 7
    guess = -1

    while guess != secret_number:
        guess = int(input("Guess the number (1-10): "))

        if guess == secret_number:
            print("🎉 Congratulations! You guessed the correct number.")
        else:
            print("❌ Wrong guess. Try again!")

guess_number()