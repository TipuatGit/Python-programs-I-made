from tkinter import *
'''-----------------------------------------------------------------------------'''
#TASK 1
#define codes and prices for each journey stage in arrays
journeyStageOne = [['C1',1.50],['C2',3.00],['C3',4.50],['C4',6.00],['C5',8.00]]
journeyStageTwo = [['M1',5.75],['M2',12.50],['M3',22.25],['M4',34.50],['M5',45.00]]
journeyStageThree = [['F1',1.50],['F2',3.00],['F3',4.50],['F4',6.00],['F5',8.00]]

#define passenger account information array (its a 2d array/list)
# will contain unique account number & passenger name
# will be populated later in TASK 2
passengerAccounts = [['A',1],['B',2]]
name = str()
accountID = int() # passngerAccounts[-1][1]

#define booking array. its a 2d array where each row contains 4 elements
# will include unique booking number for journey of a passenger
# will be populated later in TASK 2
bookings = [[1,'02:30','C3','M2','F4',1],[2,'09:45','C1','M1','F1',2]]
bookingID = int() #bookings[-1][5]
'''-----------------------------------------------------------------------------'''

root = Tk()
root.title('Journey Booking Service')

starting_text = 'Enter account number to make a booking: (Press Enter to create account)'
label = Label(root, text=starting_text)
label.grid(row=0, column=0)

user_input = Entry(root, borderwidth=2)
user_input.grid(row=1, column=0)

def get_user_input_1():
    if user_input.get() == '':
        label.destroy()
        user_input.insert(0,'Enter full name ')
        
        entry_button.destroy()
        Button(root, text='Create Account', command=get_user_input_2).grid(row=2, column=0)


    if user_input.get().isdigit():# and len(entry) == 6:
        # make new variables for label wigets
        startTime = 'Enter journey starting time: '
        code1 = 'Enter code for stage 1 of journey: '
        code2 = 'Enter code for stage 2 of journey: '
        code3 = 'Enter code for stage 3 of journey: '

        # define new widgets
        start_time_label = Label(root, text=startTime)
        code_label_1 = Label(root, text=code1)
        code_label_2 = Label(root, text=code2)
        code_label_3 = Label(root, text=code3)
                
        start_time_entry = Entry(root, borderwidth=2)
        code_entry_1 = Entry(root,borderwidth=2)
        code_entry_2 = Entry(root,borderwidth=2)
        code_entry_3 = Entry(root,borderwidth=2)

        # mechanism for checking account number implemented
        for count in range(len(passengerAccounts)):            
            if passengerAccounts[count][1] == int(user_input.get()): # important to convert str to int or comparison fails!
                
                #destroy old widgets
                label.destroy()
                user_input.destroy()
                entry_button.destroy()

                # place new widgets
                start_time_label.grid(row=0, column=0)
                code_label_1.grid(row=1, column=0)
                code_label_2.grid(row=2, column=0)
                code_label_3.grid(row=3, column=0)

                start_time_entry.grid(row=0, column=1)
                code_entry_1.grid(row=1, column=1)
                code_entry_2.grid(row=2, column=1)
                code_entry_3.grid(row=3, column=1)

                #let passenger book a journey upon verfication
                bookingID = bookings[-1][5] + 1
                booking = [user_input.get(), start_time_entry.get(), code_entry_1.get(), code_entry_2.get(), code_entry_3.get(), bookingID]
                bookings.append(booking)
                break

def get_user_input_2():
    #account creation mechanism implemented
    name = user_input.get()
    accountID = passengerAccounts[-1][1] + 1
    newAccount = [name, accountID]
    passengerAccounts.append(newAccount)
    
    Label(root, text=name+', your account number is: '+str(accountID)).grid(row=3, column=0)
    
    

entry_button = Button(root, text='Enter', padx=5, command=get_user_input_1)
entry_button.grid(row=2,column=0)






root.mainloop()
