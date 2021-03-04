#Reverse the following list using for loop

#function to reverse the elements of the given list
def reverse_list(num_list):
    start = len(num_list) - 1
    stop = -1 
    step = -1
    #-----------#
    #using direct reverse function of list
    new_list = num_list.copy()
    new_list.reverse()
    print(new_list)
    #-----------#
    #using slicing operator
    new_sliced_list = num_list.copy()
    reverse_list=new_sliced_list[::-1]
    print(reverse_list)
    #-----------#
    #using loop to reverse a list
    for items in range(start,stop,step):
        print(num_list[items],end=' ')
    #-----------#

#displaying the result
num_list = [10, 20, 30, 40, 50]
reverse_list(num_list)