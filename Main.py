
import customtkinter as ctk
from Telas import TelaLogin
from Telas import TelaMenu
from Telas import TelaCadastro



ctk.set_appearance_mode("dark")

Main = ctk.CTk()
Main.title("SISTEMA")
Main.geometry("500x400")

frame = TelaLogin.TelaLogin(Main)

Main.mainloop()
