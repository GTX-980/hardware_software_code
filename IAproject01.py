def question():
    print("Do you like programming {}? (yes or no)-->".format(name))
    answer = input().lower().strip()
    if answer == "yes":
        print("Great! You said {}!".format(answer))
        print("We can't wait to teach you sone Python!-->")
    elif answer == "no":
        print("Hmm... You said {}?".format(answer))
        print("Well we hope you change your mind once we start learning.-->")
    else:
        print("I do not understand what you mean by {}".format(answer))
        question()
    answer = input()
def main():
    print("Hello user-->")
    answer = input()
    print("This program is designed to figure out if you like programing")
    print()
    print("And if it would be a good fit for you")
    print()
    print("But first, we would like to know your name.-->")
    name = input()
    print("Great!")
    print()
    question()
    print("Before you go we have a few more questions {} -->".format(name))
    answer = input()

if __name__ == "__main__":
    main()
