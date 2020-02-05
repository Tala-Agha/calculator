
def main():
    #write your code here
    num1 = input("Enter the first number:  ")
    num2 = input("Enter the second number:  ")
    oper = input("Choose the operation (+, -, /, *):  ")

    if (num1 and num2).isdigit():
        num1 = int(num1)
        num2 = int(num2)
        if oper == '+':
            print('{} + {} = '.format(num1, num2))
            print(num1 + num2)
        elif oper == '-':
            print('{} - {} = '.format(num1, num2))
            print(num1 - num2)
        elif oper == '*':
            print('{} * {} = '.format(num1, num2))
            print(num1 * num2)
        elif oper == '/':
            print('{} / {} = '.format(num1, num2))
            print(num1 / num2)
        else:
            print("Invalid operator")
    else:
        print("The numbers are invalid")

    pass




if __name__ == '__main__':
    main()
