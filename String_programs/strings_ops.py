#function to uppercase the string
def uppercasestring(name):
    x = name.upper()
    return x

#function to split a string
def splitstring(name):
    y = name.split('n')
    return y

#using format command in the string
def formatstring(name):
    a = 'My name is {}'
    z = a.format(name)
    return z

name = 'Anshu'
upper_check = uppercasestring(name)
split_check = splitstring(name)
format_check = formatstring(name)

#displaying results
print(upper_check)
print(split_check)
print(format_check)