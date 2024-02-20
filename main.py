import tkinter as tk
import random
import string

class App:
    def __init__(self, title):
        root = tk.Tk()
        root.title(title)

        self.text_entry = tk.Text(root, height=5, width=30)
        self.text_entry.pack()
        self.text_entry.config(font=("Arial", 20))

        self.checkbox_num = tk.BooleanVar()
        self.checkbox_num_checkbutton = tk.Checkbutton(root, text="Цифры", variable=self.checkbox_num)
        self.checkbox_num_checkbutton.pack()
        self.checkbox_num_checkbutton.config(font=("Arial", 20))

        self.checkbox_uplet = tk.BooleanVar()
        self.checkbox_uplet_checkbutton = tk.Checkbutton(root, text="Заглавные буквы", variable=self.checkbox_uplet)
        self.checkbox_uplet_checkbutton.pack()
        self.checkbox_uplet_checkbutton.config(font=("Arial", 20))

        self.checkbox_downlet = tk.BooleanVar()
        self.checkbox_downlet_checkbutton = tk.Checkbutton(root, text="Строчные буквы", variable=self.checkbox_downlet)
        self.checkbox_downlet_checkbutton.pack()
        self.checkbox_downlet_checkbutton.config(font=("Arial", 20))

        self.checkbox_spec = tk.BooleanVar()
        self.checkbox_spec_checkbutton = tk.Checkbutton(root, text="Специальные символы", variable=self.checkbox_spec)
        self.checkbox_spec_checkbutton.pack()
        self.checkbox_spec_checkbutton.config(font=("Arial", 20))

        self.generate_button = tk.Button(root, text="Сгенерировать", command=self.generate_password)
        self.generate_button.pack()
        self.generate_button.config(font=("Arial", 20))

        root.mainloop()

    def generate_password(self):
        text = ""
        length = random.randint(8, 16)
        chars = ''

        if self.checkbox_num.get():
            chars += string.digits
        if self.checkbox_uplet.get():
            chars += string.ascii_uppercase
        if self.checkbox_downlet.get():
            chars += string.ascii_lowercase
        if self.checkbox_spec.get():
            chars += "!@#$%^&*()_-+=[]"

        if not chars:
            return

        for _ in range(length):
            text += random.choice(chars)

        password_list = list(text)
        random.shuffle(password_list)
        password_shuffled = '\n\n' + ''.join(password_list)

        self.text_entry.delete(1.0, tk.END)
        self.text_entry.insert(tk.END, password_shuffled)
        
        self.text_entry.tag_configure("center", justify='center')
        self.text_entry.tag_add("center", "1.0", "end")

test = App("khL0K[lg%ljC^-")
