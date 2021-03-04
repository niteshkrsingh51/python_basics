#function to display the required pattern
def pattern_1(pattern_limit):
    for row in range(1, pattern_limit):
        for column in range(1, row+1):
            print(column, end=' ')
        print()


#diplaying the result
pattern_limit = int(input('Enter your pattern limit: '))
pattern_1(pattern_limit)
