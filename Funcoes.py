
from Telas.TelaMenu import TelaMenu


def validar_login(entry_usuario, entry_senha, resultado, frame, Main):

        usuario = entry_usuario.get()
        senha = entry_senha.get()

        if usuario == 'Guga' and senha == '1234':
            resultado.configure(
                text="Login realizado com sucesso!",
                text_color="green",
            )
            
            frame.destroy()
            TelaMenu(Main)
            
        else:
            resultado.configure(
                text="Usuário ou senha inválido",
                text_color="red"
            )


    


