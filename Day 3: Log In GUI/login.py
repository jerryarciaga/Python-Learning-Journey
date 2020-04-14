#!/usr/bin/python

import tkinter as tk
import json
import CustomDefaults

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.configure(bg='lightgrey')
        self.geometry('250x300')
        self.resizable(False, False)
        
        ## Login Frame ##
        # Log In banner
        self.banner = tk.Label(text='Log In', bg='lightgrey', fg='black')
        self.banner.configure(font=('Comic Sans', 30))
        self.banner.grid(row=0, column=0, sticky='N')
        # Username
        self.loginFrame = tk.Frame(bg='lightgrey')
        self.userName = CustomDefaults.DefaultLabel(self.loginFrame, row=1, text='Username: ')
        self.userEntry = CustomDefaults.DefaultEntry(self.loginFrame, row=1)
        self.userEntry.focus_set()
        # Password
        self.passwordLabel = CustomDefaults.DefaultLabel(self.loginFrame, row=2, text='Password: ')
        self.passwordEntry = CustomDefaults.DefaultEntry(self.loginFrame, row=2, show='*')
        # Login Button
        self.loginButton = tk.Button(self.loginFrame, text='Log In!', command=self.Login)
        self.loginButton.configure(bg='lightgrey', fg='black', font=('Arial', 8))
        self.loginButton.grid(row=3, column=1, padx=5, pady=10, ipady=5, sticky='NESW')
        self.bind('<Return>', self.Login)
        self.loginFrame.grid(row=1, column=0, sticky='news')
        ## End Login Frame ##

    def Login(self, event=None):
        if self.userEntry.get() and self.passwordEntry.get():
            account = {
                'uname': self.userEntry.get(),
                'passwd': self.passwordEntry.get()
            }
            print(account)

if __name__ == '__main__':
    login = Login()
    login.mainloop()
