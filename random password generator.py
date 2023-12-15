import tkinter as tk
from tkinter import ttk
import string
import random
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_var = tk.IntVar(value=12)
        self.length_entry = ttk.Entry(root, textvariable=self.length_var, width=5)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.lower_var = tk.BooleanVar(value=True)
        self.lower_check = ttk.Checkbutton(root, text="Include lowercase", variable=self.lower_var)
        self.lower_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="W")

        self.upper_var = tk.BooleanVar(value=True)
        self.upper_check = ttk.Checkbutton(root, text="Include uppercase", variable=self.upper_var)
        self.upper_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="W")

        self.digit_var = tk.BooleanVar(value=True)
        self.digit_check = ttk.Checkbutton(root, text="Include digits", variable=self.digit_var)
        self.digit_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="W")

        self.special_var = tk.BooleanVar(value=True)
        self.special_check = ttk.Checkbutton(root, text="Include special characters", variable=self.special_var)
        self.special_check.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="W")

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.result_var = tk.StringVar(value="")
        self.result_label = ttk.Label(root, textvariable=self.result_var, font=("Courier", 12))
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

        self.copy_button = ttk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=7, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        lowercase = string.ascii_lowercase if self.lower_var.get() else ""
        uppercase = string.ascii_uppercase if self.upper_var.get() else ""
        digits = string.digits if self.digit_var.get() else ""
        special_chars = string.punctuation if self.special_var.get() else ""

        all_chars = lowercase + uppercase + digits + special_chars

        if not any([self.lower_var.get(), self.upper_var.get(), self.digit_var.get(), self.special_var.get()]):
            self.result_var.set("Please select at least one option")
            return

        password = ''.join(random.choice(all_chars) for _ in range(length))
        self.result_var.set(password)

    def copy_to_clipboard(self):
        password = self.result_var.get()
        if password:
            pyperclip.copy(password)
            self.result_var.set("Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
