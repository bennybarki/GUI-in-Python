#!/usr/bin/env python
# coding: utf-8

# In[20]:




from tkinter import *
from tkinter import filedialog 
from tkinter import messagebox


def func(race,input):
    if race == input:
        return 100
    else:
        return 0
    
    
def firstName(name):
    file = open('FirstName.txt', 'w',encoding="utf-8")
    for s in name:
        
         file.write(
     
                 '{'+"\n"+
        f'"name" : "{s}",'+"\n"+
        '"categories" : ['+"\n"+
                 f'"{e4.get()}"'+"\n"+

        '],'+"\n"+
        '"usedin" : ['+"\n"+
        f'"{e5.get()}"'+"\n"+

        '],'+"\n"+
        f'"gender" : "{e6.get()}",'+"\n"+
        '"origins" : ['+"\n"+
                 f'"{e7.get()}"'+"\n"+

        '],'+"\n"+
        f'"migrationCode" : "{e2.get()}",'+"\n"+
        '"races" : ['+"\n"+
                 f'"{e8.get()}"'+"\n"+

        ']'+"\n"+
        '}'+"\n"+"\n"

         )
     
    file.close()  
    
    
def click_me_First():
    name = open_txt ()
    firstName(name)
    messagebox.showinfo(title='Message', message='Done!')    

def script_LastName(name,box):

    race_input=box
    white='white'
    black='black'
    asian='asian'
    hispanic='hispanic'
    native_american='native american'
    unknown='unknown'

    file = open('LastNameFile.txt', 'w',encoding="utf-8")
    
    
    for s in name:
         file.write(
    "{"+"\n"+
        f'"name" : "{s}",'+"\n"+
        '"masterName" : null,'+"\n"+
        '"count" : 100,'+"\n"+
        '"use" : true,'+"\n"+
        '"auto" : {'+"\n"+
            '"masterName" : null,'+"\n"+
            '"use" : true,'+"\n"+
            f'"race" : "{race_input}",'+"\n"+
            f'"lastUpdate" : ISODate("2020-{e1.get()}-{e.get()}T12:30:53.533Z")'+"\n"+
        '},'+"\n"+
        '"manual" : {'+"\n"+
            '"masterName" : null,'+"\n"+
            '"use" : true,'+"\n"+
            f'"race" : "{race_input}",'+"\n"+
            f'"lastUpdate" : ISODate("2020-{e1.get()}-{e.get()}T12:30:53.533Z")'+"\n"+
        '},'+"\n"+
       f'"created" : ISODate("2020-{e1.get()}-{e.get()}T11:27:12.083Z"),'+"\n"+
        f'"lastUpdate" : ISODate("2020-{e1.get()}-{e.get()}T12:30:53.533Z"),'+"\n"+
        f'"race" : "{race_input}",'+"\n"+
        '"races" : [' +"\n"+
            '{'+"\n"+
                f'"white" : {func(white,race_input)}'+"\n"+
            '},' +"\n"+
            '{'+"\n"+
                f'"black" : {func(black,race_input)}'+"\n"+
            '},' +"\n"+
            '{'+"\n"+
                f'"asian" : {func(asian,race_input)}'+"\n"+
            '},' +"\n"+
            '{'+"\n"+
                f'"hispanic" : {func(hispanic,race_input)}'+"\n"+
            '},' +"\n"+
            '{'+"\n"+
                f'"native american" : {func(native_american,race_input)}'+"\n"+
            '},' +"\n"+
            '{'+"\n"+
                f'"unknown" : {func(unknown,race_input)}'+"\n"+
            '}'+"\n"+
        ']'+"\n"+
    '}'+"\n"+"\n"
     )
    file.close()  
    
    
name=[]

def clear ():
    tbox1.delete(1.0,END)
    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    
    
def open_txt ():
    text_file = filedialog.askopenfilename()
    name = load (text_file)
    text_file = open(text_file,'r')
    stuff = text_file.read()
    tbox1.insert(END,stuff)
    text_file.close()
    return name
    
def load(a):
    text_file = open(a,'r')
    name1 = [line.split(',') for line in text_file.readlines()]    
    name1 = name1[0]
    text_file.close()
    #global name
    #name=name1
    return name1

def click_me_white():
    name = open_txt ()
    script_LastName(name,'white') 
    messagebox.showinfo(title='Message', message='Done!')
    
def click_me_asian():
    name = open_txt ()
    script_LastName(name,'asian')
    messagebox.showinfo(title='Message', message='Done!')

    
def click_me_black():
    name = open_txt ()
    script_LastName(name,'black')
    messagebox.showinfo(title='Message', message='Done!')

    
def click_me_his():
    name = open_txt ()
    script_LastName(name,'hispanic')
    messagebox.showinfo(title='Message', message='Done!')
    
def click_me_na():
    name = open_txt ()
    script_LastName(name,'native american')
    messagebox.showinfo(title='Message', message='Done!')
    
def click_me_un():
    name = open_txt ()
    script_LastName(name,'unknown')
    messagebox.showinfo(title='Message', message='Done!')
    


root = Tk()
root.title("Script For Insert First&Last Names")
frame=Frame(root, width=750, height=350)
frame.pack()

#Last Name

text3 = Label(text="Last Name:",font='Helvetica 12 bold')
text3.place(x=10, y=10)

text2 = Label(text="Day")
text2.place(x=10 ,y=30)
e = Entry(frame)
e.place(x=10, y=50, height=20, width=20)


text2 = Label(text="Month")
text2.place(x=40, y=30)
e1 = Entry(frame)
e1.place(x=40, y=50, height=20, width=20)


button1 = Button(frame, text="White",command=click_me_white,activebackground='#00ff00')
button1.place(x=10, y=90, height=30, width=100)

button2 = Button(frame, text="Asian",command=click_me_asian,activebackground='#00ff00')
button2.place(x=10, y=130, height=30, width=100)

button3 = Button(frame, text="Black",command=click_me_black,activebackground='#00ff00')
button3.place(x=10, y=170, height=30, width=100)

button4 = Button(frame, text="Hispanic",command=click_me_his,activebackground='#00ff00')
button4.place(x=10, y=210, height=30, width=100)

button5 = Button(frame, text="Native American",command=click_me_na,activebackground='#00ff00')
button5.place(x=10, y=250, height=30, width=100)

button6 = Button(frame, text="Unknown",command=click_me_un,activebackground='#00ff00')
button6.place(x=10, y=290, height=30, width=100)





text1 = Label(text="List Of Names:")
text1.place(x=255, y=10)
tbox1 = Text(frame)
tbox1.place(x=150, y=40, height=250, width=300)

button7 = Button(frame, text="Clear",bg='#F3A59F',command=clear,font=('Arial', 12))
button7.place(x=250 ,y=300, height=30, width=120)



#First Name

text3 = Label(text="First Name:",font='Helvetica 12 bold')
text3.place(x=500, y=10)

text2 = Label(text="MigrationCode - Name")
text2.place(x=590 ,y=50)
e2 = Entry(frame)
e2.place(x=500, y=50, height=20, width=80)


text4 = Label(text="Category")
text4.place(x=590 ,y=80)
e4 = Entry(frame)
e4.place(x=500, y=80, height=20, width=80)

text5 = Label(text="Usedin")
text5.place(x=590 ,y=110)
e5 = Entry(frame)
e5.place(x=500, y=110, height=20, width=80)

text6 = Label(text="Gender")
text6.place(x=590 ,y=140)
e6 = Entry(frame)
e6.place(x=500, y=140, height=20, width=80)

text7 = Label(text="Origin")
text7.place(x=590 ,y=170)
e7 = Entry(frame)
e7.place(x=500, y=170, height=20, width=80)

text8 = Label(text="Race")
text8.place(x=590 ,y=200)
e8 = Entry(frame)
e8.place(x=500, y=200, height=20, width=80)

button9 = Button(frame, text="Go!",command=click_me_First,font=('Arial', 12),activebackground='#00ff00')
button9.place(x=500 ,y=230, height=30, width=80)



root.mainloop()    

