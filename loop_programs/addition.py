#function to return the sum of digits smaller than the given input
def addition_number(num):
    sum = 0
    for items in range(num+1):
        sum = sum + items
    return sum
    
#displaying the result
num = 10
result = addition_number(num)
print(result)
