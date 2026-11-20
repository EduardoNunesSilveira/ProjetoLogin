#----------------
# TELA LOGIN
#----------------

import customtkinter as ctk
from Funcoes import validar_login
from Funcoes import Cadastrar_usuario
from Funcoes import Voltar_Login




def TelaLogin(Main):

    frame = ctk.CTkFrame(Main)

    frame.pack( 
        fill="both",
        expand=True,
        padx=0,
        pady=0
    )

    label_usuario = ctk.CTkLabel(   # AQUI TEMOS A PALAVRA USUÁRIO APARECENDO NA TELA
        frame,
        text="Usuário",
    )
    label_usuario.pack(pady=15)


    entry_usuario = ctk.CTkEntry(    # AQUI TEMOS A CAIXA DE PREENCHER USUÁRIO APARECENDO NA TELA
        frame,
        placeholder_text="Digite seu usuário",
        justify="center",
        width=200
    )
    entry_usuario.pack(pady=2)


    label_senha = ctk.CTkLabel(      # AQUI TEMOS A PALAVRA SENHA APARECENDO NA TELA
        frame,
        text="Senha",   
    )
    label_senha.pack(pady=15)


    entry_senha = ctk.CTkEntry(      # AQUI TEMOS A CAIXA DE PREENCHER SENHA APARECENDO NA TELA, COM MASCARA *
        frame,
        placeholder_text="Digite sua senha",
        show="*",
        justify="center",
        width=200
    )
    entry_senha.pack(pady=2)

    botao_entrar = ctk.CTkButton(    # AQUI TEMOS O BOTÃO PARA ENTRAR, USAMOS A FUNÇÃO PARA VALIDAR, O COMMAND PRECISA DO LAMBDA POIS PRECISAMOS PASSAR PARAMETROS
        frame,
        text="ENTRAR",
        command=lambda: validar_login(
            entry_usuario,
            entry_senha,
            resultado,      
            frame,
            Main
        )
    )
    botao_entrar.pack(pady=10)

    resultado = ctk.CTkLabel(frame, text="")
    resultado.pack(pady=5)
   
    botao_cad_usuario = ctk.CTkButton(
        frame,
        text="CADASTRAR USUÁRIO",
        command=lambda:Cadastrar_usuario(
            frame,
            Main
        )
    )
    botao_cad_usuario.pack(pady=15)


 




    return frame
