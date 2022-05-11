#TASK 1
#define codes and prices for each journey stage in arrays
journeyStageOne = [['C1',1.50],['C2',3.00],['C3',4.50],['C4',6.00],['C5',8.00]]
journeyStageTwo = [['M1',5.75],['M2',12.50],['M3',22.25],['M4',34.50],['M5',45.00]]
journeyStageThree = [['F1',1.50],['F2',3.00],['F3',4.50],['F4',6.00],['F5',8.00]]

#define passenger account information array (its a 2d array/list)
# will contain unique account number & passenger name
# will be populated later in TASK 2
passengerAccounts = [['A',1],['B',2]] #dummy entries
name = str()
accountID = int() # passngerAccounts[-1][1]

#define booking array. its a 2d array where each row contains 6 elements
# will include account number,start time of journey,codes of each stage and
# unique booking number for journey of a passenger
# will be populated later in TASK 2
bookings = [[1,'02:30','C3','M2','F4',1],[2,'09:45','C1','M1','F1',2]] #dummy entries
bookingID = int() #bookings[-1][5]

#TASK 2
entry = input('Enter account number to make a booking: (Press Enter to create account)')

passengerConfirmation = False

while passengerConfirmation is False:
    if entry == '':
        #account creation mechanism implemented
        name = input('Enter full name: ')
        accountID = accountID + 1
        newAccount = [name, accountID]
        passengerAccounts.append(newAccount)

        #passenger will probably wanna book after creating account
        entry = input('Enter account number to make a booking: ')

    if entry.isdigit():# and len(entry) == 6:

        # mechanism for checking account number implemented
        for count in range(len(passengerAccounts)):
            if passengerAccounts[count][1] == int(entry): # important to convert str to int or comparison fails!
                #let passenger book a journey upon verfication
                startTime = input('Enter journey starting time: ')
                code1 = input('Enter code for stage 1 of journey: ')
                code2 = input('Enter code for stage 2 of journey: ')
                code3 = input('Enter code for stage 3 of journey: ')
                bookingID = bookingID + 1
                booking = [entry, startTime, code1, code2, code3, bookingID]
                bookings.append(booking)
                break #no need to scan further if account found earlier in list
                        
            #final action to do if not found after searching through all account numbers
            elif count == (len(passengerAccounts) - 1) :
                print('Account does not exist.')
            
    else: print('Incorrect entry')

    #calculate total price of journey for a passenger
    total = 0
    price1 = 0
    price2 = 0
    price3 = 0
    for count in range(5):
        if journeyStageOne[count][0] == code1.upper():
            price1 = journeyStageOne[count][1]

        if journeyStageTwo[count][0] == code2.upper():
            price2 = journeyStageTwo[count][1]

        if journeyStageThree[count][0] == code3.upper():
            price3 = journeyStageThree[count][1]
            
    total = price1+price2+price3

    ##print(passengerAccounts)
    

    #TAKS 3
    time = startTime.split(':')
    if int(time[0]) > 10:
        total = total * 0.6

    print(total)
    print(bookings[-1])
    answer = input('Confirm all details and book your journey(y/n)? ')
    if answer == 'y':
        passengerConfirmation = True
    else: pass
