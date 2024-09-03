from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import math

root = Tk()

root.title('Format ID')
root.geometry('410x670')

global b, c, sql_ids, all_ids, outp, page, l

b = 1
c = 0
l = 1
all_ids = []

def clean(arr):

    for i in arr:
        if len(i) == 1: arr.remove(i)
            
    return arr
    
def getinput(w):
    inpu = textvar.get()
    textvar.set('')
    total.config(text = '')
    
    ids = inpu.split('\n')
    ids = clean(ids)
    new_ids = list(filter(None, ids))

    if w == 1: new_ids = new_ids[b:]
    
    return new_ids
    
def formatids_HES():

    global outp

    b3["state"] = DISABLED
    b4["state"] = DISABLED
    
    new_ids = getinput(1)
    output(new_ids, 100000,'Output (HES): ', 'HES')
    
    # act_total.config(text = 'Total IDs = ' + str(len(new_ids)))
    # stri = str(','.join(new_ids))

    # textbox.delete('1.0', END)
    # textbox.insert(END, stri)
    # outp.config(text = 'Output (HES): ')
    # page.config(text = '1 of 1')
    
def formatids_SQL():

    global all_ids, ind, flag
    b3["state"] = DISABLED
    b4["state"] = DISABLED
    # ind = 0
    # all_ids = []

    new_ids = getinput(1)
    output(new_ids, 1000,'Output (SQL): ', 'SQL')
    # all_ids.append(new_ids)
    
    # act_total.config(text = 'Total IDs = ' + str(len(new_ids)))
    
    # if len(new_ids) > 1000:
    #     flag = 'SQL'
    #     divide(new_ids, 1000)

    # textbox.delete('1.0', END)
    # textbox.insert(END,'\'' + '\',\''.join(all_ids[ind]) + '\'')
    
    # total.config(text = 'Displayed IDs = ' + str(len(all_ids[ind])))
    # outp.config(text = 'Output (SQL): ')
    # page.config(text = '1 of ' + str(len(all_ids)))
    
    return all_ids
    
def divide(array,lim):

    global all_ids, ind

    all_ids = []
    for i in range(math.ceil(len(array)/lim)):
        temp = array[lim*i:lim*(i+1)]
        print(len(temp))
        all_ids.append(temp)
    
    b4["state"] = NORMAL   
    return all_ids
    
def nextt():

    global all_ids, ind, flag
       
    b3["state"] = NORMAL
    b4["state"] = DISABLED
    ind += 1
    
    textbox.delete('1.0', END)

    if flag == 'MDMS': textbox.insert(END, str(','.join(all_ids[ind])))
    else: textbox.insert(END,'\'' + '\',\''.join(all_ids[ind]) + '\'')  
    
    if ind < len(all_ids)-1: b4["state"] = NORMAL

    total.config(text = 'Displayed IDs = ' + str(len(all_ids[ind])))
    page.config(text = str(ind+1) + ' of ' + str(len(all_ids)))
   
def back():
    global all_ids, ind, flag
    
    b4["state"] = NORMAL
    b3["state"] = DISABLED
    ind -= 1
    
    textbox.delete('1.0', END)
    
    if flag == 'MDMS': textbox.insert(END, str(','.join(all_ids[ind])))   
    else: textbox.insert(END,'\'' + '\',\''.join(all_ids[ind]) + '\'')
    
    if ind != 0: b3["state"] = NORMAL 
   
    total.config(text = 'Displayed IDs = ' + str(len(all_ids[ind])))
    page.config(text = str(ind+1) + ' of ' + str(len(all_ids)))

 
def formatids_MDMS():

    global c, b, flag, ind, all_ids

    total.config(text = '')
    b4["state"] = DISABLED
    b3["state"] = DISABLED
    # all_ids = []
    
    c = 0 
    # ind = 0
    
    new_ids = getinput(1)

    output(new_ids, 12,'Output (MDMS): ', 'MDMS')
    # all_ids.append(new_ids)

    # textbox.delete('1.0', END)
    
    # act_total.config(text = 'Total IDs = ' + str(len(new_ids)))
    
    # if len(new_ids) > 12:
    #     flag = 'MDMS'
    #     divide(new_ids, 12)
        
    # stri = str(','.join(all_ids[ind]))
    # total.config(text = 'Displayed IDs = 12') #+ str(len(all_ids[ind])))
    # page.config(text = '1 of ' + str(len(all_ids)))
    # outp.config(text = 'Output (MDMS): ')
    
    # textbox.delete('1.0', END)
    # textbox.insert(END, stri)    
    
    # total.config(text = 'Displayed IDs = ' + str(len(new_ids)))
      
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
    page.config(text = '1 of 1')
    outp.config(text = 'Output (3MS): ')

def output(new_ids, num, instr, fl): 
    global flag, all_ids, ind, act_total, total, page, outp, textbox, l
    ind = 0
    all_ids = []
            
    # new_ids = list(filter(None, outt))
    all_ids.append(new_ids)
    act_total.config(text = 'Total IDs = ' + str(len(new_ids)))

    if l == 0: num = 100000

    if len(new_ids) > num:
        divide(new_ids, num)
        flag = fl

    # stri = str(','.join(all_ids[ind]))
    total.config(text = 'Displayed IDs = ' + str(len(all_ids[ind])))
    page.config(text = '1 of ' + str(len(all_ids)))

    textbox.delete('1.0', END)

    if fl == 'SQL': textbox.insert(END,'\'' + '\',\''.join(all_ids[ind]) + '\'')
    else: textbox.insert(END, str(','.join(all_ids[ind])))
    outp.config(text = instr)  

    return all_ids



# def woheader():
#     global b 

#     if b2["state"] == DISABLED:
#         b1["state"] = DISABLED
#         b2["state"] = NORMAL
#     b = 0
    
# def wheader():
#     global b

#     if b1["state"] == DISABLED:
#         b2["state"] = DISABLED
#         b1["state"] = NORMAL
#     b = 1

def header():
    global b
    
    if var.get() == 1: b = 1
    else: b = 0
    print(b)
    return b

def limit():
    global l

    if var2.get() == 1: l = 1
    else: l = 0
    # if b5['state'] == DISABLED: b5['state'] = NORMAL
    # else: b5['state'] = DISABLED
    

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
    
def testtt():
    print('it worked')
    
textvar = StringVar()
textbox = ScrolledText(root, height = 30, width = 43)
textbox.place(x = 30, y = 130)


Button(root, text = 'HES', command = formatids_HES).place(x = 30, y = 70)
Button(root, text = 'SQL', command = formatids_SQL).place(x = 65, y = 70)
Button(root, text = 'MDMS', command = formatids_MDMS).place(x = 100, y = 70)
Button(root, text = '3MS', command = formatids_3MS).place(x = 150, y = 70)

outp = Label(root, text = 'Output: ')
outp.place(x = 30, y = 107)
total = Label(root, text = '')
total.place(x = 265, y = 622)
act_total = Label(root, text = '')
act_total.place(x = 105, y = 622)
page = Label(root, text = '')
page.place(x = 335, y = 107)

# b1 = Button(root, text = 'No Header', command = woheader)
# b1.place(x = 255, y = 70) 
# b2 = Button(root, text = 'Header', command = wheader)
# b2.place(x = 325, y = 70) 
var = IntVar()
var2 = IntVar()

headerc = Checkbutton(root, text = 'With Header', variable = var, command = header)
headerc.place(x = 286, y = 71)

limc = Checkbutton(root, text = 'With Limit', variable = var2, command = limit)
limc.place(x = 200, y = 71)

var.set(1)
var2.set(1)


b3 = Button(root, text = 'Back', command = back)
b3.place(x = 30, y = 620)
b4 = Button(root, text = 'Next', command = nextt)
b4.place(x = 67, y = 620)
# b5 = Button(root, text = 'Limit', command = limit)
# b5.place(x = 200, y = 70) 

# b2["state"] = DISABLED
b3["state"] = DISABLED
b4["state"] = DISABLED
# b5["state"] = DISABLED

inpu = Entry(root, textvariable = textvar, width = 48, font = ('calibre',10,'normal'))
inpu.place(x = 30, y = 30)

Label(root, text = 'SAB').place(x = 380, y = 650)

root.resizable(False, False) 
root.bind('<Key>', shortcut)
root.bind('<Escape>', exitt)
root.mainloop()
