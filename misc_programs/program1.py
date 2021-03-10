def stringValidator(s):

    s = input()

    #intializing the condition check variables
    digitCount = 0
    islowerCount = 0
    isUpperCount = 0
    isAlphaNum   = 0
    isAlphaCount = 0

    #check the conditions
    for items in s:
        if items.isdigit():
            digitCount += 1 
        if items.islower():
            islowerCount += 1
        if items.isupper():
            isUpperCount += 1
        if items.isalpha():
            isAlphaCount += 1
        if items.isalnum():
            isAlphaNum += 1
    
    #displaying the result for any alphanumeric characters
    if isAlphaNum > 0:
        print(True)
    if isAlphaNum <= 0:
        print(False)
    
    #displaying the result for any alphabet characters
    if isAlphaCount > 0:
        print(True)
    if isAlphaCount <= 0:
        print(False)
    
    #displaying the result for any digits characters
    if digitCount > 0:
        print(True)
    if digitCount <= 0:
        print(False)
    
    #displaying the result for any lowerCase characters
    if islowerCount > 0:
        print(True)
    if islowerCount <= 0:
        print(False)
    
    #displaying the result for any uppercase characters
    if isUpperCount > 0:
        print(True)
    if isUpperCount <= 0:
        print(False)
     

s = '123'
stringValidator(s)

