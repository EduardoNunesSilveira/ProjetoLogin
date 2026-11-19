import customtkinter as ctk

def TelaMenu(Main):

    frame = ctk.CTkFrame(Main)

    frame.pack(
        fill="both",
        expand=True
    )


    label = ctk.CTkLabel(
        frame,
        text="MENU PRINCIPAL"
    )
    label.pack(pady=10)

    return frame