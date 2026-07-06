def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):   
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

s = str(input("Enter the operation (add, subtract, multiply, divide): "))

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

if s == "add":
    result = add(n1, n2)
elif s == "subtract":
    result = subtract(n1, n2)
elif s == "multiply":
    result = multiply(n1, n2)
elif s == "divide":
    result = divide(n1, n2)

print("The result is:", result)