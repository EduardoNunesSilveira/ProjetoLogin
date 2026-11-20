import customtkinter as ctk
from Funcoes import Voltar_Login



def TelaCadastro (Main):

    frame = ctk.CTkFrame(Main)

    frame.pack(
        fill="both",
        expand=True,
        padx=0,
        pady=0
    )



    btn_voltar = ctk.CTkButton(
        frame,
        text="VOLTAR",
        command=lambda: Voltar_Login(
            frame,
            Main
        )
    )
    btn_voltar.place(x=10, y=10)
