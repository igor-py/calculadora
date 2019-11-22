# coding=utf-8
from tkinter import *
from calcular import *


class Calculadora(object):
    def __init__(self, instancia):
        # Expression that will be used with visor
        self.Expressao = StringVar()
        self.temp = StringVar()
        # Variable that will be used to concatenate expression
        self.exp = ''
        self.lst = ['+', '(', ')', '-', '/', '*', '^']
        self.equation = []
        # visor 1
        self.visor1 = Entry(instancia, bg='black', bd=21,
                            insertwidth=4, width=24,
                            fg='#BD8D2B',
                            textvariable=self.Expressao,
                            font=("Verdana", 20, "bold"),
                            justify=RIGHT)
        # Pack visor as grid
        self.visor1.grid(row=0, columnspan=6)
        self.Expressao.set('0')
        # Visor 2
        self.visor2 = Entry(instancia, bg='blue',
                            bd=21, fg='white',
                            insertwidth=4, width=24,
                            textvariable=self.temp,
                            font=("Verdana", 20, "bold"),
                            justify=RIGHT)
        # Pack visor as grid
        self.visor2.grid(row=1, columnspan=6)

        # Defining Buttons
        # ----------- Numbers ------------

        # 0
        self.b0 = Button(instancia, bg="yellow", bd=20,
                         text="0", width=2, height=1,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.button_click('0'))
        self.b0.grid(row=5, column=0, sticky=W)

        # 1
        self.b1 = Button(instancia, bg="yellow", bd=20,
                         text="1", width=2, height=1,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.button_click('1'))
        self.b1.grid(row=4, column=2, sticky=W)

        # 2
        self.b2 = Button(instancia, bg="yellow", bd=20,
                         text="2", width=2, height=1,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.button_click('2'))
        self.b2.grid(row=4, column=1, sticky=W)

        # 3
        self.b3 = Button(instancia, bg="yellow", bd=20,
                         text="3", width=2, height=1,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.button_click('3'))
        self.b3.grid(row=4, column=0, sticky=W)

        # 4
        self.b4 = Button(instancia, bg="yellow", bd=20,
                         text="4", width=2, height=1,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.button_click('4'))
        self.b4.grid(row=3, column=2, sticky=W)

        # 5
        self.b5 = Button(instancia, bg="yellow", bd=20,
                         text="5", width=2, height=1,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.button_click('5'))
        self.b5.grid(row=3, column=1, sticky=W)

        # 6
        self.b6 = Button(instancia, bg="yellow", bd=20,
                         text="6", width=2, height=1,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.button_click('6'))
        self.b6.grid(row=3, column=0, sticky=W)

        # 7
        self.b7 = Button(instancia, bg="yellow", bd=20,
                         text="7", width=2, height=1,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.button_click('7'))
        self.b7.grid(row=2, column=2, sticky=W)

        # 8
        self.b8 = Button(instancia, bg="yellow", bd=20,
                         text="8", width=2, height=1,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.button_click('8'))
        self.b8.grid(row=2, column=1, sticky=W)

        # 9
        self.b9 = Button(instancia, bg="yellow", bd=20,
                         text="9", width=2, height=1,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.button_click('9'))
        self.b9.grid(row=2, column=0, sticky=W)

        # -------- Operators ---------------

        # +
        self.soma = Button(instancia, bg="red", bd=20,
                           text="+", width=2, height=1,
                           font=("Arial", 20, "bold"),
                           command=lambda: self.button_click('+'))
        self.soma.grid(row=2, column=4, sticky=W)

        # -
        self.diminuir = Button(instancia, bg="red", bd=20,
                               text="-", width=2, height=1,
                               font=("Arial", 20, "bold"),
                               command=lambda: self.button_click('-'))
        self.diminuir.grid(row=3, column=4, sticky=W)

        # /
        self.div = Button(instancia, bg="red", bd=20,
                          text="÷", width=2, height=1,
                          font=("Arial", 20, "bold"),
                          command=lambda: self.button_click('/'))
        self.div.grid(row=4, column=4, sticky=W)

        # *
        self.mult = Button(instancia, bg="red", bd=20,
                           text="X", width=2, height=1,
                           font=("Arial", 20, "bold"),
                           command=lambda: self.button_click('*'))
        self.mult.grid(row=5, column=4, sticky=W)

        # ^
        self.el = Button(instancia, bg="red", bd=20,
                         text="x²", width=2, height=1,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.button_click('^'))
        self.el.grid(row=2, column=5, sticky=W)

        # (
        self.par1 = Button(instancia, bg="red", bd=20,
                           text="(", width=2, height=1,
                           font=("Arial", 20, "bold"),
                           command=lambda: self.button_click('('))
        self.par1.grid(row=3, column=5, sticky=W)

        # )
        self.par2 = Button(instancia, bg="red", bd=20,
                           text=")", width=2, height=1,

                           font=("Arial", 20, "bold"),
                           command=lambda: self.button_click(')'))
        self.par2.grid(row=4, column=5, sticky=W)

        # .
        self.point = Button(instancia, bg="red", bd=20,
                            text=".", width=2, height=1,
                            font=("Arial", 20, "bold"),
                            command=lambda: self.button_click('.'))
        self.point.grid(row=5, column=5, sticky=W)

        # Button to clear everything in the visor
        self.c = Button(instancia, bg="green", bd=20,
                        text="C", width=2, height=1, padx=6,
                        font=("Arial", 20, "bold"),
                        command=lambda: self.clear(1))
        self.c.grid(row=4, column=3, sticky=W)

        # Button to clear last entry in the visor
        self.ce = Button(instancia, bg="green", bd=20,
                         text="CE", width=2, height=1, padx=6,
                         font=("Arial", 20, "bold"),
                         command=lambda: self.clear(0))
        self.ce.grid(row=5, column=3, sticky=W)

        # Solve expression with this button
        self.sol = Button(instancia, bg="green", bd=20,
                          text="=", width=6, height=1,
                          padx=8, pady=3,
                          font=("Arial", 20, "bold"),
                          command=lambda: self.calculate())
        self.sol.grid(row=5, column=1, sticky=W, columnspan=2)

        # Button to clear visor 1
        self.cup = Button(instancia, bg='black', bd=20, padx=6,
                          text='⌫ ',  width=2, height=1, fg='#BD8D2B',
                          font=('Arial', 20, 'bold'), command=lambda: self.clear(2))
        self.cup.grid(row=2, column=3)

        # Button to get result from visor 1
        self.rs = Button(instancia, bg='black', bd=20, padx=6,
                         text='▼',  width=2, height=1, fg='#BD8D2B',
                         font=('Arial', 20, 'bold'), command=lambda: self.get_result())
        self.rs.grid(row=3, column=3, sticky=W)

    # Space for functions that will be used with command
    def button_click(self, st):
        if st in self.lst:
            st = ' ' + st + ' '
            self.equation.append('-->')
        self.exp += st
        self.temp.set(self.exp)

    # Solve expression
    def calculate(self):
        # Solution to handle inputs that come straight from keyboard
        if self.exp is '':
            self.exp = self.visor2.get()
            s = ''
            for token in self.exp:
                if token in self.lst:
                    s = s + ' ' + token + ' '
                else:
                    s = s + token
            self.exp = s
        # Using the class Calcular to solve equation
        try:
            d = Calcular(self.exp.split())
            exp = d.evaluate_exp()
            self.Expressao.set(str(exp))
            self.exp = str(exp)
            self.temp.set('')
            self.exp = ''
        except SyntaxError:
            self.Expressao.set('Expressão não aceita')
            self.exp = ''
            self.temp.set('')

    # Clear visor
    def clear(self, i):
        if len(self.exp) == 0 and i != 2:
            self.Expressao.set('Não há digito a ser apagado')
            return
        if i == 0:
            if len(self.exp) == 1:
                self.exp = ''
                self.temp.set(self.exp)
            elif self.exp[-2] == ' ' or self.exp[-1] == ' ':
                self.exp = self.exp[:-2]
                self.temp.set(self.exp)
            else:
                self.exp = self.exp[:-1]
                self.temp.set(self.exp)
        # To clear visor 1
        elif i == 2:
            self.Expressao.set('0')
        else:
            self.exp = ''
            self.temp.set(self.exp)

    def get_result(self):
        self.exp = self.visor1.get()
        self.temp.set(self.exp)
        self.Expressao.set('0')

    # End of class
    pass


if __name__ == '__main__':
    tela = Tk()
    # Initialize the calculator
    c = Calculadora(tela)
    # Change App title and Define grid
    tela.title('Calculadora')
    tela.grid()
    # Fix calculator window size
    tela.resizable(width=FALSE, height=FALSE)
    # Close window
    tela.mainloop()
