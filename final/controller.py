#!/usr/bin/python3
#--------------------------------#
# File name: controller.py
#--------------------------------#

import tkinter as tk
from tkinter import messagebox
import RPi.GPIO as GPIO
import time
import sys, traceback
import subprocess
import time
import os
import signal
import pyaudio, wave

## pin information for GPIO
IN1 = 11    # pin11
IN2 = 12
IN3 = 13
IN4 = 15

## record audio code
BUFFER_SIZE = 1024
REC_SECONDS = 2
RATE = 48000
WAV_FILENAME = "temp.wav"
FORMAT = pyaudio.paInt16

def record():
     pa = pyaudio.PyAudio()
     for i in range(pa.get_device_count()):
          dev = pa.get_device_info_by_index(i)
     print((i,dev['name'],dev['maxInputChannels']))

     stream = pa.open(
          format = FORMAT,
          input = True,
          channels = 1,
          rate = RATE,
          input_device_index = 2,
          frames_per_buffer = BUFFER_SIZE
     )

     #run recording
     print('Recording...')
     data_frames = []
     toRange = int(RATE/BUFFER_SIZE * REC_SECONDS)
     for f in range(0, toRange):
          data = stream.read(BUFFER_SIZE)
          data_frames.append(data)
     print('Finished recording...')
     stream.stop_stream()
     stream.close()
     pa.terminate()

     wf = wave.open(WAV_FILENAME, 'wb')
     wf.setnchannels(1)
     wf.setsampwidth(pa.get_sample_size(FORMAT))
     wf.setframerate(RATE)
     wf.writeframes(b''.join(data_frames))
     wf.close()

     text = 'hello'
     proc = subprocess.Popen(
     ['./transcibeAudio.sh', WAV_FILENAME],stdout=subprocess.PIPE)

     result = proc.stdout.read()
     print(result)
     
     with open("transcription-log.txt", "a") as myFile:
          myFile.write(result.decode("utf-8"))

     modifiedResult = result[16:].decode("utf-8").strip()
     print (modifiedResult)
     # Transcription:  

     return modifiedResult

#step motor set up
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

        time.sleep(delay)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(IN1, GPIO.OUT)      # Set pin's mode is output
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

def destroy():
    GPIO.cleanup()             # Release resource
   
# voice control 
voice_increment=1
keypad_determine=0

voice_correct_phrase = 'open the door' # default passcode

def start_recording():
   voice_phrase = record().lower() ## 'abcd' #call voice record & google translation function
   
   global keypad_determine
   global voice_increment
   
   if (voice_phrase.startswith(voice_correct_phrase.lower())):
      unlock_determine=1
   else:
      unlock_determine=0
      
   if (unlock_determine==1):
      print('correct passphrase')
      print('open lock')
      tk.Label(voice_interface,text='Correct Passphrase',fg="green").place(x=120,y=50)
      keypad_determine=0
      voice_interface.destroy()
   else:
      if (voice_increment<3):
         tk.Label(voice_interface,text='Wrong Passphrase',fg="red").place(x=120,y=50)
         print('wrong passphrase')
         tk.Label(voice_interface,text=str(3-voice_increment)+' times left',fg="red").place(x=150,y=75)
         print(str(3-voice_increment)+' times left')
         voice_increment=voice_increment+1
      else:
         keypad_determine=1
         voice_interface.destroy()
      

def voice_changephrase():
   def changepharase():
      global voice_correct_phrase
      old_passphrase = old_phrase.get()
      new_passphrase = new_phrase.get()
      confirm_phrase = new_phrase_confirm.get()
      if new_passphrase != confirm_phrase:
         tk.messagebox.showerror('Error','Passcode and cofirm passcode must be same!')
      elif old_passphrase != voice_correct_phrase:
         tk.messagebox.showerror('Error','Wrong old passcode, please try again!')
      else:
         tk.messagebox.showinfo('Welcome', 'You have successfully changed passcode!')
         window_changephrase.destroy()
         voice_correct_phrase = new_passphrase

   window_changephrase = tk.Toplevel(voice_interface)
   window_changephrase.geometry('350x200')
   window_changephrase.title('Change passphrase')

   old_phrase = tk.StringVar()
   tk.Label(window_changephrase, text='Old passphrase: ').place(x=10, y=10)
   entry_old_phrase = tk.Entry(window_changephrase, textvariable=old_phrase, show='*')
   entry_old_phrase.place(x=150, y=10)

   new_phrase = tk.StringVar()
   tk.Label(window_changephrase, text='New passphrase: ').place(x=10, y=50)
   entry_new_phrase = tk.Entry(window_changephrase, textvariable=new_phrase, show='*')
   entry_new_phrase.place(x=150, y=50)

   new_phrase_confirm = tk.StringVar()
   tk.Label(window_changephrase, text='Confirm passphrase: ').place(x=10, y= 90)
   entry_new_phrase_confirm = tk.Entry(window_changephrase, textvariable=new_phrase_confirm, show='*')
   entry_new_phrase_confirm.place(x=150, y=90)

   btn_comfirm_changephrase = tk.Button(window_changephrase, text='Change Passphrase', command=changepharase)
   btn_comfirm_changephrase.place(x=150, y=130)
   

def keypad_enter():
   keypad_pwd = var_keypad_pwd.get()

   if (keypad_correct_pwd == keypad_pwd):
      unlock_determine=1
   else:
      unlock_determine=0
      
   if (unlock_determine==1):
      print('correct passcode')
      print('open lock')
      tk.Label(keypad_interface,text='Correct passcode',fg="green").place(x=135,y=50)
      keypad_interface.destroy()
   else:
      tk.Label(keypad_interface,text='Wrong passcode',fg="red").place(x=135,y=50)
      print('wrong passcode')
      

def keypad_changepwd():
   def changepwd():
      global keypad_correct_pwd
      old_pd = old_pwd.get()
      new_pd = new_pwd.get()
      confirm_pd = new_pwd_confirm.get()
      if new_pd != confirm_pd:
         tk.messagebox.showerror('Error','Passcode and cofirm passcode must be same!')
      elif old_pd != keypad_correct_pwd:
         tk.messagebox.showerror('Error','Wrong old passcode, please try again!')
      else:
         tk.messagebox.showinfo('Welcome', 'You have successfully changed passcode!')
         window_changepwd.destroy()
         keypad_correct_pwd = new_pd

   window_changepwd = tk.Toplevel(keypad_interface)
   window_changepwd.geometry('350x200')
   window_changepwd.title('Change passcode')

   old_pwd = tk.StringVar()
   tk.Label(window_changepwd, text='Old passcode: ').place(x=10, y=10)
   entry_old_pwd = tk.Entry(window_changepwd, textvariable=old_pwd, show='*')
   entry_old_pwd.place(x=150, y=10)

   new_pwd = tk.StringVar()
   tk.Label(window_changepwd, text='Passcode: ').place(x=10, y=50)
   entry_new_pwd = tk.Entry(window_changepwd, textvariable=new_pwd, show='*')
   entry_new_pwd.place(x=150, y=50)

   new_pwd_confirm = tk.StringVar()
   tk.Label(window_changepwd, text='Confirm passcode: ').place(x=10, y= 90)
   entry_new_pwd_confirm = tk.Entry(window_changepwd, textvariable=new_pwd_confirm, show='*')
   entry_new_pwd_confirm.place(x=150, y=90)

   btn_comfirm_changepwd = tk.Button(window_changepwd, text='Change Passcode', command=changepwd)
   btn_comfirm_changepwd.place(x=150, y=130)

def lock_request():
    waiting_to_lock_interface.destroy()
    
state="locked" #close means lock is already locked, open means lock is unlocked
while True:
    voice_increment=1
    keypad_determine=0
    #process begin, voice interface UI creating
    voice_interface=tk.Tk()
    voice_interface.title('voice input')
    voice_interface.geometry('350x250+400+250')

    voice_unlock_determine=tk.BooleanVar()
    # keypad control

    keypad_increment=1

    keypad_correct_pwd = '1234' # default passcode

    # start recording button
    VoiceGather = tk.Button(voice_interface, text='Start recording', command=start_recording)
    VoiceGather.place(x=120, y=90)

    # change passphrase button
    VoiceGather = tk.Button(voice_interface, text='Change Passphrase', command=voice_changephrase)
    VoiceGather.place(x=100, y=150)


    voice_interface.mainloop()


    #keypad UI will be created if we were not able to give correct voice input in three times  
    if (keypad_determine==1):
        keypad_interface=tk.Tk()
        keypad_interface.title('Keypad input')
        keypad_interface.geometry('350x250+400+250')
        #tk.Label(window,text='Keypad correct passcode: ' + keypad_correct_pwd).place(x=50,y=30)

        tk.Label(keypad_interface,text='Keypad passcode: ').place(x=130,y=100)
        var_keypad_pwd=tk.StringVar()
        unlock_determine=tk.BooleanVar()
        entry_keypad_pwd = tk.Entry(keypad_interface, textvariable=var_keypad_pwd, show='*')
        entry_keypad_pwd.place(x=110, y=150)
   
        # enter button
        keypadGather = tk.Button(keypad_interface, text='Enter', command=keypad_enter)
        keypadGather.place(x=80, y=190)

        # change password button
        keypadGather = tk.Button(keypad_interface, text='Change Passcode', command=keypad_changepwd)
        keypadGather.place(x=140, y=190)
   
        keypad_interface.mainloop()
        
 
    if __name__ == '__main__':     # Program start from here
        setup()
    print ('rotating clockwise...')
    forward(0.002, 400)
                
    print ('stop...')
    stop()

    waiting_to_lock_interface=tk.Tk()
    waiting_to_lock_interface.title('Waiting for lock request')
    waiting_to_lock_interface.geometry('350x250+400+250')
    # change passphrase button
    LockGather = tk.Button(waiting_to_lock_interface, text='Lock again', command=lock_request)
    LockGather.place(x=130, y=150)

    waiting_to_lock_interface.mainloop()
        
    print ('rotating counter-clockwise...')
    backward(0.002, 400)
    print ('stop...')
    stop()

    #time.sleep(1)
