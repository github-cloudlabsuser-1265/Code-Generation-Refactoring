# Create a basic calculator
def add(x, y):
    """Add two numbers."""
    return x + y
def subtract(x, y):
    """Subtract two numbers."""
    return x - y
def multiply(x, y):
    """Multiply two numbers."""
    return x * y
def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
def calculator(x, y, operation):
    """Perform a calculation based on the operation."""
    if operation == 'add':
        return add(x, y)
    elif operation == 'subtract':
        return subtract(x, y)
    elif operation == 'multiply':
        return multiply(x, y)
    elif operation == 'divide':
        return divide(x, y)
    else:
        raise ValueError("Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'.")
def main():
    """Main function to run the calculator."""
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
        result = calculator(x, y, operation)
        print(f"The result of {operation}ing {x} and {y} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
# This code defines a simple calculator that can perform addition, subtraction, multiplication, and division.
# It includes error handling for invalid operations and division by zero.
# The main function prompts the user for input and displays the result of the calculation.
# The calculator can be extended with more operations if needed.