#function to display the required pattern
def pattern3(pattern_range):
    for rows in range(0,pattern_range):
        for columns in range(0,rows+1):
            print('*',end='')
        print('\r')
    
    for rows in range(pattern_range,0,-1):
        for columns in range(0,rows-1):
            print('*',end='')
        print('\r')

#displaying the result by calling the function and passing the argument in its
pattern_range = 6
pattern3(pattern_range)