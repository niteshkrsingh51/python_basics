def captilized(myStr):
    new_str = myStr.split(' ')
    my_list = []
    for items in new_str:
        my_list.append(items.capitalize())
    
    new_name = ' '.join(my_list)
    print(new_name)

myStr = 'nitesh kumar'
captilized(myStr)
