#Given a dictionary get all values from the dictionary and add them to a list but don’t add duplicates

def dictTOlist(my_dict):

    values = my_dict.values()
    values_list = list(values)

    new_list = []

    for items in values_list:
        if items not in new_list:
            new_list.append(items)
    
    return new_list


my_dict = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
display_Result = dictTOlist(my_dict)
print(display_Result)
