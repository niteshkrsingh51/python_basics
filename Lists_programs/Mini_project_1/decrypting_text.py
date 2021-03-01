#decryption of text using caesar-cipher method

#function to decrypt the text
def decrypting_text(name):
    shift_value = 4
    decryption = ''
    for item in name:
        #checking the character is uppercase or not
        if item.isupper():
            #find the position is 0-25
            item_unicode = ord(item) - ord('A')
            #perform the shift using the caesar-cipher process
            new_index = (item_unicode - shift_value) % 26
            #convert to actual character
            item_new_unicode = new_index + ord('A')
            char_Item_new = chr(item_new_unicode)
            #append the decrypted string 
            decryption = decryption + char_Item_new
        else:
            #since the character is not upper case leave as it is
            decryption = decryption + item
    return decryption

name = 'EnsLu'
decryption_check = decrypting_text(name)
#displaying the result
print(decryption_check) 