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
global b, c, sql_ids, flag, lim

b = 1
c = 0
lim = 0


#all functions takes column headers too - default
#SQL 12 at a time

# add shortcut to entry & exit
# add total number of accs

# def formatids_HES():
    
    # global flag, all_ids, total, lim
    # b4["state"] = NORMAL
    
    # print(lim)
    # inpu = textvar.get()
    # textvar.set('')
    # ids = inpu.split('\n')
    
    # new_ids = list(filter(None, ids))
    # new_ids = new_ids[b:]
    # all_ids = []
    
    # act_total.config(text = 'Total IDs = ' + str(len(new_ids)))
    
    # if len(new_ids) > 150 and lim == 1:
        # all_ids = new_ids[150:]
        # new_ids = new_ids[:150]
        # b3["state"] = NORMAL
        # flag = 'HES'
        # lim = 0
    
    # stri = str(','.join(new_ids))

    # textbox.delete('1.0', END)
    # textbox.insert(END, stri)
    
    # total.config(text = 'Displayed IDs = ' + str(len(new_ids)))
    
    # return all_ids
    
def formatids_HES():
    
    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    
    new_ids = list(filter(None, ids))
    new_ids = new_ids[b:]
    
    act_total.config(text = 'Total IDs = ' + str(len(new_ids)))
    stri = str(','.join(new_ids))

    textbox.delete('1.0', END)
    textbox.insert(END, stri)
    
def formatids_SQL():

    global all_ids, total, flag, lim
    b4["state"] = DISABLED
    lim = 0

    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
    
    new_ids = list(filter(None, ids))
    new_ids = new_ids[b:]
    
    act_total.config(text = 'Total IDs = ' + str(len(new_ids)))
    
    if len(new_ids) > 1000:
        all_ids = new_ids[1000:]
        new_ids = new_ids[:1000]
        b3["state"] = NORMAL
        # flag = 'SQL'

    textbox.delete('1.0', END)
    textbox.insert(END,'\'' + '\',\''.join(new_ids) + '\'')
   
    total.config(text = 'Displayed IDs = ' + str(len(new_ids)))
    

    return all_ids
    
def nextt():

    global all_ids, total, flag
       
    b3["state"] = DISABLED
    
    new_ids = []
    new_ids = all_ids
    
    # if flag == 'HES':
        # num = 150
        # if len(new_ids) > num:
            # all_ids = new_ids[num:]
            # new_ids = new_ids[:num]
            # b3["state"] = NORMAL
            
        # stri = str(','.join(new_ids))

        # textbox.delete('1.0', END)
        # textbox.insert(END, stri)
        
    # else:
    num = 1000
    
    if len(new_ids) > num:
        all_ids = new_ids[num:]
        new_ids = new_ids[:num]
        b3["state"] = NORMAL
    
    textbox.delete('1.0', END)
    textbox.insert(END,'\'' + '\',\''.join(new_ids) + '\'')  
 
    total.config(text = 'Displayed IDs = ' + str(len(new_ids)))
   
    
def formatids_MDMS():

    global c, b
    total.config(text = '')
    b4["state"] = DISABLED
    lim = 0

    
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
    
    total.config(text = 'Displayed IDs = ' + str(len(new_ids)))
    
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
    
    global lim 
    
    total.config(text = '')
    b4["state"] = DISABLED
    lim = 0
    
    inpu = textvar.get()
    textvar.set('')
    ids = inpu.split('\n')
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
    
def limit():
    global lim
    
    lim = 1
    
    formatids_HES()

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


total = Label(root, text = '')
total.place(x = 265, y = 602)
act_total = Label(root, text = '')
act_total.place(x = 70, y = 602)

b1 = Button(root, text = 'Without Header', command = woheader)
b1.place(x = 202, y = 70) 
b2 = Button(root, text = 'With Header', command = wheader)
b2.place(x = 298, y = 70) 
b3 = Button(root, text = 'Next', command = nextt)
b3.place(x = 30, y = 600)
b4 = Button(root, text = 'Limit HES', command = limit)
# b4.place(x = 70, y = 600)


b2["state"] = DISABLED
b3["state"] = DISABLED
b4["state"] = DISABLED

inpu = Entry(root, textvariable = textvar, width = 48, font = ('calibre',10,'normal')).place(x = 30, y = 30)

Label(root, text = 'SAB').place(x = 380, y = 630)

root.resizable(False, False) 
root.bind('<Key>', shortcut)
root.bind('<Escape>', exitt)
root.mainloop()