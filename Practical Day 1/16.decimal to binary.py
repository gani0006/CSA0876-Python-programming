def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num).replace("0b", "")
    return binary_num

# Example usage:
decimal_number = 10
binary_number = decimal_to_binary(decimal_number)
print("Binary representation of", decimal_number, "is:", binary_number)
