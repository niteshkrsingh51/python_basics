def sum_elements(num_list):
    sum = 0
    for x in num_list:
        sum = sum + x
    return(sum)

num_list = [1,2,3,4,5]
result = sum_elements(num_list)
print(result)