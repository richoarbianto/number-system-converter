from utils import ExtractToDecimal as ex
import os

ex = ex()
menu = """
1. Decimal to Binary
2. Decimal to Octal
3. Decimal to Hexadecimal

4. Binary to Decimal
5. Octal to Decimal
6. Hexadecimal to Decimal

7. Binary to Octal
8. Octal to Hexadecimal

9. Octal to Binary
10. Hexadecimal to Octal
11. Hexadecimal to Binary
12. Binary to Hexadecimal

99. Exit
"""
while True:
    print(menu)
    choice = input("Enter your choice: ")
    if choice == '99':
        print("Exit.")
        break
    elif choice == '1':
        decimal = int(input("Enter a decimal number: "))
        binary = ex.decimal_to_binary(decimal)[::-1]
        print(f"{decimal} in binary is: {binary}")
    elif choice == '2':
        decimal = int(input("Enter a decimal number: "))
        octal = ex.decimal_to_octal(decimal)
        print(f"{decimal} in octal is: {octal}")
    elif choice == '3':
        decimal = int(input("Enter a decimal number: "))
        hexadecimal = ex.decimal_to_hex(decimal)
        print(f"{decimal} in hexadecimal is: {hexadecimal}")
    elif choice == '4':
        binary = input("Enter a binary number: ")
        decimal = ex.binary_to_decimal(binary)
        print(f"{binary} in decimal is: {decimal}")
    elif choice == '5':
        octal = input("Enter an octal number: ")
        decimal = ex.octal_to_decimal(octal)
        print(f"{octal} in decimal is: {decimal}")
    elif choice == '6':
        hexadecimal = input("Enter a hexadecimal number: ")
        decimal = ex.hex_to_decimal(hexadecimal)
        print(f"{hexadecimal} in decimal is: {decimal}")
    elif choice == '7':
        binary = input("Enter a binary number: ")
        octal = ex.binary_to_octal(binary)
        print(f"{binary} in octal is: {octal}")
    elif choice == '8':
        octal = input("Enter an octal number: ")
        hexadecimal = ex.octal_to_hexadecimal(octal)
        print(f"{octal} in hexadecimal is: {hexadecimal}")
    elif choice == '9':
        octal = input("Enter an octal number: ")
        binary = ex.octal_to_binary(octal)[::-1]
        print(f"{octal} in binary is: {binary}")
    elif choice == '10':
        hexadecimal = input("Enter a hexadecimal number: ")
        octal = ex.hexadecimal_to_octal(hexadecimal)
        print(f"{hexadecimal} in octal is: {octal}")
    elif choice == '11':
        hexadecimal = input("Enter a hexadecimal number: ")
        binary = ex.hexadecimal_to_binary(hexadecimal)[::-1]
        print(f"{hexadecimal} in binary is: {binary}")
    elif choice == '12':
        binary = input("Enter a binary number: ")
        hexadecimal = ex.binary_to_hexadecimal(binary)
        print(f"{binary} in hexadecimal is: {hexadecimal}")
    else:
        print("[!] Invalid choice. Please try again.")
        print()
        continue
    print()
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')