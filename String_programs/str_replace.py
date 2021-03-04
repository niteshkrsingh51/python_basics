#function to remove characters from a string

def new_str(name):

    #converting the string into list
    name_list = list(name) 

    #iterating the to find the character in the list
    for items in name:
        if items == 'n':

            #below conditions we can execute only one condition

            #condition 1: replacing the character with the required one 
            name_list.insert(name_list.index(items),'x')

            #condition 2: removing the character from the list
            name_list.remove(items)      

        else:
            pass

    #one line process to convert the list into string    
    new_name = ''.join(name_list)    
    return new_name

name = 'Anshunn'

#displaying the result
show_result = new_str(name)
print(show_result)

