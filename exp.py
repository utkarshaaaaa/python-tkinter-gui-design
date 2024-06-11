from tkinter import *
r = Tk()
def tab1():
    r.title("name ")
    o=Entry(r,width =20)
    o.pack()
    v = Entry(r,width=23)
    v.pack()
    surrr= Label(r,text=" sur name ")
    surrr.pack()
    new = Label(r,text="")
    new.pack() 

    
    def tab2():
       
        lab.destroy()
        but1.destroy()
        surrr.destroy()
        
        
        my.destroy()
        butr.destroy()
        lab1= Label(r,text = "this is the second tab",font = ('Times_New_Roman'))
        lab1.pack()
        def back():
            lab1.destroy()
            but2.destroy()
            tab1()
        but2=Button(r,text="BACK",font = ('Times_New_Roman',25),command = back)
        but2.pack(side = BOTTOM)
    lab= Label(r,text = "Enter your name",font = ('Times_New_Roman'))
    lab.pack()
    e = Entry(r,width=23)
    e.pack()
    my = Label(r,text=" welcome  " +   e.get())
    my.pack()
    butr= Button(r,text="click to proceed",command=e.get )
    butr.pack()
    but1=Button(r,text="NEXT",font = ('Times_New_Roman',25),command=tab2)
    but1.pack(side = BOTTOM)
    
        
tab1()


r.mainloop()
