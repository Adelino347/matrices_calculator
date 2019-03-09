from tkinter import *
class Colorizador_RGB(object):
    def __init__(self, conteiner, cor_bg = "gray"):
        self.bg = cor_bg
        #Frames
        self.frame1 = Frame(conteiner, bg = self.bg) 
        self.frame2 = Frame(conteiner, bg = self.bg)
        self.frame3 = Frame(conteiner, bg = self.bg)
        self.frame4 = Frame(conteiner, bg = self.bg)
        self.frame5 = Frame(conteiner, bg = self.bg)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        #Labels
        self.label1 = Label(self.frame1, text = "R:", bg = self.bg, fg = "red")
        self.label2 = Label(self.frame2, text = "G:", bg = self.bg, fg = "green")
        self.label3 = Label(self.frame3, text = "B:", bg = self.bg, fg = "blue")
        self.label4 = Label(self.frame4, text = "#000000", bg = self.bg, fg = "#000000", height = 3, font = ("Arial", 13))
        self.label1.pack(side = LEFT)
        self.label2.pack(side = LEFT)
        self.label3.pack(side = LEFT)
        self.label4.pack(side = LEFT)

        #Scales
        self.scale1 = Scale(self.frame1, from_ = 0, to = 255, orient = "horizontal", bg = self.bg,troughcolor = "white", activebackground = "gray", length = 400, command = self.colorir_canvas)
        self.scale2 = Scale(self.frame2, from_ = 0, to = 255, orient = "horizontal", bg = self.bg,troughcolor = "white", activebackground = "gray", length = 400, command = self.colorir_canvas)
        self.scale3 = Scale(self.frame3, from_ = 0, to = 255, orient = "horizontal", bg = self.bg,troughcolor = "white", activebackground = "gray", length = 400, command = self.colorir_canvas)
        self.scale1.pack(side = LEFT)
        self.scale2.pack(side = LEFT)
        self.scale3.pack(side = LEFT)

        #Canvas
        self.canvas = Canvas(self.frame5, width = 300, height = 300, bg = "#000000")
        self.canvas.pack()

    def colorir_canvas(self, event):
        self.hexadecimais = [(hex(self.scale1.get())), (hex(self.scale2.get())), (hex(self.scale3.get()))]
        self.red = self.hexadecimais[0][2:len(self.hexadecimais[0])]
        if len(self.red) ==1:
            self.red = '0' + self.red
        self.green = self.hexadecimais[1][2:len(self.hexadecimais[1])]
        if len(self.green) ==1:
            self.green = '0' + self.green
        self.blue = self.hexadecimais[2][2:len(self.hexadecimais[2])]
        if len(self.blue) ==1:
            self.blue = '0' + self.blue
        self.rgb_hex = "#" + self.red + self.green + self.blue
        self.label4.config(text = self.rgb_hex.upper())
        self.label4.config(fg = self.rgb_hex)
        self.canvas.config(bg = self.rgb_hex)
    
        
class Colorizador_options(object):
    def __init__(self, conteiner, cor_bg = "gray"):
        self.bg = cor_bg
        #Frames
        self.frame1 = Frame(conteiner, bg = self.bg)
        self.frame2 = Frame(conteiner, bg = self.bg)

        self.frame1.pack()
        self.frame2.pack()

        #Labels
        self.label1 = Label(self.frame1, text = "CORES:", bg = self.bg, width = 30, height = 3)
        self.label2 = Label(self.frame1, text = "#000000", bg = self.bg, fg = "#000000", font = ("Arial", 13), height = 3)

        self.label1.pack()
        self.label2.pack()
        
        #Listas
        self.color_options = [["#000000", "#353535", "#505050", "#6d6d6d", "#bfbfbf", "#ffffff"],
                              ["#00002d", "#00006d", "#0000b8", "#0000ff", "#0040ff", "#0096ff"],
                              ["#000f00", "#003500", "#006200", "#009600", "#00CB00", "#00FF00"],
                              ["#380000", "#920000", "#b00000", "#D20000", "#e50000", "#ff0000"],
                              ["#8f0031", "#8f0071", "#8f00b0", "#8f00d2", "#8f00ff", "#8f40ff"],
                              ["#FF00FF", "#FF26FF", "#FF5FFF", "#FF85FF", "#FFB8FF", "#FFDAFF"],
                              ["#8B8040", "#B88040", "#D28040", "#FF8040", "#FF9E40", "#FFCB40"],
                              ["#ff3100", "#ff6d00", "#ff8900", "#ffbc00", "#ffff00", "#ffff44"]]
        self.lista_cores = []

        #Canvas
        self.canvas = Canvas(self.frame2, cursor = 'hand2', width = (42)*6-2, height = (40+2)*8-1)
        self.canvas.pack()
        self.canvas.bind("<1>", self.colorir)
        
        x0, y0 = 3, 3
        x, y = 40, 40
        
        for cores in self.color_options:
            for cor in cores:
                self.canvas.create_rectangle(x0, y0, x, y, fill = cor)
                self.lista_cores.append(cor)
                x0 += 40+2
                x += 40+2
            y0 += 40+2
            y += 40+2
            x = 3
            x0 = 40
        
    def colorir(self, event):
        x_origem = self.canvas.winfo_rootx()
        y_origem = self.canvas.winfo_rooty()
        x_abs = self.canvas.winfo_pointerx()
        y_abs = self.canvas.winfo_pointery()

        ponto_x, ponto_y = (x_abs - x_origem), (y_abs - y_origem)
        numero_cor = self.canvas.find_closest(ponto_x, ponto_y)[0]
        self.label2['fg'] = self.lista_cores[numero_cor-1]
        self.label2['text'] = (self.lista_cores[numero_cor-1]).upper()
        
if __name__ == '__main__':
    janela1 = Tk()
    janela1.configure(background = "gray")
    frame1 = Frame(janela1, bg = "gray", borderwidth = 75)
    frame2 = Frame(janela1, bg = "gray", borderwidth = 50)
    frame1.pack(side = LEFT, anchor = N)
    frame2.pack(side = LEFT, anchor = N)
    Colorizador_options(frame1)
    Colorizador_RGB(frame2)
    janela1.mainloop()
