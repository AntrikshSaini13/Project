print("Hello project")

from tkinter import *
#some usefull variables

font=("Arial",22)

#important function

def show(a):
    btn=a.widget
    Text=btn["text"]
    print(Text)

    if Text=="x":
        textfield.insert(END,"*")
        return

    if Text=="=":
        try:
            ex=textfield.get()
            answer=eval(ex)
            textfield.delete(0,END)
            textfield.insert(0,answer)
        except Exception as e:
            print("ERROR",e)
            showerror("ERROR",e)
        return

    textfield.insert(END,Text)

def showAC(a):
    textfield.delete(0,END)

def showBack(a):
    ex=textfield.get()
    ex=ex[0:len(ex)-1]
    textfield.delete(0,END)
    textfield.insert(0,ex)

#Creating a Windows
window=Tk()
window.geometry("450x450")
window.resizable(0,0)
window.configure(background="black")

#Create a Picture Label
headingLabel=Label(window,text="My Calculater",font=font,underline=0,bg="yellow",fg="black")
headingLabel.pack(side=TOP,pady=10)

#Textfield Entry
textfield=Entry(window,font=font,justify=CENTER,fg="blue",bg="yellow")
textfield.pack(side=TOP,pady=10,fill=X,padx=10)

# Button Frame
buttonFrame=Frame(window,bg="yellow")
buttonFrame.pack(side=TOP)

# Adding Botton loop

temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp),font=font,width="5",relief="ridge",bg="black",fg="yellow",activebackground="blue")
        btn.grid(row=i,column=j,padx=3,pady=3)
        btn.bind("<Button>",show)
        temp += 1

# add seperate button
Zero_btn=Button(buttonFrame,text="0",font=font,width="5",relief="ridge",bg="black",fg="yellow",activebackground="blue")
Zero_btn.grid(row=3,column=0,padx=3,pady=3)
Zero_btn.bind("<Button>",show)

Decimal_btn=Button(buttonFrame,text=".",font=font,width="5",relief="ridge",bg="black",fg="yellow",activebackground="blue")
Decimal_btn.grid(row=3,column=1,padx=3,pady=3)
Decimal_btn.bind("<Button>",show)

Equal_to_btn=Button(buttonFrame,text="=",font=font,width="5",relief="ridge",bg="black",fg="yellow",activebackground="blue")
Equal_to_btn.grid(row=3,column=2,padx=3,pady=3)
Equal_to_btn.bind("<Button>",show)

Add_btn=Button(buttonFrame,text="+",font=font,width="5",relief="ridge",bg="black",fg="yellow",activebackground="blue")
Add_btn.grid(row=0,column=4,padx=3,pady=3)
Add_btn.bind("<Button>",show)

Sub_btn=Button(buttonFrame,text="-",font=font,width="5",relief="ridge",bg="black",fg="yellow",activebackground="blue")
Sub_btn.grid(row=1,column=4,padx=3,pady=3)
Sub_btn.bind("<Button>",show)

Mul_btn=Button(buttonFrame,text="x",font=font,width="5",relief="ridge",bg="black",fg="yellow",activebackground="blue")
Mul_btn.grid(row=2,column=4,padx=3,pady=3)
Mul_btn.bind("<Button>",show)

Div_btn=Button(buttonFrame,text="/",font=font,width="5",relief="ridge",bg="black",fg="yellow",activebackground="blue")
Div_btn.grid(row=3,column=4,padx=3,pady=3)
Div_btn.bind("<Button>",show)

Back_btn=Button(buttonFrame,text="Back",font=font,width="11",relief="ridge",bg="black",fg="yellow",activebackground="blue")
Back_btn.grid(row=4,column=0,columnspan=2,padx=3,pady=3)
Back_btn.bind("<Button>",showBack)

AC_btn=Button(buttonFrame,text="AC",font=font,width="11",relief="ridge",bg="black",fg="yellow",activebackground="blue")
AC_btn.grid(row=4,column=2,columnspan=4,padx=3,pady=3)
AC_btn.bind("<Button>",showAC)

window.mainloop()
