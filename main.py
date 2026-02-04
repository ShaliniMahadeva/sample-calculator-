from add import add
from sub import subtract
from mul import multiply
from div import divide

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1-4): "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Result:", add(a, b))
elif choice == 2:
    print("Result:", subtract(a, b))
elif choice == 3:
    print("Result:", multiply(a, b))
elif choice == 4:
    print("Result:", divide(a, b))
else:
    print("Invalid choice")
