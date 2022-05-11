from time import sleep
from tkinter import *
from tkinter import messagebox

time = int(input('Enter time in minutes: ')) * 60

root= Tk()
print('timer started!')
sleep(time)
response= messagebox.showinfo('Timer' , 'Time\'s Up!')
root.destroy()

