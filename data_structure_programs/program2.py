#Given a list, remove the element at index 4 and 
#add it to the 2nd position and at the end of the list

def alterListIndexValue(num_list):

    element = num_list.pop(4)
    num_list.insert(2, element)
    num_list.append(element)

    return num_list

num_list = [34, 54, 67, 89, 11, 43, 94]
displayResult = alterListIndexValue(num_list)
print(displayResult)