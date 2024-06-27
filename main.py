import tkinter as tk
from customtkinter import *
import math

# Hungarian alphabet
alphabet = [
    "A", "Á", "B", "C", "Cs", "D", "Dz", "Dzs", "E", "É", "F",
    "G", "Gy", "H", "I", "Í", "J", "K", "L", "Ly", "M", "N",
    "Ny", "O", "Ó", "Ö", "Ő", "P", "Q", "R", "S", "Sz", "T",
    "Ty", "U", "Ú", "Ü", "Ű", "V", "W", "X", "Y", "Z", "Zs"
]

# Initialize the main window
app = CTk()
app.title("Hungarian Alphabet Table")
app.geometry("600x400")

# Textbox to display the typed string
textbox = CTkTextbox(app, width=550, height=50)
textbox.pack(pady=20)

# Frame for the alphabet table
table_frame = CTkFrame(app)
table_frame.pack()

# Calculate the number of columns
num_columns = math.ceil(len(alphabet) / 4)

# Variables to manage highlighting and typing
highlight_index = 0
typed_string = ""
highlight_running = True
highlight_update_id = None

# Function to update the highlighting
def update_highlight():
    global highlight_index, highlight_running, highlight_update_id
    if highlight_running:
        for i in range(4):
            for j in range(num_columns):
                index = i * num_columns + j
                if index < len(alphabet):
                    label = labels[i][j]
                    if index == highlight_index:
                        label.configure(bg_color="gray")
                    else:
                        label.configure(bg_color="white")
        highlight_index = (highlight_index + 1) % len(alphabet)
        highlight_update_id = app.after(2000, update_highlight)  # Schedule next update

# Function to handle left mouse click
def on_click(event):
    global typed_string, highlight_index, highlight_running, highlight_update_id

    typed_string += alphabet[highlight_index - 1]
    textbox.insert(tk.END, alphabet[highlight_index - 1])
    highlight_index = 0  # Reset the highlight index to start from the beginning
    if highlight_update_id is not None:
        app.after_cancel(highlight_update_id)  # Cancel the previous highlight cycle
    highlight_update_id = app.after(0, update_highlight)  # Restart the highlighting process

# Function to handle double click
def on_double_click(event):
    global typed_string, highlight_running, highlight_update_id
    with open("typed_strings.txt", "a") as file:
        file.write(typed_string + "\n")
    typed_string = ""
    textbox.delete("1.0", tk.END)
    if highlight_update_id is not None:
        app.after_cancel(highlight_update_id)  # Stop the highlighting process
    highlight_update_id = None
    highlight_running = True
    highlight_update_id = app.after(2000, update_highlight)  # Restart the highlighting process

# Create labels for the alphabet table
labels = []
for i in range(4):
    row_labels = []
    for j in range(num_columns):
        index = i * num_columns + j
        if index < len(alphabet):
            label = CTkLabel(table_frame, text=alphabet[index], width=40, height=40, corner_radius=5)
            label.grid(row=i, column=j, padx=2, pady=2)
            label.bind("<Button-1>", on_click)
            label.bind("<Double-1>", on_double_click)
            row_labels.append(label)
    labels.append(row_labels)

# Start the highlighting process
update_highlight()

# Run the main event loop
app.mainloop()
