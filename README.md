
# Number System Converter

This project is a basic **Number System Converter** implemented in Python. It supports conversion between different number systems (decimal, binary, octal, hexadecimal) **WITHOUT** using the built-in Python functions like `bin()`, `oct()`, or `hex()`.

## Features

This program allows conversions between the following number systems:

1. **Decimal to Binary**
2. **Decimal to Octal**
3. **Decimal to Hexadecimal**
4. **Binary to Decimal**
5. **Octal to Decimal**
6. **Hexadecimal to Decimal**
7. **Binary to Octal**
8. **Octal to Hexadecimal**
9. **Octal to Binary**
10. **Hexadecimal to Octal**
11. **Hexadecimal to Binary**
12. **Binary to Hexadecimal**

The program provides a simple CLI (Command Line Interface) with a menu for selecting the type of conversion.

## Installation

No special setup is required since this project does not use any external Python modules or libraries. You only need to have Python installed on your machine.

1. **Clone the repository**
   ```bash
   git clone https://github.com/richoarbianto/number-system-converter
   ```

2. **Run the program**
   ```bash
   python main.py
   ```

## How It Works

This project manually implements the logic for converting between different number systems, without relying on Python’s built-in functions (`bin()`, `oct()`, `hex()`). Each conversion is handled step-by-step by calculating remainders, powers, and other operations required for these transformations.

### Example Usage
You can choose the appropriate number from the menu, and the program will prompt you to enter a number for conversion.

### Sample Conversion

For example, to convert a decimal number `10` to binary:
1. Choose option `1` for "Decimal to Binary."
2. Enter the decimal number `10`.
3. The program will return: `1010` (the binary equivalent of `10`).

## Contributing

Feel free to fork this project and submit pull requests for any improvements or additional features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.