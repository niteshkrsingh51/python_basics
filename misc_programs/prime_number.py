#prime number program

def checkPrime(num):
    NotPrime = 0
    if num < 0:
        print('Enter the number again: ')
    else:
        for x in range(1,num):
            if num % x == 0:
                 NotPrime  += 1
        if NotPrime > 1:
            print('It is not a prime number')
        else:
            print('It is a prime number')
       
    
num = int(input('Enter the number: '))
checkPrime(num)
