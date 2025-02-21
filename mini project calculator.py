# Simple Calculator
def main():
    print("Welcome to the Calculator: Less talk, more math.")
    print("You can perform the following operations:")
    print("Addition (+), Subtraction (-), Multiplication (*), Division (/)")
    print("Type 'q' to quit the calculator.")

    while True:
        # Asking for the operation that to be performed
        operation = input("\nEnter an operation (+, -, *, /) or 'q' to quit: ").strip()

        # Exit if the user types 'q'
        if operation == 'q':
            print("Thank you for using the calculator. Goodbye!")
            break

        # Check if the operation is valid
        if operation not in ['+', '-', '*', '/']:
            print("Error: Invalid operation! Please choose +, -, *, or /.")
            continue

        # Ask for the user input value
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Invalid input! Please enter numeric values.")
            continue

        # Perform the calculations
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!...Give valid input")
                continue
            result = num1 / num2

        # Display the result to the user
        print(f"Result: {num1} {operation} {num2} = {result}")

# TO run the calculator
if __name__ == "__main__":
    main()