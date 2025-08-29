from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
from tkinter import messagebox

root = Tk()
root.title('To Do')
root.geometry('750x600')
root.resizable(0,0)

root.rowconfigure(0,weight=100)
root.columnconfigure(0,weight=50)
root.columnconfigure(1,weight=50)

submit = LabelFrame(root, text="Data", bg="#e77070",fg='black')
submit.grid(row=0,column=0,sticky='nsew')

Done = LabelFrame(root, text="Info", bg='brown',fg='white')
Done.grid(row=0,column=1,sticky='nsew')

categories = []
to_do_values = []
i = 0

def Inserted():
    global to_do_values
    if len(t_n_e.get())>0 and len(t_cat_e.get())>0 and len(t_pri_e.get())>0:
        categories.append(t_cat_e.get())
        t_cat_e.configure(values=categories)
        t_cat_e.current(len(categories)-1)
        to_do_values.append(t_n_e.get())
        to_do_values.append(t_pri_e.get())
        to_do_values.append(t_cat_e.get())
        to_do_values.append('pending..')
        allTasks.insert('','end',values=list(to_do_values))
        to_do_values = []
        t_n_e.delete(0,1000)
        t_pri_e.delete(0,1000)
        

def deletePart():
    try:
        itemId = allTasks.focus()
        allTasks.delete(itemId)
    except:
        messagebox.showwarning(title='WHAT!', message='You have not even selected something budd:)')

def checkDone():
    itemiid = allTasks.focus()
    inVals = allTasks.item(itemiid)
    penDoneNum = 0
    try:
        penDoneNum = inVals['values'].index('pending..')
        inVals['values'][penDoneNum] = 'Done:)'
        allTasks.item(itemiid,values=inVals['values'])
    except ValueError:
        if str(type(itemiid)) == 'int':
            messagebox.showwarning(title='WHAT!', message='Hey You already done this task once:)')
        else:
            messagebox.showwarning(title='WHAT!', message='You have not even selected something budd:)')
    doneBtn.deselect()

status = ''
categ_current = ''

def updateDone():
    global status
    global categ_current
    try:
        itemiid = allTasks.focus()
        inVals = allTasks.item(itemiid)
        t_n_e.insert(0,inVals['values'][0])
        t_pri_e.insert(0,inVals['values'][1])
        t_cat_e.current(categories.index(inVals['values'][2]))
        categ_current = categories.index(inVals['values'][2])
        status = inVals['values'][3]
    except:
        messagebox.showwarning(title='WHAT!', message='You have not even selected something budd:)')





# Remember to get your update button working
def updateBtnFunc():
    global status
    itemId = allTasks.focus()
    categories[categ_current] = t_cat_e.get()
    t_cat_e.config(values=categories)
    allTasks.item(itemId, values=[t_n_e.get(), t_pri_e.get(), t_cat_e.get(),status])

# Left side grid

submit.rowconfigure(0,weight=20)
submit.rowconfigure(1,weight=20)
submit.rowconfigure(2,weight=20)
submit.rowconfigure(3,weight=20)
submit.rowconfigure(4,weight=20)

submit.columnconfigure(0,weight=100)

t0 = Frame(submit,bg='#e77070')
t0.grid(row=1,sticky='nsew')


t1 = Frame(submit,bg='#e77070')
t1.grid(row=2,sticky='nsew')

t2 = Frame(submit,bg='#e77070')
t2.grid(row=3,sticky='nsew')


# Last Frame placement

lF = Frame(submit, bg="#e77070")
lF.grid(row=4,sticky='nsew')

lF.columnconfigure(0,weight=50)
lF.columnconfigure(1,weight=50)
lF.rowconfigure(0,weight=100)

halfingLF1 = Frame(lF,bg="#e77070")
halfingLF1.grid(column=0,row=0,sticky="nsew")

halfingLF2 = Frame(lF,bg="#e77070")
halfingLF2.grid(column=1,row=0,sticky="nsew")

# Task Name

t_n = Label(t0, text="Task Name", bg="#e77070",font=('', '11', 'bold'))
t_n.pack(pady=5)
t_n_e  = Entry(t0)
t_n_e.pack()

t_pri = Label(t1, text="Task Priority", bg="#e77070",font=('', '11', 'bold'))
t_pri.pack(pady=5)
t_pri_e = Entry(t1)
t_pri_e.pack()

category_selected = StringVar()
t_cat = Label(t2, text="Task Category", bg="#e77070",font=('', '11', 'bold'))
t_cat.pack(pady=5)
t_cat_e = Combobox(t2, textvariable=category_selected, values=categories)
t_cat_e.pack()
categories.append(t_cat_e.get())
t_cat_e.config(values=categories)


# Buttons: 


bIn = Button(halfingLF1, text='Insert', bg='#e77070',command=Inserted)
bIn.pack()

bUp = Button(halfingLF2, text='Update', bg='#e77070',command=updateBtnFunc)
bUp.pack()


### SUBMIT SECTION

#TreeView

Done.rowconfigure(0,weight=50)
Done.rowconfigure(1,weight=50)
Done.columnconfigure(0,weight=100)

treeSection = Frame(Done)
treeSection.grid(row=0,column=0,sticky='nsew')

buttonSection = Frame(Done,bg="brown")
buttonSection.grid(row=1,column=0,sticky='nsew')

assigned_values = ['one','two','three','four']
allTasks = Treeview(treeSection, columns=assigned_values)
allTasks.heading('one', text='name')
allTasks.heading('two', text='priority')
allTasks.heading('three', text='category')
allTasks.heading('four', text='status')

allTasks.column('#0',width=0)
allTasks.column('one', width=120)
allTasks.column('two', width=120)
allTasks.column('three', width=120)
allTasks.column('four', width=120)
allTasks.pack(expand=True,fill='both')

# Buttons 

buttonSection.rowconfigure(0,weight=100)
buttonSection.columnconfigure(0,weight=33)
buttonSection.columnconfigure(1,weight=33)
buttonSection.columnconfigure(2,weight=33)


delSecB = Label(buttonSection,bg="brown")
delSecB.grid(row=0,column=0,sticky='nsew')

updateSecB = Label(buttonSection,bg="brown")
updateSecB.grid(row=0,column=1,sticky='nsew')

doneSecB = Label(buttonSection,bg="brown")
doneSecB.grid(row=0,column=2,sticky='nsew')


# Tear the button section to 3 parts first 

delButt = Button(buttonSection,text='Delete',bg='brown', command=deletePart)
delButt.grid(row=0,column=0,sticky='nsew')

upButt = Button(buttonSection,text='Update',bg='brown',command=updateDone)
upButt.grid(row=0,column=1,sticky='nsew')

hasDone = IntVar(value=0)

doneBtn = Checkbutton(buttonSection,text='Done',variable=hasDone,onvalue=1,offvalue=0,bg='brown',command=checkDone)
doneBtn.grid(row=0,column=2,sticky='nsew')


root.mainloop()