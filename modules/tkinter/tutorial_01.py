"""
Working with tkinter in Python.

Creating a simple GUI application.
"""

import tkinter as tk

# This is creating the application window
root = tk.Tk()
root.title("Simple GUI Application") # Create a title for the window

def on_button_click():
    """Function will be called when the button is clicked."""
    print("Testing") # Print a message to the console
    lbl.config(text="Button clicked!") # Change the label text

# Adding a label to the window
lbl = tk.Label(root, text="Label 1") # Create a label
# Use grid layout to place the label
lbl.grid(row=0,   # The row in the grid layout
        column=0, # The column in the grid layout
        )

print(lbl.config().keys()) # Print the keys of the label configuration

# Add a button to the window
btn = tk.Button(root, text="Button 1", command=on_button_click) # Create a button
# Use grid layout to place the button
btn.grid(row=0,   # The row in the grid layout
        column=1, # The column in the grid layout
        )

# This will keep the window open
root.mainloop()
