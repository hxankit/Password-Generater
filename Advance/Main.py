import tkinter as tk
import tkinter.ttk as ttk
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.root.grid_columnconfigure(0, weight=1)

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.length_entry = ttk.Entry(root, width=5)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.lower_var = tk.IntVar()
        self.lower_check = ttk.Checkbutton(root, text="Include lowercase", variable=self.lower_var)
        self.lower_check.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.upper_var = tk.IntVar()
        self.upper_check = ttk.Checkbutton(root, text="Include uppercase", variable=self.upper_var)
        self.upper_check.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.digits_var = tk.IntVar()
        self.digits_check = ttk.Checkbutton(root, text="Include digits", variable=self.digits_var)
        self.digits_check.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        self.symbols_var = tk.IntVar()
        self.symbols_check = ttk.Checkbutton(root, text="Include symbols", variable=self.symbols_var)
        self.symbols_check.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

      
        self.password_label = ttk.Label(root, text="Generated Password:")
        self.password_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.E)

        self.password_entry = ttk.Entry(root, width=30, state="readonly")
        self.password_entry.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)
       
        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

    def generate_password(self):
        length = int(self.length_entry.get())
        include_lower = bool(self.lower_var.get())
        include_upper = bool(self.upper_var.get())
        include_digits = bool(self.digits_var.get())
        include_symbols = bool(self.symbols_var.get())

        if not (include_lower or include_upper or include_digits or include_symbols):
            return  

        lowercase = string.ascii_lowercase if include_lower else ''
        uppercase = string.ascii_uppercase if include_upper else ''
        digits = string.digits if include_digits else ''
        symbols = string.punctuation if include_symbols else ''
        all_chars = lowercase + uppercase + digits + symbols
        password = ''.join(random.choice(all_chars) for _ in range(length))
        self.password_entry.config(state="normal")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.config(state="readonly")
    
    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
