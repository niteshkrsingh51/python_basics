#Arrange string characters such that lowercase letters should come first

#function for logic
def char_arrange(name):
    lower = []
    upper = []
    for char in name:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
    sorted_name = ''.join(lower+upper)
    return sorted_name

name = 'ANSHUhiii'
result = char_arrange(name)
print(result)
    
