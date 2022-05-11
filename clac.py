a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
o = input("Enter any operator")

if o == '+':
    print("The sum of the two numbers is ", a + b)
    
elif o == '-':
    print("The diffrence of the two numbers is ", a - b)

elif o == '*':
    print("The product of the two numbers is ", a * b)
    
elif o == '/':
    print("The qoutient of the two numbers is ", a / b)
    
elif o == '%':
    print("The remainder of the two numbers is ", a % b)    
 
elif o == '<':
    print("That's correct, ", a, "is less than ", b)
    
else:
    print("That's not correct")
    
elif o == '>':
    print("That's correct, ", a, "is greater than ", b)
    
else:
    print("That's not correct")
    
elif o == '=':
    print("That's correct, ", a, "is equal to ", b)
    
else:
    print("That's not correct")
