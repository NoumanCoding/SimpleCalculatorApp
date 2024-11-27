# Simple Calculator App

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the Simple Calculator App!")
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == '1':
                    print(f"The result is: {add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result is: {divide(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numerical values.")
        else:
            print("Invalid choice! Please select a valid option.")
            
# Run the calculator
if __name__ == "__main__":
    calculator()
