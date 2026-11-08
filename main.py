
import random

# ==========================================
# CODEALPHA PYTHON PROGRAMMING INTERNSHIP
# PROJECT 1: HANGMAN GAME
# ==========================================

WORDS = ["PYTHON", "APPLE", "CODING", "COMPUTER", "DEVELOPER"]

MAX_ATTEMPTS = 6

HANGMAN_STAGES = [
    """
       +---+
           |
           |
           |
          ===
    """,
    """
       +---+
       O   |
           |
           |
          ===
    """,
    """
       +---+
       O   |
       |   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|   |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\\  |
           |
          ===
    """,
    """
       +---+
       O   |
      /|\\  |
      /    |
          ===
    """,
    """
       +---+
       O   |
      /|\\  |
      / \\  |
          ===
    """
]


def display_welcome():
    print("\n" + "=" * 45)
    print("              HANGMAN GAME")
    print("       CodeAlpha Python Internship")
    print("=" * 45)

    print("\nGuess the hidden word one letter at a time!")
    print(f"You have {MAX_ATTEMPTS} incorrect attempts.")


def display_game(secret_word, guessed_letters,
                 wrong_guesses, attempts):

    print(HANGMAN_STAGES[attempts])

    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Word:", display_word)

    all_guesses = guessed_letters | wrong_guesses

    print(
        "Guessed letters:",
        ", ".join(sorted(all_guesses)) or "None"
    )

    print("Incorrect attempts:", attempts)
    print("Remaining attempts:", MAX_ATTEMPTS - attempts)


def play_game():

    secret_word = random.choice(WORDS)

    guessed_letters = set()
    wrong_guesses = set()

    attempts = 0

    while attempts < MAX_ATTEMPTS:

        display_game(
            secret_word,
            guessed_letters,
            wrong_guesses,
            attempts
        )

        print("\nEnter a letter: ", end="", flush=True)

        guess = input().strip().upper()

        # Validate input
        if not guess.isalpha() or len(guess) != 1:
            print("\nInvalid input! Enter only one alphabet.")
            continue

        # Check repeated guesses
        if guess in guessed_letters or guess in wrong_guesses:
            print("\nYou already guessed that letter. Try again!")
            continue

        # Check the guessed letter
        if guess in secret_word:

            guessed_letters.add(guess)
            print("\nCorrect guess!")

            # Check winning condition
            if all(letter in guessed_letters for letter in secret_word):

                display_game(
                    secret_word,
                    guessed_letters,
                    wrong_guesses,
                    attempts
                )

                print("\nCongratulations! You won!")
                print("The correct word was:", secret_word)
                return

        else:

            wrong_guesses.add(guess)
            attempts += 1

            print("\nWrong guess! Try another letter.")

    # Losing condition
    display_game(
        secret_word,
        guessed_letters,
        wrong_guesses,
        attempts
    )

    print("\nGame Over!")
    print("The correct word was:", secret_word)


def main():

    display_welcome()

    while True:

        play_game()

        print("\nWould you like to play again? (yes/no): ", end="", flush=True)

        choice = input().strip().lower()

        if choice not in ("yes", "y"):
            print("\nThank you for playing Hangman!")
            print("Project developed for CodeAlpha Internship.")
            break


if __name__ == "__main__":
    main()
