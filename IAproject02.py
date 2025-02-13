def question():
    print("Q1: What is your name?")
    name = input()
    if name == "exit":
        exit()
    print("Q2: What is your favorite car {}?".format(name))
    answer = input()
    if answer == "exit":
        exit()
    print("Q3: what genre of music do you listen to the most {}?".format(name))
    answer = input()
    if answer == "exit":
        exit()
    print("Q4: ")
    answer = input()
    if answer == "exit":
        exit()
    question()
def main():
    print("Welcome user!")
    print()
    print("I will ask you 4 questions and repeat them over and over until")
    print("you type the word exit")
    print()
    print("I will also keep track of how many times you answered a queston")
    print("as well as keep track of how many times you went through a full loop")
    question()
def exit():
    print("You answered {count} questions!")
    quit()
if __name__ == "__main__":
    main()
