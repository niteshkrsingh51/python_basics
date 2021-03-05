# Given two strings, s1, and s2 return a new string made of the
# first, middle, and last characters each input string


#function for logic
def string_merge(name1,name2):
    name1_size = len(name1)
    name2_size = len(name2)
    first_char = name1[:1] + name2[:1]
    middle_char = name1[int(name1_size/2):int(name1_size/2)+1] + name2[int(name2_size/2):int(name2_size/2)+1]
    last_char = name1[name1_size-1] + name2[name2_size-1]
    new_name = first_char + middle_char + last_char
    return new_name

name1 = 'America'
name2 = 'Japan'
result = string_merge(name1,name2)
print(result)