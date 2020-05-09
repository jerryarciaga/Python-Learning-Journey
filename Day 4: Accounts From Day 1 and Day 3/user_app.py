#!/usr/bin/python

import tkinter as tk
import json

import CustomDefaults
import form_filler
import login

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Account')
        self.configure(bg='lightgrey')
        self.geometry('500x250')
        
        self.AppFrame = tk.Frame(bg='lightgrey')
        # Welcome Banner
        self.WelcomeBanner = tk.Label(self.AppFrame, text='Welcome to Your Account')
        self.WelcomeBanner.configure(font=('Arial Bold', 15), bg='lightgrey', fg='black')
        self.WelcomeBanner.grid(row=0, column=0, sticky='new')
        #Login Button
        self.LoginButton = tk.Button(self.AppFrame, text='Log In', command=self.Login())
        self.bind('<Return>', self.Login())
        self.LoginButton.configure(bg='lightgrey', fg='black')
        self.LoginButton.grid(row=1, column=0, sticky='ew')
        self.AppFrame.grid(row=0, column=0)

    def Login(self, event=None):
        loginApp = login.LoginApp()
        loginApp.mainloop()



if __name__ == '__main__':
    userApp = MainApp()
    userApp.mainloop()
