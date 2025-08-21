# Simple Calculator Program
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:  # Check for division by zero
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

# Function to run the calculator(ROOT)
def main():
    # Asking the user for inputs
    try:
        num1 = float(input("Enter the first number: "))  # First number
        num2 = float(input("Enter the second number: "))  # Second number
        operation = input("Enter the operation (+, -, *, /): ")  # Operation

        # Function to perform the calculation
        result = calculate(num1, num2, operation)

        # Display the result
        if isinstance(result, str):  # Check if the result is an error message
            print(result)
        else:
            print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the main function for confirmation
if __name__ == "__main__":
    main()
