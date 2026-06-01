import random

HANGMAN = [
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

words = [
    "python",
    "apple",
    "computer",
    "laptop",
    "gaming",
    "keyboard",
    "internet",
    "software",
    "database",
    "monitor"
]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("=" * 40)
print("🎮 WELCOME TO HANGMAN GAME")
print("=" * 40)

while wrong_guesses < max_guesses:

    print(HANGMAN[wrong_guesses])

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Lives Left:", max_guesses - wrong_guesses)
    print("Guessed Letters:", guessed_letters)

    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter only one alphabet!")
        continue

    if guess in guessed_letters:
        print("⚠ Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong Guess!")

if wrong_guesses == max_guesses:
    print(HANGMAN[6])
    print("\n💀 GAME OVER!")
    print("Correct Word:", word)

print("\n🎮 Thanks for playing!")