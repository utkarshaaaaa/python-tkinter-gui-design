from tkinter import *
r = Tk()

def tab1():
    e = Entry(r,width=20)
    e.pack()
    def tab2():
        lab.destroy()
        but1.destroy()
        e.destroy()
        butr.destroy()
        lab1= Label(r,text = "U",font = ('Times_New_Roman'))
        lab1.pack()
        def back():
            lab1.destroy()
            but2.destroy()
            e.destroy()
            
            tab1()
        but2=Button(r,text="BACK",font = ('Times_New_Roman',12),command = back)
        but2.pack(side = BOTTOM)
        
    lab= Label(r,text = "Enter your name",font = ('Times_New_Roman'))
    lab.pack()
    
    
    butr= Button(r,text="exit",command=r.quit )
    butr.pack()
    but1=Button(r,text="NEXT",font = ('Times_New_Roman',25),command=tab2)
    but1.pack(side = BOTTOM)
tab1()


r.mainloop()

