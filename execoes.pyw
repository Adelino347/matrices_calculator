import tkinter as t
class MensagemDeErro(object):
    def __init__(self, mensagem, corDeFundo = 'white', corDeLetra = "red"):
        self.janelaDeErro = t.Tk()
        self.janelaDeErro.title("MENSAGEM DE ERRO")
        self.janelaDeErro.configure(background = corDeFundo)
        self.mensagemDeErro = t.Label(self.janelaDeErro,bg = corDeFundo, fg = corDeLetra, text = mensagem, font = ("Times New Roman", 12, "bold"))
        self.mensagemDeErro.pack(side = t.LEFT)
        self.janelaDeErro.mainloop()
if __name__ == '__main__':
    MensagemDeErro("Erro")
