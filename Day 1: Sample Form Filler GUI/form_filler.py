#!/usr/bin/python

import tkinter as tk
import json

class Form(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Some User Form')
        self.configure(bg='lightgrey')
        self.geometry('250x300')
        self.grid_columnconfigure(0, weight=1)

        ## Title Banner ##
        self.banner = tk.Label(text='Sign Up')
        self.banner.configure(bg='lightgrey', fg='black', pady=20)
        self.banner.configure(font=('Arial Bold', 15))
        self.banner.grid(sticky='new')
        ## End Title Banner ##

        ## User Info ##
        self.userForm = tk.Frame(self)
        self.userForm.configure(bg='lightgrey')
        self.firstNameLabel = DefaultLabel(self.userForm, row=0, text='First Name: ')
        self.firstNameEntry = DefaultEntry(self.userForm, row=0)
        self.lastNameLabel = DefaultLabel(self.userForm, row=1, text='Last Name: ')
        self.lastNameEntry = DefaultEntry(self.userForm, row=1)
        self.userNameLabel = DefaultLabel(self.userForm, row=2, text='Username: ')
        self.userNameEntry = DefaultEntry(self.userForm, row=2)
        self.passwordLabel = DefaultLabel(self.userForm, row=3, text='Password: ')
        self.passwordEntry = DefaultEntry(self.userForm, row=3, show='*')
        self.userForm.grid(row=1, sticky='w')
        ## End User Info ##
        

        ## Login/Create Account ##
        
        # Enter Information Button #
        self.createAccountButton = tk.Button(self, text='Create Account',
                                                command=self.CreateAccount)
        self.createAccountButton.configure(bg='lightgrey', fg='black', font=('Arial', 8))
        self.createAccountButton.grid(row=4)
        self.bind('<Return>', self.CreateAccount)

    def CreateAccount(self, event=None):
        fname = self.firstNameEntry.get()
        lname = self.lastNameEntry.get()
        uname = self.userNameEntry.get()
        passwd =  self.passwordEntry.get()

        account = {
            'fname': fname,
            'lname': lname,
            'uname': uname,
            'passwd': passwd
        }
        if fname and lname and uname and passwd:
            with open('accounts', 'a') as file:
                json.dump(account, file)


class DefaultLabel(tk.Label):
    def __init__(self, master, row, text):
        super().__init__(master, text=text)
        self.configure(bg='lightgrey', fg='black', font=('Arial', 8))
        self.grid(row=row, column=0, pady=10, sticky='w')


class DefaultEntry(tk.Entry):
    def __init__(self, master, row, show=''):
        super().__init__(master, show=show)
        self.configure(bg='lightgrey', fg='black', justify='center')
        self.grid(row=row, column=1, sticky='w')


if __name__ == '__main__':
    userForm = Form()
    userForm.mainloop()
