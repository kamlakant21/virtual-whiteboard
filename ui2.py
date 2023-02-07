import tkinter as tk
from tkinter import ttk

def change_color(color):
    # Function to change the color of the text and button
    button1.config(bg=color, fg="white")
    button2.config(bg=color, fg="white")
    label1.config(fg=color)
    label2.config(fg=color)

root = tk.Tk()
root.geometry("500x500")
root.config(bg="lightgray")

label1 = tk.Label(root, text="Virtual Whiteboard", font=("Arial", 20))
label1.pack(pady=30)

label2 = tk.Label(root, text="Powerpoint Control", font=("Arial", 20))
label2.pack(pady=10)

frame = tk.Frame(root, bg="white", relief="sunken", bd=2)
frame.pack(fill="both", expand=True, padx=20, pady=20)

button1 = tk.Button(frame, text="Virtual Whiteboard", font=("Arial", 15), command=lambda: change_color("blue"))
button1.pack(side="top", pady=10, padx=10, fill="both", expand=True)

button2 = tk.Button(frame, text="Powerpoint Control", font=("Arial", 15), command=lambda: change_color("red"))
button2.pack(side="bottom", pady=10, padx=10, fill="both", expand=True)

root.mainloop()
