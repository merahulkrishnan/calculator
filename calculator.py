import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the display
        self.display = tk.Entry(master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create the buttons
        self.create_button('C', self.clear, 1, 0)
        self.create_button('%', self.percent, 1, 1)
        self.create_button('<-', self.backspace, 1, 2)
        self.create_button('/', self.divide, 1, 3)

        self.create_button('7', lambda: self.add_digit('7'), 2, 0)
        self.create_button('8', lambda: self.add_digit('8'), 2, 1)
        self.create_button('9', lambda: self.add_digit('9'), 2, 2)
        self.create_button('*', self.multiply, 2, 3)

        self.create_button('4', lambda: self.add_digit('4'), 3, 0)
        self.create_button('5', lambda: self.add_digit('5'), 3, 1)
        self.create_button('6', lambda: self.add_digit('6'), 3, 2)
        self.create_button('-', self.subtract, 3, 3)

        self.create_button('1', lambda: self.add_digit('1'), 4, 0)
        self.create_button('2', lambda: self.add_digit('2'), 4, 1)
        self.create_button('3', lambda: self.add_digit('3'), 4, 2)
        self.create_button('+', self.add, 4, 3)

        self.create_button('00', lambda: self.add_digit('00'), 5, 0)
        self.create_button('0', lambda: self.add_digit('0'), 5, 1)
        self.create_button('.', lambda: self.add_digit('.'), 5, 2)
        self.create_button('=', self.calculate, 5, 3)

        # Initialize variables
        self.first_operand = None
        self.operator = None

    def create_button(self, text, command, row, column):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16), command=command)
        button.grid(row=row, column=column, padx=5, pady=5)

    def add_digit(self, digit):
        self.display.insert(tk.END, digit)

    def clear(self):
        self.display.delete(0, tk.END)
        self.first_operand = None
        self.operator = None

    def percent(self):
        try:
            value = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(value / 100))
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def backspace(self):
        self.display.delete(len(self.display.get()) - 1, tk.END)

    def multiply(self):
        try:
            self.operator = '*'
            self.first_operand = float(self.display.get())
            self.display.delete(0, tk.END)
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def subtract(self):
        try:
            self.operator = '-'
            self.first_operand = float(self.display.get())
            self.display.delete(0, tk.END)
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def add(self):
        try:
            self.operator = '+'
            self.first_operand = float(self.display.get())
            self.display.delete(0, tk.END)
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def divide(self):
        try:
            self.operator = '/'
            self.first_operand = float(self.display.get())
            self.display.delete(0, tk.END)
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def calculate(self):
        try:
            second_operand = float(self.display.get())
            if self.operator == '+':
                result = self.first_operand + second_operand
            elif self.operator == '-':
                result = self.first_operand - second_operand
            elif self.operator == '*':
                result = self.first_operand * second_operand
            elif self.operator == '/':
                if second_operand == 0:
                    raise ZeroDivisionError
                result = self.first_operand / second_operand
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.first_operand = None
            self.operator = None
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
        except ZeroDivisionError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error: Division by zero")


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
