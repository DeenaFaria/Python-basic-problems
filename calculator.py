def calculator():
    input1=float(input("Enter the first number:"))
    operation=input("Enter the operator:")
    input2=float(input("Enter the second number:"))

    operations={
        '+': input1+input2,
        '-': input1-input2,
        '*': input1*input2,
        '/': input1/input2 if input2!=0 else "Error:division by zero"
    }
    
    result= operations.get(operation, "Invalid operation")
    print(f"The result is:{result}")

calculator()