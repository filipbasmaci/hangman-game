import random
from Hangman_words import word_list
from Hangman_art import stages, logo

print(logo)
chosen_word = random.choice(word_list)

display = []
for i in chosen_word:
    display.append("_")

print("".join(display))

end_of_game = False
lives = 6

while end_of_game == False:
    guess = input("Take a guess:").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1



    print("".join(display))

    print(stages[lives])

    if not "_" in display:
        end_of_game = True
        print("You won!")

    elif lives == 0:
        end_of_game = True
        print("You lost!")
        print(f"The word was {chosen_word}")