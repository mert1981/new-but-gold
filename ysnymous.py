print("""
CALCULATOR
""")

on_off = int(input("ON(1),OFF(2):"))
if (on_off != 1 and on_off != 2):
    print("WRONG CHARACTER!!!(TRY AGAİN)")


while on_off == 1:
    number1 = float(input("ENTER NUMBER:"))
    operation = int(input("OPERATİON" "\nAdd(1)" "\nSubtract(2)" "\nMultiply(3)" "\nDivide(4)" "\nOFF(5)" "\nENTER:"))

    if (operation == 1):
        number2 = float(input("ENTER NUMBER:"))
        total = number1+number2
        print("{}+{} = {} ".format(number1,number2,total))

    elif (operation == 2):
        number2 = float(input("ENTER NUMBER:"))
        Extraction = number1-number2
        print("{}-{} = {} ".format(number1,number2,Extraction))
    elif (operation == 3):
        number2 = float(input("ENTER NUMBER:"))
        multiplication = number1 * number2
        print("{}x{} = {} ".format(number1,number2,multiplication))
    elif (operation == 4):
        number2 = float(input("ENTER NUMBER:"))
        partition = number1/number2
        print("{}/{} = {} ".format(number1,number2,partition))

    elif (operation == 5):
        break
    else:
        print("WRONG CHARACTER!!!(TRY AGAİN)")




