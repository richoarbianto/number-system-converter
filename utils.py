class ExtractToDecimal:
    def __init__(self):
        self.hex_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'A': 10, 'b': 11, 'B': 11, 'c': 12, 'C': 12, 'd': 13, 'D': 13, 'e': 14, 'E': 14, 'f': 15, 'F': 15}
    
    def decimal_to_binary(self, data_decimal: int) -> str:
        result_in_binary = ""
        remain = data_decimal
        while True:
            result_in_binary += str(remain % 2).split('.')[0]
            remain = remain / 2
            if remain < 1:
                break
        return result_in_binary
    
    def decimal_to_octal(self, data_decimal: int) -> str:
        result_in_octal = ""
        remain = data_decimal
        while True:
            result_in_octal += str(remain % 8).split('.')[0]
            remain = remain / 8
            if remain < 1:
                break
        return result_in_octal[::-1]
    
    def decimal_to_hex(self, data_decimal: int) -> str:
        result_in_hex = ""
        remain = data_decimal
        while True:
            result_in_hex += [keys for keys,value in self.hex_digits.items() if int(str(remain % 16).split('.')[0]) == value][0]
            remain = int(str(remain / 16).split('.')[0])
            if remain < 1:
                break
        return result_in_hex[::-1].upper()
    
    def binary_to_decimal(self, data_binary: str) -> int:
        return self.to_decimal(data_binary, 2)
    
    def octal_to_decimal(self, data_octal: str) -> int:
        return self.to_decimal(data_octal, 8)
    
    def hex_to_decimal(self, data_hex: str) -> int:
        return self.to_decimal(data_hex, 16)
    
    def binary_to_octal(self, data_binary: str) -> str:
        decimal = self.binary_to_decimal(data_binary)
        return self.decimal_to_octal(decimal)
    
    def octal_to_hexadecimal(self, data_octal: str) -> str:
        decimal = self.octal_to_decimal(data_octal)
        return self.decimal_to_hex(decimal)

    def octal_to_binary(self, data_octal: str) -> str:
        decimal = self.octal_to_decimal(data_octal)
        return self.decimal_to_binary(decimal)

    def hexadecimal_to_octal(self, data_hex: str) -> str:
        decimal = self.hex_to_decimal(data_hex)
        return self.decimal_to_octal(decimal)

    def hexadecimal_to_binary(self, data_hex: str) -> str:
        decimal = self.hex_to_decimal(data_hex)
        return self.decimal_to_binary(decimal)
    
    def binary_to_hexadecimal(self, data_binary: str) -> str:
        decimal = self.binary_to_decimal(data_binary)
        return self.decimal_to_hex(decimal)
    
    # !IMPORTANT
    def to_decimal(self, data: str, type_length: int):
        list_search = list(data)
        total_char = len(data)
        total_in_decimal = 0
        for i in list_search:
            if type_length == 16:
                x = self.hex_digits[i]
            elif type_length == 2 or type_length == 8:
                x = int(i)

            result = x * (type_length ** (total_char - 1))
            total_in_decimal += result
            total_char -= 1
        return total_in_decimal
    
    
    
    

    
    
    
    
    
    
    
    
    