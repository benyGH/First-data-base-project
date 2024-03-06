import myclass
from tkinter import *
from tkinter import messagebox
#========GUI========
win = Tk()
width = win.winfo_screenwidth()
height = win.winfo_screenheight()

x = 400 
y = 400

ww = width//2 - x//2
wh = height//2 - y//2

win.geometry(f'{x}x{y}+{ww}+{wh}')
win.configure(bg = '#FFCC66')
win.title('Contct Management')

db = myclass.Contact('d:/newdata.db')
#========Def========

def show():
    lstbox.delete(0,END)
    records = db.fetch()
    for i in records:
        lstbox.insert(END,i)

def remove():
    index = lstbox.curselection()
    res = lstbox.get(index)
    m = messagebox.askyesno('warn' , 'Are you sure ?')
    if m == True :
        db.remove(res[0]) 
        show()

def insert():
    fname= ent_fname.get()
    lname=ent_lname.get()
    city=ent_city.get()
    tel=ent_tel.get()
    lstbox.insert(END,fname + ','+lname+','+city+','+tel)    
    db.insert(ent_fname.get(),ent_lname.get(),ent_city.get(),int(ent_tel.get()))
    ent_city.delete(0,END)
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_tel.delete(0,END)
    ent_fname.focus_set()
def clear():
    m = messagebox.askyesno('warn' , 'Are you sure ?')
    if m == True :
            ent_city.delete(0,END)
            ent_fname.delete(0,END)
            ent_lname.delete(0,END)
            ent_tel.delete(0,END)

def update():
    index = lstbox.curselection()
    res = lstbox.get(index)
    db.update(res[0], ent_fname.get(),ent_lname.get(),ent_city.get(),ent_tel.get())
   
def search():
    result = db.search(ent_search.get())
    lstbox.delete(0 , END)
    for i in result:
        lstbox.insert(END , i)
        ent_search.delete(0 , END)

def exit():
    m = messagebox.askyesno('warn' , 'Are you sure ?')
    if m == True :
         win.destroy()
#========LABELS========
lbl_fname = Label(text= 'Fname:',font='arial 11',bg= '#FFCC66')
lbl_fname.place(x=15,y=15)


lbl_lname = Label(text= 'Lname:',font='arial 11',bg= '#FFCC66')
lbl_lname.place(x=200,y=15)

lbl_city = Label(text= 'City:',font='arial 11',bg= '#FFCC66')
lbl_city.place(x=35,y=60)

lbl_search = Label(text= 'search:',font='arial 11',bg= '#FFCC66')
lbl_search.place(x= 15 , y = 105)

lbl_Tel = Label(text= 'Tel:',font='arial 11',bg= '#FFCC66')
lbl_Tel.place(x=225,y=60)

#========ENTRY========
ent_fname= Entry(width='15')
ent_fname.place(y=15,x=70)

ent_lname= Entry(width='15')
ent_lname.place(y=15,x=255)

ent_city= Entry(width='15')
ent_city.place(y=60,x=70)

ent_tel= Entry(width='15')
ent_tel.place(y=60,x=255)

ent_search = Entry(width= '15')
ent_search.place(y = 105,  x = 70)
#========List Box========
lstbox = Listbox(width= 30,height= 15)
lstbox.place(y= 130, x = 50)

#========Button========
btn_insert= Button(text='Insert',command=insert)
btn_insert.place(x=300,y=130)

btn_remove= Button(text='Remove',command=remove)
btn_remove.place(x=300,y=170)

btn_update= Button(text='Update',command= update)
btn_update.place(x=300,y=210)

btn_show= Button(text='Show',command= show)
btn_show.place(x=300,y=250)

btn_search= Button(text='Search',command= search)
btn_search.place(x=300,y=290)

btn_clear= Button(text='Clear Entry',command=clear)
btn_clear.place(x=300,y=330)

btn_exit= Button(text='Exit',command=exit)
btn_exit.place(x=300,y=370)



win.mainloop()