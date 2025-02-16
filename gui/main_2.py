import customtkinter as CTk
from tkinter.messagebox import showerror, showinfo

class App(CTk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("600x470")
        self.title("Задача №2")

        self.textbox = CTk.CTkTextbox(self, height=20, fg_color="transparent", text_color="orange",
                                      font=('Times New Roman', 20))
        self.textbox.grid(row=0)
        self.textbox.insert('0.0', "Account")

        self.entry_name = CTk.CTkEntry(self, placeholder_text="Full Name")
        self.entry_name.grid(row=1, column=0, columnspan=2, ipadx=70, pady=10)

        self.entry_email = CTk.CTkEntry(self, placeholder_text="Email Adress")
        self.entry_email.grid(row=2, column=0, columnspan=2, ipadx=70, pady=10)

        self.entry_email2 = CTk.CTkEntry(self, placeholder_text="Email Adress")
        self.entry_email2.grid(row=3, column=0, columnspan=2, ipadx=70, pady=10)

        self.textbox2 = CTk.CTkTextbox(self, height=20, fg_color="transparent", text_color="orange",
                                      font=('Times New Roman', 20))
        self.textbox2.grid(row=4)
        self.textbox2.insert('0.0', "Gender")

        self.radio_var = CTk.IntVar(value=0)
        self.rb_male = CTk.CTkRadioButton(self, text="Male", variable=self.radio_var, value=1)
        self.rb_male.grid(row=5, column=0, pady=10)

        self.rb_Female = CTk.CTkRadioButton(self, text="Female", variable=self.radio_var, value=2)
        self.rb_Female.grid(row=5, column=1, pady=10)

        self.textbox3 = CTk.CTkTextbox(self, height=20, fg_color="transparent", text_color="orange",
                                      font=('Times New Roman', 20))
        self.textbox3.grid(row=6)
        self.textbox3.insert('0.0', "Programm languages")

        self.checkbox = CTk.CTkCheckBox(self, text="Python")
        self.checkbox.grid(row=7, column=0, pady=10)

        self.checkbox2 = CTk.CTkCheckBox(self, text="Java")
        self.checkbox2.grid(row=7, column=1, pady=10)

        self.checkbox3 = CTk.CTkCheckBox(self, text="C#")
        self.checkbox3.grid(row=7, column=2, pady=10)

        self.checkbox4 = CTk.CTkCheckBox(self, text="C++")
        self.checkbox4.grid(row=7, column=3, pady=10)

        self.button = CTk.CTkButton(self, text="SUBMIT", fg_color="orange", text_color="black", command=self.click_send)
        self.button.grid(row=8, column=0, pady=10)

    def click_send(self):

        if self.check_entry():
            showinfo(message="Пользователь успешно зарегистрирован в системе")
            print(self.result_info())
        else:
            showerror(title='Error', message="Данные заполнены не верно")

    def check_entry(self):
        if self.entry_name.get() == "":
            return False
        if '@' not in self.entry_email.get() and '@' not in self.entry_email2.get():
            return False
        if self.radio_var.get() == 0:
            return False
        return True

    def result_info(self):
        result = ""
        result += f"name:{self.entry_name.get()}\n"
        result += f"email:{self.entry_email.get()}\n"
        if self.radio_var.get() == 1:
            result += f"Gender:Male"
        else:
            result += f"Gender:Female"
        return result

app = App()
app.mainloop()