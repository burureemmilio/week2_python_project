import random

def save_score(username, difficulty, score):
    file = open("scores.txt", "a")
    file.write(f"{username},{difficulty},{score}\n")
    file.close()


def play_game(difficulty, max_attempts):
    attempts = 0
    number = random.randint(1, 100)

    print(f"\nThis is the {difficulty} level, you have {max_attempts} attempts")

    while attempts < max_attempts:
        guess = int(input("Enter your guess between 1 and 100: "))
        attempts += 1

        if guess < number:
            print(f"Low, try a higher number. You have {max_attempts - attempts} attempts remaining")

        elif guess > number:
            print(f"High, try a lower number. You have {max_attempts - attempts} attempts remaining")

        else:
            print("Congrats! You guessed correctly")

            score = max_attempts - attempts + 1
            return score

    print(f"You ran out of guesses. The correct number was {number}")
    return 0


print("--WELCOME TO THE GUESSING GAME--")

username = input("Enter your username: ")

print("Choose the level of difficulty")
difficulty = input("A: Hard B: Medium C: Easy (A, B or C): ").lower()

if difficulty != "a" and difficulty != "b" and difficulty != "c":
    print("Invalid choice")

elif difficulty == "a":
    difficulty_name = "Hard"
    score = play_game(difficulty_name, 5)

    save_score(username, difficulty_name, score)

    print(f"\n{username}, your score is {score}")
    print("Score saved successfully!")

elif difficulty == "b":
    difficulty_name = "Medium"
    score = play_game(difficulty_name, 7)

    save_score(username, difficulty_name, score)

    print(f"\n{username}, your score is {score}")
    print("Score saved successfully!")

else:
    difficulty_name = "Easy"
    score = play_game(difficulty_name, 10)

    save_score(username, difficulty_name, score)

    print(f"{username}, your score is {score}")
    print("Score saved successfully!")