#!/usr/bin/python3
#--------------------------------#
# File name: StepMotor.py
#--------------------------------#

import RPi.GPIO as GPIO
import time

IN1 = 11    # pin11
IN2 = 12
IN3 = 13
IN4 = 15

def setStep(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)

def stop():
    setStep(0, 0, 0, 0)

def forward(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)

def backward(delay, steps):
    for i in range(0, steps):
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(IN1, GPIO.OUT)      # Set pin's mode is output
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    print ('Lock initialized to locked state...')
    forward(0.002, 400)

def keypad():
    access = 0
    password1 = 1234;
    password2 = 4321;

    # pwd = int(input(">>> Input: "))
    while True:
        try:
            pwd=input('Please enter password>>> ')
            pwd = int(pwd)
            break
        except ValueError:
            print('no valid integer! Please try again')
    print('Great,you successfully entered an integer')
    
    if pwd == password1:
        access = 1
        print('Access authorized.')
        print("%d" %access)
    else:
        if pwd == password2:
            access = -1
            print('Lock authorized.')
            print("%d" %access)
        else:
            print('Request denied.')
            print("%d" %access)
  
    return access

def loop():
    while True:
        print ('backward...')
        backward(0.002, 400)  # 512 steps --- 360 angle
                
        print ('stop...')
        stop()                 # stop
        time.sleep(1)          # sleep 3s
           
        print ('forward...')
        forward(0.002, 400)
                
        print ('stop...')
        stop()
        time.sleep(1)


def destroy():
    GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
#    try:
#        loop()
#    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
#        destroy()

state="close" #close means lock is already locked, open means lock is unlocked
while True:
    
    result=keypad()
#    while (result == 0):
#        result =keypad()
  
    print ("state= " , state)
    if (result==1):
        if (state=="close"):
            print ('forward...')
            forward(0.002, 400)
                
            print ('stop...')
            stop()
            state = "open"
            print ("state= " , state)
        else:
            print ('lock is already unlocked...')
            print ("state= " , state)
    else:
        if (result==-1):
            if (state=="open"):
                print ('backward...')
                backward(0.002, 400)
                
                print ('stop...')
                stop()
                state = "close"
                print ("state= " , state)
            else:
                print ('lock is already locked...')
                print ("state= " , state)
    time.sleep(1)


