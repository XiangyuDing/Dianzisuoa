def keypad():
    access = 0
    password = 1234;
    pwd = int(input(">>> Input: "))
    if pwd == password:
        access = 1
        print('Access authorized.')
        print("%d" %access)
    else:
        print('Request denied.')
        print("%d" %access)

    return access

while True :
    keypad()
