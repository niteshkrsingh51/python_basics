#function to find the element in a list
def find_element(num_list):
    for x in num_list:
        if x == 4:
            return True
        else:
            pass

#alternative way to find the element in a list
def find_element1(num_list):
    if 4 in num_list:
        return True
    else:
        pass


num_list = [1,4,6,7,8]
find_result = find_element(num_list)
find_result1 = find_element1(num_list)
#displaying results
print(find_result)
print(find_result1)