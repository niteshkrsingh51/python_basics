#function to remove duplicates from a list
def duplicates_elements(num_list):
    dup_lists = set()
    unique_lists = []
    for x in num_list:
        if x not in dup_lists:
            unique_lists.append(x)
            dup_lists.add(x)
    return dup_lists

num_lists = [1,2,6,4,5,6,5]
dupli_check = duplicates_elements(num_lists)

#diplaying the result
print(dupli_check)

