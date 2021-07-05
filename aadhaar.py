# Learning Tkinter ...
try:
    import os
    from tkinter import *
    from tkinter import messagebox as box
    def create_btn():
        name_info = name.get()
        mname_info = mname.get()
        lname_info = lname.get()
        age_info = str(age.get())
        mobile_info = str(mobile.get())

        # Error Calling ...
        if name_info == "" or age_info == "" or mobile_info == "":
            box.showwarning('Warning','Please!, fill everything.')
        elif name_info.isalpha() == False:
            box.showerror('Error','Invalid First Name!')
        elif mname_info and (mname_info.isalpha() == False):
            box.showerror('Error', 'Invalid Middle Name!')
        elif lname_info and (lname_info.isalpha() == False):
            box.showerror('Error', 'Invalid Last Name!')
        elif len(mobile_info) != 10:
            box.showerror('Error','Invalid Mobile Number')
        else:
            try:
                age1 = int(age_info)
                mobile1 = int(mobile_info)

                # Creating a File ...
                if os.path.exists(f'./{mobile_info}.txt') == True:
                    box.showinfo('Info','Mobile Number Already used!')
                else:
                    file = open(f"{mobile_info}.txt", "w")
                    file.write(f'Name          : {name_info} {mname_info} {lname_info}')
                    file.write(f'\nAge           : {age_info}')
                    file.write(f'\nMobile Number : {mobile_info}')
                    file.write(f'\nAadhaar ID    : {mobile_info[6:]} {mobile_info[:4]} {mobile_info[3:7]} {mobile_info[::3]}')
                    file.close()
                    print(f"{name_info}, you have created Aadhaar successfully!")

                    # Deleting Entry Fields ...
                    name_iput.delete(0, END)
                    mname_iput.delete(0, END)
                    lname_iput.delete(0, END)
                    age_iput.delete(0, END)
                    mobile_iput.delete(0, END)
            except ValueError:
                box.showerror('Error!','Age and Mobile.No should be in digits!')


    screen = Tk()
    screen.title('Aadhaar Management System')
    screen.geometry('500x600')

    # Label Section ...
    heading = Label(text = ' AADHAAR  MANAGEMENT  SYSTEM ',bg='navyblue',fg='white',height=3,width=500,font=('TimesnewRoman',16,'bold'))
    heading.pack()
    name = Label(text='Enter First Name ',fg='blue')
    name.place(x=20,y=100)
    mname = Label(text='Enter Middle Name ',fg='blue')
    mname.place(x=20, y=150)
    lname = Label(text='Enter Last Name ', fg='blue')
    lname.place(x=20, y=200)
    age = Label(text='Enter Your Age ',fg='blue')
    age.place(x=20,y=250)
    mobilNo = Label(text='Enter Your Mobile.No ',fg='blue')
    mobilNo.place(x=20,y=300)

    # Input Entry Section ...
    # Datatype section ...
    name = StringVar()
    mname = StringVar()
    lname = StringVar()
    age = StringVar()
    mobile = StringVar()

    name_iput = Entry(textvariable=name,font=('TimesnewRoman',10,'bold'))
    name_iput.place(x=170,y=100,width=200)
    mname_iput = Entry(textvariable=mname,font=('TimesnewRoman',10,'bold'))
    mname_iput.place(x=170, y=150, width=200)
    lname_iput = Entry(textvariable=lname,font=('TimesnewRoman',10,'bold'))
    lname_iput.place(x=170, y=200, width=200)
    age_iput = Entry(textvariable=age,font=('TimesnewRoman',10,'bold'))
    age_iput.place(x=170,y=250,width=200)
    mobile_iput = Entry(textvariable=mobile,font=('TimesnewRoman',10,'bold'))
    mobile_iput.place(x=170,y=300,width=200)

    # Button Section ...
    submit = Button(text='CREATE',bg='green',fg='White',borderwidth=3,command=create_btn,font=('TimesnewRoman',10,'bold'))
    submit.place(x=270,y=350,width=100)


    screen.mainloop()
except ValueError:
    box.showerror('Error','Something Went Wrong')