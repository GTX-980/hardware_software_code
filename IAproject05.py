def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == "exit":
            exit()
        if user_input.lower() == "return":
            print()
            print("calculation halted.")
            print("returning to selection.")
            print()
            choice()
        if is_valid_integer(user_input):
            return user_input
        else:
            print("Invalid number. Please try again.")
def is_valid_integer(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False
def main():
    print("This program is a rudementary calculator.")
    print("(can only calculate two whole numbers.)")
    print("type 'exit' if you wish to stop")
    print()
    choice()
def choice():
    print("will you be adding(a) subtracting(b) multiplying(c) or dividing(d)?")
    print("remember you can also type 'return' if you wish to come back here")
    print()
    print("type (a) (b) (c) or (d)")
    option = input().lower()
    if option == "a":
        calc1()
    elif option == "b":
        calc2()
    elif option == "c":
        calc3()
    elif option == "d":
        calc4()
    elif option == "exit":
        exit()
def calc1():
    x = get_valid_input("Enter first whole number: ")
    y = get_valid_input("Enter second whole number: ")
    sum = int(x) + int(y)
    print("{} + {} = {}".format(x, y, sum))
    calc1()
def calc2():
    x = get_valid_input("Enter first whole number: ")
    y = get_valid_input("Enter second whole number: ")
    sum = int(x) - int(y)
    print("{} - {} = {}".format(x, y, sum))
    calc2()
def calc3():
    x = get_valid_input("Enter first whole number: ")
    y = get_valid_input("Enter second whole number: ")
    sum = int(x) * int(y)
    print("{} * {} = {}".format(x, y, sum))
    calc3()
def calc4():
    x = get_valid_input("Enter first whole number: ")
    y = get_valid_input("Enter second whole number: ")
    if int(y) == 0:
        print("Are you trying to give me a stroke?")
        Print("you can't divide things by zero!")
        calc4()
        return
    sum = int(x) / int(y)
    print("{} / {} = {}".format(x, y, sum))
    calc4()
def exit():
    print()
    print ("calculation halted.")
    print ("program closed successfuly.")
    quit()
if __name__ == "__main__":
    main()
