def IntToRoman(num):
    # Dictionary mapping integer values to Roman numerals
    values = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    
    # Variable to store the resulting Roman numeral
    totalS = ""
    
    # Iterate over key-value pairs in the values dictionary
    for integer, roman in values.items():
        # While the remaining number is greater than or equal to the current integer value
        while num >= integer:
            # Append the corresponding Roman numeral to the result
            totalS += roman
            # Subtract the current integer value from the remaining number
            num -= integer
    
    # Return the final Roman numeral representation
    return totalS

# Test the function with an example
result = IntToRoman(10)
print(result)
