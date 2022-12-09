x = '0'
y = '0'
z = '0'
q = '0'

while q != '1':
    print("\n1 Multipy")
    print("2 Divide")
    print("3 Add")
    print("4 Subtract\n")

    z = input("Enter selection: ")

    if z == '1':
        x = input("number 1: ")
        y = input("number 2: ")
        print(int(x) * int(y))
    elif z == '2':
        x = input("number 1: ")
        y = input("number 2: ")
        print(int(x) / int(y))
    elif z == '3':
        x = input("number 1: ")
        y = input("number 2: ")
        print(int(x) + int(y))
    elif z == '4':
        x = input("number 1: ")
        y = input("number 2: ")
        print(int(x) - int(y))
    elif z == 'q' or z == 'Q':
        print("Good bye")
        q = '1'
    else:
        print("Invalid input")
        q = '1'
