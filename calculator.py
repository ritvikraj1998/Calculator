from tkinter import *
from tkinter import ttk
from main import *


ex=""




def get_sum(event):
	global ex
	ex=ex+"+"
	sumEntry.delete(0, "end")
	sumEntry.insert(0, ex)
	
	

def get_diff(event):
	global ex
	ex=ex+"-"
	sumEntry.delete(0, "end")
	sumEntry.insert(0, ex)
	

def get_pro(event):
	global ex
	ex=ex+"*"
	sumEntry.delete(0, "end")
	sumEntry.insert(0, ex)
	

def get_div(event):
	global ex
	ex=ex+"/"
	sumEntry.delete(0, "end")
	sumEntry.insert(0, ex)
	
	
	
def equals(event):
	global ex

	
	re=solve(ex)
	sumEntry.delete(0, "end")
	sumEntry.insert(0,re)
	ex=str(re)

def i1(event):
	global ex
	ex=ex+"1"
	sumEntry.delete(0,"end")
	sumEntry.insert(0,ex)

def i2(event):
	global ex
	ex=ex+"2"
	sumEntry.delete(0,"end")
	sumEntry.insert(0,ex)

def i3(event):
	global ex
	ex=ex+"3"
	sumEntry.delete(0,"end")
	sumEntry.insert(0,ex)

def i4(event):
	global ex
	ex=ex+"4"
	sumEntry.delete(0,"end")
	sumEntry.insert(0,ex)

def i5(event):
	global ex
	ex=ex+"5"
	sumEntry.delete(0,"end")
	sumEntry.insert(0,ex)

def i6(event):
	global ex
	ex=ex+"6"
	sumEntry.delete(0,"end")
	sumEntry.insert(0,ex)

def i7(event):
	global ex
	ex=ex+"7"
	sumEntry.delete(0,"end")
	sumEntry.insert(0,ex)

def i8(event):
	global ex
	ex=ex+"8"
	sumEntry.delete(0,"end")
	sumEntry.insert(0,ex)

def i9(event):
	global ex
	ex=ex+"9"
	sumEntry.delete(0,"end")
	sumEntry.insert(0,ex)






root = Tk()



equalButton = Button(root, text = "=")
equalButton.bind("<Button-1>",equals)
equalButton.grid(column=3,row=1)

pButton = Button(root, text = "+")
pButton.bind("<Button-1>",get_sum)
pButton.grid(column=3,row=2)

mButton = Button(root, text = "-")
mButton.bind("<Button-1>",get_diff)
mButton.grid(column=3,row=3)

p1Button = Button(root, text = "*")
p1Button.bind("<Button-1>",get_pro)
p1Button.grid(column=3,row=4)


dButton = Button(root, text = "/")
dButton.bind("<Button-1>",get_div)
dButton.grid(column=3,row=5)


Button1 = Button(root, text = "1")
Button1.bind("<Button-1>",i1)
Button1.grid(column=0,row=1)

Button2 = Button(root, text = "2")
Button2.bind("<Button-1>",i2)
Button2.grid(column=1,row=1)

Button3 = Button(root, text = "3")
Button3.bind("<Button-1>",i3)
Button3.grid(column=2,row=1)

Button4 = Button(root, text = "4")
Button4.bind("<Button-1>",i4)
Button4.grid(column=0,row=2)

Button5 = Button(root, text = "5")
Button5.bind("<Button-1>",i5)
Button5.grid(column=1,row=2)

Button6 = Button(root, text = "6")
Button6.bind("<Button-1>",i6)
Button6.grid(column=2,row=2)

Button7 = Button(root, text = "7")
Button7.bind("<Button-1>",i7)
Button7.grid(column=0,row=3)

Button8 = Button(root, text = "8")
Button8.bind("<Button-1>",i8)
Button8.grid(column=1,row=3)

Button9 = Button(root, text = "9")
Button9.bind("<Button-1>",i9)
Button9.grid(column=2,row=3)


sumEntry= Entry(root)
sumEntry.grid(row =0, column =0)



root.mainloop()
