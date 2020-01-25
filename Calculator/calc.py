import sys
num1 = int(input("Enter first number. "))
num2 = int(input("Enter second number. "))
while True:
    op = str(input("Choose an operation."))
    
# Logic

    if (op == 'Add', 'Addition'):
        print('Your result is ' + str((num1 + num2)))
        break
        
    if (op == 'Subtract', 'Sub'):
        print('Your result is ' + str((num1 - num2)))
        break
        
    if (op == 'Divide', 'Div'):
        print('Your result is ' + str((num1 / num2)))
        break
        
    if (op == 'Multipy', 'Mul'):
        print('Your result is ' + str((num1 * num2)))
        break
        
    else:
        print('Please use capitalization and guarantee correct spelling. ')
        continue
    
    sys.exit()
        
