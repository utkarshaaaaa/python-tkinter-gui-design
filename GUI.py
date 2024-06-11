from tkinter import *
c = "1234"
r = Tk()
r.title("name ")
o=Entry(r,width =20)
o.grid(row=2,column=3)
v = Entry(r,width=23)
v.grid(row=50,column=52)
myy = Label(r,text="Enter your name:   ",font = ('Times_New_Roman'))
surrr= Label(r,text=" sur name ")
surrr.grid(row=2,column =2)
new = Label(r,text="")
new.grid(row=5,column=5)
myy.grid(row=0,column=2)
e = Entry(r,width = 20)
e.grid(row=0,column=3)
def key():
    my = Label(r,text=" welcome  " +   e.get()+ o.get()+ "\n press >> to proceed :  ",width=23)
    hello = "hello "+e.get()
    my.grid(row=5,column=3)   
    def forward():
        global fr
        global bc
my= Button(r,text="click to proceed",command = key )
my.grid(row=3,column=3)
yu= Button(r,text= "exit program",command= r.quit)
yu.grid(row=2,column=10)
fr = Button(r,text="<<")
fr.grid(row=5,column=1 )
def sec():
    pas= Label(r,text="Enter  yr password :  "+ v.get())
    pas.grid(row=12,column=7)
    if v ==c:
            print(" correct")  
    
bc = Button(r,text=">>" ,command = sec)
bc.grid(row =2,column=5)
r.mainloop()