from tkinter import * 
from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import filedialog as fd
from webbrowser import BackgroundBrowser

from PIL import Image, ImageTk

from tkcalendar import Calendar, DateEntry
from datetime import date

from view import*
import os

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

# Criando funções ------------------------------------------------
global tree

# Função Inserir
def inserir():
    global imagem, imagem_string, l_imagem

    nome = entrada_nome.get()
    local = entrada_local.get()
    descricao = entrada_descricao.get()
    modelo = entrada_modelo.get()
    data = entrada_data.get()
    valor = entrada_valor.get()
    serie = entrada_serie.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, modelo, data, valor, serie, imagem]

    for i in lista_inserir:
        if i =="":
            messagebox.showerror("Erro", "Preencha todos os campos, por favor")
            return
        
    inserir_form(lista_inserir)

    messagebox.showinfo("Sucesso", "Os dados foram inseridos com sucesso")


    entrada_nome.delete(0, "end")
    entrada_local.delete(0, "end")
    entrada_descricao.delete(0, "end")
    entrada_modelo.delete(0, "end")
    entrada_data.delete(0, "end")
    entrada_valor.delete(0, "end")
    entrada_serie.delete(0, "end")
    

    mostrar()


# Funcao atualizar

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]
         
    
        entrada_nome.delete(0, "end")
        entrada_local.delete(0, "end")
        entrada_descricao.delete(0, "end")
        entrada_modelo.delete(0, "end")
        entrada_data.delete(0, "end")
        entrada_valor.delete(0, "end")
        entrada_serie.delete(0, "end")

        id = int(treev_lista[0])
        entrada_nome.insert(0, treev_lista[1])
        entrada_local.insert(0, treev_lista[2])
        entrada_descricao.insert(0, treev_lista[3])
        entrada_modelo.insert(0, treev_lista[4])
        entrada_data.insert(0, treev_lista[5])
        entrada_valor.insert(0, treev_lista[6])
        entrada_serie.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]



        def update():
            global imagem, imagem_string, label_imagem

            nome = entrada_nome.get()
            local = entrada_local.get()
            descricao = entrada_descricao.get()
            modelo = entrada_modelo.get()
            data = entrada_data.get()
            valor = entrada_valor.get()
            serie = entrada_serie.get()
            imagem = imagem_string

            if imagem =="":
                imagem = entrada_serie.insert(0, treev_lista[7])

            lista_update = [nome, local, descricao, modelo, data, valor, serie, imagem, id]

            for i in lista_update:
                if i=="":
                    messagebox.showerror("Erro", "Preencha todos os campos, por favor")
                    return

            atualizar_form(lista_update)
            messagebox.showinfo("Sucesso", "Os dados foram atualizados com sucesso")
            
            entrada_nome.delete(0, "end")
            entrada_local.delete(0, "end")
            entrada_descricao.delete(0, "end")
            entrada_modelo.delete(0, "end")
            entrada_data.delete(0, "end")
            entrada_valor.delete(0, "end")
            entrada_serie.delete(0, "end")

            botao_confirmar.destroy()

            mostrar()

        botao_confirmar = Button(frame_meio, command=update, text="  Confirmar".upper(), overrelief=RIDGE, font=("Ivy 8 bold"), bg=cor2, fg=cor1)
        botao_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror("Erro", "selecione um dos dados na tabela, por favor")



# Funcao Deletar

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo("Sucesso", "Os dados foram deletados com sucesso")

        mostrar()

    except IndexError:
        messagebox.showerror("Erro", "selecione um dos dados na tabela, por favor")



# Funcão para a escolha da imagem
global imagem, imagem_string, label_imagem

def escolher_imagem():
    global imagem, imagem_string, label_imagem
    imagem = fd.askopenfilename()
    imagem_string = imagem
    

    # Abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    app_logo = Label(frame_meio, image=imagem, bg=cor1, fg=cor4)
    app_logo.place(x=700, y=10)


# Função ver a imagem do item

def ver_imagem():
    global imagem, imagem_string, label_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]
    
    itens = ver_item(valor)

    imagem = itens[0][8]

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = treev_lista[0]
         
    
    entrada_nome.delete(0, "end")
    entrada_local.delete(0, "end")
    entrada_descricao.delete(0, "end")
    entrada_modelo.delete(0, "end")
    entrada_data.delete(0, "end")
    entrada_valor.delete(0, "end")
    entrada_serie.delete(0, "end")

    id = int(treev_lista[0])
    entrada_nome.insert(0, treev_lista[1])
    entrada_local.insert(0, treev_lista[2])
    entrada_descricao.insert(0, treev_lista[3])
    entrada_modelo.insert(0, treev_lista[4])
    entrada_data.insert(0, treev_lista[5])
    entrada_valor.insert(0, treev_lista[6])
    entrada_serie.insert(0, treev_lista[7])
    imagem_string = treev_lista[8]


    # Abrindo imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    label_imagem = Label(frame_meio, image=imagem, bg=cor1, fg=cor4)
    label_imagem.place(x=700, y=10)



# Estilização frame cima --------------------------------------
# Abrindo imagem
app_img = Image.open("icones/agenda.png")
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

label_modelo = Label(frame_meio, text="Modelo", height=1,anchor=NW, font=("Ivy 10 bold"), bg=cor1, fg=cor4)
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
botao_carregar = Button(frame_meio, command=escolher_imagem, width=29, text="carregar".upper(), compound=CENTER,anchor=CENTER, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor0)
botao_carregar.place(x=130, y=221)

# Botão Inserir
# Abrindo imagem
img_add = Image.open("icones/add.png")
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

botao_inserir = Button(frame_meio, command=inserir, image=img_add, width=95, text="  Adicionar".upper(), compound=LEFT,anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor0)
botao_inserir.place(x=330, y=10)

# Botão Atualizar
# Abrindo imagem
img_update = Image.open("icones/update.png")
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

botao_update = Button(frame_meio, command=atualizar, image=img_update, width=95, text="  Atualizar".upper(), compound=LEFT,anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor0)
botao_update.place(x=330, y=50)

# Botão Deletar
# Abrindo imagem
img_delete = Image.open("icones/delete.png")
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)

botao_deletar = Button(frame_meio, command=deletar, image=img_delete, width=95, text="  Apagar".upper(), compound=LEFT,anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor0)
botao_deletar.place(x=330, y=90)

# Botão Ver Item
# Abrindo item
img_item = Image.open("icones/item.png")
img_item = img_item.resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)

botao_item = Button(frame_meio,command=ver_imagem, image=img_item, width=95, text="  Ver Item".upper(), compound=LEFT,anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=cor1, fg=cor0)
botao_item.place(x=330, y=221)

# Labels Quantidade Total e Valores

label_total = Label(frame_meio, text="",width=14, height=2, pady=6, anchor=CENTER, font=("Ivy 17 bold"), bg=cor7, fg=cor1)
label_total.place(x=450, y=17)
label_total_ = Label(frame_meio, text="        Valor Total dos Itens      ", height=1,anchor=NW, font=("Ivy 10 bold"), bg=cor7, fg=cor1)
label_total_.place(x=450, y=18)

label_quantidade = Label(frame_meio, text="",width=14, height=2, pady=15, anchor=CENTER, font=("Ivy 17 bold"), bg=cor7, fg=cor1)
label_quantidade.place(x=450, y=90)
label_quantidade_ = Label(frame_meio, text="   Quantidade Total dos Itens   ", height=1,anchor=CENTER, font=("Ivy 10 bold"), bg=cor7, fg=cor1)
label_quantidade_.place(x=450, y=92)


# Tabela
def mostrar():
    global tree

# Criando tabela descrição de itens  -----------------

    tabela_head = ['#Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

    lista_itens = ver_form()

    tree = ttk.Treeview(frame_baixo, selectmode="extended",columns=tabela_head, show="headings")

    # barra vertical
    vsb = ttk.Scrollbar(frame_baixo, orient="vertical", command=tree.yview)

    # barra horizontal
    hsb = ttk.Scrollbar(frame_baixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_baixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    label_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    label_quantidade['text'] = Total_itens

mostrar()



janela.mainloop()
