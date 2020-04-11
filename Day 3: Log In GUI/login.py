#!/usr/bin/python

import tkinter as tk

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.configure(bg='lightgrey')
        self.geometry('600x200')

        ## Sign In Banner ##
        self.banner = tk.Label()
        ## End Sign In Banner ##
        
        ## Login Frame ##
        self.loginFrame = tk.Frame(bg='lightgrey')
        self.userName = DefaultLabel(self.loginFrame, 'Username: ', row=1)
        self.userEntry = DefaultEntry(self.loginFrame, row=1)
        self.loginFrame.grid(row=0, column=0)
        ## End Login Frame ##

class DefaultLabel(tk.Label):
    def __init__(self, master, text, row):
        super().__init__(master, text=text)
        self.configure(bg='lightgrey', fg='black', font=('Arial', 20))
        self.grid(row=row, column=0, ipady=20, sticky='W')

class DefaultEntry(tk.Entry):
    def __init__(self, master, row, show=''):
        super().__init__(master, show=show)
        self.configure(bg='lightgrey', fg='black')
        self.configure(justify='center', font=('Arial', 20))
        self.grid(row=row, column=1, ipady=20, sticky='E')




if __name__ == '__main__':
    login = Login()
    login.mainloop()
