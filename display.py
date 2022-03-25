from tkinter import *
import parser
from math import factorial

i = 0

class   display(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculator")
        screen = Entry(self)
        screen.grid(row=1,columnspan=6,sticky=N+E+W+S)

        
        def clearAll():
            screen.delete(0,END)
        def errorCheck():
            if screen.get() == "Error":
                clearAll()
        def displayVariables(n):
            errorCheck()
            global i
            screen.insert(i, n)
            i += 1
        Button(self,text="1",command = lambda:displayVariables(1)).grid(row=2,column=0, sticky=N+S+E+W)
        Button(self,text=" 2 ",command = lambda:displayVariables(2)).grid(row=2,column=1, sticky=N+S+E+W)
        Button(self,text=" 3 ",command = lambda:displayVariables(3)).grid(row=2,column=2, sticky=N+S+E+W)
        Button(self,text="4",command = lambda:displayVariables(4)).grid(row=3,column=0, sticky=N+S+E+W)
        Button(self,text=" 5 ",command = lambda:displayVariables(5)).grid(row=3,column=1, sticky=N+S+E+W)
        Button(self,text=" 6 ",command = lambda:displayVariables(6)).grid(row=3,column=2, sticky=N+S+E+W)
        Button(self,text="7",command = lambda:displayVariables(7)).grid(row=4,column=0, sticky=N+S+E+W)
        Button(self,text=" 8 ",command = lambda:displayVariables(8)).grid(row=4,column=1, sticky=N+S+E+W)
        Button(self,text=" 9 ",command = lambda:displayVariables(9)).grid(row=4,column=2, sticky=N+S+E+W)
        Button(self,text=" 0 ",command = lambda:displayVariables(0)).grid(row=5,column=1, sticky=N+S+E+W)
        Button(self,text=" . ",command = lambda:displayVariables(".")).grid(row=5, column=2, sticky=N+S+E+W)
        Button(self,text="AC",command=lambda :clearAll()).grid(row=5,column=0, sticky=N+S+E+W)
        
        def check():
            if screen.get() == "":
                return False
            else:
                return True

        def displayOperator(operator):
            errorCheck()
            global i
            if check():
                length = len(operator)
                screen.insert(i,operator)
                i+=length
        Button(self,text=" + ",command= lambda:displayOperator("+")).grid(row=2,column=3, sticky=N+S+E+W)
        Button(self,text=" / ",command= lambda:displayOperator("/")).grid(row=5,column=3, sticky=N+S+E+W)
        Button(self,text=" - ",command= lambda:displayOperator("-")).grid(row=3,column=3, sticky=N+S+E+W)
        Button(self,text=" * ",command= lambda:displayOperator("*")).grid(row=4,column=3, sticky=N+S+E+W)
        Button(self,text="pi",command= lambda:displayOperator("*3.14")).grid(row=2,column=4, sticky=N+S+E+W)
        Button(self,text="%",command= lambda:displayOperator("%")).grid(row=3,column=4, sticky=N+S+E+W)
        Button(self,text="(",command= lambda:displayOperator("(")).grid(row=4,column=4, sticky=N+S+E+W)
        Button(self,text="exp",command= lambda:displayOperator("**")).grid(row=5,column=4, sticky=N+S+E+W)
        Button(self,text=")",command= lambda :displayOperator(")")).grid(row=4,column=5, sticky=N+S+E+W)
        Button(self,text="^2",command= lambda :displayOperator("**2")).grid(row=5,column=5, sticky=N+S+E+W)
        
        def undo():
            errorCheck()
            if check():
                string = screen.get()
                if len(string):
                    string2 = string[:-1]
                    clearAll()
                    screen.insert(0,string2)
                else:
                    clearAll()
                    screen.insert(0,"Error")
        Button(self,text="<-",command= lambda :undo()).grid(row=2,column=5, sticky=N+S+E+W)

        def fact():
            errorCheck()
            if check():
                string = screen.get()
                try:
                    result = factorial(int(string))
                    clearAll()
                    screen.insert(0,result)
                except Exception:
                    clearAll()
                    screen.insert(0,"Error")
        Button(self,text="x!", command= lambda: fact()).grid(row=3,column=5, sticky=N+S+E+W)

        def calculate():
            errorCheck()
            if check():
                string = screen.get()
                try:
                    a = parser.expr(string).compile()
                    result = eval(a)
                    clearAll()
                    screen.insert(0,result)
                except Exception:
                    clearAll()
                    screen.insert(0,"Error")
        Button(self,text="=",command= lambda :calculate()).grid(columnspan=6, sticky=N+S+E+W)
        self.mainloop()
        
