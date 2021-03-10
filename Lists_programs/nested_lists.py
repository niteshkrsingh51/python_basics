def nested_list(my_list,scores):
    
    second_lowest_names = []
   
    my_list.sort(key=lambda e: e[1])
    
    second_lowest = sorted(scores) [1]

    for name, score in my_list:
        if score == second_lowest:
            second_lowest_names.append(name)
    
    for name in sorted(second_lowest_names):
        print(name, end='\n')


my_list = []
scores = set()
strength = int(input('Total No. Of Students: '))
for _ in range(strength):
    name = input('Enter the name: ')
    score = float(input('Enter the score: '))
    item = name,score
    my_list.append([name, score])
    scores.add(score)
nested_list(my_list,scores)
