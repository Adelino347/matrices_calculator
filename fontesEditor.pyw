from tkinter import *
class FontesDeTexto(object):
    def __init__(self, conteiner):
        self.tipoDeFontes = ["Arial","Arial Black", "Arial Bold", "Arial Bold Italic", "Arial Italic",
                    "Comic Sans MS", "Comic Sans MS Bold",
                    "Courier 10","Courier 12", "Courier 15", "Courier New", "Courier New Bold", "Courier New Bold Italic", "Courier New Italic"
                    "Georgia","Georgia Bold","Georgia Bold Italic","Georgia Italic",
                    "Impact",
                    "Lucida Console", "Lucida Sans Unicode", "Microsoft Sans Serif", "Modern",
                    "MS Sans Serif 8","MS Sans Serif 10","MS Sans Serif 12","MS Sans Serif 14","MS Sans Serif 18","MS Sans Serif 24",
                    "Palatino Linotype","Palatino Linotype Bold","Palatino Linotype Bold Italic","Palatino Linotype Italic",
                    "Roman",
                    "Script",
                    "Small Fonts",
                    "Symbol",
                    "Symbol 8","Symbol 10","Symbol 12","Symbol 14","Symbol 18","Symbol 24",
                    "Tahoma","Tahoma Bold",
                    "Times New Roman","Times New Roman Bold","Times New Roman Bold Italic","Times New Roman Italic",
                    "Trebuchet MS","Trebuchet MS Bold","Trebuchet MS Bold Italic","Trebuchet MS Italic"
                    "Verdana","Verdana Bold","Verdana Bold Italic","Verdana Italic",
                    "Webdings",
                    "WingDings"]
        self.bg = "#f9f9f9"
        conteiner['bg'] = self.bg
        
        if str(type(conteiner)) == "<class 'tkinter.Tk'>":
            conteiner.geometry("750x550")
            conteiner.mainloop

        #Frames
        self.frame1 = Frame(conteiner, bg = self.bg)
        self.frame2 = Frame(conteiner, bg = self.bg, padx = 10)
        self.labelFrame1 = LabelFrame(self.frame2, text = "Opções:", bg = self.bg, padx = 20, pady = 10)
        self.labelFrame2 = LabelFrame(self.frame2, text = "Exemplo:", bg = self.bg, padx = 20)
        self.frame1.pack(side = LEFT, anchor = N)
        self.frame2.pack(side = LEFT, anchor = N)
        self.labelFrame1.pack(anchor = N)
        self.labelFrame2.pack(anchor = CENTER)
        #Label
        self.label1 = Label(self.frame1, text = "Fontes:", font = ("Times New Roman", 14, "bold"), bg = self.bg)
        self.label2 = Label(self.labelFrame2, text = "Arial", font = ("Arial", 16), bg = self.bg)
        self.label1.pack(side = TOP, anchor = N)
        self.label2.pack(side = LEFT, anchor = W)
        
        #Scrollbar+Listbox
        self.yScroll = Scrollbar(self.frame1, orient= VERTICAL, width = 30,)
        self.yScroll.pack(side = LEFT)
        
        self.listbox = Listbox(self.frame1, yscrollcommand = self.yScroll.set, height = 30, width = 30)
        self.listbox.pack(side = LEFT)
        self.listbox.bind("<Any-ButtonRelease>", self.mudar_fonte)
        self.listbox.bind("<KeyRelease-Return>", self.mudar_fonte) 

        self.yScroll['command'] = self.listbox.yview

        for fonte in self.tipoDeFontes[::-1]:
            self.listbox.insert(0, fonte)
        self.listbox.selection_anchor(0)

        #Botões
        self.negrito = Button(self.labelFrame1, text = "Negrito", font = ("Arial", 13, 'bold'), width = 7, command = self.boldar)
        self.italico = Button(self.labelFrame1, text = "Itálico", font = ("Times New Roman", 12, 'italic'), width = 7,command = self.italizar)
        self.negrito.pack(side = LEFT)
        self.italico.pack(side = LEFT)
        
    def mudar_fonte(self, event):
        indice = (self.listbox.curselection())[0]
        self.label2['text'] = self.tipoDeFontes[indice]
        self.label2['font'] = (self.tipoDeFontes[indice], 16)
        if self.negrito['relief'] == GROOVE:
            if self.italico['relief'] == GROOVE:
                self.label2['font']= (self.tipoDeFontes[indice], 16, 'bold', 'italic')
            else:
                self.label2['font']= (self.tipoDeFontes[indice], 16, 'bold')
        elif self.italico['relief'] == GROOVE:
            self.label2['font']= (self.tipoDeFontes[indice], 16, 'italic')
        else:
            self.label2['font'] = (self.tipoDeFontes[indice], 16)

        

    def boldar(self):
        if self.negrito['relief'] == GROOVE:
            self.negrito['relief'] = RAISED
            if self.italico['relief'] == GROOVE:
               self.label2['font'] = (self.label2['text'], 16, 'italic')
            else:
                self.label2['font'] = (self.label2['text'], 16)
        else:
            self.negrito['relief'] = GROOVE
            if self.italico['relief'] == GROOVE:
               self.label2['font'] = (self.label2['text'], 16, 'bold', 'italic')
            else:
                self.label2['font'] = (self.label2['text'], 16, 'bold')
                
        self.variavel = self.label2['font']
        
    def italizar(self):
        if self.italico['relief'] == GROOVE:
            self.italico['relief'] = RAISED
            if self.negrito['relief'] == GROOVE:
               self.label2['font'] = (self.label2['text'], 16, 'bold')
            else:
                self.label2['font'] = (self.label2['text'], 16)
        else:
            self.italico['relief'] = GROOVE
            if self.negrito['relief'] == GROOVE:
               self.label2['font'] = (self.label2['text'], 16, 'bold', 'italic')
            else:
                self.label2['font'] = (self.label2['text'], 16, 'italic')
        self.variavel = self.label2['font']

if __name__ == '__main__':
    variavel = "0"
    FontesDeTexto(Tk())
    
