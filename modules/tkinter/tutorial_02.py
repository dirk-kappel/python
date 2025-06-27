"""
Working with tkinter in Python.

Creating a simple GUI application.
"""

import tkinter as tk

root = tk.Tk()
root.title("Simple GUI Application")

def add_to_list(event=None): # Set event to None to allow for keyboard binding
    """Function will be called when the button is clicked."""
    text = entry.get()  # Get the text from the entry widget
    if text:
        text_list.insert(tk.END, text) # Insert the text at the end of the listbox
        entry.delete(0, tk.END) # Delete the text in the entry widget

# Format the root window. Make it resizable.
root.columnconfigure(0, weight=1) # Configure the first column to expand
root.columnconfigure(1, weight=1) # Configure the second column to expand
root.rowconfigure(0, weight=1) # Configure the first row to expand
root.rowconfigure(1, weight=1) # Configure the second row to expand

# Using a frame to organize widgets
# A frame is a container for organizing widgets
frame = tk.Frame(root)
frame.grid(row=0,
           column=0,
           sticky="nsew", # Stretch the frame to fill the window in all directions.
           padx=5, # Padding on the x-axis
           pady=5, # Padding on the y-axis
        )

frame.columnconfigure(0, weight=1) # Configure the first column to expand
frame.rowconfigure(1, weight=0) # Configure the second column to not expand

# Widgets can be added to the frame
entry = tk.Entry(frame)  # Create an entry widget
entry.grid(row=0, column=0, sticky="ew")  # Place the entry in the frame

# Bind the entry to a keyboard event
entry.bind("<Return>", add_to_list)  # Pressing Enter will call add_to_list

entry_btn = tk.Button(frame, text="Add", command=add_to_list)  # Create a button
entry_btn.grid(row=0, column=1)  # Place the button in the frame

text_list = tk.Listbox(frame)  # Create a listbox
# Place the listbox in the frame
text_list.grid(row=1,
               column=0,
               columnspan=2, # Span two columns
               sticky="nsew", # Stretch the listbox to stick to the sides (east and west)
               )


# ---------------- Frame 2 ----------------
# Themed tkinter widgets
from tkinter import ttk

frame2 = ttk.Frame(root) # Use ttk.
frame2.grid(row=0,
           column=1,
           sticky="nsew",
        )

frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(1, weight=0)

entry = ttk.Entry(frame2)
entry.grid(row=0, column=0, sticky="ew")

entry.bind("<Return>", add_to_list)

entry_btn = ttk.Button(frame2, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

text_list = tk.Listbox(frame2) # Listbox does not have a ttk equivalent

text_list.grid(row=1,
               column=0,
               columnspan=2,
               sticky="nsew",
               padx=5,
               pady=5,
               )



root.mainloop()
