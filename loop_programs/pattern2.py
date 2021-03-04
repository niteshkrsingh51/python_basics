#function to display the required pattern
def pattern_1(pattern_limit):
    for row in range(0, pattern_limit+1):
        for column in range(pattern_limit-row,0,-1):
            print(column, end=' ')
        print()


#diplaying the result
pattern_limit = int(input('Enter your pattern limit: '))
pattern_1(pattern_limit)
