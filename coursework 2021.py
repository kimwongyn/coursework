# import openpyxl and tkinter modules
import tkinter as tk
from tkinter import filedialog
from tkinter import *

# globally declare wb and sheet variable
root = Tk()

# setting the windows size
root.geometry("1200x700")
# setting the app name
root.title("coursework")

# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()
 
  
# a function that will get the name and password and store them in a text file
def createAccount():
 
    name=name_var.get()
    password=passw_var.get()
     
    print("The name is : " + name)
    print("The password is : " + password)

    file1 = open("coursework.txt", "w")
    file1.write("user:" + name + "  ")
    file1.write("password:" + password)
    file1.close()
    
    name_var.set("")
    passw_var.set("")
    
# a function that will get the name and password and store them in a text file
def signIn():
    fin = open("data_out.txt", "r")

    
# creating a label for name
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
  
# creating a input text box
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
  
# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
  
# creating a input text box for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
  
# creating a button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = createAccount)

# creating a button that will call the sign-in function
sign_btn=tk.Button(root,text = 'Already have an account? Sign In !', command = signIn)
  
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
sign_btn.grid(row=3,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()
