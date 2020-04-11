#!/usr/bin/python

import tkinter as tk

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.configure(bg='lightgrey')
        self.geometry('600x300')
        
        ## Login Frame ##
        self.loginFrame = tk.Frame()
        self.userName = DefaultLabel(self.loginFrame, 'Username: ', column=0)
        self.loginFrame.grid(row=0, column=0)
        ## End Login Frame ##


class DefaultLabel(tk.Label):
    def __init__(self, master, text, column):
        super().__init__(master, text=text)
        self.configure(bg='lightgrey', fg='black', font=('Arial', 20))
        self.grid(row=1, column=column)
        




if __name__ == '__main__':
    login = Login()
    login.mainloop()
