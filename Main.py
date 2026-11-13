
import customtkinter as ctk
from Telas import TelaLogin

ctk.set_appearance_mode("dark")

Main = ctk.CTk()
Main.title("SISTEMA")
Main.geometry("500x400")

frame = TelaLogin.TelaLogin(Main)

Main.mainloop()
