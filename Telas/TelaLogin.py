#----------------
# TELA LOGIN
#----------------

import customtkinter as ctk

def TelaLogin(Main):

    frame = ctk.CTkFrame(Main)

    frame.pack(
        fill="both",
        expand=True,
        padx=0,
        pady=0
    )

    return frame
