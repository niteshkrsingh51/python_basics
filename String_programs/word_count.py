#function to find the word count in a sentence

def wordCount(name,sentence):
    sentence = sentence.lower()
    count = sentence.count(name.lower())
    return count
            
sentence = "Welcome to USA. usa awesome, isn't it?"  
name = 'USA'
result = wordCount(name,sentence)
print(result)
