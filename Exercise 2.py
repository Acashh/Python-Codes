#Design a calculator which will solve all the problems
#except the following one:
# 45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
c =(input("Enter the operation : \n1. Addition\n2. Multiplication\n3. Division \n: "))
#print(type(c))
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
if c == '1' or c == '2' or c == '3' or c == '4':
    if c == '2' and num1 == 45 and num2 == 3:
        print("45 * 3 = 555");
    elif c == '2':
        print(num1, " * ", num2, " = " ,  (num1*num2))
    elif c == '1' and num1 == 56 and num2 == 9:
        print("56 + 9 = 77")
    elif c == '1':
        print(num1, " + ", num2, " = ", num1+num2)
    elif c == '3' and num1 == 56 and num2 == 6:
        print("56/6 = 4")
    elif c == '3':
        print(num1, "/", num2, " = ", float (num1/num2))
    else:
        print("Please Enter the valid numbers")
else:
    print("Please Enter the Operation from above given Menu: ")

