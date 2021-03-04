#Given a string of odd length greater than 7,
#return a new string made of the middle three characters of a given String

#function to return a new string made of middle three characters of a given string
def strprg1(name):
    middleindex = int(len(name)/2)
    middlethree = name[middleindex-1:middleindex+2]
    print(middlethree)

#displaying the result
name1 = 'JhonDipPeta'
name2 = 'JaSonAy'
strprg1(name1)
strprg1(name2)
