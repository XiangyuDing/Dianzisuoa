import tkinter as tk
from tkinter import messagebox

# keypad control
keypad_increment=1
keypad_determine=1

keypad_correct_pwd = '1234' # default passcode

def keypad_enter():
   keypad_pwd = var_keypad_pwd.get()

   if (keypad_correct_pwd == keypad_pwd):
      unlock_determine=1
   else:
      unlock_determine=0
      
   if (unlock_determine==1):
      print('correct passcode')
      print('open lock')
      tk.Label(window,text='Correct passcode',fg="green").place(x=120,y=100)
      window.quit()
   else:
      tk.Label(window,text='Wrong passcode',fg="red").place(x=120,y=100)
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

   window_changepwd = tk.Toplevel(window)
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

if (keypad_determine==1):
   window=tk.Tk()
   window.title('Keypad input')
   window.geometry('350x250+400+250')
   tk.Label(window,text='Keypad correct passcode: ' + keypad_correct_pwd).place(x=50,y=30)
   tk.Label(window,text='Keypad passcode: ').place(x=50,y=150)
   var_keypad_pwd=tk.StringVar()
   unlock_determine=tk.BooleanVar()
   entry_keypad_pwd = tk.Entry(window, textvariable=var_keypad_pwd, show='*')
   entry_keypad_pwd.place(x=100, y=150)
   
   # enter button
   keypadGather = tk.Button(window, text='Enter', command=keypad_enter)
   keypadGather.place(x=70, y=190)

   # change password button
   keypadGather = tk.Button(window, text='Change Passcode', command=keypad_changepwd)
   keypadGather.place(x=130, y=190)
   
   window.mainloop()
