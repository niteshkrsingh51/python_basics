#function to return true if any common elements in the two lists
def compare_common_ele(num_list1,num_list2):
    for x in num_list1:
        if x in num_list2:
            return True
        else:
            pass


num_list1 = [1,3,4,5]
num_list2 = [2,7,6,7]

#displaying the results
print(compare_common_ele(num_list1,num_list2))