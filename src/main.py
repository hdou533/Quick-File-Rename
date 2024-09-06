import os
import tkinter as tk
from tkinter import filedialog, messagebox

__version__ = "1.0"

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
folder_entry.grid(row=0, column=1, padx=10, pady=5)
select_button = tk.Button(root, text="Browse", command=select_folder)
select_button.grid(row=0, column=2, padx=10, pady=5)

# Old file name input
tk.Label(root, text="Old name:").grid(row=1, column=0, padx=10, pady=5)
old_name_entry = tk.Entry(root, width=50)
old_name_entry.grid(row=1, column=1, padx=10, pady=5)

# New file name input
tk.Label(root, text="New name:").grid(row=2, column=0, padx=10, pady=5)
new_name_entry = tk.Entry(root, width=50)
new_name_entry.grid(row=2, column=1, padx=10, pady=5)

# Rename button
rename_button = tk.Button(root, text="Rename Files", 
                          command=lambda: rename_files(folder_entry.get(), old_name_entry.get(), new_name_entry.get()))
rename_button.grid(row=3, column=1, pady=20)

if __name__ == "__main__":
    main() 

# Start the main loop
root.mainloop()
