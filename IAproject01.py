def main():
    print("Hello user-->")
    answer = input()
    print("This program is designed to figure out if you like programing")
    print()
    print("And if it would be a good fit for you")
    print()
    print("But first, we would like to know your name.-->")
    name = input()
    print("Do you like programming {}? (yes or no)-->".format(name))
    answer0 = input().lower().strip()
    if answer0 == "yes":
        print("Great! You said {}!".format(answer0))
        print("We can't wait to teach you sone Python!-->")
    elif answer0 == "no":
        print("Hmm... You said {}?".format(answer0))
        print("Well we hope you change your mind once we start learning.-->")
    else:
        print("I do not understand what you mean by {}".format(answer0))
        def question():
            print("Do you like programming {}? (yes or no)-->".format(name))
            answer0 = input().lower().strip()
            if answer0 == "yes":
                print("Great! You said {}!".format(answer0))
                print("We can't wait to teach you some Python!-->")
            elif answer0 == "no":
                print("Hmm... You said {}?".format(answer0))
                print("Well we hope you change your mind once we start learning.-->")
            else:
                print("I do not understand what you mean by {}".format(answer0))
                question()
        question()
    answer = input()
    print("Before you go we have a few more questions {} -->".format(name))
    answer = input()
    print("What college are you going to {}? -->".format(name))
    answer1 = input()
    print("Now what highschool did you go to before coming to {}? -->".format(answer1))
    answer2 = input()
    print("which of the two did you like most? -->")
    answer3 = input()
    print("Amazing!")
    print()
    print("now i know that your name is {}".format(name))
    print("you go to {}".format(answer1))
    print("your highschool used to be {}". format(answer2))
    print("you liked {} the most".format(answer3))
    if answer0 == "yes":
        print("and that you like programing!-->")
    elif answer0 == "no":
        print("and that your not too fond of programing.-->")
    answer = input()
    print("well thats all the time we have now see you later!")

if __name__ == "__main__":
    main()
