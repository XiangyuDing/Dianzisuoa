<<<<<<< HEAD
=======
#!/usr/bin/python3
#--------------------------------#
# File name: keypad.py
#--------------------------------#

import sys, traceback

>>>>>>> develop
def keypad():
    access = 0
    password = 1234;
    pwd = int(input(">>> Input: "))
    if pwd == password:
        access = 1
        print('Access authorized.')
<<<<<<< HEAD
        print("%d" %access)
    else:
        print('Request denied.')
        print("%d" %access)

    return access

while True :
    keypad()
=======
        ## print("%d" %access)
    else:
        print('Request denied.')
        ## print("%d" %access)

    return access


## start of main

def main():
    try:
        while True :
            keypad()
                
    except KeyboardInterrupt:
        print("\nShutdown requested...exiting")
        
    except Exception:
        traceback.print_exc(file=sys.stdout)
        
    sys.exit(0)
## end of animate pet

if __name__ == "__main__":
    main()


>>>>>>> develop
