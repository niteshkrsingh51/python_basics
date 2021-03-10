import textwrap

def wrap(string, max_width):
    new_string = textwrap.wrap(string, width=max_width)
    myName = '\n'.join(new_string)
    return myName

string = 'adfafafasfasfafafaff'    
max_width = 4

result = wrap(string,max_width)
print(result)

