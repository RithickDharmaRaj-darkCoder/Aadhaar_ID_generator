# Learning Tkinter ...
from tkinter import *

def create_btn():
    name_info = name.get()
    age_info = str(age.get())
    mobile_info = str(mobile.get())

    # Creating a File ...
    file = open(f"{name_info}.txt","w")
    file.write(f'Name          : {name_info}')
    file.write(f'\nAge           : {age_info}')
    file.write(f'\nMobile Number : {mobile_info}')
    file.write(f'\nAadhaar ID    : {mobile_info[6:]} {mobile_info[:4]} {mobile_info[3:7]} {mobile_info[::3]}')
    file.close()
    print(f"{name_info}, you have created Aadhaar successfully!")

    # Deleting Entry Fields ...
    name_iput.delete(0,END)
    age_iput.delete(0,END)
    mobile_iput.delete(0,END)


screen = Tk()
screen.title('Aadhaar Management System')
screen.geometry('500x600')

# Label Section ...
heading = Label(text = ' AADHAAR  MANAGEMENT  SYSTEM ',bg='navyblue',fg='white',height=3,width=500)
heading.pack()
name = Label(text='Enter Your Name ',fg='blue')
name.place(x=20,y=100)
age = Label(text='Enter Your Age ',fg='blue')
age.place(x=20,y=150)
mobilNo = Label(text='Enter Your Mobile.No ',fg='blue')
mobilNo.place(x=20,y=200)

# Input Entry Section ...
# Datatype section ...
name = StringVar()
age = IntVar()
mobile = IntVar()

name_iput = Entry(textvariable=name)
name_iput.place(x=170,y=100,width=200)
age_iput = Entry(textvariable=age)
age_iput.place(x=170,y=150,width=200)
mobile_iput = Entry(textvariable=mobile)
mobile_iput.place(x=170,y=200,width=200)

# Button Section ...
submit = Button(text='CREATE',bg='green',fg='White',borderwidth=3,command=create_btn)
submit.place(x=270,y=250,width=100)





screen.mainloop()