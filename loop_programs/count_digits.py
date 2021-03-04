#Given a number count the total number of digits in a number

#function to give the no. of digits in the given input
def count_digit(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

#displaying the result
num = 2453
result = count_digit(num)
print(result)