#Count all lower case, upper case, digits, and special symbols from a given string

#function for logic
def count_category(name):
    lower_count = 0
    upper_count = 0
    digits_count = 0
    special_sym_count = 0
    for char in name:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        elif char.isnumeric():
            digits_count += 1
        else:
            special_sym_count += 1
    print('LowerChar: {} '.format(lower_count))   
    print('UpperChar: {} '.format(upper_count))
    print('Digits: {} '.format(digits_count))
    print('SpecialSymbol: {} '.format(special_sym_count))

name = 'anSHU!@#25'
count_category(name)
    