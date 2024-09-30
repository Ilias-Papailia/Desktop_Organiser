import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


 
def browse_directory():
    folder_selected = filedialog.askdirectory()
    
    directory_var.set(folder_selected)



def sort_files(directory):
    
    if not directory:
        messagebox.showerror("Error", "Please select a valid directory.")
        return

    desktop_path =Path(directory)     


    for file in os.listdir(desktop_path):
            file_path = desktop_path / file
            file_format = file.rsplit('.', 1)[-1]
            files_sort = False

            try:
                #simple if for basic format (png, jpeg, pdf etc)
                if file_format == "jpg" or file_format == "png" :
                    name = "Photos"    
                    folder = desktop_path  /  name
                    print("I WENT HERE")
                elif file_format == "pdf" or file_format == "docx" or file_format == "doc" or file_format == "csv" :
                    name = "Documents"
                    folder = desktop_path  /  name
                elif file_format == "exe" :
                    name = "General"
                    folder = desktop_path  /  name
                elif file_format == 'folder' :
                    continue
                    
                folder.mkdir(exist_ok = True) #check if folder exists   
                shutil.move(str(file_path), folder / file)
                files_sort = True
            except PermissionError:
                print(f"Skipped : {file} because it's being used")
            except FileNotFoundError:
                print(f"File not found: {file}. It may have been moved or deleted.")
            except Exception as e:
                print(f"An error occurred with {file}")
            
    if files_sort:
            messagebox.showinfo("Success", "Files successfully sorted!")
    else:
            messagebox.showinfo("No Files Moved", "No files were sorted!")
    print("Sucessfully sorted!")


# GUI 
root = tk.Tk()
root.title("File Sorter")
root.geometry("400x200")

label = tk.Label(root, text="Select a directory to sort:")
label.pack(pady=10)

directory_var = tk.StringVar()
directory_entry = tk.Entry(root, textvariable=directory_var, width=50)
directory_entry.pack(pady=10)


browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack(pady=5)


sort_button = tk.Button(root, text="Sort Files", command=lambda: sort_files(directory_var.get()))
sort_button.pack(pady=20)


root.mainloop()
