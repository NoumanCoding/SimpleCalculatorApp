import math
import tkinter as tk

# OOP-based Calculator class
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b != 0:
            result = a / b
            self.history.append(f"{a} / {b} = {result}")
            return result
        else:
            self.history.append(f"{a} / {b} = Error! Division by zero.")
            return "Error! Division by zero."

    def show_history(self):
        print("\nHistory of calculations:")
        for record in self.history:
            print(record)

    def square_root(self, a):
        return math.sqrt(a)

    def power(self, a, b):
        return a ** b

    def trigonometric_operations(self):
        print("\nTrigonometric Functions:")
        angle = float(input("Enter the angle in degrees: "))
        radian = math.radians(angle)
        print(f"sin({angle}) = {math.sin(radian)}")
        print(f"cos({angle}) = {math.cos(radian)}")
        print(f"tan({angle}) = {math.tan(radian)}")

# Main CLI-based calculator
def calculator():
    calc = Calculator()
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Square Root")
        print("7. Power")
        print("8. Trigonometric Functions")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ")
        if choice == '9':
            print("Thank you for using the calculator. Goodbye!")
            break
        elif choice == '5':
            calc.show_history()
        elif choice == '6':
            num = float(input("Enter the number: "))
            print(f"Square root: {calc.square_root(num)}")
        elif choice == '7':
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the exponent: "))
            print(f"The result is: {calc.power(num1, num2)}")
        elif choice == '8':
            calc.trigonometric_operations()
        elif choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == '1':
                print(f"The result is: {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {calc.multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {calc.divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid option.")

# Run the calculator
if __name__ == "__main__":
    calculator()


# Optional GUI with Tkinter
class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.result_var = tk.StringVar()

        # Create input field for result display
        result_entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), borderwidth=2, relief="solid", width=20)
        result_entry.grid(row=0, column=0, columnspan=4)

        # Add buttons for each operation
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button("C", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 18), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col)

    def on_button_click(self, text):
        current_text = self.result_var.get()
        if text == "=":
            try:
                result = eval(current_text)  # Evaluate the math expression
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif text == "C":
            self.result_var.set("")
        else:
            self.result_var.set(current_text + text)

# Run the GUI version
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
