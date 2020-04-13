#!/usr/bin/python

import tkinter as tk

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.configure(bg='lightgrey')
        self.geometry('450x250')
        
        ## Login Frame ##
        # Log In banner
        self.banner = tk.Label(text='Log In', bg='lightgrey', fg='black')
        self.banner.configure(font=('Arial Black', 30))
        self.banner.grid(row=0, column=0, sticky='new')
        # Username and Password
        self.loginFrame = tk.Frame(bg='lightgrey')
        self.userName = DefaultLabel(self.loginFrame, 'Username: ', column=0)
        self.userEntry = DefaultEntry(self.loginFrame, column=1)
        self.userEntry.focus_set()
        self.passwordLabel = DefaultLabel(self.loginFrame, 'Password: ', column=2)
        self.passwordEntry = DefaultEntry(self.loginFrame, column=3, show='*')
        self.loginButton = tk.Button(self.loginFrame, text='Log In!', command=self.Login)
        self.loginButton.configure(bg='lightgrey', fg='black', font=('Arial', 8))
        self.loginButton.grid(row=2, column=0, padx=5, pady=10, ipady=5, sticky='NEWS')
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

class DefaultLabel(tk.Label):
    def __init__(self, master, text, column):
        super().__init__(master, text=text)
        self.configure(bg='lightgrey', fg='black', font=('Arial', 8))
        self.grid(row=1, column=column, padx=5, pady=10, ipady=5, sticky='NESW')

class DefaultEntry(tk.Entry):
    def __init__(self, master, column, show=''):
        super().__init__(master, show=show)
        self.configure(bg='lightgrey', fg='black')
        self.configure(justify='center', font=('Arial', 8))
        self.grid(row=1, column=column, padx=5, pady=10, ipady=5, sticky='NESW')



if __name__ == '__main__':
    login = Login()
    login.mainloop()
