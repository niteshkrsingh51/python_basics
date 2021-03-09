#Remove duplicate from a list and create a tuple and find the minimum and maximum number

def remListTup(num_list):
    new_list = []
    for items in num_list:
        if items not in new_list:
            new_list.append(items)
        else:
            pass
    print(f'unique items {new_list}')
    new_tuple = tuple(new_list)
    print(f'tuple {new_tuple}')
    print(f'min: {min(new_tuple)}')
    print(f'max: {max(new_tuple)}')

num_list = [87, 45, 41, 65, 94, 41, 99, 94]
remListTup(num_list)

