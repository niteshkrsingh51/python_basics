#Given a two list of equal size create a Python
#set such that it shows the element from both lists in the pair

def twoLists(list1, list2):

    new_list = []
    
    for items1,items2 in zip(list1,list2):
        new_list_case = (items1,items2)
        new_list.append(new_list_case)
    
    return set(new_list)

list1 = [2, 3, 4, 5, 6, 7, 8]
list2 = [4, 9, 16, 25, 36, 49, 64]

displayResult = twoLists(list1,list2)
print(displayResult)

