# These label configurations should be used for uniformity purposes
import tkinter as tk


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

class DefaultMessage(tk.Label):
    def __init__(self, master, row, text):
        super().__init__(master, text=text)
        self.configure(bg='lightgrey', fg='red')
        self.row = row
    def PrintToScreen(self):
        self.grid(row=self.row, column=1, sticky='s')

if __name__ == '__main__':
    pass
