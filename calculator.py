num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ")

# Perform the operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

# Display the result
print(f"{num1} {operator} {num2} = {result}")