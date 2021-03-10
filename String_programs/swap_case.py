def swap_case(my_str):

    my_list = list(my_str)
    new_list = []

    for items in my_list:

        if items.isupper():
            new_list.append(items.lower()) 
                  
        elif items.islower():
            new_list.append(items.upper())

        else:
            new_list.append(items)

    name = ''.join(new_list)
    return name

my_str = 'HackerRank.com presents "Pythonist 2".'
result = swap_case(my_str)
print(result)


#alternative is to use the build in function

# new_word = my_str.swapcase()
# return new_word
