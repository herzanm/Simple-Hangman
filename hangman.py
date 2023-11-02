# Write your code here
import random


def menu():
    wins = 0
    losses = 0
    while True:
        choice = (input("""Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: """))
        if choice == 'play':
            if play_game(8):
                wins += 1
            else:
                losses += 1
        elif choice == "results":
            print(f"You won: {wins} times.")
            print(f"You lost: {losses} times.")
        else:
            exit(1)


def check_winner(word, current):
    if word == current:
        return True
    else:
        return False


def play_game(attempts):

    words = ["python", "java", "swift", "javascript"]
    answer = random.choice(words)
    letters = set(answer)
    counter = 0

    hidden_word = '-' * len(answer)
    guessed_letters = set()

    while attempts > 0:
        print()
        print(hidden_word)
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("Please, input a single letter.")
            continue
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        if guess not in guessed_letters:
            guessed_letters.add(guess)
        else:
            print(f"You've already guessed this letter.")
            continue
        if guess in letters:
            for i in answer:
                if i == guess:
                    hidden_word = list(hidden_word)
                    hidden_word[counter] = i
                    hidden_word = "".join(hidden_word)
                counter += 1
            counter = 0
            if check_winner(answer, hidden_word):
                print()
                print(answer)
                print(f"""You guessed the word {answer}!
You survived!""")
                return True
        else:
            attempts -= 1
            print(f"That letter doesn't appear in the word. # {attempts} attempts\n")
    print(hidden_word)
    print("You lost!")
    return False


menu()
