from tkinter import *

class Window(object):
    def __init__(self):
        self.span = 4
        self.indSpan = 1
        self.win = Tk()
        self.frame = Frame(self.win)
        self.frame.pack()

        self.createButtons()
        self.createEntry()
        self.bindFunctions()
        
        self.win.mainloop()

    def createButtons(self):


        self.zeroButton = Button(self.frame, text="0", fg="black", command=lambda x='0':self.updateEntry(x))        
        self.oneButton = Button(self.frame, text="1", fg="black", command=lambda x='1':self.updateEntry(x))
        self.twoButton = Button(self.frame, text="2", fg="black", command=lambda x='2':self.updateEntry(x))
        self.threeButton = Button(self.frame, text="3", fg="black", command=lambda x='3':self.updateEntry(x))
        self.fourButton = Button(self.frame, text="4", fg="black", command=lambda x='4':self.updateEntry(x))
        self.fiveButton = Button(self.frame, text="5", fg="black", command=lambda x='5':self.updateEntry(x))
        self.sixButton = Button(self.frame, text="6", fg="black", command=lambda x='6':self.updateEntry(x))
        self.sevenButton = Button(self.frame, text="7", fg="black", command=lambda x='7':self.updateEntry(x))
        self.eightButton = Button(self.frame, text="8", fg="black", command=lambda x='8':self.updateEntry(x))
        self.nineButton = Button(self.frame, text="9", fg="black", command=lambda x='9':self.updateEntry(x))
        
        # first row
        self.oneButton.grid(row=4, column=1, columnspan=self.indSpan, ipadx=10, ipady=10, sticky='NESW')
        self.twoButton.grid(row=4, column=2, columnspan=self.indSpan, ipadx=10, ipady=10, sticky='NESW')
        self.threeButton.grid(row=4, column=3, columnspan=self.indSpan, ipadx=10, ipady=10, sticky='NESW')
        # second row
        self.fourButton.grid(row=3, column=1, columnspan=self.indSpan, ipadx=10, ipady=10, sticky='NESW')
        self.fiveButton.grid(row=3, column=2, columnspan=self.indSpan, ipadx=10, ipady=10, sticky='NESW')
        self.sixButton.grid(row=3, column=3, columnspan=self.indSpan, ipadx=10, ipady=10, sticky='NESW')
        # third row
        self.sevenButton.grid(row=2, column=1, columnspan=self.indSpan, ipadx=10, ipady=10, sticky='NESW')
        self.eightButton.grid(row=2, column=2, columnspan=self.indSpan, ipadx=10, ipady=10, sticky='NESW')
        self.nineButton.grid(row=2, column=3, columnspan=self.indSpan, ipadx=10, ipady=10, sticky='NESW')
        # fourth row
        self.zeroButton.grid(row=5, column=1, columnspan=self.span-1, sticky='NESW')

        # + - / * = buttons #
        self.plusButton = Button(self.frame, text="+", fg="black", command=lambda x="+":self.operator(x))
        self.minusButton = Button(self.frame, text="-", fg="black", command=lambda x="-":self.operator(x))
        self.divideButton = Button(self.frame, text="/", fg="black", command=lambda x="/":self.operator(x))
        self.multiplyButton = Button(self.frame, text="*", fg="black", command=lambda x="*":self.operator(x))
        self.equalButton = Button(self.frame, text="=", fg="black", command=lambda x="=":self.operator(x))
        self.clearButton = Button(self.frame, text="CE", fg="black", command=lambda x="CE":self.entry.delete(0, END))

        self.plusButton.grid(row=2, column=4, columnspan=self.indSpan, rowspan=2, ipadx=15, ipady=10, sticky='NESW')
        self.minusButton.grid(row=1, column=4, columnspan=self.indSpan, ipadx=15, ipady=10, sticky='NESW')
        self.divideButton.grid(row=1, column=2, columnspan=self.indSpan, ipadx=15, ipady=10, sticky='NESW')
        self.multiplyButton.grid(row=1, column=3, columnspan=self.indSpan, ipadx=15, ipady=10, sticky='NESW')
        self.equalButton.grid(row=4, column=4, columnspan=self.indSpan, rowspan=2, ipadx=15, ipady=10, sticky='NESW')
        self.clearButton.grid(row=1, column=1, columnspan=self.indSpan, ipadx=15, ipady=10, sticky='NESW')

    def createEntry(self):
        self.entry = Entry(self.frame, justify=RIGHT)
        self.entry.grid(row=0, column=1, columnspan=self.span, sticky='NESW')

    def updateEntry(self, x):
        self.entry.insert(END, x)

    def bindFunctions(self):
        self.frame.bind("<Return>", lambda event:self.updateEntry())

    def operator(self, x):
        if x != '=':
            self.entry.insert(END, x)
        else:
            text = self.entry.get()
            try:
                if '+' in text:
                    textArr = text.split('+')
                    self.execute('+', textArr[0], textArr[1])
                elif '-' in text:
                    textArr = text.split('-')
                    self.execute('-', textArr[0], textArr[1])
                elif '/' in text:
                    textArr = text.split('/')
                    self.execute('/', textArr[0], textArr[1])
                elif '*' in text:
                    textArr = text.split('*')
                    self.execute('*', textArr[0], textArr[1])
                else:
                    raise ValueError
            except ValueError:
                print('')
            try:
                x = textArr     # just using this to pull an error
            except UnboundLocalError:
                print('Value Error')

    def execute(self, operator, left, right):
        print (operator, left, right)
        try:
            self.entry.delete(0, END)  # delete the string in entry
            if operator == '+':
                ans = int(left) + int(right)
            elif operator == '-':
                ans = int(left) - int(right)
            elif operator == '/':
                ans = int(left) / int(right)
            elif operator == '*':
                ans = int(left) * int(right)
            self.entry.insert(END, ans)
        except ValueError:
            self.entry.delete(0, END)
            self.entry.insert(END, "ERROR")
            

if __name__=="__main__":
    Window()
