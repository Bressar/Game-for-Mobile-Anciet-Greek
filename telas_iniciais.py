# telas_iniciais do jogo
# criado:  18/12/24
# atualizado: 


import ctypes
import tkinter as tk
from tkinter import font
from tkinter import filedialog, messagebox, Label, Tk, Canvas, PhotoImage
import customtkinter as ctk
from customtkinter import CTkImage, CTkFont 
from PIL import Image, ImageDraw, ImageFont, ImageTk

from back_end import Back_End
from tela_jogo import Tela_Jogo


class Telas:
    def __init__(self, root, interface_jogo):
        self.root = root  # Referência à janela principal
        self.interface_jogo = interface_jogo  # Referência à instância de Interface_Jogo

        self.widgets_dinamicos = []  # Lista para armazenar widgets dinâmicos
          
        self.back_end = Back_End()
        self.back_end.load_fonts()

        #self.tela_jogo = Tela_Jogo(root)
        # Passa a referência de Telas para Tela_Jogo
        self.tela_jogo = Tela_Jogo(root, self, interface_jogo)  
        

        
             
    def on_button_click_personagem(self, personagem):
        """Lida com o clique no botão, atualiza a imagem e chama o backend."""
        # Atualiza a imagem para o estado de clique
        image_click = getattr(self, f"image_{personagem.lower()}_click", None)
        img_id = getattr(self, f"img_{personagem.lower()}_id", None)
        if img_id and image_click:
            self.canvas_abre.itemconfig(img_id, image=image_click)

        # Atualiza o personagem no backend
        self.back_end.escolher_personagem(personagem)
        print(f"Personagem {personagem} clicado e selecionado!")
      
        
    def on_button_click_carta(self, carta_num):
        """Lida com o clique na carta, atualiza a imagem e chama o backend."""
        # Seleciona a imagem de clique com base no número da carta
        image_click = getattr(self, f"image_carta_escolha_click{carta_num}", None)  # Usando o número da carta
        img_id = getattr(self, f"img_carta_escolhida_id{carta_num}", None)  # Usando o número da carta
        if img_id and image_click:
            # Atualiza a imagem para o estado de clique da carta
            self.canvas_abre.itemconfig(img_id, image=image_click)
            
        # Chama a função do backend para escolher a carta
        self.back_end.escolher_carta()
        print(f"Carta {carta_num} Escolhida!")



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
            font=("Gelio Fasolada", 45)) # Fonte e tamanho
           
        label_titulo.place(relx=0.5, y=20, anchor="n")
        self.widgets_dinamicos.append(label_titulo)
        
        # SubTitulo    
        label_subtitulo = ctk.CTkLabel(
            self.root,
            text= "The Ancient Greek Game",
            text_color='#FF0000',  # Cor do texto vermelho
            bg_color="black",
            font=("Gelio Greek Diner", 25) )
                   
        label_subtitulo.place(relx=0.5, y=65, anchor="n")
        self.widgets_dinamicos.append(label_subtitulo)
        
        # Linha           
        self.canvas_abre.create_text(
            400,  # Coordenada X (centralizado na tela)
            110,   # Coordenada Y (acima da imagem)
            text="<><><><><><><><><><><><><><><><><><><><>",  # Texto que será exibido
            fill='#B8860B',  # Cor do texto RGB color: 184/255, 134/255, 11/255, 1
            font=("Arial", 12),  # Fonte e Tamanho
            anchor="center")  # Alinhamento centralizado   
                
        self.imagem_abre = "images/abre.jpg"
        
        try:
            imagem_tela_01 = Image.open(self.imagem_abre) # Carrega a imagem com Pillow
            largura_canvas, altura_canvas = 360, 262  # Dimensões da imagem
            imagem_tela_01.thumbnail((largura_canvas, altura_canvas), Image.Resampling.LANCZOS)  # Redimensionamento proporcional
            self.imagem_canvas = ImageTk.PhotoImage(imagem_tela_01)   
            # Adiciona a imagem ao Canvas 
            self.canvas_abre.create_image(220, 120, anchor="nw", image=self.imagem_canvas) # posição da imagem
        except FileNotFoundError:
            print("Erro: Não foi possível carregar a imagem:", self.imagem_abre)  
                    
        self.canvas_abre.create_text(
            400,  # Coordenada X 
            387,   # Coordenada Y 
            text="<><><><><><><><><><><><><><><><><><><><>",  
            fill='#B8860B', 
            font=("Arial", 12), 
            anchor="center")  
        
        texto_abertura =(
"""Embark on a Greek Mythology Adventure!

Roll the dice, collect cards, overcome challenges,and conquer Olympus!
Move across the board by rolling the dice. Win battles by rolling 4 or more.
Use cards to overcome obstacles. Collect up to 3 cards."""
               )
        
        label_texto_abertura = ctk.CTkLabel(
            self.root,
            text=texto_abertura,
            text_color="white",  # Cor do texto
            bg_color="black",  # Cor de fundo
            font=("Cambria", 18)) # Fonte e tamanho      "Olympus" 

        label_texto_abertura.place(relx=0.5, y=405, anchor="n")
        self.widgets_dinamicos.append(label_texto_abertura)
        
        # # linha        
        # self.canvas_abre.create_text(
        #     400,  
        #     530,   
        #     text="<><><><><><><><><><><><><><><><><><><><>", 
        #     fill='#B8860B',  
        #     font=("Arial", 12),  
        #     anchor="center")  
               
        # Botão iniciar
        botao_iniciar = ctk.CTkButton(
            self.canvas_abre,
            width= 100,
            fg_color='#FF0000',
            hover_color="#FFA500", #self.back_end.cores_layout['laranja']  # "#FFA500"
            text="Become a Legend!", 
            font= ("Gelio Fasolada", 21),
            command=lambda: self.tela_02()
        )
        botao_iniciar.place(relx=0.5, y=550, anchor="n")
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
            text="<><><><><><><><><><><><><><><><><><><><><><><>",  
            fill='#B8860B',  # Cor do texto RGB color: 184/255, 134/255, 11/255, 1
            font=("Arial", 12), 
            anchor="center")  
               
        self.canvas_abre.create_text(
            400,  
            100,  
            text="Reach Mount Olympus and receive the Gods' gift!",  
            fill='white',
            font=("Cambria", 15), # Olympus
            anchor="center") 
        
        self.canvas_abre.create_text(
            400,  
            125,  
            text="<><><><><><><><><><><><><><><><><><><><><><><>", 
            fill='#B8860B',  
            font=("Arial", 12), 
            anchor="center")   
        
        self.canvas_abre.create_text(
            400,  
            170,   
            text="Choose a Player", 
            fill='#FF8C00',  # Cor do texto RGB color: 255/255, 140/255, 0/255, 1  # DarkOrange
            font=("Gelio Fasolada", 20),  
            anchor="center") 
                
        # Botões Players        
        
        # Botão Hippolita
        self.image_hipolita_menu = PhotoImage(file="images/carinha_hipolita_menu.png")
        self.image_hipolita_hover = PhotoImage(file="images/carinha_hipolita_hover.png")
        self.image_hipolita_click = PhotoImage(file="images/carinha_hipolita_click.png")

        # Adiciona a imagem inicial ao Canvas
        self.img_hipolita_id = self.canvas_abre.create_image(400, 240, image=self.image_hipolita_menu)
        # Evento de clique
        self.canvas_abre.tag_bind(self.img_hipolita_id, '<Button-1>', lambda event: self.on_button_click_personagem("hippolita"))
        # Evento de hover (mouse entra)
        self.canvas_abre.tag_bind(self.img_hipolita_id, '<Enter>', lambda event: self.canvas_abre.itemconfig(self.img_hipolita_id, image=self.image_hipolita_hover))
        # Evento de hover (mouse sai)
        self.canvas_abre.tag_bind(self.img_hipolita_id, '<Leave>', lambda event: self.canvas_abre.itemconfig(self.img_hipolita_id, image=self.image_hipolita_menu))

        label_botao_hipolita = ctk.CTkLabel(
            self.root,
            text="Hippolita",
            text_color='white',
            bg_color="black",
            font=("Gelio Fasolada", 18)
        )
        label_botao_hipolita.place(relx=0.5, y=290, anchor="n")
        self.widgets_dinamicos.append(label_botao_hipolita)

        # Botão Odysseus
        self.image_odisseu_menu = PhotoImage(file="images/carinha_odisseu_menu.png")
        self.image_odisseu_hover = PhotoImage(file="images/carinha_odisseu_hover.png")
        self.image_odisseu_click = PhotoImage(file="images/carinha_odisseu_click.png")

        self.img_odisseu_id = self.canvas_abre.create_image(280, 240, image=self.image_odisseu_menu)
        self.canvas_abre.tag_bind(self.img_odisseu_id, '<Button-1>', lambda event: self.on_button_click_personagem("odysseus"))
        self.canvas_abre.tag_bind(self.img_odisseu_id, '<Enter>', lambda event: self.canvas_abre.itemconfig(self.img_odisseu_id, image=self.image_odisseu_hover))
        self.canvas_abre.tag_bind(self.img_odisseu_id, '<Leave>', lambda event: self.canvas_abre.itemconfig(self.img_odisseu_id, image=self.image_odisseu_menu))

        label_botao_odisseu = ctk.CTkLabel(
            self.root,
            text="Odysseus",
            text_color='white',
            bg_color="black",
            font=("Gelio Fasolada", 18)
        )
        label_botao_odisseu.place(x=280, y=290, anchor="n")
        self.widgets_dinamicos.append(label_botao_odisseu)

        # Botão Achilles
        self.image_aquiles_menu = PhotoImage(file="images/carinha_aquiles_menu.png")
        self.image_aquiles_hover = PhotoImage(file="images/carinha_aquiles_hover.png")
        self.image_aquiles_click = PhotoImage(file="images/carinha_aquiles_click.png")

        self.img_aquiles_id = self.canvas_abre.create_image(160, 240, image=self.image_aquiles_menu)
        self.canvas_abre.tag_bind(self.img_aquiles_id, '<Button-1>', lambda event: self.on_button_click_personagem("achilles"))
        self.canvas_abre.tag_bind(self.img_aquiles_id, '<Enter>', lambda event: self.canvas_abre.itemconfig(self.img_aquiles_id, image=self.image_aquiles_hover))
        self.canvas_abre.tag_bind(self.img_aquiles_id, '<Leave>', lambda event: self.canvas_abre.itemconfig(self.img_aquiles_id, image=self.image_aquiles_menu))

        label_botao_aquiles = ctk.CTkLabel(
            self.root,
            text="Achilles",
            text_color='white',
            bg_color="black",
            font=("Gelio Fasolada", 18)
        )
        label_botao_aquiles.place(x=160, y=290, anchor="n")
        self.widgets_dinamicos.append(label_botao_aquiles)

        # Botão Atalanta
        self.image_atalanta_menu = PhotoImage(file="images/carinha_atalanta_menu.png")
        self.image_atalanta_hover = PhotoImage(file="images/carinha_atalanta_hover.png")
        self.image_atalanta_click = PhotoImage(file="images/carinha_atalanta_click.png")

        self.img_atalanta_id = self.canvas_abre.create_image(520, 240, image=self.image_atalanta_menu)
        self.canvas_abre.tag_bind(self.img_atalanta_id, '<Button-1>', lambda event: self.on_button_click_personagem("atalanta"))
        self.canvas_abre.tag_bind(self.img_atalanta_id, '<Enter>', lambda event: self.canvas_abre.itemconfig(self.img_atalanta_id, image=self.image_atalanta_hover))
        self.canvas_abre.tag_bind(self.img_atalanta_id, '<Leave>', lambda event: self.canvas_abre.itemconfig(self.img_atalanta_id, image=self.image_atalanta_menu))

        label_botao_atalanta = ctk.CTkLabel(
            self.root,
            text="Atalanta",
            text_color='white',
            bg_color="black",
            font=("Gelio Fasolada", 18)
        )
        label_botao_atalanta.place(x=520, y=290, anchor="n")
        self.widgets_dinamicos.append(label_botao_atalanta)

        # Botão Theseus
        self.image_teseu_menu = PhotoImage(file="images/carinha_teseu_menu.png")
        self.image_teseu_hover = PhotoImage(file="images/carinha_teseu_hover.png")
        self.image_teseu_click = PhotoImage(file="images/carinha_teseu_click.png")

        self.img_teseu_id = self.canvas_abre.create_image(640, 240, image=self.image_teseu_menu)
        self.canvas_abre.tag_bind(self.img_teseu_id, '<Button-1>', lambda event: self.on_button_click_personagem("theseus"))
        self.canvas_abre.tag_bind(self.img_teseu_id, '<Enter>', lambda event: self.canvas_abre.itemconfig(self.img_teseu_id, image=self.image_teseu_hover))
        self.canvas_abre.tag_bind(self.img_teseu_id, '<Leave>', lambda event: self.canvas_abre.itemconfig(self.img_teseu_id, image=self.image_teseu_menu))

        label_botao_teseu = ctk.CTkLabel(
            self.root,
            text="Theseus",
            text_color='white',
            bg_color="black",
            font=("Gelio Fasolada", 18)
        )
        label_botao_teseu.place(x=640, y=290, anchor="n")
        self.widgets_dinamicos.append(label_botao_teseu)
        
                
        # CARTAS       
         # Escolha uma carta
        self.canvas_abre.create_text(
        400,  
        365,   
        text= "Click on a card to draw your starting card", 
        fill='#FF8C00',  # Cor do texto RGB color: 255/255, 140/255, 0/255, 1  # DarkOrange
        font=("Gelio Fasolada", 16),  
        anchor="center") 
        
        # Carta 1
        self.image_carta_escolha_menu1 = PhotoImage(file="images/carta_escolha_menu.png")
        self.image_carta_escolha_hover1 = PhotoImage(file="images/carta_escolha_hover.png")
        self.image_carta_escolha_click1 = PhotoImage(file="images/carta_escolha_click.png")

        self.img_carta_escolhida_id1 = self.canvas_abre.create_image(280, 470, image=self.image_carta_escolha_menu1)
        # Passando o número 1 para identificar a carta 1
        self.canvas_abre.tag_bind(self.img_carta_escolhida_id1, '<Button-1>', lambda event: self.on_button_click_carta(1))  
        self.canvas_abre.tag_bind(self.img_carta_escolhida_id1, '<Enter>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id1 , image=self.image_carta_escolha_hover1))
        self.canvas_abre.tag_bind(self.img_carta_escolhida_id1, '<Leave>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id1 , image=self.image_carta_escolha_menu1))

        # Carta 2
        self.image_carta_escolha_menu2 = PhotoImage(file="images/carta_escolha_menu.png")
        self.image_carta_escolha_hover2 = PhotoImage(file="images/carta_escolha_hover.png")
        self.image_carta_escolha_click2 = PhotoImage(file="images/carta_escolha_click.png")

        self.img_carta_escolhida_id2 = self.canvas_abre.create_image(400, 470, image=self.image_carta_escolha_menu2)
        # Passando o número 2 para identificar a carta 2
        self.canvas_abre.tag_bind(self.img_carta_escolhida_id2, '<Button-1>', lambda event: self.on_button_click_carta(2))  
        self.canvas_abre.tag_bind(self.img_carta_escolhida_id2, '<Enter>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id2 , image=self.image_carta_escolha_hover2))
        self.canvas_abre.tag_bind(self.img_carta_escolhida_id2, '<Leave>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id2 , image=self.image_carta_escolha_menu2))

        # Carta 3
        self.image_carta_escolha_menu3 = PhotoImage(file="images/carta_escolha_menu.png")
        self.image_carta_escolha_hover3 = PhotoImage(file="images/carta_escolha_hover.png")
        self.image_carta_escolha_click3 = PhotoImage(file="images/carta_escolha_click.png")

        self.img_carta_escolhida_id3 = self.canvas_abre.create_image(520, 470, image=self.image_carta_escolha_menu3)
        # Passando o número 3 para identificar a carta 3
        self.canvas_abre.tag_bind(self.img_carta_escolhida_id3, '<Button-1>', lambda event: self.on_button_click_carta(3))  
        self.canvas_abre.tag_bind(self.img_carta_escolhida_id3, '<Enter>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id3 , image=self.image_carta_escolha_hover3))
        self.canvas_abre.tag_bind(self.img_carta_escolhida_id3, '<Leave>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id3 , image=self.image_carta_escolha_menu3))


        # Botão de voltar
        botao_voltar = ctk.CTkButton(
        self.canvas_abre,
        width=50,
        fg_color='black',
        border_width= 1,
        border_color= "white",
        hover_color="black",
        text="<-",
        font=("Gelio Fasolada", 25),
        command=lambda: self.tela_01()
        
        )
        botao_voltar.place(x=20, y=550)
        self.widgets_dinamicos.append(botao_voltar)


    # Botão de avançar
        botao_avancar = ctk.CTkButton(
        self.canvas_abre,
        width=50,
        fg_color='black',
        border_width= 1,
        border_color= "white",
        hover_color="black",
        text="->",
        font=("Gelio Fasolada", 25),
        command=lambda: self.tela_03()
        
        )
        botao_avancar.place(x=730, y=550)
        self.widgets_dinamicos.append(botao_avancar)


    def tela_03(self):
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
            text="<><><><><><><><><><><><><><><><><><><><><><><><><><><><>",  
            fill='#B8860B',  # Cor do texto RGB color: 184/255, 134/255, 11/255, 1
            font=("Arial", 12), 
            anchor="center")  


        # Imagem Carinha
        self.image_carinha_jogador = PhotoImage(file="images/carinha_default.png") # depois trocar pela variável dinâmica
        self.img_carinha = self.canvas_abre.create_image(220, 165, image=self.image_carinha_jogador)
        
        # Titulo nome               
        label_titulo_nome = ctk.CTkLabel(
            self.root,
            text= (f"Your player is: {self.back_end.personagem_escolhido }"), # trocar o nome pela variável de sistema
            text_color='#FF8C00',  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Gelio Fasolada", 22),
            )  # Alinha o texto à esquerda (west))            
        label_titulo_nome.place(x=480, y=100, anchor="n") # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_titulo_nome)
        
        # Titulo texto player
        
        texto_player = (
"""king of Ithaca, outsmarts monsters and gods
on his epic journey home after the Trojan War.
He wants to reach Olympus to attain
the status of a demigod."""
        )

        # Criar o label de descrição do jogador
        label_descricao_player = ctk.CTkLabel(
            self.root,
            text=texto_player,  # Substituir pelo texto dinâmico, se necessário
            text_color="white",  
            fg_color="black",  # Cor de fundo
            font=("Cambria", 17), 
        )
        label_descricao_player.place(x=480, y=130, anchor="n")
        self.widgets_dinamicos.append(label_descricao_player)

     
      # Titulo carta              
        label_titulo_carta = ctk.CTkLabel(
            self.root,
            text= "Your initial card is: ZEUS", # trocar o nome pela variável de sistema
            text_color='#FF8C00',  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Gelio Fasolada", 22),
            anchor="w", ) 
           
        label_titulo_carta.place(x=400, y=240, anchor="n") # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_titulo_carta)
        
        # Titulo texto player        
        texto_carta = "Card abilities: Advance 6 spaces, or roll 2 dice"      
        # trocar pelo caminho variável do personagem   
             # texto about do player selecionado
            # id: player_about
            # text: app.about_player           
        label_descricao_carta = ctk.CTkLabel(
            self.root,
            text= texto_carta, # trocar o nome pela variável de sistema
            text_color='white',  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Cambria", 17) ) 
           
        label_descricao_carta.place(x=400, y=265, anchor="n") # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_descricao_carta)
        
        # Imagem Carta
        self.image_carta_jogador = PhotoImage(file="images/carta_default.png") # depois trocar pela variável dinâmica
        self.img_carta_layout = self.canvas_abre.create_image(400, 400, image=self.image_carta_jogador)
        
       
        # Linha           
        self.canvas_abre.create_text(
            400,  
            520,   
            text="<><><><><><><><><><><><><><><><><><><><><><><><><><><><>",  
            fill='#B8860B',  # Cor do texto RGB color: 184/255, 134/255, 11/255, 1
            font=("Arial", 12), 
            anchor="center")        
 
    
 # Botão de voltar
        botao_voltar = ctk.CTkButton(
        self.canvas_abre,
        width=50,
        fg_color='black',
        border_width= 1,
        border_color= "white",
        hover_color="black",
        text="<-",
        font=("Gelio Fasolada", 25),
        command=lambda: self.tela_02()
        
        )
        botao_voltar.place(x=20, y=550)
        self.widgets_dinamicos.append(botao_voltar)
        
        # Botão de PLAY
        botao_start = ctk.CTkButton(
            self.canvas_abre,
            width=100,
            fg_color='#FF0000',
            hover_color="#FFA500",
            text="START GAME",
            font=("Gelio Fasolada", 20),
            command=lambda: self.tela_jogo.tela_game()
        )
        botao_start.place(x=400, y=550, anchor="n")
        self.widgets_dinamicos.append(botao_start)
        
        
         # Botão de sair
        botao_avancar = ctk.CTkButton(
        self.canvas_abre,
        width=50,
        fg_color='black',
        border_width= 1,
        border_color= "white",
        hover_color="black",
        text="EXIT",
        font=("Gelio Fasolada", 18),
        command=lambda: self.interface_jogo.sair_jogo()# acrescentar função de saída!!!!
        )
        botao_avancar.place(x=730, y=550)
        self.widgets_dinamicos.append(botao_avancar)
 













