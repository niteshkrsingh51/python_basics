#function to swap elements in a list by giving user input
def swap_elements(num_list):
    pos1 = int(input('Enter first position: '))
    pos2 = int(input('Enter Second Position: '))
    temp = num_list[pos1]
    num_list[pos1] = num_list[pos2]
    num_list[pos2] = temp
    return num_list

num_list = [1,5,6,4,3]
swapped_elements = swap_elements(num_list)

#displaying the results
print(swapped_elements)
