import customtkinter as CTk
from tkinter.messagebox import showerror, showinfo

class App(CTk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("600x470")
        self.title("Задача №1")

        self.entry_name = CTk.CTkEntry(self, placeholder_text="Name")
        self.entry_name.grid(row=0, column=0, padx=20, pady=10)

        self.entry_email = CTk.CTkEntry(self, placeholder_text="Email")
        self.entry_email.grid(row=1, column=0, padx=20, pady=10)

        self.entry_age = CTk.CTkEntry(self, placeholder_text="Age")
        self.entry_age.grid(row=2, column=0, padx=20, pady=10)

        self.button = CTk.CTkButton(self, text="Отправить", command=self.click_send)
        self.button.grid(row=3, column=0, padx=20, pady=10)

    def click_send(self):

        if self.check_entry():
            showinfo(message="Данные заполнены верно")
        else:
            showerror(title='Error', message="Данные заполнены не верно")

    def check_entry(self):
        if self.entry_name.get() == "":
            return False
        if int(self.entry_age.get()) <= 0:
            return False
        if '@' not in self.entry_email.get():
            return False
        return True

app = App()
app.mainloop()