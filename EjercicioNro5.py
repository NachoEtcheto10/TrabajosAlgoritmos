def roman_to_decimal(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_num = 0
    prev_value = 0
    
    for char in roman_numeral[::-1]:
        value = roman_dict[char]
        if value < prev_value:
            decimal_num -= value
        else:
            decimal_num += value
        prev_value = value
    
    return decimal_num
print(roman_to_decimal('IV'))