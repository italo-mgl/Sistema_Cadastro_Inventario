from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk


#Cores

cor0 = "#2e2d2b" # Preta
cor1 = "#feffff"  # Branca
cor2 = "#4fa882"  # Verde
cor3 = "#38576b"  # Valor
cor4 = "#403d3d"  # Letra
cor5 = "#e06636"  # - profit
cor6 = "#038cfc"  # Azul
cor7 = "#3fbfb9"  # verde
cor8 = "#263238"  # + verde
cor9 = "#e9edf5"  # + verde


# Criando layout
janela = Tk()
janela.title("")
janela.geometry("900x600")
janela.configure(background=cor9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


# Criando 1° frame
frame_cima = Frame(janela, width=1043, height=50, bg=cor1, relief=FLAT)
frame_cima.grid(row=0, column=0)

# Criando 2° frame
frame_meio = Frame(janela, width=1043, height=303, bg=cor1, pady=20, relief=FLAT)
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Criando 3° frame
frame_baixo = Frame(janela, width=1043, height=300, bg=cor1, pady=20, relief=FLAT)
frame_baixo.grid(row=2, column=0, pady=1, padx=1, sticky=NSEW)

# Abrindo imagem
app_img = Image.open("agenda.png")
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, text=" Inventário Doméstico", width=900, compound=LEFT, relief=RAISED, anchor=NW, font=("Verdana 20 bold"), bg=cor1, fg=cor4)
app_logo.place(x=0, y=0)


janela.mainloop()

