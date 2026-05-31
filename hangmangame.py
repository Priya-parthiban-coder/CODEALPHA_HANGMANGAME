
import random

def play_word_rescue():
    words = ["PUZZLE", "ROCKET", "GARDEN", "WIZARD", "CASTLE"]
    word = random.choice(words).upper()
    guessed, wrong = [], 0
    stages = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
    ]

    print("--- WORD RESCUE ---")
    while wrong < 6:
        print(stages[wrong])
        print("Word: " + " ".join([l if l in guessed else "_" for l in word]))
        guess = input("Guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed:
            guessed.append(guess)
            if guess not in word:
                wrong += 1
            if all(l in guessed for l in word):
                print(f"Victory! The word was {word}")
                return
    print(stages[6] + f"\nGame Over! The word was {word}")

if __name__ == "__main__":
    play_word_rescue()
