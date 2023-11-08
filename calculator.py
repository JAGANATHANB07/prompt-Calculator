print("                              THIS IS PROMPT CALCULATOR               ")
print("                              *************************               ")
print("     Select the operator to perform:     ")
print("             1.Addition")
print("             2.Substraction")
print("             3.Multiplication")
print("             4.Division")

operation=input()

if operation == "1":
    num1=input("Enter First Element:    ")
    num2=input("Enter Second Element:   ")
    print("Your Adding Number is:   "+ str(int(num1) + int(num2)))
elif operation == "2":
    num1=input("Enter First Element:    ")
    num2=input("Enter Second Element:   ")
    print("Your Adding Number is:   "+ str(int(num1) - int(num2)))
elif operation == "3":
    num1=input("Enter First Element:    ")
    num2=input("Enter Second Element:   ")
    print("Your Adding Number is:   "+ str(int(num1) * int(num2)))
elif operation == "4":
    num1=input("Enter First Element:    ")
    num2=input("Enter Second Element:   ")
    print("Your Adding Number is:   "+ str(int(num1) / int(num2)))
else:
    print("You are Invalid Entry")