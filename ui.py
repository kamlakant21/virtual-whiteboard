import tkinter as tk

root = tk.Tk()
root.title("Virtual Whiteboard & PowerPoint Control")
root.config(bg='black')

# Define buttons
button_1 = tk.Button(root, text="Virtual Whiteboard", font=("Helvetica", 20), bg='yellow', fg='black')
button_2 = tk.Button(root, text="PowerPoint Control", font=("Helvetica", 20), bg='yellow', fg='black')

# Place buttons on the screen
button_1.pack(side='top', fill='both', expand=True)
button_2.pack(side='bottom', fill='both', expand=True)

# Add rounded corners to buttons
button_1.config(highlightbackground='black', relief='solid', bd=4, bg='yellow')
button_1.config(highlightcolor='black', highlightthickness=2, bg='yellow')
button_2.config(highlightbackground='black', relief='solid', bd=4, bg='yellow')
button_2.config(highlightcolor='black', highlightthickness=2, bg='yellow')

# Add shadow to buttons
button_1.config(highlightbackground='black', highlightthickness=2, bg='yellow')
button_2.config(highlightbackground='black', highlightthickness=2, bg='yellow')

# Reduce 20 pixels from the edge of the screen
root.geometry("{}x{}".format(root.winfo_screenwidth()-20, root.winfo_screenheight()-20))

# Set border color
root.config(highlightbackground='red', highlightthickness=4)

root.mainloop()
