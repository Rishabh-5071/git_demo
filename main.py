a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == '+':
    print(f"Addition: {a+b}")
elif op == '-':
    print(f"Subtraction: {a-b}")
elif op == '/':
    print(f"Division: {a/b}")
elif op == '*':
    print(f"Multiplication: {a*b}")
else:
    print("Invalid operation")
