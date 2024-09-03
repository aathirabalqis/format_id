from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from datetime import date, datetime
import math

root = Tk()

root.title('Format ID')
root.geometry('410x650')
global b, c

b = 1
c = 0

#all functions takes column headers too - default
#SQL 12 at a time

# add shortcut to entry & exit
# add total number of accs

def formatids_HES():
    
    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    
    new_ids = list(filter(None, ids))
    stri = str(','.join(new_ids[b:]))

    textbox.delete('1.0', END)
    textbox.insert(END, stri)
    
    
    
def formatids_SQL():

    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    
    new_ids = list(filter(None, ids))
    
    total = Label(root, text = 'Total IDs = ' + str(len(new_ids))).place(x = 290, y = 595)

    textbox.delete('1.0', END)
    textbox.insert(END,'\'' + '\',\''.join(new_ids[b:]) + '\'')
    
    
def formatids_MDMS():

    global c, b
    out = ''
    c = 0 
    d = 0
    
    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    ids = list(filter(None, ids))

    textbox.delete('1.0', END)

    if b == 1:
        ids.pop(0)
    
    num = math.floor(len(ids)/12)
    
    for i in range(num+1):
        start = 12*i
        end = 12 + (12*i)
        
        if i == num:
            stri = str(','.join(ids[start:]))
        else:
            stri = str(','.join(ids[start:end]))
        
        textbox.insert(END, stri)
        textbox.insert(END, '\n')
        textbox.insert(END, '\n')
            
def formatids_3MS():
    
    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    stri = ''
    
    new_ids = list(filter(None, ids))
    
    for i in range(b, len(new_ids)):
        stri += '=' + str(new_ids[i]) + ','

    textbox.delete('1.0', END)
    textbox.insert(END, stri[:-1])
    
            
def woheader():
    global b 

    if b2["state"] == DISABLED:
        b1["state"] = DISABLED
        b2["state"] = NORMAL
    b = 0
    
def wheader():
    global b

    if b1["state"] == DISABLED:
        b2["state"] = DISABLED
        b1["state"] = NORMAL
    b = 1
    
def shortcut(event):   
    if event.char == 'e':
        inpu.focus()
        
def exitt(event):
    root.quit()
    
textvar = StringVar()
textbox = ScrolledText(root, height = 30, width = 43)
textbox.place(x = 30, y = 110)


Button(root, text = 'HES', command = formatids_HES).place(x = 30, y = 70)
Button(root, text = 'SQL', command = formatids_SQL).place(x = 65, y = 70)
Button(root, text = 'MDMS', command = formatids_MDMS).place(x = 100, y = 70)
Button(root, text = '3MS', command = formatids_3MS).place(x = 150, y = 70)


b1 = Button(root, text = 'Without Header', command = woheader)
b1.place(x = 202, y = 70) 
b2 = Button(root, text = 'With Header', command = wheader)
b2.place(x = 298, y = 70) 

b2["state"] = DISABLED

inpu = Entry(root, textvariable = textvar, width = 48, font = ('calibre',10,'normal')).place(x = 30, y = 30)


root.bind('<Key>', shortcut)
root.bind('<Escape>', exitt)
root.mainloop()