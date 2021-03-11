from collections import OrderedDict 

def mergeTheTools(string,k):
    for i in range(0,len(string),k):
        chunks = string[i:i+k]
        new_chunk = "".join(OrderedDict.fromkeys(chunks))
        print(new_chunk)

    

    

string = 'AABCAAADA'
k = 3
mergeTheTools(string,k)
