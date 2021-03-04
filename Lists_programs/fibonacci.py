#function to return the list containing fibonacci series

#-----------
#This sign is used to indicate that those lines are required when you a list of fibonacci numbers 
#-----------

def fibonacci_func(nterms):
    count = 0
    a,b = 0,1
    #-----------
    #num_list = []
    #-----------
    while count < int(nterms):
        #printing the number of fibonacci series in a line
        print(a, end=' ')
        #-----------
        #num_list.append(a)
        #-----------
        c = a+b
        a = b
        b = c
        count +=1
    #-----------
    #return num_list
    #-----------

#displaying the result
nterms = input('Enter the nterms: ')
fibonacci_func(nterms) 
#-----------
#result = fibonacci_func(nterms) 
#print(result)
#-----------

    