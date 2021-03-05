
#checking whether a year is a leap year or not

def leapyearcheck(year):
    #first divide the year with 4 if it is divisible go for further process else it is not a leap year
    if year % 4 == 0:
        #then divide the year with 100 if it is divisible go for further process else it is leap year 
        if year % 100 == 0:
            #then divide the year with 400 if it is divisible go for it is a leap year else not a leap year
            if year % 400 == 0:
                print('Leap Year')
            else:
                print('Not Leap Year')
        else:
            print ('Leap Year')
    else:
        print('Not Leap Year')
        
 #displaying the result   
year = int(input('Enter the year: '))
leapyearcheck(year)



