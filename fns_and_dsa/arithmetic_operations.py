"""
Perform basic arithmetic operations on two numbers.

args:
    num1 (float): First number
    nume (float): Second Number
    operation (str): Operation to perform - 'add', 'subtraction', 'multiplication', or 'divide'

Returns:
    float or str: Result of the operation or error message for division by zero
"""
def perform_operations(num1, num2, operation):

    operation = operation.lower().strip()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'"


    