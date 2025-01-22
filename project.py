import random


def Message():

    print("")
    print("Welcome to Wordle\n")
    print("A random word has been generated and you have 5 GUESSES")
    print("There are THREE levels:")
    print("Level 1: Guess a three letter word")
    print("Level 2: Guess a four letter word")
    print("Level 3: Guess a five+ letter word\n")

    valid = False
    while valid == False:
        level = int(input("Choose your level: "))
        if level in [1, 2, 3]:
            level += 2
            print()
            return level
        else:
            print("Pick a valid level")


def random_word(level):

    # Randomly choose a word from the 5-letter words list
    with open("words.txt", "r") as file:
        temp = file.read().splitlines()

    # Filter the list for 5-letter words
    if level != 5:
        words = [word for word in temp if len(word) == level]
        answer = random.choice(words)
        print("The length of the word is " + str(level))
    else:
        words = [word for word in temp if len(word) >= 5]
        answer = random.choice(words)
        print("The length of the word is " + str(len(answer)))

    return answer


def letter(word):

    letters = []
    for i in word:
        letters.append(i)

    return letters


def end():

    valid = False
    while valid == False:
        retry = input("Do you want to try again? (Y/N):").lower()
        if retry != "y" and retry != "n":
            print("Please enter N or Y")
        else:
            valid = True
    if retry == "n":
        exit()
    else:
        print("_" * 65)
        main()


def main():

    # print the message
    level = Message()
    # get the random number
    answer = random_word(level)
    length = len(answer)

    for i in range(5):

        # Make sure the right amount of letters are inputted
        valid = False
        while valid == False:
            words = input("Guess " + str(i+1) + ": ").lower()
            if len(words) != length or words.isalpha() == False:
                print("Incorrect word length/ only use letters \n")
            else:
                valid = True

        letters = letter(answer)
        word = list(words)
        # Right letter in the right position
        for j in range(length):
            if answer[j] == words[j]:
                letters.remove(word[j])
                word[j] = "\033[32m" + words[j] + "\033[0m"

        # Right letter but wrong position
        for j in range(length):
            if words[j] in answer and words[j] in letters and words[j] != answer[j]:
                letters.remove(word[j])
                word[j] = "\033[38;5;214m" + words[j] + "\033[0m"

        print("".join(word))
        # check if the user has won
        if answer == words:
            print("Congratulations!!! You guessed the word")
            print("You won in " + str(i+1) + " guesses!" )
            end()

    print("You lost... Better luck next time")
    print("The word was " + str(answer))
    end()
main()
