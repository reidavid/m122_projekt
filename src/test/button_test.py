# src   : https://stackoverflow.com/questions/66720961/function-calls-with-without-parentheses

import tkinter as tk


def func():
    print('func is running')


def get_func():
    return func


root = tk.Tk()
b = tk.Button(root, text='exampel', command=get_func())
b.pack()

print(get_func)
print(get_func())
print('next')
print(func)
print(func())

root.mainloop()
