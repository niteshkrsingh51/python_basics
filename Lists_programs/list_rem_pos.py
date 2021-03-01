#function to remove elements by thier index position in a list
def list_rem_position(num_list):
    del num_list[0]
    del num_list[4]
    del num_list[5]
    return num_list

num_list = [1,2,3,4,5,6,7,9]
list_rem_position_check = list_rem_position(num_list)

#display the results
print(list_rem_position_check)    