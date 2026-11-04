
import tkinter as tk

from interfaces.login import create_login


def login_success():
    print("Login successful!")


root = tk.Tk()

create_login(root, login_success)

root.mainloop()
