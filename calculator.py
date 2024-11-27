import math

# History list to store previous calculations
history = []

def add_to_history(calculation):
    history.append(calculation)

def show_history():
    print("Calculation History:")
    for item in history:
        print(item)

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    return math.factorial(n)

def calculator():
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Square Root")
        print("7. Power")
        print("8. Modulo")
        print("9. Factorial")
        print("10. Trigonometric Functions")
        print("11. Exit")

        try:
            choice = int(input("Enter your choice (1-11): "))
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 11.")
            continue

        if choice == 11:
            print("Exiting the calculator. Goodbye!")
            break
        elif choice == 5:
            show_history()
            continue
        
        # Handling invalid inputs for numeric operations
        try:
            if choice in [1, 2, 3, 4, 6, 7, 8]:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            elif choice == 9:
                num1 = int(input("Enter a number for factorial: "))
            elif choice == 10:
                angle = float(input("Enter the angle in degrees: "))
            else:
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if choice == 1:
            result = num1 + num2
            add_to_history(f"{num1} + {num2} = {result}")
            print(f"The result is: {result}")
        elif choice == 2:
            result = num1 - num2
            add_to_history(f"{num1} - {num2} = {result}")
            print(f"The result is: {result}")
        elif choice == 3:
            result = num1 * num2
            add_to_history(f"{num1} * {num2} = {result}")
            print(f"The result is: {result}")
        elif choice == 4:
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
                continue
            result = num1 / num2
            add_to_history(f"{num1} / {num2} = {result}")
            print(f"The result is: {result}")
        elif choice == 6:
            result = math.sqrt(num1)
            add_to_history(f"Square root of {num1} = {result}")
            print(f"The result is: {result}")
        elif choice == 7:
            result = math.pow(num1, num2)
            add_to_history(f"{num1} raised to the power of {num2} = {result}")
            print(f"The result is: {result}")
        elif choice == 8:
            result = num1 % num2
            add_to_history(f"{num1} % {num2} = {result}")
            print(f"The result is: {result}")
        elif choice == 9:
            result = factorial(num1)
            add_to_history(f"Factorial of {num1} = {result}")
            print(f"The result is: {result}")
        elif choice == 10:
            # Converting angle to radians for trigonometric functions
            radian_angle = math.radians(angle)
            sine = math.sin(radian_angle)
            cosine = math.cos(radian_angle)
            tangent = math.tan(radian_angle)
            add_to_history(f"Trigonometric values for {angle} degrees: sin = {sine}, cos = {cosine}, tan = {tangent}")
            print(f"Trigonometric values for {angle} degrees: sin = {sine}, cos = {cosine}, tan = {tangent}")
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    print("Welcome to the Simple Calculator App!")
    calculator()
