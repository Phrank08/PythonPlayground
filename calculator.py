from tkinter import Tk, Entry, Button, StringVar
"""Import necessary modules from tkinter for GUI components
"""

class Calculator:
    def __init__(self, master):
        master.title("Dev Frank's Calculator")  # Set the title of the window
        master.geometry('357x420+0+0')  # Set the size and position of the window
        master.config(bg='gray')    # Set the background color of the window
        master.resizable(False,False)   # Make the window non-resizable

        self.equation = StringVar()     # Create a StringVar to store the equation
        self.entry_value = ''   # Initialize the entry value as an empty string
        Entry(width = 17,bg='#ccddff',font=('Arial Bold',28), textvariable=self.equation).place(x=0,y=0)
        """
        # Create an Entry widget for displaying the equation
        """


        """ BUTTONS """
        """ Create buttons for different operations and numbers"""
        Button(width=11,height=4,text='(',relief='flat',bg='white',command=lambda:self.show('(')).place(x=0 ,y=50)
        Button(width=11,height=4,text=')',relief='flat',bg='white',command=lambda:self.show(')')).place(x=90 ,y=50)
        Button(width=11,height=4,text='%',relief='flat',bg='white',command=lambda:self.show('%')).place(x=180 ,y=50)
        Button(width=11,height=4,text='1',relief='flat',bg='white',command=lambda:self.show(1)).place(x=0 ,y=125)
        Button(width=11,height=4,text='2',relief='flat',bg='white',command=lambda:self.show(2)).place(x=90 ,y=125)
        Button(width=11,height=4,text='3',relief='flat',bg='white',command=lambda:self.show(3)).place(x=180 ,y=125)
        Button(width=11,height=4,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=0 ,y=200)
        Button(width=11,height=4,text='5',relief='flat',bg='white',command=lambda:self.show(5)).place(x=90 ,y=200)
        Button(width=11,height=4,text='6',relief='flat',bg='white',command=lambda:self.show(6)).place(x=180 ,y=200)
        Button(width=11,height=4,text='7',relief='flat',bg='white',command=lambda:self.show(7)).place(x=0 ,y=275)
        Button(width=11,height=4,text='8',relief='flat',bg='white',command=lambda:self.show(8)).place(x=180 ,y=275)
        Button(width=11,height=4,text='9',relief='flat',bg='white',command=lambda:self.show(9)).place(x=90 ,y=275)
        Button(width=11,height=4,text='0',relief='flat',bg='white',command=lambda:self.show(0)).place(x=90 ,y=350)
        Button(width=11,height=4,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=180 ,y=350)
        Button(width=11,height=4,text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=270 ,y=275)
        Button(width=11,height=4,text='-',relief='flat',bg='white',command=lambda:self.show('-')).place(x=270 ,y=200)
        Button(width=11,height=4,text='/',relief='flat',bg='white',command=lambda:self.show('/')).place(x=270 ,y=50)
        Button(width=11,height=4,text='x',relief='flat',bg='white',command=lambda:self.show('*')).place(x=270 ,y=125)
        Button(width=11,height=4,text='=',relief='flat',bg='lightblue',command=self.solve).place(x=270 ,y=350)
        Button(width=11,height=4,text='C',relief='flat',command=self.clear).place(x=0 ,y=350)

        """Each button has a command to call the 'show' method with the respective value. (similar buttons for other operations and numbers)
        """




    def show(self, value):
        """ 
        Method to append the clicked value to the entry
        """
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        """
        Method to clear the entry
        """
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        """
        Method to evaluate the expression and set the result in the entry
        """
        result = eval(self.entry_value)
        self.equation.set(result)

root = Tk()     # Create Tkinter root window
Calculator = Calculator(root)       # Create an instance of the Calculator class
root.mainloop()     # Run the Tkinter event loop