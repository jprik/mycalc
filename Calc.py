def main():
    try:
        num1 = int(input("Enter Num1 "))
        num2 = int(input("Enter Num2 "))
        operation = input("Choose specified operation. 1.) Add 2.) Subtract 3.) Multiply 4.) Divide")
    except:
        print('Invalid Input. Exiting gracefully.')
        return #exits gracefully in wake of errors.
    if (operation == '1', 'Add'):
        print(num1 + num2)
    elif (operation == '2', 'Subtract'):
        print(num1 - num2) 
    elif (operation == '3', 'Multiply'):
        print(num1 * num2)
    elif (operation == '4', 'Divide'):
        print(num1 / num2)
    else:
        print('Argument unknown.')
        
main()