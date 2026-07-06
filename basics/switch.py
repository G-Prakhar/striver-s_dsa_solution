n = int(input("Enter a number between 1 and 3: "))

match n:
    case 1:
        print("You entered one.")
    case 2:
        print("You entered two.")
    case 3:
        print("You entered three.")
    case _:
        print("You entered a number other than between 1 and 5.")
        