from tkinter import*
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os

#Programa que mostra os valores em hexadecimal das 10 cores mais predominantes em uma imagem selecionada.

janela_principal= Tk() #Criando uma instância de frame ou janela tkinter
janela_principal.title("ColorHex") # Nome do programa na barra superior
janela_principal.geometry("1200x630+30+10") # Tamanho da janela
janela_principal.configure(bg="#e4e8eb")
janela_principal.resizable(False, False) # False a janela não ser redimensionada

def showimage ():
    global filename #filename sendo global, poderá ser usado em qualquer função (def)
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Abrir Imagem", filetype=(
        ("Arquivo JPG", "*.jpg"),
        ("Arquivo JPEG", "*.jpeg"),
        ("Arquivo PNG", "*.png")
    ))
    img=Image.open(filename)
    tamanho_imagem=(725,440)
    img=img.resize(tamanho_imagem)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=725, height=440) #Tamanho da janela que irá abrir a imagem que é a última "Label" antes dos botões
    lbl.image=img

def FindColor ():
    ct=ColorThief(filename)
    palette=ct.get_palette(color_count=11)

    rgb1=palette[0]
    rgb2=palette[1]
    rgb3=palette[2]
    rgb4=palette[3]
    rgb5=palette[4]
    rgb6=palette[5]
    rgb7=palette[6]
    rgb8=palette[7]
    rgb9=palette[8]
    rgb10=palette[9]

    color1=f"#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}"
    color2=f"#{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}"
    color3=f"#{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}"
    color4=f"#{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}"
    color5=f"#{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}"
    color6=f"#{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}"
    color7=f"#{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}"
    color8=f"#{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}"
    color9=f"#{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}"
    color10=f"#{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}"

    colors.itemconfig(id1, fil=color1)
    colors.itemconfig(id2, fil=color2)
    colors.itemconfig(id3, fil=color3)
    colors.itemconfig(id4, fil=color4)
    colors.itemconfig(id5, fil=color5)

    colors2.itemconfig(id6, fil=color6)
    colors2.itemconfig(id7, fil=color7)
    colors2.itemconfig(id8, fil=color8)
    colors2.itemconfig(id9, fil=color9)
    colors2.itemconfig(id10, fil=color10)

#Ícone
image_icon=PhotoImage(file="icon_cd.png")
janela_principal.iconphoto(False, image_icon)

#Faixa topo (cor grafite)
Label(janela_principal, width=220, height=10, bg="#363636").pack()
Label(janela_principal, text="ColorHex - Detector de Cores", font="arial 25 bold", foreground="white", bg="#363636").place(x=50, y=5)

#Frame de dentro (cor branco)
frame=Frame(janela_principal, width=1100, height=530, bg="#fff")
frame.place(x=50, y=50)

logo=PhotoImage(file="logo_cd.png")
Label(frame, image=logo, bg="#fff").place(x=10, y=1)

#Bloco de Cores - Esquerda
colors=Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors.place(x=20, y=105)

id1=colors.create_rectangle((10, 10, 50, 50), fill="#b8255f")
id2=colors.create_rectangle((10, 50, 50, 100), fill="#db4035")
id3=colors.create_rectangle((10, 100, 50, 150), fill="#ff9933")
id4=colors.create_rectangle((10, 150, 50, 200), fill="#fad000")
id5=colors.create_rectangle((10, 200, 50, 250), fill="#afb83b")

hex1=Label(colors, text="#b8255f", fg="#000", font="arial 12 bold", bg="white")
hex1.place(x=60, y=15)

hex2=Label(colors, text="#db4035", fg="#000", font="arial 12 bold", bg="white")
hex2.place(x=60, y=65)

hex3=Label(colors, text="#ff9933", fg="#000", font="arial 12 bold", bg="white")
hex3.place(x=60, y=115)

hex4=Label(colors, text="#fad000", fg="#000", font="arial 12 bold", bg="white")
hex4.place(x=60, y=165)

hex5=Label(colors, text="#afb83b", fg="#000", font="arial 12 bold", bg="white")
hex5.place(x=60, y=215)

#Bloco de Cores - Direita
colors2=Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors2.place(x=180, y=105)

id6=colors2.create_rectangle((10, 10, 50, 50), fill="#7ecc49")
id7=colors2.create_rectangle((10, 50, 50, 100), fill="#299438")
id8=colors2.create_rectangle((10, 100, 50, 150), fill="#6accbc")
id9=colors2.create_rectangle((10, 150, 50, 200), fill="#158fab")
id10=colors2.create_rectangle((10, 200, 50, 250), fill="#14aaf5")

hex6=Label(colors2, text="#7ecc49", fg="#000", font="arial 12 bold", bg="white")
hex6.place(x=60, y=15)

hex7=Label(colors2, text="#299438", fg="#000", font="arial 12 bold", bg="white")
hex7.place(x=60, y=65)

hex8=Label(colors2, text="#6accbc", fg="#000", font="arial 12 bold", bg="white")
hex8.place(x=60, y=115)

hex9=Label(colors2, text="#158fab", fg="#000", font="arial 12 bold", bg="white")
hex9.place(x=60, y=165)

hex10=Label(colors2, text="#14aaf5", fg="#000", font="arial 12 bold", bg="white")
hex10.place(x=60, y=215)

#Janela instruções
jan_inst=Label(frame, text="Instruções:\n\n1. Clicar em 'Abrir Imagem'\n2. Selecionar a imagem desejada\n3. Clicar em 'Valor das Cores\n4. O programa irá mostrar:\n    - As 10 cores predominantes na imagem\n    - Seus valores em hexadecimal.", fg="#000", font="arial 10 bold", justify=LEFT, bg="white",width=35, height=8, bd=0).place(x=19, y=384)

#Selecionando a imagem:

#Quadro cinza criado para emoldurar o quadro da imagem
selectimage=Frame(frame, width=745, height=510, bg="#d6dee5")
selectimage.place(x=345, y=10)

#Quadro preto dentro da moldura
f=Frame(selectimage, bd=3, bg="black", width=725, height=440, relief=GROOVE)
f.place(x=10, y=10)

#Etiqueta onde aparecerá a imagem escolhida que será 'puxada' na função 'showimage'
lbl=Label(f, bg="black")
lbl.place(x=0, y=0)

#Botões:

#Classe(Local_btn_ficará, texto_btn, larg_btn, alt_btn, _fontetipo_tamanho_negrito, funçao_btn, lugar_btn)
#Botão para escolher a foto
Button(selectimage, text="Abrir Imagem", width=16, height=1, font="arial 14 bold", command=showimage).place(x=100, y=460)
#Botão para gerar o valor das cores
Button(selectimage, text="Valor das Cores", width=16, height=1, font="arial 14 bold", command=FindColor).place(x=432, y=460)

janela_principal.mainloop()