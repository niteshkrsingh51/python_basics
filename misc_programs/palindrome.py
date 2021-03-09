#function to check whether a number is palindrome or not

#function for logic
def CheckPalindrome(num):
    num_list = list(num)
    reverse_list = num_list.copy()
    reverse_list.reverse()
    reverse_num = ''.join(reverse_list)
    if num == reverse_num:
        print('{} is a palindrome number'.format(num))
    else:
        print('{} is not a palindrome number'.format(num))


#displaying the result by calling the function
num = input('Enter The Number: ')
CheckPalindrome(num)

    
        