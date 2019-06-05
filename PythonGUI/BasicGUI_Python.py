from tkinter import *
from tkinter import ttk

class HelloApp:
    def __init__(self,master):
        self.label=ttk.Label(master,text="Hello tkinter!!")
        self.label.grid(row=0,column=0,columnspan=2)

        ttk.Button(master, text="Bengaluru", command=self.bengaluru_hello).grid(row=1,column=0)
        ttk.Button(master, text="Mysuru", command=self.mysuru_hello).grid(row=1, column=1)


    def bengaluru_hello(self):
        self.label.config(text="Hegiddira, tkinter!")

    def mysuru_hello(self):
        self.label.config(text="Namaskara, tkinter!")


def main():
    root=Tk()
    app=HelloApp(root)
    root.mainloop()

if __name__ == "__main__": main()
