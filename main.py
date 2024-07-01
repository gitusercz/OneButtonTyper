import tkinter as tk
from customtkinter import *
import math

# Hungarian alphabet
alphabet = [
    "_", "BSpace","E", "T", "A", "L", "K", "N", "R", "S", "I", "Újra",
    "O", "Á", "Z", "É", "M", "G", "D", "B", "V", "SZ", "H", "Újra",
    "U", "P", "J", "F", "Ó", "Ö", "C", "Ő", "Í", "NY", "Ü", "Újra",
    "GY", "CS", "Ú", "Ű", "ZS", "TY", "W", "X", "Y", "Q", "Mentés", "Újra"
]

# Initialize the main window
app = CTk()
app.title("1-bit typer")
app.geometry("1200x800")

# Textbox to display the typed string
textbox = CTkTextbox(app, width=1100, height=100, font=("Helvetica", 24))
textbox.pack(pady=40)

# Frame for the alphabet table
table_frame = CTkFrame(app)
table_frame.pack()

# Calculate the number of columns
num_columns = math.ceil(len(alphabet) / 4)

# Variables to manage highlighting and typing
highlight_mode = 'row'  # Modes: 'row', 'cell'
highlight_row = 0
highlight_col = 0
typed_string = ""
highlight_update_id = None

# Function to update the highlighting
def update_highlight():
    global highlight_row, highlight_col, highlight_mode, highlight_update_id

    for i in range(4):
        for j in range(num_columns):
            index = i * num_columns + j
            if index < len(alphabet):
                label = labels[i][j]
                if highlight_mode == 'row':
                    if i == highlight_row:
                        label.configure(bg_color="white")
                    else:
                        label.configure(bg_color="gray")
                elif highlight_mode == 'cell':
                    if i == highlight_row:
                        if j == highlight_col:
                            label.configure(bg_color="white")
                        else:
                            label.configure(bg_color="gray")

    if highlight_mode == 'row':
        highlight_row = (highlight_row + 1) % 4
    elif highlight_mode == 'cell':
        highlight_col = (highlight_col + 1) % num_columns

    highlight_update_id = app.after(600, update_highlight)

# Function to handle left mouse click
def on_click(event):
    global highlight_mode, highlight_row, highlight_col, highlight_update_id

    if highlight_mode == 'row':
        highlight_mode = 'cell'
        highlight_col = 0  # Start cell highlight from the first column
    elif highlight_mode == 'cell':
        index = highlight_row * num_columns + highlight_col - 1
        if index < len(alphabet):
            if alphabet[index] == "Mentés": on_save()
            elif alphabet[index] == "Újra": pass
            elif  alphabet[index] == "BSpace": textbox.delete("end-2c", "end-1c")
            else:
                textbox.insert(tk.END, alphabet[index])
        highlight_mode = 'row'  # Reset to row highlight
        highlight_row = 0  # Start from the first row

    if highlight_update_id is not None:
        app.after_cancel(highlight_update_id)
    highlight_update_id = app.after(0, update_highlight)

# Function to handle double click
def on_save():
    global typed_string, highlight_mode, highlight_update_id
    with open("typed_strings.txt", "a") as file:
        file.write(textbox.get("1.0", tk.END).strip() + "\n")
    textbox.delete("1.0", tk.END)
    if highlight_update_id is not None:
        app.after_cancel(highlight_update_id)
    highlight_mode = 'row'  # Restart from row highlight mode
    highlight_update_id = app.after(600, update_highlight)

# Create labels for the alphabet table
labels = []
for i in range(4):
    row_labels = []
    for j in range(num_columns):
        index = i * num_columns + j
        if index < len(alphabet):
            label = CTkLabel(table_frame, text=alphabet[index], width=80, height=80, corner_radius=10, font=("Helvetica", 24))
            label.grid(row=i, column=j, padx=4, pady=4)
            label.bind("<Button-1>", on_click)
            row_labels.append(label)
    labels.append(row_labels)

# Start the highlighting process
update_highlight()

# Run the main event loop
app.mainloop()
