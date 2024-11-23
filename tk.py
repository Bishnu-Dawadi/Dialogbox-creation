import tkinter as tk
from tkinter import simpledialog, messagebox

def ask_and_show_string():
    user_input = simpledialog.askstring("Input", "Enter a string:")
    
    if user_input is not None:
        messagebox.showinfo("Your String", f"You entered: {user_input}")
    else:
        messagebox.showinfo("No Input", "You didn't enter anything.")

root = tk.Tk()
root.withdraw()  

ask_and_show_string()

root.destroy()
