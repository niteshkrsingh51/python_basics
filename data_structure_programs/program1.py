# Given two lists create a third list by picking an odd-index element from the first list and 
# even index elements from the second.

def twoOddEvenList(list1, list2):

    odd_list1 = []
    even_list2= []

    #taking out the odd-index elements of list1
    for OddIndex,OddItems in enumerate(list1):
        if OddIndex % 2 != 0:
            odd_list1.append(OddItems)
        else:
            pass

    #taking out the even-index elements of list2
    for EvenIndex,EvenItems in enumerate(list2):
        if EvenIndex % 2 == 0:
            even_list2.append(EvenItems)
        else:
            pass
    
    #adding the two lists
    final_list = odd_list1 + even_list2 
    return final_list


list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

#displaying results
DisplayResult = twoOddEvenList(list1,list2)
print(DisplayResult)
