import os
import tkinter as tk
from tkinter import filedialog, messagebox

__version__ = "1.1"

def rename_files(folder_path, old_name, new_name):
    if not folder_path or not old_name: # new name can be empty
        messagebox.showerror("Error", "All fields are required")
        return
    
    try:
        files = os.listdir(folder_path)
        for file in files:
            if old_name in file:
                new_file = file.replace(old_name, new_name)
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_file))
        messagebox.showinfo("Success", "Files renamed successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def add_prefix_suffix_to_files(folder_path, text, option):
    if not folder_path or not text:
        messagebox.showerror("Error", "Folder and text are required")
        return
    
    try:
        files = os.listdir(folder_path)
        for file in files:
            name, ext = os.path.splitext(file)
            if option == "prefix":
                new_file = text + name + ext
            else:  # suffix
                new_file = name + text + ext
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_file))
        messagebox.showinfo("Success", "Text added to all files successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# def add_prefix_to_files(folder_path, prefix):
#     if not folder_path or not prefix:
#         messagebox.showerror("Error", "Folder and Prefix are required")
#         return
    
#     try:
#         files = os.listdir(folder_path)
#         for file in files:
#             new_file = prefix + file
#             os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_file))
#         messagebox.showinfo("Success", "Prefix added to all files successfully")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

def main():
    print(f"BatchRenamer version {__version__}")
   
# Main application window
root = tk.Tk()
root.title("File Renamer")

# Folder selection
tk.Label(root, text="Folder:").grid(row=0, column=0, padx=10, pady=5)
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
select_button = tk.Button(root, text="Browse", command=select_folder)
select_button.grid(row=0, column=2, padx=10, pady=5)

renameBlock = tk.LabelFrame(root, text="Replace", padx=10, pady=10)
renameBlock.grid(row=1, column=0,columnspan=3, padx=10,pady=10, sticky="nsew")

# Old file name input
tk.Label(renameBlock, text="Old name:").grid(row=1, column=0, padx=10, pady=5)
old_name_entry = tk.Entry(renameBlock, width=50)
old_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# New file name input
tk.Label(renameBlock, text="New name:").grid(row=2, column=0, padx=10, pady=5)
new_name_entry = tk.Entry(renameBlock, width=50)
new_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Rename button
rename_button = tk.Button(renameBlock, text="Rename", 
                          command=lambda: rename_files(folder_entry.get(), old_name_entry.get(), new_name_entry.get()))
rename_button.grid(row=2, column=2, pady=20, sticky="ew")


# add prefix to files

addTextBlock = tk.LabelFrame(root, text="Add", padx=10, pady=10)
addTextBlock.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

prefix_suffix_var = tk.StringVar(value="prefix")
tk.Radiobutton(addTextBlock, text="Prefix", variable=prefix_suffix_var, value="prefix").grid(row=0, column=0, padx=10, pady=5, sticky="ew")
tk.Radiobutton(addTextBlock, text="Suffix", variable=prefix_suffix_var, value="suffix").grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Prefix input
tk.Label(addTextBlock, text="Add Text:").grid(row=1, column=0, padx=10, pady=5)
prefix_entry = tk.Entry(addTextBlock, width=50)
prefix_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Update the command for adding prefix/suffix
add_prefix_button = tk.Button(addTextBlock, text="Add", 
                              command=lambda: add_prefix_suffix_to_files(folder_entry.get(), prefix_entry.get(), prefix_suffix_var.get()))
add_prefix_button.grid(row=1, column=2, padx=10, pady=5, sticky="ew")






if __name__ == "__main__":
    main() 

# Start the main loop
root.mainloop()
