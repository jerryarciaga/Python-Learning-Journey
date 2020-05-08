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
        self.geometry('200x250')
        
        self.AppFrame = tk.Frame(bg='lightgrey')
        self.WelcomeBanner = CustomDefaults.DefaultLabel(self.AppFrame, 0,
                                                            "Welcome to your Account!")
        self.AppFrame.grid(row=0, column=0)



if __name__ == '__main__':
    loginApp = MainApp()
    loginApp.mainloop()
