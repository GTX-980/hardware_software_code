def question(answer_count, loop_count):
    print("Q1: What is your name?")
    name = input()
    if name == "exit":
        exit(answer_count, loop_count)
    answer_count += 1
    print("Q2: What is your favorite car {}?".format(name))
    answer = input()
    if answer == "exit":
        exit(answer_count, loop_count)
    answer_count += 1  # Increment answer count
    print("Q3: What genre of music do you listen to the most {}?".format(name))
    answer = input()
    if answer == "exit":
        exit(answer_count, loop_count)
    answer_count += 1  # Increment answer count
    print("Q4: would you be willing to answer all of these again?")
    answer = input().lower()
    if answer == "exit":
        exit(answer_count, loop_count)
    elif answer == "no":
        print("well too bad we're doing this again lol.")
    elif answer == "yes":
        print("oh you said yes? well good for you lets start over")
    answer_count += 1  # Increment answer count

    loop_count += 1  # Increment loop count after a full loop
    question(answer_count, loop_count)  # Recursive call with updated counts

def exit(answer_count, loop_count):
    print(f"You answered {answer_count} questions!")
    print(f"You completed {loop_count} full loops!")
    quit()

def main():
    print("Welcome user!")
    print()
    print("I will ask you 4 questions and repeat them over and over until")
    print("you type the word exit")
    print()
    print("I will also keep track of how many times you answered a question")
    print("as well as keep track of how many times you went through a full loop")
    question(0, 0)  # Initialize the counters when starting the question loop

if __name__ == "__main__":
    main()
