#loop for rows
for i in range(5):

    #loop for space
    for j in range(5-i-1):
        print(' ', end=' ')

    #loop for cloumnsy
    for j in range(i+1):
        print(j+1,end=" ")

    print()