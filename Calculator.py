def add(num1, num2):
    answer = num1 + num2
    print(f"{num1} + {num2} = {answer}")

def subtract(num1, num2):
    answer = num1 - num2
    print(f"{num1} - {num2} = {answer}")

def multiply(num1, num2):
    answer = num1 * num2
    print(f"{num1} * {num2} = {answer}")
    
def divide(num1, num2):
    answer = round(num1 / num2, 2)
    print(f"{num1} / {num2} = {answer}")

print("*** Welcome to the Basic Calculator ***")
exit = False

while(exit == False):
    print("Type one of the following letters")
    print("A. Addition")
    print("S. Subtration")
    print("M. Multiplication")
    print("D. Division")

    operation = input("Operation: ")

    if operation.lower() == "a":
        num1Valid = False
        num2Valid = False
        while num1Valid == False:
            num1 = input("Enter the first number: ")
            try:
                num1 = int(num1)
                num1Valid = True
            except:
                try:
                    num1 = float(num1)
                    num1Valid = True
                except:
                    print("Please enter a number.")
                    print()

        while num2Valid == False:            
            num2 = input("Enter the second number: ")
            try:
                num2 = int(num2)
                num2Valid = True
            except:
                try:
                    num2 = float(num2)
                    num2Valid = True
                except:
                    print("Please enter a number.")
                    print()

        add(num1, num2)
        print()
        valid = False
        while valid == False:
            selection = input("Would you like to do another calculation? Y/N: ")
            if selection.lower() == "y":
                valid = True
                continue
            elif selection.lower() == "n":
                valid = True
                exit = True
            else:
                continue

    elif operation.lower() == "s":
        num1Valid = False
        num2Valid = False
        while num1Valid == False:
            num1 = input("Enter the first number: ")
            try:
                num1 = int(num1)
                num1Valid = True
            except:
                try:
                    num1 = float(num1)
                    num1Valid = True
                except:
                    print("Please enter a number.")
                    print()

        while num2Valid == False:            
            num2 = input("Enter the second number: ")
            try:
                num2 = int(num2)
                num2Valid = True
            except:
                try:
                    num2 = float(num2)
                    num2Valid = True
                except:
                    print("Please enter a number.")
                    print()

        subtract(num1, num2)
        print()
        valid = False
        while valid == False:
            selection = input("Would you like to do another calculation? Y/N: ")
            if selection.lower() == "y":
                valid = True
                continue
            elif selection.lower() == "n":
                valid = True
                exit = True
            else:
                continue
    elif operation.lower() == "m":
        num1Valid = False
        num2Valid = False
        while num1Valid == False:
            num1 = input("Enter the first number: ")
            try:
                num1 = int(num1)
                num1Valid = True
            except:
                try:
                    num1 = float(num1)
                    num1Valid = True
                except:
                    print("Please enter a number.")
                    print()

        while num2Valid == False:            
            num2 = input("Enter the second number: ")
            try:
                num2 = int(num2)
                num2Valid = True
            except:
                try:
                    num2 = float(num2)
                    num2Valid = True
                except:
                    print("Please enter a number.")
                    print()

        multiply(num1, num2)
        print()
        valid = False
        while valid == False:
            selection = input("Would you like to do another calculation? Y/N: ")
            if selection.lower() == "y":
                valid = True
                continue
            elif selection.lower() == "n":
                valid = True
                exit = True
            else:
                continue
    elif operation.lower() == "d":
        num1Valid = False
        num2Valid = False
        while num1Valid == False:
            num1 = input("Enter the first number: ")
            try:
                num1 = int(num1)
                num1Valid = True
            except:
                try:
                    num1 = float(num1)
                    num1Valid = True
                except:
                    print("Please enter a number.")
                    print()

        while num2Valid == False:            
            num2 = input("Enter the second number: ")
            if num2 == "0":
                print("No dividing by 0 today!")
                print()
            else:
                try:
                    num2 = int(num2)
                    num2Valid = True
                except:
                    try:
                        num2 = float(num2)
                        num2Valid = True
                    except:
                        print("Please enter a number.")
                        print()

        divide(num1, num2)
        print()
        valid = False
        while valid == False:
            selection = input("Would you like to do another calculation? Y/N: ")
            if selection.lower() == "y":
                valid = True
                continue
            elif selection.lower() == "n":
                valid = True
                exit = True
            else:
                continue
    else:
        print("Please enter a valid letter: A S M D")
        print()

print("*** Thank you for using the Basic Calculator ***")