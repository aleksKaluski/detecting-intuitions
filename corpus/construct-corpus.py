import tkinter as tk
from tkinter import ttk

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

##########
# Fields to insert DOI/ISBN and text
##########

root = tk.Tk()
root.geometry("700x700")
root.title("Creating the corpus")

# DOI and text
tk.Label(root, text="DOI/ISBN").grid(row=0, column=0, padx=20, pady=20)
tk.Label(root, text="Text").grid(row=2, column=0, padx=20, pady=20)

# entries
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
entry2.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

# allow the column to expand
root.columnconfigure(1, weight=1)

##########
# Drop-down list to choose from
##########

# combobox and its label
tk.Label(root).grid(row=1, column=0, padx=20, pady=20)
combo_box = ttk.Combobox(
    root,
    values=["Ethics", "Epistemology", "Ontology", "Philosophy of Mind", "Philosophy of Language"],
    state="readonly"
)
combo_box.grid(row=1, column=0, padx=5, pady=5)
combo_box.set("Ethics")  # Valid default

# Selected item label
label = tk.Label(root, text="Category:")
label.grid(row=1, column=0, columnspan=2, pady=10)

combo_box.bind("<<ComboboxSelected>>", select)

root.mainloop()