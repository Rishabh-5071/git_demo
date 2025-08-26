a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
op = input("Choose from add and sub: ")

if (op == '+' ):
    print("Add: ", a+b)
elif (op == '-'):
    print("Sub: ", a-b)
else:
    print("Invalid")