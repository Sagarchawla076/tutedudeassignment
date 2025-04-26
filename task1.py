

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print("Addition: ",n1+n2)
print("Subtraction: ",n1-n2)
print("Multiplication: ",n1*n2)

try:
    print("Division: ",n1/n2)
except ZeroDivisionError:
    print("You can't divide by zero")

