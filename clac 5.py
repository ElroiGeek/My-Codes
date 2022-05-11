a = int(input("Enter first number "))
b = int(input("Enter second number "))
o = input("Enter an operator 6")

if o == '+':
    print("The sum of the two numbers is ", a + b)
    
elif o == '-':
    print("The diffrence of the two numbers is ", a - b)
    
elif o == '/':
    print("The qoutient of the two numbers is ", a / b)
    
elif  o == '*':
    print("The product of the two nubers is ", a * b)
    
else:
    print("Please enter the correct operator")

