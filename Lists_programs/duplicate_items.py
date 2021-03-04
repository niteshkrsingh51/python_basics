#function to eliminate the duplicate the values in the list
def duplicate_items(input_list):
    new_list = []
    for x in input_list:
        if x not in new_list:
            new_list.append(x)
        else:
            pass
    return new_list

#displaying the results
input_list = [1,2,1,3,4,2,3,4,5]
result = duplicate_items(input_list)
print(result)
