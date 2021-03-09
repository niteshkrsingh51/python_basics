#Iterate a given list and count the occurrence of each element and
#create a dictionary to show the count of each element

def listTodictionary(num_list):

    my_list = []

    for items in num_list:
        elementCount = num_list.count(items)
        my_list_case = (items, elementCount)
        my_list.append(my_list_case)
        
    dictt = dict(my_list)

    return dictt

num_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
displayResult = listTodictionary(num_list)
print(displayResult)
        