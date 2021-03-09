#program to check whether the number is armstring number or not

#function for the logic
def checkArmStrong(num):
    sum = 0
    num_list = list(num)
    for items in num_list:
        items_cube = int(items) * int(items) * int(items)
        sum = sum + items_cube
    if sum == int(num):
        print('{} is a Armstring Number'.format(num))
    else:
        print('{} is not a Armstrong number'.format(num))

#displaying the result by calling the above function
num = input('Enter the number: ')
checkArmStrong(num)