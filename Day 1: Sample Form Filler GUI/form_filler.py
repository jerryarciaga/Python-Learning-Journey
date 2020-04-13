#!/usr/bin/python

import tkinter as tk
import json
import os.path

class Form(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Some User Form')
        self.configure(bg='lightgrey')
        self.geometry('250x350')
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
        self.firstNameEntry.focus_set()
        self.middleNameLabel = DefaultLabel(self.userForm, row=1, text='Middle Name: ')
        self.middleNameEntry = DefaultEntry(self.userForm, row=1)
        self.lastNameLabel = DefaultLabel(self.userForm, row=2, text='Last Name: ')
        self.lastNameEntry = DefaultEntry(self.userForm, row=2)
        self.userNameLabel = DefaultLabel(self.userForm, row=3, text='Username: ')
        self.userNameEntry = DefaultEntry(self.userForm, row=3)
        self.passwordLabel = DefaultLabel(self.userForm, row=4, text='Password: ')
        self.passwordEntry = DefaultEntry(self.userForm, row=4, show='*')
        self.userForm.grid(row=1, sticky='w')
        ## End User Info ##
        

        ## Login/Create Account ##
        
        # Enter Information Button #

        # Create account by pressing login button or pressing <Return> key
        self.createAccountButton = tk.Button(self, text='Create Account',
                                                command=self.CreateAccount)
        self.createAccountButton.configure(bg='lightgrey', fg='black', font=('Arial', 8))
        self.createAccountButton.grid(row=4)
        self.bind('<Return>', self.CreateAccount)

    def CreateAccount(self, event=None):
        fname = self.firstNameEntry.get()
        lname = self.lastNameEntry.get()
        mname = self.middleNameEntry.get()
        uname = self.userNameEntry.get()
        passwd =  self.passwordEntry.get()
        
        account = {
            'fname': fname,
            'mname': mname,
            'lname': lname,
            'uname': uname,
            'passwd': passwd
        }

        # Initialize file if it doesn't exist,
        # otherwise append to it
        if not os.path.isfile('accounts.json'):
            accounts = []
        else:
            with open('accounts.json') as file:
                accounts = json.load(file)
        accounts.append(account)

        # Write account details into a file
        if fname and lname and uname and passwd:
            with open('accounts.json', 'w') as file:
                json.dump(accounts, file, indent=4)
                self.quit()


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
