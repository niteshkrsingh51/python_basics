#function to print the multiplication table of the given input
def mul_table(num):
    for item in range(1,11):
        product = num * item
        print('{} * {} = {}'.format(num,item,product))

#displaying result
num = 2
mul_table(num)
