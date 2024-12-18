# telas do jogo
import ctypes
import tkinter as tk
from tkinter import font
from tkinter import filedialog, messagebox, Label, Tk, Canvas, PhotoImage
import customtkinter as ctk
from customtkinter import CTkImage, CTkFont 
from PIL import Image, ImageDraw, ImageFont, ImageTk


class Telas:
    def __init__(self, root):
        self.widgets_dinamicos = []  # Lista para armazenar widgets dinâmicos
        self.root = root  # Referência à janela principal
        self.load_fonts()  # Carrega as fontes personalizadas
        
        
        
    def load_font(self, font_path):  # Método para carregar fontes personalizadas
        FR_PRIVATE = 0x10
        FR_NOT_ENUM = 0x20
        pathbuf = ctypes.create_unicode_buffer(font_path)
        ctypes.windll.gdi32.AddFontResourceExW(pathbuf, FR_PRIVATE | FR_NOT_ENUM, 0)


    def load_fonts(self):  # Método para inicializar e verificar fontes
        self.load_font("fonts/Gelio Fasolada.ttf")
        self.load_font("fonts/OlympusBold.ttf")        
        # Força registro das fontes
        temp_widget = tk.Label(self.root, text="")
        temp_widget.destroy()       
        # Verifica as fontes carregadas
        #print("Fontes disponíveis:", font.families())  # Opcional: listar todas as fontes disponíveis  

# TELAS
    def tela_01(self):
        self.canvas_abre = Canvas(self.root, width=800, height=600, bg="black", bd=0, highlightthickness=0)
        self.canvas_abre.place(x=0, y=0)  # Posição do Canvas na tela
        self.widgets_dinamicos.append(self.canvas_abre)
        
        # Titulo                
        label_titulo = ctk.CTkLabel(
            self.root,
            text= "Ascent To Olympus",
            text_color='#DAA520',  # Cor do texto
            bg_color="black",  # Cor de fundo
            font=("Gelio Fasolada", 28)) # Fonte e tamanho
           
        label_titulo.place(relx=0.5, y=10, anchor="n")
        self.widgets_dinamicos.append(label_titulo)
        
        # SubTitulo    
        label_subtitulo = ctk.CTkLabel(
            self.root,
            text= "The Ancient Greek Game",
            text_color='#FF0000',  # Cor do texto vermelho
            bg_color="black",
            font=("Gelio Greek Diner", 17) )
                   
        label_subtitulo.place(relx=0.5, y=40, anchor="n")
        self.widgets_dinamicos.append(label_subtitulo)
        
        # Linha           
        self.canvas_abre.create_text(
            400,  # Coordenada X (centralizado na tela)
            75,   # Coordenada Y (acima da imagem)
            text="<><><><><><><><><><><><><><><><><><><><><><><><><><><>",  # Texto que será exibido
            fill='#B8860B',  # Cor do texto RGB color: 184/255, 134/255, 11/255, 1
            font=("Arial", 12),  # Fonte e Tamanho
            anchor="center")  # Alinhamento centralizado   
        
        
        self.imagem_abre = "images/abre.jpg"
        
        try:
            imagem_tela_01 = Image.open(self.imagem_abre) # Carrega a imagem com Pillow
            largura_canvas, altura_canvas = 500, 364  # Dimensões da imagem
            imagem_tela_01.thumbnail((largura_canvas, altura_canvas), Image.Resampling.LANCZOS)  # Redimensionamento proporcional
            self.imagem_canvas = ImageTk.PhotoImage(imagem_tela_01)   
            # Adiciona a imagem ao Canvas 
            self.canvas_abre.create_image(150, 80, anchor="nw", image=self.imagem_canvas)
        except FileNotFoundError:
            print("Erro: Não foi possível carregar a imagem:", self.imagem_abre)  
                    
        self.canvas_abre.create_text(
            400,  # Coordenada X 
            440,   # Coordenada Y 
            text="<><><><><><><><><><><><><><><><><><><><><><><><><><><>",  
            fill='#B8860B', 
            font=("Arial", 12), 
            anchor="center")  
        
        texto_abertura =(
"""Embark on a Greek Mythology Adventure !
Roll the dice, collect cards, overcome challenges, and conquer Olympus !
Move across the board by rolling the dice.
Win battles by rolling 4 or more.
Use cards to overcome obstacles. Collect up to 3 cards."""
               )
        
        label_texto_abertura = ctk.CTkLabel(
            self.root,
            text=texto_abertura,
            text_color="white",  # Cor do texto
            bg_color="black",  # Cor de fundo
            font=("Olympus", 16)) # Fonte e tamanho      

        label_texto_abertura.place(relx=0.5, y=460, anchor="n")
        self.widgets_dinamicos.append(label_texto_abertura)
        
        # linha        
        self.canvas_abre.create_text(
            400,  
            540,   
            text="<><><><><><><><><><><><><><><><><><><><><><><><><><><>", 
            fill='#B8860B',  
            font=("Arial", 12),  
            anchor="center")  
               
        # Botão iniciar
        botao_iniciar = ctk.CTkButton(
            self.canvas_abre,
            width= 100,
            fg_color='#FF0000',
            hover_color="#FFA500",
            text="Become a Legend!",
            font= ("Gelio Fasolada", 14),
            command=lambda: self.tela_02()
        )
        botao_iniciar.place(x=350, y=560)
        self.widgets_dinamicos.append(botao_iniciar)    


    def tela_02(self):
        self.canvas_abre = Canvas(self.root, width=800, height=600, bg="black", bd=0, highlightthickness=0)
        self.canvas_abre.place(x=0, y=0) 
        self.widgets_dinamicos.append(self.canvas_abre)
        
        # Titulo                
        label_titulo = ctk.CTkLabel(
            self.root,
            text= "Ascent To Olympus",
            text_color='#DAA520',  # Cor do texto amarela
            bg_color="black",  
            font=("Gelio Fasolada", 28)) 
           
        label_titulo.place(relx=0.5, y=10, anchor="n")
        self.widgets_dinamicos.append(label_titulo)
        
        # SubTitulo    
        label_subtitulo = ctk.CTkLabel(
            self.root,
            text= "The Ancient Greek Game",
            text_color='#FF0000',  # Cor do texto vermelho
            bg_color="black",
            font=("Gelio Greek Diner", 17) )
                   
        label_subtitulo.place(relx=0.5, y=40, anchor="n")
        self.widgets_dinamicos.append(label_subtitulo)
        
        # Linha           
        self.canvas_abre.create_text(
            400,  
            75,   
            text="<><><><><><><><><><><><><><><><><><><><><><><><><><><>",  
            fill='#B8860B',  # Cor do texto RGB color: 184/255, 134/255, 11/255, 1
            font=("Arial", 12), 
            anchor="center")  
        
        
        self.canvas_abre.create_text(
            400,  
            100,  
            text="Reach Mount Olympus and receive the Gods' gift!",  
            fill='white',
            font=("Olympus", 16), 
            anchor="center") 
        
        self.canvas_abre.create_text(
            400,  
            125,  
            text="<><><><><><><><><><><><><><><><><><><><><><><><><><><>", 
            fill='#B8860B',  
            font=("Arial", 12), 
            anchor="center")   
        
        self.canvas_abre.create_text(
            400,  
            160,   
            text="Choose a Player", 
            fill='#FF8C00',  # Cor do texto RGB color: 255/255, 140/255, 0/255, 1  # DarkOrange
            font=("Gelio Fasolada", 20),  
            anchor="center") 
        
        
        # Imagem botão Hipolita
        self.image_hipolita_menu = PhotoImage(file="images/carinha_hipolita_menu.png")  # Caminho da imagem
        self.image_hipolita_hover = PhotoImage(file="images/carinha_escolha_hipolita_hover.png")  # Imagem para o hover
        self.image_hipolita_click = PhotoImage(file="images/carinha_escolha_hipolita_click.png")  # Imagem para o clique

        # Create_image para desenhar a imagem diretamente no Canvas
        self.img_id = self.canvas_abre.create_image(400, 230, image=self.image_hipolita_menu)

        # Associando os eventos de hover e clique com a imagem
        self.canvas_abre.tag_bind(self.img_id, '<Button-1>', self.on_button_click)  # Evento de clique
        self.canvas_abre.tag_bind(self.img_id, '<Enter>', self.on_hover_enter)  # Evento de hover (mouse entra)
        self.canvas_abre.tag_bind(self.img_id, '<Leave>', self.on_hover_leave)  # Evento de hover (mouse sai)
        
        label_botao_hipolita = ctk.CTkLabel(
        self.root,
        text= "Hippolita",
        text_color='white',  
        bg_color="black",
        font=("Gelio Fasolada", 18) )
                   
        label_botao_hipolita.place(relx=0.5, y=280, anchor="n")
        self.widgets_dinamicos.append(label_botao_hipolita)
        
        
        
        
        # Escolha uma carta
        self.canvas_abre.create_text(
        400,  
        350,   
        text= "Click on a card to draw your starting card", 
        fill='#FF8C00',  # Cor do texto RGB color: 255/255, 140/255, 0/255, 1  # DarkOrange
        font=("Gelio Fasolada", 16),  
        anchor="center") 
    
        
        

        
        
        
        
        
        

        # Botão de voltar
        botao_voltar = ctk.CTkButton(
            self.canvas_abre,
            width=100,
            fg_color='#FF0000',
            hover_color="#FFA500",
            text="Go Back!",
            font=("Gelio Fasolada", 14),
            command=lambda: self.tela_01()
        )
        botao_voltar.place(x=350, y=550)
        self.widgets_dinamicos.append(botao_voltar)

    def on_button_click(self, event):  # Adicionando o parâmetro 'event'
        print("Botão Circular Clicado!")
        # Altera a imagem para a versão 'clicada' após o clique
        self.canvas_abre.itemconfig(self.img_id, image=self.image_hipolita_click)
        self.executar_comando()  # Chama a função interna após o clique

    def on_hover_enter(self, event):
        # Quando o mouse entra, altera a imagem para a versão 'hover'
        self.canvas_abre.itemconfig(self.img_id, image=self.image_hipolita_hover)

    def on_hover_leave(self, event):
        # Quando o mouse sai, retorna à imagem original
        self.canvas_abre.itemconfig(self.img_id, image=self.image_hipolita_menu)

    def executar_comando(self):
        print("Comando executado com sucesso!")  # Aqui você coloca a função que deseja chamar  

































    
    def tela_02_velha(self):
        # Criando o Canvas com as dimensões da janela (800x600)
        self.canvas_abre = Canvas(self.root, width=800, height=600, bg="black", bd=0, highlightthickness=0)
        self.canvas_abre.place(x=0, y=0)  # Posição do Canvas na tela
        self.widgets_dinamicos.append(self.canvas_abre)
        
        # Titulo
        self.canvas_abre.create_text(
            400,  # Coordenada X (centralizado na tela)
            20,   # Coordenada Y (acima da imagem)
            text="Ascent To Olympus",  # Texto que será exibido
            fill='#DAA520',  # Cor do texto RGB color: 218/255, 165/255, 32/255, 1
            font=("Gelio Fasolada", 21),  # Fonte e Tamanho
            anchor="center" ) # Alinhamento centralizado
            
        self.canvas_abre.create_text(
            400,  # Coordenada X (centralizado na tela)
            35,   # Coordenada Y (acima da imagem)
            text="The Ancient Greek Game",  # Texto que será exibido
            fill='#FF0000',  # Cor do texto RGB color: 1, 0, 0, 1
            font=("Gelio Greek Diner", 14),  # Fonte e Tamanho
            anchor="center")  # Alinhamento centralizado
        
        self.canvas_abre.create_text(
            400,  # Coordenada X (centralizado na tela)
            65,   # Coordenada Y (acima da imagem)
            text="<><><><><><><><><><><><><><><><><><><><><><><><><><><>",  # Texto que será exibido
            fill='#B8860B',  # Cor do texto RGB color: 184/255, 134/255, 11/255, 1
            font=("Arial", 12),  # Fonte e Tamanho
            anchor="center")  # Alinhamento centralizado  
        
        self.canvas_abre.create_text(
            400,  # Coordenada X (centralizado na tela)
            95,   # Coordenada Y (acima da imagem)
            text="Reach Mount Olympus and receive the Gods' gift!",  # Texto que será exibido
            fill='white',  # Cor do texto RGB color: 1, 0, 0, 1
            font=("Olympus", 16),  # Fonte e Tamanho
            anchor="center")  # Alinhamento centralizado
        
        self.canvas_abre.create_text(
            400,  # Coordenada X (centralizado na tela)
            125,   # Coordenada Y (acima da imagem)
            text="<><><><><><><><><><><><><><><><><><><><><><><><><><><>",  # Texto que será exibido
            fill='#B8860B',  # Cor do texto RGB color: 184/255, 134/255, 11/255, 1
            font=("Arial", 12),  # Fonte e Tamanho
            anchor="center")  # Alinhamento centralizado  
        
        self.canvas_abre.create_text(
            400,  # Coordenada X (centralizado na tela)
            160,   # Coordenada Y (acima da imagem)
            text="Choose a Player",  # Texto que será exibido
            fill='#FF8C00',  # Cor do texto RGB color: 255/255, 140/255, 0/255, 1  # DarkOrange
            font=("Gelio Fasolada", 20),  # Fonte e Tamanho
            anchor="center")  # Alinhamento centralizado
        
        
        # Carregar a imagem circular com fundo transparente
        self.image_hipolita_menu = PhotoImage(file="images/carinha_hipolita_menu.png")  # Caminho da imagem

        # Usar create_image para desenhar a imagem diretamente no Canvas
        self.img_id = self.canvas_abre.create_image(400, 250, image=self.image_hipolita_menu)

        # Associando o evento de clique com o botão
        self.canvas_abre.tag_bind(self.img_id, '<Button-1>', self.on_button_click)
        
        # Associando os eventos de hover e clique com a imagem
        self.canvas_abre.tag_bind(self.img_id, '<Button-1>', self.on_button_click)  # Evento de clique
        self.canvas_abre.tag_bind(self.img_id, '<Enter>', self.on_hover_enter)  # Evento de hover (mouse entra)
        self.canvas_abre.tag_bind(self.img_id, '<Leave>', self.on_hover_leave)  # Evento de hover (mouse sai)

        
        
        
        
        
                # Botão de voltar
        botao_voltar = ctk.CTkButton(
            self.canvas_abre,
            width= 100,
            fg_color='#FF0000',
            hover_color="#FFA500",
            text="Go Back!",
            font= ("Gelio Fasolada", 14),
            command=lambda: self.tela_01()
        )
        botao_voltar.place(x=350, y=550)
        self.widgets_dinamicos.append(botao_voltar)    


        
