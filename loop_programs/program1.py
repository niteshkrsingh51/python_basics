# Given a list, iterate it, and display numbers divisible by five, 
# and if you find a number greater than 150, stop the loop iteration.

def loop_program1(num_list):
    #new_list = []
    for items in num_list:
        if items % 5 == 0 and items <= 150:
            print(items,end=' ')
            #new_list.append(items)
        else:
           pass
    #return new_list

num_list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
loop_program1(num_list)
#result=loop_program1(num_list)
#print(result)
            
            