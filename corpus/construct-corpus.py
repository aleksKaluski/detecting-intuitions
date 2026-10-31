"""
This script open a GUI window designed with Tkinter. The pourpuse of the GUI is to facillitate the 
process of creating the corpus by manually adding the entries to via a simple interface. The results are 
saved into a JSON file.
"""


import tkinter as tk
from tkinter import ttk


def select(event):
    """
    Makes it possible to select a discipline from the range.
    """
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

def quit_app():
    """
    Quit button.
    """
    root.destroy()

def approve():
    """
    'Approve' button that:
    1) saves the content
    2) refreshes the window
    3) saves the result in JSON file
    """

    doi = entry1.get()
    category = combo_box.get()
    text_content = text_field.get("1.0", tk.END).strip()

    # refresh the window
    entry1.delete(0, tk.END)
    combo_box.set("Ethics")
    text_field.delete("1.0", tk.END)
    label.config(text="Approved and cleared! Ready for new entry.")

root = tk.Tk()
root.geometry("800x700")
root.title("Creating the Corpus")
root.configure(bg='#f0f0f0')  # light gray background

# grid weights
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

style = ttk.Style()
style.theme_use('clam') 

# style for buttons and combobox
style.configure('TCombobox', font=('Arial', 12), padding=5)
style.configure('TButton', font=('Arial', 12), padding=5)
style.configure('TLabel', font=('Arial', 12))

# labels
tk.Label(root, text="DOI/ISBN:", bg='#f0f0f0', font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=20, pady=(20, 5), sticky='e')
tk.Label(root, text="Category:", bg='#f0f0f0', font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=20, pady=5, sticky='e')
tk.Label(root, text="Text:", bg='#f0f0f0', font=('Arial', 12, 'bold')).grid(row=2, column=0, padx=20, pady=(5, 20), sticky='ne')

# DOI Entry
entry1 = tk.Entry(root, font=('Arial', 12), bd=2, relief='groove')
entry1.grid(row=0, column=1, padx=5, pady=(20, 5), sticky='ew')

# Category Combobox
combo_box = ttk.Combobox(
    root,
    values=["Ethics", "Epistemology", "Ontology", "Philosophy of Mind", "Philosophy of Language"],
    state="readonly",
    font=('Arial', 12)
)
combo_box.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
combo_box.set("Ethics")

# text field implementation
text_field = tk.Text(root, width=60, height=25, font=('Consolas', 12), bd=2, relief='groove', wrap='word')
text_field.grid(row=2, column=1, padx=5, pady=(5, 20), sticky='nsew')

label = tk.Label(root, text="Selected Item: None", bg='#f0f0f0', font=('Arial', 12))
label.grid(row=3, column=0, columnspan=2, pady=(0, 10))

button_frame = tk.Frame(root, bg='#f0f0f0')
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

# control buttons
approve_button = ttk.Button(button_frame, text="Approve", command=approve)
approve_button.pack(side=tk.LEFT, padx=(0, 10))

quit_button = ttk.Button(button_frame, text="Quit", command=quit_app)
quit_button.pack(side=tk.LEFT, padx=(10, 0))

combo_box.bind("<<ComboboxSelected>>", select)

root.mainloop()
