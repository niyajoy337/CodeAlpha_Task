import random

word_list = ["apple", "house", "pizza", "train", "robot"]
secret_word = random.choice(word_list).lower()
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

print("🎉 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while incorrect_guesses < max_guesses:
    print("\nWord:", display_word())
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong! You have {max_guesses - incorrect_guesses} guesses left.")

    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break
else:
    print("\n😢 Game Over! The word was:", secret_word)

