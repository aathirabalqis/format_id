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
global b, c, sql_ids

b = 1
c = 0

def clean(arr):

    for i in arr:
        if len(i) == 1:
            arr.remove(i)
            
    return arr
    
def formatids_HES():

    b4["state"] = DISABLED
    b3["state"] = DISABLED
    
    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    ids = clean(ids)
    
    new_ids = list(filter(None, ids))
    new_ids = new_ids[b:]
    
    act_total.config(text = 'Total IDs = ' + str(len(new_ids)))
    stri = str(','.join(new_ids))
    
    total.config(text = '')

    textbox.delete('1.0', END)
    textbox.insert(END, stri)
    
def formatids_SQL():

    global all_ids, ind
    b4["state"] = DISABLED
    b3["state"] = DISABLED
    ind = 0
    all_ids = []

    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    ids = clean(ids)
    
    new_ids = list(filter(None, ids))
    new_ids = new_ids[b:]
    all_ids.append(new_ids)
    
    act_total.config(text = 'Total IDs = ' + str(len(new_ids)))
    
    if len(new_ids) > 1000:
        divide(new_ids,1000)

    textbox.delete('1.0', END)
    textbox.insert(END,'\'' + '\',\''.join(all_ids[ind]) + '\'')
   
    total.config(text = 'Displayed IDs = ' + str(len(all_ids[ind])))
    

    return all_ids
    
def divide(array,lim):

    global all_ids, ind

    num = math.ceil(len(array)/lim)
    all_ids = []
    for i in range(math.ceil(len(array)/lim)):
        temp = array[lim*i:lim*(i+1)]
        print(len(temp))
        all_ids.append(temp)
    
    b4["state"] = NORMAL   
    return all_ids
    
    
def nextt():

    global all_ids, total, ind
       
    b3["state"] = NORMAL
    b4["state"] = DISABLED
    ind += 1
    
    if ind < len(all_ids)-1:
        b4["state"] = NORMAL
    
    textbox.delete('1.0', END)
    textbox.insert(END,'\'' + '\',\''.join(all_ids[ind]) + '\'')
   
    total.config(text = 'Displayed IDs = ' + str(len(all_ids[ind])))
   
def back():
    global ind
    
    b4["state"] = NORMAL
    b3["state"] = DISABLED
    ind -= 1
    
    if ind != 0:
       b3["state"] = NORMAL 
       
    textbox.delete('1.0', END)
    textbox.insert(END,'\'' + '\',\''.join(all_ids[ind]) + '\'')
   
    total.config(text = 'Displayed IDs = ' + str(len(all_ids[ind])))

 
def formatids_MDMS():

    global c, b
    total.config(text = '')
    b4["state"] = DISABLED
    b3["state"] = DISABLED
    
    out = ''
    c = 0 
    d = 0
    
    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    ids = clean(ids)
    
    new_ids = list(filter(None, ids))
    new_ids = new_ids[b:]

    textbox.delete('1.0', END)

    if b == 1:
        ids.pop(0)
    
    num = math.ceil(len(ids)/12)
    
    total.config(text = 'Displayed IDs = ' + str(len(new_ids)))
    
    for i in range(num):
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
    
    
    total.config(text = '')
    b4["state"] = DISABLED
    b3["state"] = DISABLED

    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    ids = clean(ids)
    stri = ''
    
    new_ids = list(filter(None, ids))
    new_ids = new_ids[b:]
    
    act_total.config(text = 'Total IDs = ' + str(len(new_ids)))
    
    for i in range(len(new_ids)):
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
    if event.char == 'i':
        inpu.focus()
        
    elif event.char == 'h':
        formatids_HES()
        
    elif event.char == 's':
        formatids_SQL()
        
    elif event.char == 'm':
        formatids_MDMS()
    
    elif event.char == '3':
        formatids_3MS()
        
    elif event.char == 'o':
        textbox.focus()
        
def exitt(event):
    root.quit()
    
textvar = StringVar()
textbox = ScrolledText(root, height = 30, width = 43)
textbox.place(x = 30, y = 110)


Button(root, text = 'HES', command = formatids_HES).place(x = 30, y = 70)
Button(root, text = 'SQL', command = formatids_SQL).place(x = 65, y = 70)
Button(root, text = 'MDMS', command = formatids_MDMS).place(x = 100, y = 70)
Button(root, text = '3MS', command = formatids_3MS).place(x = 150, y = 70)


total = Label(root, text = '')
total.place(x = 265, y = 602)
act_total = Label(root, text = '')
act_total.place(x = 105, y = 602)

b1 = Button(root, text = 'Without Header', command = woheader)
b1.place(x = 202, y = 70) 
b2 = Button(root, text = 'With Header', command = wheader)
b2.place(x = 298, y = 70) 
b3 = Button(root, text = 'Back', command = back)
b3.place(x = 30, y = 600)
b4 = Button(root, text = 'Next', command = nextt)
b4.place(x = 67, y = 600)

b2["state"] = DISABLED
b3["state"] = DISABLED
b4["state"] = DISABLED

inpu = Entry(root, textvariable = textvar, width = 48, font = ('calibre',10,'normal'))
inpu.place(x = 30, y = 30)

Label(root, text = 'SAB').place(x = 380, y = 630)

root.resizable(False, False) 
root.bind('<Key>', shortcut)
root.bind('<Escape>', exitt)
root.mainloop()