# import openpyxl and tkinter modules
import tkinter as tk
from tkinter import filedialog
from tkinter import *

# globally declare wb and sheet variable
root = Tk()

# setting the windows size
root.geometry("400x200")
# setting the app name
root.title("sign in")

# declaring string variable
# for storing name and password
name_sign=tk.StringVar()
passw_sign=tk.StringVar()


# a function that will get the name and password and store them in a text file
def signIn():
    fin = open("coursework.txt", "r")
    contents = fin.readlines()
    print(contents)
    fin.close()
    contents.find(name_entry_sign,4)

def reg():
    root.destroy()
    import register_page

# creating a label for name
name_label_sign = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
# creating a input text box
name_entry_sign = tk.Entry(root,textvariable = name_sign, font=('calibre',10,'normal'))
# creating a label for password
passw_label_sign = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
# creating a input text box for password
passw_entry_sign =tk.Entry(root, textvariable = passw_sign, font = ('calibre',10,'normal'), show = '*')
# creating a button that will call the submit function
signIn_btn=tk.Button(root,text = 'Sign In', command = signIn)
# creating a button that will call the sign-in function
reg_btn=tk.Button(root,text = 'Dont have an account? Register now!', command = reg)

name_label_sign.grid(row=0,column=0)
name_entry_sign.grid(row=0,column=1)
passw_label_sign.grid(row=1,column=0)
passw_entry_sign.grid(row=1,column=1)
signIn_btn.grid(row=2,column=1)
reg_btn.grid(row=3,column=1)

# performing an infinite loop
# for the window to display
root.mainloop()



    



