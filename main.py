from tkinter import *
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date

# Cores

cor0 = "#2e2d2b"  # Preta
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
frame_meio = Frame(janela, width=1043, height=303,
                   bg=cor1, pady=20, relief=FLAT)
frame_meio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Criando 3° frame
frame_baixo = Frame(janela, width=1043, height=300,
                    bg=cor1, pady=20, relief=FLAT)
frame_baixo.grid(row=2, column=0, pady=1, padx=1, sticky=NSEW)

# Estilização frame cima --------------------------------------
# Abrindo imagem
app_img = Image.open("agenda.png")
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima, image=app_img, text=" Inventário Doméstico", width=900,
                 compound=LEFT, relief=RAISED, anchor=NW, font=("Verdana 20 bold"), bg=cor1, fg=cor4)
app_logo.place(x=0, y=0)


# Estilização frame meio --------------------------------------

# Criando caixas de texto
label_nome = Label(frame_meio, text="Nome", height=1,anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_nome.place(x=10, y=10)
entrada_nome = Entry(frame_meio, width=30, justify="left", relief="solid")
entrada_nome.place(x=130, y=11)

label_local = Label(frame_meio, text="Sala/Area", height=1,anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_local.place(x=10, y=40)
entrada_local = Entry(frame_meio, width=30, justify="left", relief="solid")
entrada_local.place(x=130, y=41)

label_descricao = Label(frame_meio, text="Descrição", height=1,anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_descricao.place(x=10, y=70)
entrada_descricao = Entry(frame_meio, width=30, justify="left", relief="solid")
entrada_descricao.place(x=130, y=71)

label_modelo = Label(frame_meio, text="Nome", height=1,anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_modelo.place(x=10, y=100)
entrada_modelo = Entry(frame_meio, width=30, justify="left", relief="solid")
entrada_modelo.place(x=130, y=101)

label_data = Label(frame_meio, text="Data da compra", height=1,anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_data.place(x=10, y=130)
entrada_data = DateEntry(frame_meio, width=12, Backgroud="darkblue", bordewith=2, year=2023)
entrada_data.place(x=130, y=131)

label_valor = Label(frame_meio, text="Valor da compra", height=1,anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_valor.place(x=10, y=160)
entrada_valor = Entry(frame_meio, width=30, justify="left", relief="solid")
entrada_valor.place(x=130, y=161)

label_serie = Label(frame_meio, text="Numero de Série", height=1,anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_serie.place(x=10, y=190)
entrada_serie = Entry(frame_meio, width=30, justify="left", relief="solid")
entrada_serie.place(x=130, y=191)


# Criando botões --------------------------------------------------------

# Botão Carregar
label_carregar = Label(frame_meio, text="Imagem do item", height=1,anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_carregar.place(x=10, y=220)
botao_carregar = Button(frame_meio, width=30, text="carregar".upper(), compound=CENTER,anchor=CENTER, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor0)
botao_carregar.place(x=130, y=221)

# Botão Carregar
label_carregar = Label(frame_meio, text="Imagem do item", height=1,anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
label_carregar.place(x=10, y=220)
botao_carregar = Button(frame_meio, width=30, text="carregar".upper(), compound=CENTER,anchor=CENTER, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor0)
botao_carregar.place(x=130, y=221)

# Botão Inserir
# Abrindo imagem
img_add = Image.open("add.png")
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

botao_inserir = Button(frame_meio, image=img_add, width=95, text="  Adicionar".upper(), compound=LEFT,anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor0)
botao_inserir.place(x=330, y=10)

# Botão Atualizar
# Abrindo imagem
img_update = Image.open("update.png")
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

botao_update = Button(frame_meio, image=img_update, width=95, text="  Atualizar".upper(), compound=LEFT,anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor0)
botao_update.place(x=330, y=50)


# Botão Deletar
# Abrindo imagem
img_delete = Image.open("delete.png")
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)

botao_update = Button(frame_meio, image=img_delete, width=95, text="  Apagar".upper(), compound=LEFT,anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor0)
botao_update.place(x=330, y=90)

janela.mainloop()
