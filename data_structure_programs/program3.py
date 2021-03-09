#Given a list slice it into 3 equal chunks and reverse each chunk

def threeEqualChunks(num_list):

    #setting the variables needed
    size = len(num_list)
    chunk_size = size/3
    chunk_size2 = chunk_size + chunk_size
    chunk_size3 = chunk_size2 + chunk_size

    #initializing the list needed
    list1 = []
    list2 = []
    list3 = []

    #iterating the loop in the list to divide it into 3 chunks
    for index,items in enumerate(num_list):
        if index < chunk_size:
            list1.append(items)
        elif index < chunk_size2:
            list2.append(items)
        elif index <= chunk_size + chunk_size3:
            list3.append(items)

    #displaying the results        
    print(f'Original list {num_list}')
    print(f'Chunk 1 {list1}')
    list1.reverse()
    print(f'After reversing it {list1}')
    print(f'Chunk 2 {list2}')
    list2.reverse()
    print(f'After reversing it {list2}')
    print(f'Chunk 3 {list3}')
    list3.reverse()
    print(f'After reversing it {list3}')

#calling the function
num_list = [11, 45, 8, 23, 14, 12, 78, 45, 89] 
threeEqualChunks(num_list)

             


    
