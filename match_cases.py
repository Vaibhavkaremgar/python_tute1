lucky_num = int(input("enter a marriage date that you want : "))

match lucky_num:
    case 2:
        print("the marriage date is 2 ")
    case 4:
        print("the wedding date is 4")
    case 6:
        print("the pelli date is 6")
    case _:
        print(f"the muhurtham date will be: {lucky_num}")