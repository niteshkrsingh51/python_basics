#function two remove the even numbers from the list
def remove_even_ele(num_list):
    for x in num_list:
        if x%2 == 0:
            num_list.remove(x)
        else:
            pass
    return num_list

num_list = [1,2,3,4,5,6]
remove_even_ele_check = remove_even_ele(num_list)

#display the results
print(remove_even_ele_check)