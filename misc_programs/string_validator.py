def string_validator(s):
    
   #use of any keyword 
   print(any(c.isalnum() for c in s))
   print(any(c.isalpha() for c in s))
   print(any(c.isdigit() for c in s))
   print(any(c.islower() for c in s))
   print(any(c.isupper() for c in s)) 

s = input('Enter the String: ')
string_validator(s)