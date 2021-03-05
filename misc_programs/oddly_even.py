#program for oddly even

#function for the logic implemented
def oddlyeven(num):
    #converting the number into a list
    num_list = list(num)
    even_list = []
    odd_list = []
    even_sum = 0
    odd_sum = 0

    #iterating the elements in the list and appending the even odd digits to their separate lists
    for x in num_list:
        y = int(x)
        if y % 2 == 0:
            even_list.append(y)
        else:
            odd_list.append(y)

    #taking the sum of the even digits        
    for even_items in even_list:
        even_sum = even_sum + even_items

    #taking the sum of the odd digits    
    for odd_items in odd_list:
        odd_sum = odd_sum + odd_items
    #difference between sum of odd digits and sum of even digits

    differnce_result = odd_sum - even_sum
    return differnce_result

num = input('Enter the number: ')

#displaying the error
result = oddlyeven(num)
print(result) 

