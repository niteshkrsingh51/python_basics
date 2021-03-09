#Iterate a given list and Check if a given element already exists in a 
#dictionary as a key’s value if not delete it from the list

def listANDdict(my_list,my_dict):

    my_dict_values = my_dict.values()
    new_list = list(my_dict_values)
    new_list2 = []

    for items in my_list:
        if items not in new_list:
            pass
        else:
            new_list2.append(items)
            
    print(f'After removing unwanted elements from list {new_list2}')

my_list = [47, 64, 69, 37, 76, 83, 95, 97]
my_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
listANDdict(my_list,my_dict)