from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from datetime import date, datetime

root = Tk()

root.title('Format ID')
root.geometry('600x300')
global b, c

b = 1
c = 0

#all functions takes column headers too - default
#HES 12 at a time

def formatids_HES():
    
    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    
    new_ids = list(filter(None, ids))
    stri = str(', '.join(new_ids[b:]))

    textbox.delete('1.0', END)
    textbox.insert(END, stri)
    
def formatids_SQL():

    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    
    new_ids = list(filter(None, ids))

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

    print(ids)
    textbox.delete('1.0', END)
    #textbox.insert(END, ','.join(ids[b:-1]))
    
    for i in range(b, len(ids)):
        out = out + ids[i] + ','
    
        c += 1
        d += 1

        if c == 12:
            print(out)
            textbox.insert(END, out[:-2]) ################
            textbox.insert(END, '\n')
            textbox.insert(END, '\n')
            c = 0
            out = ''
        
        if d == len(ids)-1-b:
            textbox.insert(END, out[:-2])
            
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
    
textvar = StringVar()
textbox = ScrolledText(root, height = 14, width = 45)
textbox.place(x = 200, y = 30)


Button(root, text = 'Reformat IDs - HES', command = formatids_HES).place(x = 45, y = 80)
Button(root, text = 'Reformat IDs - SQL', command = formatids_SQL).place(x = 45, y = 130)
Button(root, text = 'Reformat IDs - MDMS', command = formatids_MDMS).place(x = 38, y = 180)


b1 = Button(root, text = 'Without Header', command = woheader)
b1.place(x = 13, y = 230) 
b2 = Button(root, text = 'With Header', command = wheader)
b2.place(x = 107, y = 230) 

b2["state"] = DISABLED

inpu = Entry(root, textvariable = textvar, font = ('calibre',10,'normal')).place(x = 30, y = 30)

root.mainloop()
