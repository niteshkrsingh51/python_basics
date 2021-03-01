#function to shuffle the list
import random
def shuffle_list(num_list):
    shuffle_list = num_list.copy()
    random.shuffle(shuffle_list)
    return shuffle_list

num_list = [1,2,3,4,5]
shuffle_list_check = shuffle_list(num_list)

#display the results
print(shuffle_list_check)