def octal_to_hex(octal_string):
    decimal_value = octal_to_decimal(octal_string)
    return decimal_to_hexadecimal(decimal_value)
def hex_to_octal(hex_string):
    decimal_value = hex_to_decimal(hex_string)
    return decimal_to_octal(decimal_value)
def octal_to_decimal(octal_string):
    decimal_value = 0
    power = len(octal_string) - 1
    for digit in octal_string:
        decimal_value += int(digit) * (8 ** power)
        power -= 1
    return decimal_value
def decimal_to_octal(decimal_num):
    if decimal_num == 0:
        return "0"
    octal_string = ""
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_string = str(remainder) + octal_string
        decimal_num //= 8
    return octal_string
def octal_to_binary(octal_string):
    binary_string = ''
    for digit in octal_string:
        binary_string += format(int(digit), '03b')
    return binary_string.lstrip('0') or '0'
def binary_to_octal(binary_string):
    decimal_value = int(binary_string, 2)
    octal_value = oct(decimal_value)
    return octal_value[2:]
def hex_to_decimal(hex_string):
    return int(hex_string, 16)
def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num)[2:]
def hex_to_binary(hex_string):
    scale = 16
    num_of_bits = 4
    return bin(int(hex_string, scale))[2:].zfill(len(hex_string) * num_of_bits)
def binary_to_hexadecimal(binary_number):
    decimal_value = int(binary_number, 2)
    hexadecimal_value = hex(decimal_value)
    return hexadecimal_value[2:]
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    binary_string = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_string = str(remainder) + binary_string
        decimal_num //= 2
    return binary_string
def binary_to_decimal(num):
    result = 0
    if len(num) > 0:
        power = len(str(num)) - 1
        for num in str(num):
            result += int(num) * 2 ** power
            power -= 1
    return result
def main():
    print("Choose the following number conversion:")
    print()
    choice()
def choice():
    print("(1) binary to decimal")
    print("(2) decimal to binary")
    print("(3) binary to hexadecimal")
    print("(4) hexadecimal to binary")
    print("(5) decimal to hexadecimal")
    print("(6) hexadecimal to decimal")
    print("(7) binary to octal")
    print("(8) octal to binary")
    print("(9) decimal to octal")
    print("(10) octal to decimal")
    print("(11) hexadecimal to octal")
    print("(12) octal to hexadecimal")
    print("(type 'exit' to quit)")
    option = input()
    if option == "1":
        option1()
    elif option == "2":
        option2()
    elif option == "3":
        option3()
    elif option == "4":
        option4()
    elif option == "5":
        option5()
    elif option == "6":
        option6()
    elif option == "7":
        option7()
    elif option == "8":
        option8()
    elif option == "9":
        option9()
    elif option == "10":
        option10()
    elif option == "11":
        option11()
    elif option == "12":
        option12()
    elif option.lower() == "exit":
        exit()
def option1():
    num = input("Enter Binary Number: ")
    binary_num = binary_to_decimal(num)
    print(f"Binary {num} to Decimal: {binary_num}")
    choice()
def option2():
    decimal_num = int(input("Enter Decimal Number: "))
    binary_result = decimal_to_binary(decimal_num)
    print(f"Decimal {decimal_num} to Binary: {binary_result}")
    choice()
def option3():
    binary_number = input("Enter Binary Number: ")
    hexadecimal_result = binary_to_hexadecimal(binary_number)
    print(f"Binary {binary_number} to Hexadecimal: {hexadecimal_result}")
    choice()
def option4():
    hex_string = input("Enter Hexadecimal Number: ")
    binary_result = hex_to_binary(hex_string)
    print(f"Hexadecimal {hex_string} to Binary: {binary_result}")
    choice()
def option5():
    decimal_num = int(input("Enter Decimal Number: "))
    hexadecimal_result = decimal_to_hexadecimal(decimal_num)
    print(f"Decimal {decimal_num} to Hexadecimal: {hexadecimal_result}")
    choice()
def option6():
    hex_string = input("Enter Hexadecimal Number: ")
    decimal_result = hex_to_decimal(hex_string)
    print(f"Hexadecimal {hex_string} to Decimal: {decimal_result}")
    choice()
def option7():
    binary_string = input("Enter Binary Number: ")
    octal_result = binary_to_octal(binary_string)
    print(f"Binary {binary_string} to Octal: {octal_result}")
    choice()
def option8():
    octal_string = input("Enter Octal Number: ")
    binary_result = octal_to_binary(octal_string)
    print(f"Octal {octal_string} to Binary: {binary_result}")
    choice()
def option9():
    decimal_num = int(input("Enter Decimal Number: "))
    octal_result = decimal_to_octal(decimal_num)
    print(f"Decimal {decimal_num} to Octal: {octal_result}")
    choice()
def option10():
    octal_string = input("Enter Octal Number: ")
    decimal_result = octal_to_decimal(octal_string)
    print(f"Octal {octal_string} to Decimal: {decimal_result}")
    choice()
def option11():
    hex_string = input("Enter Hexadecimal Number: ")
    octal_result = hex_to_octal(hex_string)
    print(f"Hexadecimal {hex_string} to Octal: {octal_result}")
    choice()
def option12():
    octal_string = input("Enter Octal Number: ")
    hexadecimal_result = octal_to_hex(octal_string)
    print(f"Octal {octal_string} to Hexadecimal: {hexadecimal_result}")
    choice()
def exit():
    print()
    print("Conversion halted.")
    print("Program closed successfully.")
    quit()
if __name__ == "__main__":
    main()
