from tkinter import *

class UserInterface(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry('324x370')
        self.keepTrack = 0              # keep track of if it should be int or operator
        self.operators = ['/', '*', '-', '+']
        #
        self.createLayout()
        self.operatorButtons()
        self.createButtons()
        #
        self.root.mainloop()

    def createLayout(self):
        # self.createButtons
        self.txt = Entry(self.root, width=50, justify=RIGHT)
        self.txt.grid(row=0, column=0, columnspan=4, ipadx=10)

    def operatorButtons(self):
        #
        self.clear = Button(self.root, text='CE', height=2, width=10, command=lambda x='CE': self.updateCalculator(x))
        self.clear.grid(row=2, column=0)
        #
        for i in range(1, 4):
            temp = Button(self.root, text=self.operators[i-1], height=2, width=10, command=lambda x=self.operators[i-1]: self.updateCalculator(x))
            temp.grid(row=2, column=i)
        plusButton = Button(self.root, text=self.operators[3], height=10, width=10, command=lambda x=self.operators[3]: self.updateCalculator(x))
        plusButton.grid(row=3, column=3, rowspan=2, ipadx=0, ipady=5)

        self.equal = Button(self.root, text='=', height=8, width=10, command=lambda x='=': self.updateCalculator(x))
        self.equal.grid(row=5, column=3, rowspan=2, ipadx=0, ipady=5)

    def createButtons(self):
        i, k = 2, 9
        for i in range(3, 6):
            for j in range(2, -1, -1):
                x = Button(self.root, text=k, height=5, width=10, command=lambda x=k: self.updateCalculator(x))
                x.grid(row=i, column=j)
                k -= 1
        zero = Button(self.root, text='0', height=3, width=30, command=lambda x=k: self.updateCalculator(x))
        zero.grid(row=6, column=0, columnspan=3, ipadx=11)

    def updateCalculator(self, x):
        # if they click clear -> delete the string
        if x == 'CE':
            self.txt.delete(0, END)
            return
        elif x == '=':
            temp = self.txt.get()
            temp = temp.split()
            # delete
            self.txt.delete(0, END)
            self.calculate(temp)
            return
        else:
            if x in self.operators:
                self.txt.insert(END, ' ')
                self.txt.insert(END, x)
                self.txt.insert(END, ' ')
                return
            else:
                self.txt.insert(END, x)

    #
    def calculate(self, x):
        if len(x) > 3 or len(x) < 3:
            self.txt.delete(0, END)
            self.txt.insert(END, 'ERROR')
            return
        ## ## ## ## ## ## ## ## ## ## ##
        if x[1] in self.operators:
            try:
                x[0] = float(x[0])
                x[2] = float(x[2])
            except ValueError:
                self.txt.insert(END, 'ERROR')
            ######
            self.c = Calculator(x[0], x[2])
            ######
            if x[1] == '/':
                self.txt.insert(END, str(self.c.divide()))
            elif x[1] == '*':
                self.txt.insert(END, str(self.c.multiply()))
            elif x[1] == '-':
                self.txt.insert(END, str(self.c.subtract()))
            elif x[1] == '+':
                self.txt.insert(END, str(self.c.add()))
            else:
                self.txt.insert(END, 'ERROR')
        else:
            self.txt.insert(END, 'ERROR')

################################################################################
class Calculator(object):
    def __init__(self, n1, n2):
        self.n1, self.n2 = n1, n2

    def add(self):
        return self.n1 + self.n2

    def subtract(self):
        return self.n1 - self.n2

    def multiply(self):
        return self.n1 * self.n2

    def divide(self):
        if self.n2 == 0:
            return "ERROR"
        elif self.n1 == 0:
            return 0
        else:
            return self.n1 / self.n2

if __name__=="__main__":
    win = UserInterface()
