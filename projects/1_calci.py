try:
    a = int(input("enter the 1st number: "))
    b = int(input("enter the 2nd number: "))

    print("what kind of operation do you want me to perform\npress + for addition\npress - for subtraction\npress * for multiplication\npress / for division\npress % for mod")

    o = input("enter the operation : ")

    match o:
        case "+":
            print(f"the result of a and b is {a+b}")
        case "-":
            print(f"the result of a and b is {a-b}")
        case "*":
            print(f"the result of a and b is {a*b}")
        case "/":
            print(f"the result of a and b is {a/b}")
        case "%":
            print(f"the result of a and b is {a%b}")
        case default:
            print("there was an error")
except Exception as e:
    print("enter a valid value of a and b")
