# tela onde o jogo se desenrola..import ctypes
import tkinter as tk
from tkinter import font
from tkinter import filedialog, messagebox, Label, Tk, Canvas, PhotoImage
import customtkinter as ctk
from customtkinter import CTkImage, CTkFont 
from PIL import Image, ImageDraw, ImageFont, ImageTk

import os


from back_end import Back_End

class Tela_Jogo:
    def __init__(self, root, telas_iniciais, interface_jogo, back_end):
        self.root = root  # Referência à janela principal
        self.widgets_dinamicos = []  # Lista para armazenar widgets dinâmicos
        self.interface_jogo = interface_jogo  # Referência à instância de Interface_Jogo
        self.telas_iniciais = telas_iniciais   # Referência à instância de Telas    
        self.back_end = back_end  #  Back_End 

        self.back_end.load_fonts()
        self.root.configure(bg="black")

        
        #self.casa_atual = self.back_end.casa_atual # Teste!
        
        # self.cor_Layout = self.back_end.cor_layout_atual # busca a cor do layout do backend  
              
    def atualizar_interface(self):
        """Atualiza a interface gráfica com os dados do Back_End."""
        # Atualiza a cor do layout
        self.cor_Layout = self.back_end.cor_layout_atual
        
         # Atualiza tijolos
        self.image_tijolinho.configure(file=self.back_end.tijolos_cor_atual)
        
        # Atualiza as casas exibidas
        casas_exibidas = self.back_end.exibir_casas(self.back_end.casas)
        for i, casa in enumerate(casas_exibidas):
            # Atualiza as imagens das casas
            getattr(self, f"casa_{i+1}_lista").configure(file=casa["imagem"])
            # Atualiza os textos associados às casas
            getattr(self, f"label_nome_casa_{i+1}").configure(text=casa["texto"], text_color=self.cor_Layout)

        # Exibe para depuração no console
        print("Dados atualizados:")
        print(f"Tijolos: {self.back_end.tijolos_cor_atual}")
        print(f"Casas exibidas: {[casa['texto'] for casa in casas_exibidas]}")
       
        # (Opcional) Imprima os valores atualizados no console para depuração
        print(f"Cor do layout: {self.cor_Layout}")
        print(f"Imagem atual dos tijolos: {self.back_end.tijolos_cor_atual}")
        print(f"Casas exibidas: {casas_exibidas}")
        
        


    def executar_rolagem_e_atualizar(self):
        """Executa as funções do Back_End e atualiza a interface."""
        self.back_end.rolar_dado()  # Rola o dado e avança a posição no tabuleiro
        self.back_end.atualizar_tijolos()  # Garante que os tijolos sejam atualizados
        self.back_end.atualizar_cor_layout()  # Atualiza o layout baseado na casa atual
        self.atualizar_interface()  # Atualiza a interface gráfica com os novos dados

        
        

        

    # def executar(self):
    #     self.root.mainloop()
        
              
        
    def play_gif(self):
       # Atualiza o quadro no Canvas
        self.canvas.itemconfig(self.image_on_canvas, image=self.frames[self.current_frame])
        
        # Avança para o próximo quadro
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        
        # Define um intervalo para o próximo quadro (em milissegundos)
        self.root.after(500, self.play_gif)  # meio frame por segundo
    
    
    
    def tela_game(self):
        self.canvas_abre = Canvas(self.root, width=800, height=600, bg="black", bd=0, highlightthickness=0)
        self.canvas_abre.place(x=0, y=0) 
        self.widgets_dinamicos.append(self.canvas_abre)
        
        
        # Exibe as casas inicialmente
        casas_exibidas = self.back_end.exibir_casas(self.back_end.casas)
        
        #self.back_end.atualizar_cor_layout()
        self.cor_Layout = self.back_end.cor_layout_atual # busca a cor do layout do backend     
        
        # Exibe as casas inicialmente
        self.atualizar_interface()
          
        # Imagem Tijolinho 
        #self.back_end.atualizar_tijolos()# atualiza as cores dos tijolos
        self.image_tijolinho = PhotoImage(file=self.back_end.tijolos_cor_atual) # Variável dinâmica
        self.img_tijolinho = self.canvas_abre.create_image(400, 25, image=self.image_tijolinho)
        

        print(f"Debug classe Tela Jogo: {self.back_end.personagem_escolhido_imagem}") 
        
        # atualizações
        # self.back_end.atualizar_cor_layout()
        # self.back_end.atualizar_tijolos()
        
        
        # Imagem Carinha Tela Jogo
        try:
            print(f"Tentando carregar imagem: {self.back_end.personagem_escolhido_imagem}")       
            imagem_original = Image.open(self.back_end.personagem_escolhido_imagem)
            imagem_redimensionada = imagem_original.resize((125, 125), Image.Resampling.LANCZOS)
            self.image_carinha_jogador = ImageTk.PhotoImage(imagem_redimensionada)       
            self.img_carinha = self.canvas_abre.create_image(80, 160, image=self.image_carinha_jogador)
            print(f"Debug Tela Jogo, imagem selecionada: {self.back_end.personagem_escolhido_imagem}") 
        except Exception as e:
            print(f"Erro ao carregar imagem selecionada: {e}")
            self.image_carinha_jogador = PhotoImage(file="images/carinha_default_menor.png")
            self.img_carinha = self.canvas_abre.create_image(80, 160, image=self.image_carinha_jogador)      
                
  
        
        # Nome do caboclinho              
        label_titulo_nome = ctk.CTkLabel(
            self.root,
            text= self.back_end.personagem_escolhido_nome, # Variável de sistema
            text_color= "white",  
            bg_color="black",  
            font=("Gelio Fasolada", 21),
            )  # Alinha o texto à esquerda (west))            
        label_titulo_nome.place(x=70, y=75, anchor="center") # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_titulo_nome)
                
         # XP            
        label_xp = ctk.CTkLabel(
            self.root,
            text= "XP: 3", # trocar o nome pela variável de sistema
            text_color=self.cor_Layout,  
            bg_color="black",  
            font=("Gelio Fasolada", 18),
            )            
        label_xp.place(x=140, y=60) # relx=0.5, y=10, anchor="n" anchor="center"
        self.widgets_dinamicos.append(label_xp)
                
        # PONTOS            
        label_pontos = ctk.CTkLabel(
            self.root,
            text= "POINTS: 999", # trocar o nome pela variável de sistema
            text_color=self.cor_Layout,  
            bg_color="black",  
            font=("Gelio Fasolada", 18),
            )            
        label_pontos.place(x=190, y=60, ) # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_pontos)
        
        
        # DADO DE ROLAGEM
        # Carrega o GIF com PIL
        self.gif = Image.open("images/dado_grego.gif")
        self.frames = []
        # Extrai os quadros do GIF
        try:
            while True:
                frame = self.gif.copy()
                frame = frame.convert("RGBA")  # Certificar-se de que está em RGBA
                # Adicionar fundo preto onde há transparência
                black_bg = Image.new("RGBA", frame.size, "black")
                frame = Image.alpha_composite(black_bg, frame)
                # Redimensionar o quadro
                frame = frame.resize((80, 80), Image.Resampling.LANCZOS) # reduz a imagem pra 80 X 80

                # Converter para PhotoImage
                self.frames.append(ImageTk.PhotoImage(frame))
                self.gif.seek(len(self.frames))  # Avançar para o próximo quadro
        except EOFError:
            pass  # Final do GIF
        
        # Configuraçºão do Canvas - tamanhao do Dado
        self.canvas = tk.Canvas(self.root, width=80, height=80, bg="black", highlightthickness=0)
        self.canvas.place(x=160, y=110)
        
        # Exibir o primeiro quadro
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor="nw", image=self.frames[0])
        
        # Inicializa o índice do quadro
        self.current_frame = 0
       
        # Exibe a animação
        self.play_gif()
         
        
        # Botão de rolagem de dados
        botao_rolar_dados = ctk.CTkButton(
        self.canvas_abre,
        fg_color='black',
        width= 100,
        border_width= 1,
        border_color= "white",
        hover_color=self.cor_Layout,
        text="Roll a die!",
        font=("Gelio Greek Diner", 18),
        command=self.executar_rolagem_e_atualizar  # Chama o método para rolar o dado e atualizar
        # command=lambda: (
        # self.back_end.rolar_dado(),
        # self.back_end.atualizar_cor_layout(),
        # self.back_end.atualizar_tijolos()
        # )  # As funções são executadas em sequência# chama função rolar dados
        )
        botao_rolar_dados.place(x=150, y=195)
        self.widgets_dinamicos.append(botao_rolar_dados)
                        
        self.canvas_abre.create_text(
            140,  
            240,  
            text="<><><><><><><><><><><><><><>", 
            fill=self.cor_Layout,  # #B8860B' dourado
            font=("Arial", 12), 
            anchor="center")  

        
        # CARTAS           
        label_cartas = ctk.CTkLabel(
            self.root,
            text= "Your Cards:", # trocar o nome pela variável de sistema
            text_color="white",  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Gelio Fasolada", 16),
            )            
        #label_cartas.place(x=140, y=240, anchor="center") # relx=0.5, y=10, anchor="n"
        label_cartas.place(x=10, y=265) # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_cartas)
                 
        # cartas pequenas
         # Carta 1
        self.image_carta_menu1 = PhotoImage(file=self.back_end.cartas_player[0]["imagem_pequena"]) 
        self.img_carta_id1 = self.canvas_abre.create_image(50, 355, image=self.image_carta_menu1)
        # Carta 2
        self.image_carta_menu2 = PhotoImage(file=self.back_end.cartas_player[1]["imagem_pequena"])
        self.img_carta_id2 = self.canvas_abre.create_image(140, 355, image=self.image_carta_menu2)
        # Carta 3
        self.image_carta_menu3 = PhotoImage(file=self.back_end.cartas_player[2]["imagem_pequena"])
        self.img_carta_id3 = self.canvas_abre.create_image(230, 355, image=self.image_carta_menu3)
  


        # Chama a função exibir_casas do back_end para obter os 8 itens da lista de casas 
        casas_exibidas = self.back_end.exibir_casas(self.back_end.casas)
        
        print(f'Lista de casas que a função retorna  {casas_exibidas}') # for debug
        
         # Imagem casa 1
        self.casa_1_lista = PhotoImage(file= casas_exibidas[0]["imagem"])  # depois trocar pela variável dinâmica
        self.img_casa_1_lista = self.canvas_abre.create_image(50, 520, image=self.casa_1_lista)
       
         # Imagem casa 2
        self.casa_2_lista = PhotoImage(file=casas_exibidas[1]["imagem"])  # depois trocar pela variável dinâmica
        self.img_casa_2_lista = self.canvas_abre.create_image(150, 520, image=self.casa_2_lista)

        # Imagem casa 3
        self.casa_3_lista = PhotoImage(file=casas_exibidas[2]["imagem"])  # depois trocar pela variável dinâmica
        self.img_casa_3_lista = self.canvas_abre.create_image(250, 520, image=self.casa_3_lista)
        
        # Imagem casa 4
        self.casa_4_lista = PhotoImage(file=casas_exibidas[3]["imagem"])  # depois trocar pela variável dinâmica
        self.img_casa_4_lista = self.canvas_abre.create_image(350, 520, image=self.casa_4_lista)

        # Imagem casa 5
        self.casa_5_lista = PhotoImage(file=casas_exibidas[4]["imagem"])  # depois trocar pela variável dinâmica
        self.img_casa_5_lista = self.canvas_abre.create_image(450, 520, image=self.casa_5_lista)

        # Imagem casa 6
        self.casa_6_lista = PhotoImage(file=casas_exibidas[5]["imagem"])  # depois trocar pela variável dinâmica
        self.img_casa_6_lista = self.canvas_abre.create_image(550, 520, image=self.casa_6_lista)

        # Imagem casa 7
        self.casa_7_lista = PhotoImage(file=casas_exibidas[6]["imagem"])  # depois trocar pela variável dinâmica
        self.img_casa_7_lista = self.canvas_abre.create_image(650, 520, image=self.casa_7_lista)
        
         # Imagem casa 8
        self.casa_8_lista = PhotoImage(file=casas_exibidas[7]["imagem"])  # depois trocar pela variável dinâmica
        self.img_casa_8_lista = self.canvas_abre.create_image(750, 520, image=self.casa_8_lista)


        # Lista de posições fixas no layout para as casas
        posicoes_x = [50, 150, 250, 350, 450, 550, 650, 750]  # As posições X para as 8 casas
        posicoes_y = 520  # Todas as casas têm a mesma posição Y fixada

        # Exibe cada uma das casas
        for i, casa in enumerate(casas_exibidas):
            # Cria o texto associado à casa, que pode ser o texto da casa ou outro
            label_nome_casa = ctk.CTkLabel(
                self.root,
                text=casa["texto"],  # Usando o texto da casa, que vem do dicionário
                text_color=self.cor_Layout,  # Cor do texto, ajuste conforme necessário
                bg_color="black",  
                font=("Gelio Fasolada", 17),
            )
            label_nome_casa.place(x=posicoes_x[i], y=posicoes_y + 65, anchor="center")  # Posição fixa para o texto

            # Armazenando os widgets (imagem e label) para manipulação futura
            # self.widgets_dinamicos.append(img_casa)
            self.widgets_dinamicos.append(label_nome_casa)

        # Exibe para debug as casas que foram exibidas
        for casa in casas_exibidas:
            print(f"Casa {casa['numero']}: {casa['texto']} - {casa['imagem']}")
            
            
            
        # # Chama a função exibir_casas do back_end para obter os 8 itens da lista de casas
        # casas_exibidas = self.back_end.exibir_casas()

        # # A posição inicial das casas será dada por self.casa_atual, e será calculada dinamicamente
        # x_position = 50 + ((self.back_end.casa_atual - 1) * 100)  # Baseando a posição X na casa_atual
        

        # # Exibe cada uma das casas
        # for casa in casas_exibidas:
        #     imagem_casa = PhotoImage(file=casa["imagem"])  # A imagem é carregada dinamicamente
            
        #     # Cria a imagem no canvas
        #     img_casa = self.canvas_abre.create_image(x_position, 520, image=imagem_casa)
            
        #     # Cria o texto associado à casa
        #     label_nome_casa = ctk.CTkLabel(
        #         self.root,
        #         text=casa["texto"],  # Usando o texto da casa
        #         text_color=self.cor_Layout,  # Cor do texto, ajuste conforme necessário
        #         bg_color="black",  
        #         font=("Gelio Fasolada", 17),
        #     )
        #     label_nome_casa.place(x=x_position, y=582, anchor="center")  # A posição das labels é ajustada dinamicamente

        #     # Armazenando os widgets (imagem e label) para manipulação futura
        #     self.widgets_dinamicos.append(img_casa)
        #     self.widgets_dinamicos.append(label_nome_casa)

        #     # Atualiza a posição para a próxima casa
        #     x_position += 100  # Distância de 100px entre as casas (ajuste conforme necessário)
        
        # # Exibe para debug as casas que foram exibidas
        # for casa in casas_exibidas:
        #     print(f"Casa {casa['numero']}: {casa['texto']} - {casa['imagem']}")

           
           

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Botão de sair
        botao_sair = ctk.CTkButton(
        self.canvas_abre,
        width=40,
        height=20,
        fg_color='black',
        border_width= 1,
        text_color= self.cor_Layout,
        border_color= self.cor_Layout,
        hover_color="white",
        text="EXIT",
        font=("Gelio Fasolada", 14),
        command=lambda: self.interface_jogo.sair_jogo()
        )
        botao_sair.place(x=750, y=60)
        self.widgets_dinamicos.append(botao_sair)
        
        
        # Linhas
        self.canvas_abre.create_text(
            550,  
            100,  
            text="<><><><><><><><><><><><><><><><><><><><><><><><>", 
            fill=self.cor_Layout,  # #B8860B' dourado
            font=("Arial", 12), 
            anchor="center")  

 
        self.canvas_abre.create_text(
            550,  
            435,  
            text="<><><><><><><><><><><><><><><><><><><><><><><><>", 
            fill=self.cor_Layout, 
            font=("Arial", 12), 
            anchor="center")  
        
        self.canvas_abre.create_text(
            140,  
            435,  
            text="<><><><><><><><><><><><><><>", 
            fill=self.cor_Layout,  # #B8860B' dourado
            font=("Arial", 12), 
            anchor="center")  
        
        
        # testando a função das cartas
        self.quadro_de_acao_carta()
       
        # teste de evento de casa 
        #self.quadro_de_acao_evento()
        
     
    def quadro_de_acao_evento(self):       
    # label do nome da casa exibida
        label_nome_casa_evento = ctk.CTkLabel(
            self.root,
            text= "Sphinx",  # Substituir pelo texto dinâmico, 
            text_color="white",  
            fg_color="black",  # Cor de fundo
            font=("Olympus", 28), 
        )
        label_nome_casa_evento.place(x=550, y=130, anchor ="center")
        self.widgets_dinamicos.append(label_nome_casa_evento)
               
        self.image_evento_exibido = PhotoImage(file="images/casa_evento_layout.png")
        # self.image_carta_escolha_hover1 = PhotoImage(file="images/carta_escolha_hover.png")
        # self.image_carta_escolha_click1 = PhotoImage(file="images/carta_escolha_click.png")
        self.img_evento_exibido= self.canvas_abre.create_image(550, 235, image=self.image_evento_exibido)
        
        texto_evento = (
"""She asked you a question.
Solve the riddle and roll a die.
If you get 3 or more, move forward 2 spaces.
If you get 2 or less, move back 2 spaces."""
        )
        # label de descrição do evento
        label_descricao_evento = ctk.CTkLabel(
            self.root,
            text=texto_evento,  # Substituir pelo texto dinâmico, se necessário
            text_color="white",  
            fg_color="black",  # Cor de fundo
            font=("Cambria", 17), # "Gelio Fasolada"
        )
        label_descricao_evento.place(x=550, y=380, anchor ="center")
        self.widgets_dinamicos.append(label_descricao_evento)
        

    def quadro_de_acao_carta(self):
        # Carta 
        self.image_carta_exibida = PhotoImage(file="images/carta_aphrodite_layout.png")
        # self.image_carta_escolha_hover1 = PhotoImage(file="images/carta_escolha_hover.png")
        # self.image_carta_escolha_click1 = PhotoImage(file="images/carta_escolha_click.png")

        self.img_carta_exibida = self.canvas_abre.create_image(440, 265, image=self.image_carta_exibida)
        
        
        texto_descricao_carta = """The Aphrodite card has
the power to move 
forward 6 spaces.

If you don´t keep
the card, move forward
3 spaces"""
        # label do nome da casa exibida
        label_descricao_carta_exibida = ctk.CTkLabel(
            self.root,
            text= texto_descricao_carta,  # Substituir pelo texto dinâmico, 
            text_color="white",  
            fg_color="black",  # Cor de fundo
            font=("Cambria", 17), 
        )
        label_descricao_carta_exibida.place(x=650, y=220, anchor ="center")
        self.widgets_dinamicos.append(label_descricao_carta_exibida)
        
        label_guardar_carta_exibida = ctk.CTkLabel(
            self.root,
            text= "Do you keep the card?",  # Substituir pelo texto dinâmico, 
            text_color=self.cor_Layout,  
            fg_color="black",  # Cor de fundo
            font=("Cambria Bold", 17), # Gelio Fasolada
        )
        label_guardar_carta_exibida.place(x=650, y=340, anchor ="center")
        self.widgets_dinamicos.append(label_guardar_carta_exibida)
               
        # Botão SIM
        botao_sim = ctk.CTkButton(
        self.canvas_abre,
        fg_color='black',
        width= 16,
        border_color= "white",
        border_width= 1,
        hover_color=self.cor_Layout,
        text="yes",
        font=("Gelio Greek Diner", 18),
        command=lambda: self.telas_iniciais.tela_03() # acrescentar função de saída!!!!
        )
        botao_sim.place(x=600, y=380, anchor="center")
        self.widgets_dinamicos.append(botao_sim)
        
        # Botão NÃO
        botao_naum = ctk.CTkButton(
        self.canvas_abre,
        fg_color='black',
        width= 16,
        border_color= "white",
        border_width= 1,
        hover_color="red",
        text="no",
        font=("Gelio Greek Diner", 18),
        command=lambda: self.telas_iniciais.tela_03() # acrescentar função de saída!!!!
        )
        botao_naum.place(x=700, y=380, anchor="center")
        self.widgets_dinamicos.append(botao_naum)
