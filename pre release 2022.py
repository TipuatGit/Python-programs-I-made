'''
Your preparation for the examination should include attempting the following practical tasks by writing 
and testing a program or programs.
A program is needed to allow a Wildlife Park to sell tickets. A booking consists of one or more tickets 
for the same day(s) and can be made up to a week in advance. A booking can be made for a visit of 
one day or two consecutive days. A booking can have extra attractions included. A booking will be valid 
for the day(s) chosen only.

Write and test a program or programs for the Wildlife Park: 
• Your program or programs must include appropriate prompts for the entry of data. Data must be 
validated on entry. 
• All outputs, including error messages, need to be set out clearly and understandably.
• All variables, constants and other identifiers must have meaningful names. 
You will need to complete these three tasks. Each task must be fully tested.


Task 1 – displaying the ticket options and the extra attractions available
Set up your program to:
• display the options, attractions and prices for one-day tickets
• display the options, attractions and prices for two-day tickets
• show the days available for booking; assume that there are tickets available for any valid day.


Task 2 – process a booking
Extend your program for Task 1 to:
• input the tickets and extra attractions required, then calculate the total cost of the booking
• allocate a unique booking number
• display the booking details, including the total cost and the unique booking number
• repeat as required.


Task 3 – ensuring each booking is the best value
Check that the total for each booking gives the best value and offer an alternative if this is not the case. 
For example, buying two family tickets is better than a group ticket for a group of 10 that includes 
four adults and six children.'''

#TASK 1
print('<< Ticket type | One day | Two days >>')
print('1 Adult | $20.00 | $30.00')
print('1 Child | $12.00 | $18.00')
print('1 Senior | $16.00 | $24.00')
print('Family(2 adults/seniors + 3 children) | $60.00 | $90.00')
print('Group ( >= 6 people, price per person ) | $15.00 | $22.50')
print()
print('<< Extra attraction | Cost per person >>')
print('lion feeding | $2.50')
print('penguin feeding | $2.00')
print('evening barbecue (two-day tickets only) | $5.00')
print()
print("Days available for booking:")
for days in range(1,31):
    print(days, end='  ')
print()

#TASK 2
ticket = input("Enter tickets. separate tickets using commas(,) .")
days_booked = input("\nEnter '1' or '2' for one-day or two-day booking: ")
date_booked = input()
total = 0
bookings = []
bookingID = 0
for t in ticket.split(','):
    if (t == 'Adult') and (days_booked == '1'):
        total += 20
    elif (t == 'Adult') and (days_booked == '2'):
        total += 30

    if (t == 'Child') and (days_booked == '1'):
        total += 12
    elif (t == 'Child') and (days_booked == '2'):
        total += 18

    if (t == 'Senior') and (days_booked == '1'):
        total += 16
    elif (t == 'Senior') and (days_booked == '2'):
        total += 24

    if (t == 'Family') and (days_booked == '1'):
        total += 60
    elif (t == 'Family') and (days_booked == '2'):
        total += 90

    if (t == 'Group') and (days_booked == '1'):
        group = input('Enter number of people: ')
        total += ( 15 * int(group) )
    elif (t == 'Family') and (days_booked == '2'):
        group = input('Enter number of people: ')
        total += ( 22.5 * int(group) )
print(total)
