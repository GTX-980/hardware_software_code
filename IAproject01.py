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
    print("Do you like programming {}? (yes or no)-->".format(name))
    answer = input()
    if answer == "yes":
        print("Great! You said {}!".format(answer))
        print("We can't wait to teach you sone Python!-->")
    else:
        print("Hmm... You said {}?".format(answer))
        print("Well we hope you change your mind once we start learning.-->")
    answer = input()
    print("Before you go we have a few more questions {} -->".format(name))
    answer = input()

if __name__ == "__main__":
    main()
