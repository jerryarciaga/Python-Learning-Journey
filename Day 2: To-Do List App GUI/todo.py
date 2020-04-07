#!/usr/bin/python

import tkinter as tk

class ToDo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()
        self.title('T0D0 by Jerry Arciaga')
        self.configure(bg='lightgrey')
        self.geometry('300x500')
        self.pack_propagate(0)

        ## Create tasks as array of labels ##
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        ## Frame: Contains task list ##
        self.taskFrame = tk.Frame(self)
        self.taskFrame.configure(bg='lightgrey')

        # Temporary Task #
        tempTask = TaskLabel(self.taskFrame,
                                text='---Add items here---',
                                bg='lightgrey', fg='black')
        self.tasks.append(tempTask)
        
        self.taskFrame.pack(side=tk.TOP, fill=tk.BOTH)
        ## End Frame ##

        ## Text Box For Task ##
        self.taskText = tk.Text(self, bg='white', fg='black')
        self.taskText.configure(height=3, font=('Calibri', 10))
        self.taskText.pack(side=tk.BOTTOM, fill=tk.X)
        self.taskText.focus_set()
        self.bind('<Return>', self.addTask)
    
    ## Add task into tasks array and to display as well ##
    def addTask(self, event=None):
        newTaskString = self.taskText.get(1.0, tk.END).strip()
        self.taskText.delete(1.0, tk.END)
        newTask = TaskLabel(self.taskFrame,
                            text=newTaskString,
                            bg='lightgrey', fg='black')
        self.tasks.append(newTask)

    def removeTask(self, event=None):
        pass
        
                            

class TaskLabel(tk.Label):
    def __init__(self, master, text, bg, fg):
        super().__init__(master=master, text=text, bg=bg, fg=fg)
        self.configure(font=('Calibri', 10), wraplength=250, pady=10)
        self.pack(side=tk.TOP, fill=tk.X)
        
        



if __name__ == '__main__':
    todoApp = ToDo()
    todoApp.mainloop()
