#encryption of text using caesar-cipher method

#function to encrypted the text
def encrypting_text_func(name):
    # defining the shift count 
    shift_value = 4 
    encryption = ''
    for item in name:
        #checking the character is uppercase or not
        if item.isupper():
            #find the position is 0-25
            item_unicode = ord(item) - ord('A')
            #perform the shift using the caesar-cipher process
            new_index = (item_unicode + shift_value) % 26
            #convert to new character
            item_new_unicode = new_index + ord('A')
            new_character = chr(item_new_unicode)
            #append the encrypted string 
            encryption = encryption + new_character
        else:
            #since the character is not upper case leave as it is
            encryption = encryption + item
    return encryption


name = 'AnsHu'
encryp_check = encrypting_text_func(name)

#displaying the result
print(encryp_check)
print(ord('A'))



          
         