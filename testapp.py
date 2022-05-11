from random import randint
from tkinter import *
import pickle

dictionary=[]
with open('Dictionary.txt', 'r') as words:
    dictionary = [word.split('\n')[0] for word in words]


root= Tk()
root.title('')
root.geometry('300x500')

progress = 0

def on_close():
    with open(r'C:\Users\Tos\Documents\t.pickle', 'wb') as t_pickle:
        pickle.dump(dictionary, t_pickle)
    root.destroy()

def yes_():
    #select a random number
    n = randint(0,len(dictionary))
    
    #pass to list and print word on label
    global text_label
    text_label.grid_forget()
    text_label = Label(root, text = dictionary[n])
    text_label.config(font=('Arial', 25))
    text_label.grid(row=0, padx=100, pady=100)

    #remove that word
    dictionary.remove(dictionary[n])
##    progress += 1

def no_():
    global text_label
    text_label.grid_forget()
    text_label = Label(root, text='test click')
    text_label.config(font=('Arial', 25))
    text_label.grid(row=0, padx=100, pady=100)

try:
    with open(r'C:\Users\Tos\Documents\t.pickle', 'rb') as t_pickle:
        dictionary = pickle.load(t_pickle)
except FileNotFoundError:
    pass

text_label = Label(root, text='Hello')
text_label.config(font=('Arial', 30))
text_label.grid(row=0, padx=100, pady=100)


question = Label(root, text='Do you know this word?', anchor='center')
question.config(font=('Arial', 12))
question.grid(row=1, pady=20)

by = Button(root, text='Yes', command=yes_)
by.config(font=('Arial', 15))
by.grid(row=2, ipadx=20)

bn = Button(root, text='No', command=no_)
bn.config(font=('Arial', 15))
bn.grid(row=3, pady=10, ipadx=26)

root.protocol('WM_DELETE_WINDOW', on_close)
root.mainloop()

def load():
    picklein = open(r'C:\Users\Tos\Documents\t.pickle', 'rb')
    pickle.load(picklein)
    picklein.close()
    print('loaded!\n')
    
    pickleOut = open(r'C:\Users\Tos\Documents\exd.pickle', 'wb')
    pickle.dump(exd, pickleOut)
    pickleOut.close()
    picklein = open(r'C:\Users\Tos\Documents\exd.pickle', 'rb')
    exd = pickle.load(picklein)
    print(exd)




