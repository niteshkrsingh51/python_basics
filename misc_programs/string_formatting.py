def print_formatted(number):
    results = []
    for items in range(1,number+1):
        OctalNumber = oct(items).lstrip("0o")
        HexaNumber  = (f"0x{items:X}").lstrip("0ox")
        BinNumber   = bin(items).lstrip("0b") 
        results.append([str(items), OctalNumber, HexaNumber, BinNumber])
   
   
   


number = 17
print_formatted(number)
    