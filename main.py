import random  # <-- Import the random module

def number_guessing_game():
    """Interactive number guessing game with statistics."""
    print("=== NUMBER GUESSING GAME ===")
    print("I'm thinking of a number between 1 and 100!")

    games_played = 0
    total_attempts = 0

    while True:
        # Generate random number
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10

        print(f"\n🎯 New Game! You have {max_attempts} attempts.")

        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
                attempts += 1

                if guess == secret_number:
                    print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                    break
                elif guess < secret_number:
                    remaining = max_attempts - attempts
                    print(f"📈 Too low! {remaining} attempts remaining.")
                else:
                    remaining = max_attempts - attempts
                    print(f"📉 Too high! {remaining} attempts remaining.")

                # Give hints based on how close they are
                if attempts > 5:
                    difference = abs(guess - secret_number)
                    if difference <= 5:
                        print("🔥 You're very close!")
                    elif difference <= 10:
                        print("🌡️  Getting warmer!")

            except ValueError:
                print("Please enter a valid number!")
                continue
        else:
            print(f"💀 Game over! The number was {secret_number}")

        # Update statistics
        games_played += 1
        total_attempts += attempts

        # Show statistics
        avg_attempts = total_attempts / games_played
        print(f"\n📊 Statistics: Games: {games_played}, Average attempts: {avg_attempts:.1f}")

        # Play again?
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("👋 Thanks for playing!")

if __name__ == "__main__":
    number_guessing_game()
