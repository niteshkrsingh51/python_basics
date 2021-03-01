#function to find out the min element in the list
def min_element(num_list):
    num_list.sort()
    return num_list[0]

#function to find out the max element in the list
def max_element(num_list):
    num_list.sort()
    size = len(num_list)
    return num_list[size-1]

num_list = [2,4,6,1,8]
min_result = min_element(num_list)
max_result = max_element(num_list)

#displaying the results
print(min_result)
print(max_result)