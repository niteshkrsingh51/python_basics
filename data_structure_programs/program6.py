#Given the following two sets find the intersection 
#and remove those elements from the first set

def setIntersection(set1, set2):
    duplicate_elements = set1.intersection(set2)
    my_list = list(duplicate_elements)
    
    #first way to do
    set1.difference_update(my_list)
    
    #second way to do
    #for items in my_list:
    #    set1.discard(items)

    print(f'Intersection is {duplicate_elements}')
    print(f'First Set after removing common element {set1}')

set1 = {65, 42, 78, 83, 23, 57, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}
setIntersection(set1, set2)
