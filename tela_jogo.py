# tela onde o jogo se desenrola..import ctypes
import tkinter as tk
from tkinter import font
from tkinter import filedialog, messagebox, Label, Tk, Canvas, PhotoImage
import customtkinter as ctk
from customtkinter import CTkImage, CTkFont 
from PIL import Image, ImageDraw, ImageFont, ImageTk

from back_end import Back_End

class Tela_Jogo:
    def __init__(self, root, telas_iniciais):
        self.root = root  # Referência à janela principal
        self.widgets_dinamicos = []  # Lista para armazenar widgets dinâmicos
          
        self.back_end = Back_End()
        self.back_end.load_fonts()
        
        # Referência à instância de Telas
        self.telas_iniciais = telas_iniciais  
        
    
    
    def tela_game(self):
        self.canvas_abre = Canvas(self.root, width=800, height=600, bg="black", bd=0, highlightthickness=0)
        self.canvas_abre.place(x=0, y=0) 
        self.widgets_dinamicos.append(self.canvas_abre)
        
        
        # Imagem Tijolinho 
        self.image_tijolinho = PhotoImage(file="images/tijolos_azuis.png") # depois trocar pela variável dinâmica
        self.img_tijolinho = self.canvas_abre.create_image(400, 25, image=self.image_tijolinho)
        
         
        
        # Imagem Carinha
        self.image_carinha_jogador = PhotoImage(file="images/carinha_default_menor.png") # depois trocar pela variável dinâmica
        self.img_carinha = self.canvas_abre.create_image(70, 150, image=self.image_carinha_jogador) 
        
        # Nome do caboclinho              
        label_titulo_nome = ctk.CTkLabel(
            self.root,
            text= "hippolyta", # trocar o nome pela variável de sistema
            text_color='white',  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Gelio Fasolada", 21),
            )  # Alinha o texto à esquerda (west))            
        label_titulo_nome.place(x=70, y=75, anchor="center") # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_titulo_nome)
        
        
         # XP            
        label_xp = ctk.CTkLabel(
            self.root,
            text= "XP: 3", # trocar o nome pela variável de sistema
            text_color='white',  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Gelio Fasolada", 18),
            )            
        label_xp.place(x=140, y=60) # relx=0.5, y=10, anchor="n" anchor="center"
        self.widgets_dinamicos.append(label_xp)
        
        
        # PONTOS            
        label_pontos = ctk.CTkLabel(
            self.root,
            text= "POINTS: 999", # trocar o nome pela variável de sistema
            text_color='white',  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Gelio Fasolada", 18),
            )            
        label_pontos.place(x=190, y=60, ) # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_pontos)
        
        

         
         
        
        # Botão de rolagem de dados
        botao_rolar_dados = ctk.CTkButton(
        self.canvas_abre,
        fg_color='black',
        width= 120,
        border_width= 1,
        border_color= "white",
        hover_color="black",
        text="Roll a die!",
        font=("Gelio Greek Diner", 20),
        command=lambda: self.telas_iniciais.tela_03() # acrescentar função de saída!!!!
        )
        botao_rolar_dados.place(x=140, y=210)
        self.widgets_dinamicos.append(botao_rolar_dados)
        
        
        
        
        # CARTAS           
        label_cartas = ctk.CTkLabel(
            self.root,
            text= "Use your Cards:", # trocar o nome pela variável de sistema
            text_color='white',  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Gelio Fasolada", 16),
            )            
        #label_cartas.place(x=140, y=240, anchor="center") # relx=0.5, y=10, anchor="n"
        label_cartas.place(x=10, y=250) # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_cartas)
                 
        # cartas
         # Carta 1
        self.image_carta_menu1 = PhotoImage(file="images/carta_menu.png")
        # self.image_carta_escolha_hover1 = PhotoImage(file="images/carta_escolha_hover.png")
        # self.image_carta_escolha_click1 = PhotoImage(file="images/carta_escolha_click.png")

        self.img_carta_id1 = self.canvas_abre.create_image(50, 340, image=self.image_carta_menu1)
        # Passando o número 1 para identificar a carta 1
        # self.canvas_abre.tag_bind(self.img_carta_escolhida_id1, '<Button-1>', lambda event: self.on_button_click_carta(1))  
        # self.canvas_abre.tag_bind(self.img_carta_escolhida_id1, '<Enter>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id1 , image=self.image_carta_escolha_hover1))
        # self.canvas_abre.tag_bind(self.img_carta_escolhida_id1, '<Leave>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id1 , image=self.image_carta_escolha_menu1))

        # Carta 2
        self.image_carta_menu2 = PhotoImage(file="images/carta_menu.png")
        # self.image_carta_escolha_hover2 = PhotoImage(file="images/carta_escolha_hover.png")
        # self.image_carta_escolha_click2 = PhotoImage(file="images/carta_escolha_click.png")

        self.img_carta_id2 = self.canvas_abre.create_image(140, 340, image=self.image_carta_menu2)
        # Passando o número 2 para identificar a carta 2
        # self.canvas_abre.tag_bind(self.img_carta_escolhida_id2, '<Button-1>', lambda event: self.on_button_click_carta(2))  
        # self.canvas_abre.tag_bind(self.img_carta_escolhida_id2, '<Enter>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id2 , image=self.image_carta_escolha_hover2))
        # self.canvas_abre.tag_bind(self.img_carta_escolhida_id2, '<Leave>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id2 , image=self.image_carta_escolha_menu2))

        # Carta 3
        self.image_carta_menu3 = PhotoImage(file="images/carta_menu.png")
        # self.image_carta_escolha_hover3 = PhotoImage(file="images/carta_escolha_hover.png")
        # self.image_carta_escolha_click3 = PhotoImage(file="images/carta_escolha_click.png")

        self.img_carta_id3 = self.canvas_abre.create_image(230, 340, image=self.image_carta_menu3)
        # # Passando o número 3 para identificar a carta 3
        # self.canvas_abre.tag_bind(self.img_carta_escolhida_id3, '<Button-1>', lambda event: self.on_button_click_carta(3))  
        # self.canvas_abre.tag_bind(self.img_carta_escolhida_id3, '<Enter>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id3 , image=self.image_carta_escolha_hover3))
        # self.canvas_abre.tag_bind(self.img_carta_escolhida_id3, '<Leave>', lambda event: self.canvas_abre.itemconfig(self.img_carta_escolhida_id3 , image=self.image_carta_escolha_menu3))
        
        
        
         
         
         
                
        # Imagem casa 1
        self.casa_1_lista = PhotoImage(file="images/casa_teste.png")  # depois trocar pela variável dinâmica
        self.img_casa_1_lista = self.canvas_abre.create_image(50, 520, image=self.casa_1_lista)

        # Imagem casa 2
        self.casa_2_lista = PhotoImage(file="images/casa_teste.png")  # depois trocar pela variável dinâmica
        self.img_casa_2_lista = self.canvas_abre.create_image(150, 520, image=self.casa_2_lista)


        # Imagem casa 3
        self.casa_3_lista = PhotoImage(file="images/casa_teste.png")  # depois trocar pela variável dinâmica
        self.img_casa_3_lista = self.canvas_abre.create_image(250, 520, image=self.casa_3_lista)
        
        label_voce_aqui_3 = ctk.CTkLabel(
            self.root,
            text= "You are here!", # trocar o nome pela variável de sistema
            text_color='white',  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Gelio Fasolada", 14),
            )            
        label_voce_aqui_3.place(x=250, y=458, anchor="center") # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_voce_aqui_3)
        
        
        label_nome_casa_3 = ctk.CTkLabel(
            self.root,
            text= "Harpies", # trocar o nome pela variável de sistema
            text_color='white',  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Gelio Fasolada", 17),
            )            
        label_nome_casa_3.place(x=250, y=582, anchor="center") # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_nome_casa_3)



        # Imagem casa 4
        self.casa_4_lista = PhotoImage(file="images/casa_teste.png")  # depois trocar pela variável dinâmica
        self.img_casa_4_lista = self.canvas_abre.create_image(350, 520, image=self.casa_4_lista)

        # Imagem casa 5
        self.casa_5_lista = PhotoImage(file="images/casa_teste.png")  # depois trocar pela variável dinâmica
        self.img_casa_5_lista = self.canvas_abre.create_image(450, 520, image=self.casa_5_lista)

        # Imagem casa 6
        self.casa_6_lista = PhotoImage(file="images/casa_teste.png")  # depois trocar pela variável dinâmica
        self.img_casa_6_lista = self.canvas_abre.create_image(550, 520, image=self.casa_6_lista)

        # Imagem casa 7
        self.casa_7_lista = PhotoImage(file="images/casa_teste.png")  # depois trocar pela variável dinâmica
        self.img_casa_7_lista = self.canvas_abre.create_image(650, 520, image=self.casa_7_lista)

        # Imagem casa 8
        self.casa_8_lista = PhotoImage(file="images/casa_teste.png")  # depois trocar pela variável dinâmica
        self.img_casa_8_lista = self.canvas_abre.create_image(750, 520, image=self.casa_8_lista)

        
        
        # Botão de sair
        botao_sair = ctk.CTkButton(
        self.canvas_abre,
        width=50,
        fg_color='black',
        border_width= 1,
        border_color= "white",
        hover_color="black",
        text="EXIT",
        font=("Gelio Fasolada", 18),
        command=lambda: self.telas_iniciais.tela_03() # acrescentar função de saída!!!!
        )
        #botao_sair.place(x=350, y=560)
        self.widgets_dinamicos.append(botao_sair)
        
        
        
        