# Given two sets, Checks if One Set is a subset or superset of another Set.
# if the subset is found delete all elements from that set

def checksets(set1,set2):
    
    case1 = set1.issubset(set2)
    case2 = set2.issubset(set1)

    if case1 == True:
        set1.clear()
    elif case2 == True:
        set2.clear()
    
    print(f'First Set {set1}')
    print(f'Second Set {set2}')

set1 = {57, 83, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}
checksets(set1,set2)