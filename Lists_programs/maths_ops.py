#function to find the sum of elements in lists
def sum_elements(num_list):
    sum = 0
    for x in num_list:
        sum = sum + x
    return(sum)

#function to find the multiplication of elements in lists
def mul_elements(num_list):
    mul = 1
    for x in num_list:
        mul = mul * x
    return(mul)

num_list = [2,4,9,5,7]
sum_list = sum_elements(num_list)
mul_list = mul_elements(num_list)

#displaying the results
print(sum_list)
print(mul_list)