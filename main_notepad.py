import tkinter as tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename

def saving_file():
    file_location = asksaveasfilename(defaultextension="txt", 
                                      filetypes=[("Text files", "*.txt"), ["All files", "*.*"]])
    if not file_location:
        return
    with open(file_location, "w") as file_output:
        text = text_edit.get(1.0, tk.END)
        file_output.write(text)
    root_window.title(f"My Own Notepad - {file_location}")

def opening_file():
    file_location = askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not file_location:
        return 
    text_edit.delete(1.0, tk.END)
    with open(file_location, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    root_window.title(f"My Own Notepad - {file_location}")

root_window = tk.Tk()
root_window.title("My Own Notepad")
root_window.rowconfigure(0, minsize=800)
root_window.columnconfigure(1, minsize=800)

text_edit = tk.Text(root_window)
text_edit.grid(row=0, column=1, sticky="nsew")

frame_button = tk.Frame(root_window, relief=tk.RAISED, bd=3)
frame_button.grid(row=0, column=0, sticky="ns")

open_file_button = tk.Button(frame_button, text="Open File", command=opening_file)
open_file_button.grid(row=0, column=0, padx=5, pady=5)

save_button = tk.Button(frame_button, text="Save As", command=saving_file)
save_button.grid(row=1, column=0, padx=5, pady=5)


root_window.mainloop()
