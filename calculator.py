# Simple Calculator App

# Functions for arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Error! Division by zero.")
    return a / b

# Main calculator function
def calculator():
    history = []  # To store the operation history

    print(f"\n{'='*40}")
    print("Welcome to the Simple Calculator App!")
    print("Options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("6. View History")
    print(f"{'='*40}\n")
    
    while True:
        choice = input("\nEnter your choice (1-6): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        elif choice == '6':
            if history:
                print("\nCalculation History:")
                for entry in history:
                    print(entry)
            else:
                print("No calculations yet!")
        
        elif choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                result = None
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                
                if result is not None:
                    print(f"The result is: {result}")
                    # Add to history
                    operation = f"{num1} {'+' if choice == '1' else '-' if choice == '2' else '*' if choice == '3' else '/'} {num2} = {result}"
                    history.append(operation)
            except ValueError as e:
                print(f"Error: {e}")
            except Exception:
                print("Something went wrong! Please try again.")
        else:
            print("Invalid choice! Please select a valid option.")

# Run the calculator
if __name__ == "__main__":
    calculator()
