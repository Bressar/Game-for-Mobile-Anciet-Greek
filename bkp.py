# tela onde o jogo se desenrola..
#  criado:  20/12/24
# atualizado: 21/12/24
# 

import tkinter as tk
from tkinter import font
from tkinter import filedialog, messagebox, Label, Tk, Canvas, PhotoImage
import customtkinter as ctk
from customtkinter import CTkImage, CTkFont 
from PIL import Image, ImageDraw, ImageFont, ImageTk
import random
from back_end import Back_End


class Tela_Jogo:
    def __init__(self, root, telas_iniciais, interface_jogo, back_end):
        self.root = root  # Referência à janela principal
        self.widgets_dinamicos = []  # Lista para armazenar widgets dinâmicos
        self.interface_jogo = interface_jogo  # Referência à instância de Interface_Jogo
        self.telas_iniciais = telas_iniciais   # Referência à instância de Telas    
        self.back_end = back_end  #  Back_End 
        self.back_end.load_fonts()
        # self.cor_Layout = self.back_end.cor_layout_atual # busca a cor do layout do backend        
        self.root.configure(bg="black")
        self.cor_Layout = self.back_end.cor_layout_atual # busca a cor do layout do 
        
    def atualizar_cor(self, nova_cor):
        self.cor_Layout = nova_cor
        self.atualizar_tela()
        #self.atualizar_interface()   
   
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
        # self.atualizar_cor_layout()
        # self.cor_Layout = self.back_end.cor_layout_atual # busca a cor do layout do backend     
                   
        # Imagem Tijolinho 
        self.atualizar_tijolos()# atualiza as cores dos tijolos
        self.image_tijolinho = PhotoImage(file=self.back_end.tijolos_cor_atual) # Variável dinâmica
        self.img_tijolinho = self.canvas_abre.create_image(400, 25, image=self.image_tijolinho)
       
        print(f"Debug classe Tela Jogo: {self.back_end.personagem_escolhido_imagem}") 
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
        self.label_titulo_nome = ctk.CTkLabel(
            self.root,
            text= self.back_end.personagem_escolhido_nome, # Variável de sistema
            text_color= "white",  
            bg_color="black",  
            font=("Gelio Fasolada", 21),
            )  # Alinha o texto à esquerda (west))            
        self.label_titulo_nome.place(x=70, y=75, anchor="center") # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(self.label_titulo_nome)
                
         # XP            
        self.label_xp = ctk.CTkLabel(
            self.root,
            text= f"XP: {str(self.back_end.player_xp)}", # self.back_end.player_xp Variável de sistema
            text_color=self.cor_Layout,  
            bg_color="black",  
            font=("Gelio Fasolada", 18),
            )            
        self.label_xp.place(x=140, y=60) # relx=0.5, y=10, anchor="n" anchor="center"
        self.widgets_dinamicos.append(self.label_xp)
                
        # PONTOS            
        self.label_pontos = ctk.CTkLabel(
            self.root,
            text= f"POINTS: {self.back_end.player_pontos}", # Variável de sistema
            text_color=self.cor_Layout,  
            bg_color="black",  
            font=("Gelio Fasolada", 18),
            )            
        self.label_pontos.place(x=190, y=60, ) # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(self.label_pontos)
        
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
        hover_color='red',
        text="Roll a die!",
        font=("Gelio Greek Diner", 18),
        command=lambda: (self.rolar_dado(), self.atualizar_tela()) # ROLAR DADO!!!
        )
        botao_rolar_dados.place(x=150, y=195)
        self.widgets_dinamicos.append(botao_rolar_dados)
         
         #linha               
        self.canvas_abre.create_text(
            140,  
            240,  
            text="<><><><><><><><><><><><><><>", 
            fill='gray', 
            font=("Arial", 12), 
            anchor="center")  
        
        # CARTAS           
        self.label_cartas = ctk.CTkLabel(
            self.root,
            text= "Your Cards:", # trocar o nome pela variável de sistema
            text_color="white",  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Gelio Fasolada", 16),
            )            
        #label_cartas.place(x=140, y=240, anchor="center") # relx=0.5, y=10, anchor="n"
        self.label_cartas.place(x=10, y=265) # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(self.label_cartas)
                 
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
        self.casas_exibidas = self.exibir_casas(self.back_end.casas)        
        print(f'Lista de casas que a função retorna  {self.casas_exibidas}') # for debug
        
         # Imagem casa 1
        self.casa_1_lista = PhotoImage(file= self.casas_exibidas[0]["imagem"]) 
        self.img_casa_1_lista = self.canvas_abre.create_image(50, 520, image=self.casa_1_lista)       
         # Imagem casa 2
        self.casa_2_lista = PhotoImage(file=self.casas_exibidas[1]["imagem"])  
        self.img_casa_2_lista = self.canvas_abre.create_image(150, 520, image=self.casa_2_lista)
        # Imagem casa 3
        self.casa_3_lista = PhotoImage(file=self.casas_exibidas[2]["imagem"]) 
        self.img_casa_3_lista = self.canvas_abre.create_image(250, 520, image=self.casa_3_lista)       
        # Imagem casa 4
        self.casa_4_lista = PhotoImage(file=self.casas_exibidas[3]["imagem"])  
        self.img_casa_4_lista = self.canvas_abre.create_image(350, 520, image=self.casa_4_lista)
        # Imagem casa 5
        self.casa_5_lista = PhotoImage(file=self.casas_exibidas[4]["imagem"]) 
        self.img_casa_5_lista = self.canvas_abre.create_image(450, 520, image=self.casa_5_lista)
        # Imagem casa 6
        self.casa_6_lista = PhotoImage(file=self.casas_exibidas[5]["imagem"])  
        self.img_casa_6_lista = self.canvas_abre.create_image(550, 520, image=self.casa_6_lista)
        # Imagem casa 7
        self.casa_7_lista = PhotoImage(file=self.casas_exibidas[6]["imagem"])  
        self.img_casa_7_lista = self.canvas_abre.create_image(650, 520, image=self.casa_7_lista)      
        # Imagem casa 8
        self.casa_8_lista = PhotoImage(file=self.casas_exibidas[7]["imagem"])  
        self.img_casa_8_lista = self.canvas_abre.create_image(750, 520, image=self.casa_8_lista)

        # Lista de posições fixas no layout para as casas
        posicoes_x = [50, 150, 250, 350, 450, 550, 650, 750]  # As posições X para as 8 casas
        posicoes_y = 520  # Todas as casas têm a mesma posição Y fixada

        # Exibe cada uma das casas
        for i, casa in enumerate(self.casas_exibidas):
            # Cria o texto associado à casa, que pode ser o texto da casa ou outro
            label_nome_casa = ctk.CTkLabel(
                self.root,
                text=casa["texto"],  # Usando o texto da casa, que vem do dicionário
                text_color=self.cor_Layout,  # Cor do texto layout
                bg_color="black",  
                font=("Gelio Fasolada", 17),
            )
            label_nome_casa.place(x=posicoes_x[i], y=posicoes_y + 65, anchor="center")  # Posição fixa para o texto
            # Armazenando os widgets (imagem e label) para manipulação futura
            # self.widgets_dinamicos.append(img_casa)
            self.widgets_dinamicos.append(label_nome_casa)
        # Exibe para debug as casas que foram exibidas
        for casa in self.casas_exibidas:
            print(f"Casa {casa['numero']}: {casa['texto']} - {casa['imagem']}")
            

        # Botão de sair
        botao_sair = ctk.CTkButton(
        self.canvas_abre,
        width=40,
        height=20,
        fg_color='black',
        border_width= 1,
        text_color= self.cor_Layout,
        border_color= self.cor_Layout,
        hover_color="red",
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
            fill='gray',  # #B8860B' dourado
            font=("Arial", 12), 
            anchor="center")  

        self.canvas_abre.create_text(
            550,  
            435,  
            text="<><><><><><><><><><><><><><><><><><><><><><><><>", 
            fill='gray', # self.cor_Layout
            font=("Arial", 12), 
            anchor="center")  
        
        self.canvas_abre.create_text(
            140,  
            435,  
            text="<><><><><><><><><><><><><><>", 
            fill='gray',  # #B8860B' dourado
            font=("Arial", 12), 
            anchor="center")  
                
        # testando a função das cartas
       # self.quadro_de_acao_carta()      
        # teste de evento de casa 
        self.quadro_de_acao_evento()
        
  
    def exibir_casas(self, lista_maior):
        # O número sorteado define de onde os 8 itens devem começar
        # Vamos garantir que o número esteja entre 1 e 120
        if self.back_end.casa_atual < 1 or self.back_end.casa_atual> 120:
            raise ValueError("O número deve estar entre 1 e 120.")
        
        # Calcular o índice de início para a exibição de 8 itens
        inicio = self.back_end.casa_atual - 1  # O índice começa de 0, então subtrai 1
        
        # Garantir que o início não ultrapasse o limite de 120 elementos
        fim = inicio + 8
        
        # Se o fim ultrapassar 120, ajustamos para pegar até o fim da lista
        if fim > len(lista_maior):
            fim = len(lista_maior)
            
         # Calcular o início para garantir que sempre mostremos 8 elementos (se possível)
        if fim - inicio < 8:  # Se o número de elementos a ser exibido for menor que 8
            inicio = max(fim - 8, 0)  # Ajusta o início para que tenha 8 itens (ou menos no final)
        
        
        # Pega os 8 itens ou até o fim da lista
        lista_exibida = lista_maior[inicio:fim]
        
        # Retorna os 8 itens para serem exibidos
        return lista_exibida
    
       
    def atualizar_tijolos(self):
        if self.back_end.casa_atual <= 16:
            self.back_end.tijolos_cor_atual = self.back_end.tijolos_cor["azul"]
        elif self.back_end.casa_atual <= 32:
            self.back_end.tijolos_cor_atual = self.back_end.tijolos_cor["verde"]
        elif self.back_end.casa_atual <= 48:
            self.back_end.tijolos_cor_atual = self.back_end.tijolos_cor["amarelo"]
        elif self.back_end.casa_atual <= 64:
            self.back_end.tijolos_cor_atual = self.back_end.tijolos_cor["laranja"]
        elif self.back_end.casa_atual <= 80:
            self.back_end.tijolos_cor_atual = self.back_end.tijolos_cor["vermelho"]
        elif self.back_end.casa_atual <= 96:
            self.back_end.tijolos_cor_atual = self.back_end.tijolos_cor["rosa"]
        elif self.back_end.casa_atual <= 112:
            self.back_end.tijolos_cor_atual = self.back_end.tijolos_cor["roxo"]
        elif self.back_end.casa_atual <= 120:
            self.back_end.tijolos_cor_atual = self.back_end.tijolos_cor["agua"]

                    
    def atualizar_cor_layout(self):
        if self.back_end.casa_atual <= 16:
            self.back_end.cor_layout_atual = self.back_end.cores_layout["azul"]
        elif self.back_end.casa_atual <= 32:
            self.back_end.cor_layout_atual = self.back_end.cores_layout["verde"]
        elif self.back_end.casa_atual <= 48:
            self.back_end.cor_layout_atual = self.back_end.cores_layout["amarelo"]
        elif self.back_end.casa_atual <= 64:
            self.back_end.cor_layout_atual = self.back_end.cores_layout["laranja"]
        elif self.back_end.casa_atual <= 80:
            self.back_end.cor_layout_atual = self.back_end.cores_layout["vermelho"]
        elif self.back_end.casa_atual <= 96:
            self.back_end.cor_layout_atual = self.back_end.cores_layout["rosa"]
        elif self.back_end.casa_atual <= 112:
            self.back_end.cor_layout_atual = self.back_end.cores_layout["roxo"]
        elif self.back_end.casa_atual <= 120:
            self.back_end.cor_layout_atual = self.back_end.cores_layout["agua"]
            
          # Atualiza a variável de instância para o uso em outros widgets
        self.cor_Layout = self.back_end.cor_layout_atual
        #self.atualizar_layout_widgets()  # Atualiza os widgets com a nova cor



    def rolar_dado(self):
            # Sorteia um número entre 1 e 6
            numero_sorteado = random.randint(1, 6)
            print(f'Número sorteado: {numero_sorteado}')
            # Atualiza os pontos           
            self.back_end.player_pontos +=  (15 * numero_sorteado)
            print(f'Pontos do jogador: {self.back_end.player_pontos}')           
            print(f'Casas do tabuleiro no momento:{self.casas_exibidas}')   
            # Atualiza a posição do jogador
            self.back_end.casa_atual += numero_sorteado            
            print(f'Casa atual: {self.back_end.casa_atual}')

            
            
            
            #self.cor_Layout = self.back_end.cor_layout_atual # busca a cor do layout do backend  
            
    
            
            #self.exibir_casas(self.back_end.casas)

            
            #Atualiza o texto do label com os novos pontos
            #self.label_pontos.configure(text=f"POINTS: {self.player_pontos}")


    def atualizar_tela(self):
        """Atualiza os widgets e elementos gráficos baseados nas variáveis do backend."""  
        
        # Atualiza a cor do layout antes de usá-la
        self.atualizar_cor_layout()  # Atualiza a cor do layout com o valor do backend
        
        # Atualizar a lista de casas exibidas
        self.casas_exibidas = self.exibir_casas(self.back_end.casas)
        if not self.casas_exibidas or len(self.casas_exibidas) < 8:
            print("Erro: A lista de casas exibidas está incompleta ou vazia.")
            return
        
       # Verificar se os widgets ainda existem antes de configurá-los
        if hasattr(self, 'label_titulo_nome') and self.label_titulo_nome.winfo_exists():
            self.label_titulo_nome.configure(text= (self.back_end.personagem_escolhido_nome), text_color="white")

        if hasattr(self, 'label_pontos') and self.label_pontos.winfo_exists():
            self.label_pontos.configure(text=f"POINTS: {self.back_end.player_pontos}", text_color=self.cor_Layout)

        if hasattr(self, 'label_xp') and self.label_xp.winfo_exists():
            self.label_xp.configure(text=f"XP: {str(self.back_end.player_xp)}",text_color=self.cor_Layout)
            
        if hasattr(self, 'label_cartas') and self.label_cartas.winfo_exists():
            self.label_cartas.configure(text="Your Cards:",text_color="white")
            
     
        # Atualizar a cor de fundo de todos os labels
        for widget in self.widgets_dinamicos:
            if isinstance(widget, ctk.CTkLabel):
                # Atualiza a cor do texto e do fundo de todos os labels
                widget.configure(bg_color="black",)  #text_color=self.cor_Layout
                
                
        for widget in self.widgets_dinamicos:
            if isinstance(widget, ctk.CTkLabel) and widget not in [self.label_pontos, self.label_xp, self.label_titulo_nome,self.label_cartas]:
                widget.destroy()
                self.widgets_dinamicos = [self.label_pontos, self.label_xp, self.label_titulo_nome, self.label_cartas]  # Mantém o 'label_pontos' na lista


        
        
        
        # Atualiza as imagens das casas
        for i, casa in enumerate(self.casas_exibidas):
            nova_imagem = PhotoImage(file=casa["imagem"])
            try:
                if i == 0:
                    self.canvas_abre.itemconfig(self.img_casa_1_lista, image=nova_imagem)
                    self.casa_1_lista = nova_imagem
                elif i == 1:
                    self.canvas_abre.itemconfig(self.img_casa_2_lista, image=nova_imagem)
                    self.casa_2_lista = nova_imagem
                elif i == 2:
                    self.canvas_abre.itemconfig(self.img_casa_3_lista, image=nova_imagem)
                    self.casa_3_lista = nova_imagem
                elif i == 3:
                    self.canvas_abre.itemconfig(self.img_casa_4_lista, image=nova_imagem)
                    self.casa_4_lista = nova_imagem
                elif i == 4:
                    self.canvas_abre.itemconfig(self.img_casa_5_lista, image=nova_imagem)
                    self.casa_5_lista = nova_imagem
                elif i == 5:
                    self.canvas_abre.itemconfig(self.img_casa_6_lista, image=nova_imagem)
                    self.casa_6_lista = nova_imagem
                elif i == 6:
                    self.canvas_abre.itemconfig(self.img_casa_7_lista, image=nova_imagem)
                    self.casa_7_lista = nova_imagem
                elif i == 7:
                    self.canvas_abre.itemconfig(self.img_casa_8_lista, image=nova_imagem)
                    self.casa_8_lista = nova_imagem
            except Exception as e:
                print(f"Erro ao atualizar imagem da casa {i + 1}: {e}")

        # Atualiza manualmente os textos dos labels das casas
        # for widget in self.widgets_dinamicos:
        #     if isinstance(widget, ctk.CTkLabel) and widget != self.label_pontos:
        #         widget.destroy()
        # self.widgets_dinamicos = [self.label_pontos, self.label_xp]  # Mantém o 'label_pontos' na lista
        

        # Lista de posições fixas no layout para as casas
        posicoes_x = [50, 150, 250, 350, 450, 550, 650, 750]  # As posições X para as 8 casas
        posicoes_y = 520  # Todas as casas têm a mesma posição Y fixada

        # Criando e posicionando manualmente cada label
        for i, casa in enumerate(self.casas_exibidas):
            if casa["texto"]:  # Apenas cria labels para casas com texto
                try:
                    label_nome_casa = ctk.CTkLabel(
                        self.root,
                        text=casa["texto"],  # Usando o texto da casa
                        text_color=self.cor_Layout,  # Cor do texto layout
                        bg_color="black",  
                        font=("Gelio Fasolada", 17),
                    )
                    label_nome_casa.place(x=posicoes_x[i], y=posicoes_y + 65, anchor="center")  # Posição fixa para o texto
                    self.widgets_dinamicos.append(label_nome_casa)  # Adiciona o label para controle futuro
                except Exception as e:
                    print(f"Erro ao criar label para a casa {i + 1}: {e}")














    def atualizar_tela_mais_ou_menos(self):
        """Atualiza os widgets e elementos gráficos baseados nas variáveis do backend."""  
        
        # Atualiza a cor do layout antes de usá-la
        self.atualizar_cor_layout() # Atualiza a cor do layout com o valor do backend
         
        # Atualizar a lista de casas exibidas
        self.casas_exibidas = self.exibir_casas(self.back_end.casas)
        if not self.casas_exibidas or len(self.casas_exibidas) < 8:
            print("Erro: A lista de casas exibidas está incompleta ou vazia.")
            return
        

        # # Atualizar o texto do label de pontos
        # self.label_pontos.configure(text=f"POINTS: {self.back_end.player_pontos}")
          # Atualizar o texto dos labels, incluindo o label de pontos
        self.label_pontos.configure(text=f"POINTS: {self.back_end.player_pontos}", text_color=self.cor_Layout)
        
        # Atualizar a cor de fundo de todos os labels
        for widget in self.widgets_dinamicos:
            if isinstance(widget, ctk.CTkLabel):
                widget.configure(bg_color="black", text_color=self.cor_Layout)  # Atualiza cor do texto e fundo


        # Atualiza as imagens das casas
        for i, casa in enumerate(self.casas_exibidas):
            nova_imagem = PhotoImage(file=casa["imagem"])
            try:
                if i == 0:
                    self.canvas_abre.itemconfig(self.img_casa_1_lista, image=nova_imagem)
                    self.casa_1_lista = nova_imagem
                elif i == 1:
                    self.canvas_abre.itemconfig(self.img_casa_2_lista, image=nova_imagem)
                    self.casa_2_lista = nova_imagem
                elif i == 2:
                    self.canvas_abre.itemconfig(self.img_casa_3_lista, image=nova_imagem)
                    self.casa_3_lista = nova_imagem
                elif i == 3:
                    self.canvas_abre.itemconfig(self.img_casa_4_lista, image=nova_imagem)
                    self.casa_4_lista = nova_imagem
                elif i == 4:
                    self.canvas_abre.itemconfig(self.img_casa_5_lista, image=nova_imagem)
                    self.casa_5_lista = nova_imagem
                elif i == 5:
                    self.canvas_abre.itemconfig(self.img_casa_6_lista, image=nova_imagem)
                    self.casa_6_lista = nova_imagem
                elif i == 6:
                    self.canvas_abre.itemconfig(self.img_casa_7_lista, image=nova_imagem)
                    self.casa_7_lista = nova_imagem
                elif i == 7:
                    self.canvas_abre.itemconfig(self.img_casa_8_lista, image=nova_imagem)
                    self.casa_8_lista = nova_imagem
            except Exception as e:
                print(f"Erro ao atualizar imagem da casa {i + 1}: {e}")

        # Atualiza manualmente os textos dos labels das casas
        # Remover labels antigos, mas sem remover o 'label_pontos'
        for widget in self.widgets_dinamicos:
            if isinstance(widget, ctk.CTkLabel) and widget != self.label_pontos:
                widget.destroy()
        self.widgets_dinamicos = [self.label_pontos]  # Mantém o 'label_pontos' na lista


        # Lista de posições fixas no layout para as casas
        posicoes_x = [50, 150, 250, 350, 450, 550, 650, 750]  # As posições X para as 8 casas
        posicoes_y = 520  # Todas as casas têm a mesma posição Y fixada

        # Criando e posicionando manualmente cada label
        for i, casa in enumerate(self.casas_exibidas):
            if casa["texto"]:  # Apenas cria labels para casas com texto
                try:
                    label_nome_casa = ctk.CTkLabel(
                        self.root,
                        text=casa["texto"],  # Usando o texto da casa
                        text_color=self.cor_Layout,  # Cor do texto layout
                        bg_color="black",  
                        font=("Gelio Fasolada", 17),
                    )
                    label_nome_casa.place(x=posicoes_x[i], y=posicoes_y + 65, anchor="center")  # Posição fixa para o texto
                    self.widgets_dinamicos.append(label_nome_casa)  # Adiciona o label para controle futuro
                except Exception as e:
                    print(f"Erro ao criar label para a casa {i + 1}: {e}")


    # def atualizar_layout_widgets_(self):
    #     # Atualiza todas as cores de fundo e texto
    #     for widget in self.widgets_dinamicos:
    #         if isinstance(widget, ctk.CTkLabel):
    #             widget.configure(bg_color="black", text_color=self.cor_Layout)
    #         elif isinstance(widget, tk.Canvas):
    #             widget.configure(bg="black")  # Atualiza o fundo do Canvas, se necessário





    def atualizar_tela4(self):
        """Atualiza os widgets e elementos gráficos baseados nas variáveis do backend."""
        
        # Atualizar a lista de casas exibidas
        self.casas_exibidas = self.exibir_casas(self.back_end.casas)
        if not self.casas_exibidas or len(self.casas_exibidas) < 8:
            print("Erro: A lista de casas exibidas está incompleta ou vazia.")
            return

         # Atualizar o texto do label de pontos
        if hasattr(self, "label_pontos"):  # Verifica se o widget 'label_pontos' existe
            self.label_pontos.configure(text=f"POINTS: {self.back_end.player_pontos}")
        else:
            # Se não existe, cria o widget pela primeira vez
            self.label_pontos = ctk.CTkLabel(
                self.root,
                text=f"POINTS: {self.back_end.player_pontos}",
                text_color=self.cor_Layout,
                bg_color="black",
                font=("Gelio Fasolada", 18),
            )
            self.label_pontos.place(x=190, y=60)
            self.widgets_dinamicos.append(self.label_pontos)
        # # Atualizar o texto do label de pontos
        # if hasattr(self, "label_pontos"):
        #     self.label_pontos.configure(text=f"POINTS: {self.back_end.player_pontos}")
        # else:
        #     print("Erro: 'label_pontos' não foi inicializado corretamente.")

        # Atualiza as imagens das casas
        for i, casa in enumerate(self.casas_exibidas):
            nova_imagem = PhotoImage(file=casa["imagem"])
            try:
                if i == 0:
                    self.canvas_abre.itemconfig(self.img_casa_1_lista, image=nova_imagem)
                    self.casa_1_lista = nova_imagem
                elif i == 1:
                    self.canvas_abre.itemconfig(self.img_casa_2_lista, image=nova_imagem)
                    self.casa_2_lista = nova_imagem
                elif i == 2:
                    self.canvas_abre.itemconfig(self.img_casa_3_lista, image=nova_imagem)
                    self.casa_3_lista = nova_imagem
                elif i == 3:
                    self.canvas_abre.itemconfig(self.img_casa_4_lista, image=nova_imagem)
                    self.casa_4_lista = nova_imagem
                elif i == 4:
                    self.canvas_abre.itemconfig(self.img_casa_5_lista, image=nova_imagem)
                    self.casa_5_lista = nova_imagem
                elif i == 5:
                    self.canvas_abre.itemconfig(self.img_casa_6_lista, image=nova_imagem)
                    self.casa_6_lista = nova_imagem
                elif i == 6:
                    self.canvas_abre.itemconfig(self.img_casa_7_lista, image=nova_imagem)
                    self.casa_7_lista = nova_imagem
                elif i == 7:
                    self.canvas_abre.itemconfig(self.img_casa_8_lista, image=nova_imagem)
                    self.casa_8_lista = nova_imagem
            except Exception as e:
                print(f"Erro ao atualizar imagem da casa {i + 1}: {e}")

        # Atualiza manualmente os textos dos labels
        # Remove labels antigos se necessário
        for widget in self.widgets_dinamicos:
            if isinstance(widget, ctk.CTkLabel):
                widget.destroy()
        self.widgets_dinamicos = []  # Reseta a lista para novos widgets
        
        # Lista de posições fixas no layout para as casas
        posicoes_x = [50, 150, 250, 350, 450, 550, 650, 750]  # As posições X para as 8 casas
        posicoes_y = 520  # Todas as casas têm a mesma posição Y fixada

        # Criando e posicionando manualmente cada label
        for i, casa in enumerate(self.casas_exibidas):
            if casa["texto"]:  # Apenas cria labels para casas com texto
                try:
                    label_nome_casa = ctk.CTkLabel(
                        self.root,
                        text=casa["texto"],  # Usando o texto da casa
                        text_color=self.cor_Layout,  # Cor do texto layout
                        bg_color="black",  
                        font=("Gelio Fasolada", 17),
                    )
                    label_nome_casa.place(x=posicoes_x[i], y=posicoes_y + 65, anchor="center")  # Posição fixa para o texto
                    self.widgets_dinamicos.append(label_nome_casa)  # Adiciona o label para controle futuro
                except Exception as e:
                    print(f"Erro ao criar label para a casa {i + 1}: {e}")

    def atualizar_tela3(self):
        """Atualiza os widgets e elementos gráficos baseados nas variáveis do backend."""
        
        # Atualizar a lista de casas exibidas
        self.casas_exibidas = self.exibir_casas(self.back_end.casas)
        if not self.casas_exibidas or len(self.casas_exibidas) < 8:
            print("Erro: A lista de casas exibidas está incompleta ou vazia.")
            return

        # Atualizar o texto do label de pontos
        self.label_pontos.configure(text=f"POINTS: {self.back_end.player_pontos}")
        
        # Atualiza as imagens das casas
        for i, casa in enumerate(self.casas_exibidas):
            nova_imagem = PhotoImage(file=casa["imagem"])
            if i == 0:
                self.canvas_abre.itemconfig(self.img_casa_1_lista, image=nova_imagem)
                self.casa_1_lista = nova_imagem
            elif i == 1:
                self.canvas_abre.itemconfig(self.img_casa_2_lista, image=nova_imagem)
                self.casa_2_lista = nova_imagem
            elif i == 2:
                self.canvas_abre.itemconfig(self.img_casa_3_lista, image=nova_imagem)
                self.casa_3_lista = nova_imagem
            elif i == 3:
                self.canvas_abre.itemconfig(self.img_casa_4_lista, image=nova_imagem)
                self.casa_4_lista = nova_imagem
            elif i == 4:
                self.canvas_abre.itemconfig(self.img_casa_5_lista, image=nova_imagem)
                self.casa_5_lista = nova_imagem
            elif i == 5:
                self.canvas_abre.itemconfig(self.img_casa_6_lista, image=nova_imagem)
                self.casa_6_lista = nova_imagem
            elif i == 6:
                self.canvas_abre.itemconfig(self.img_casa_7_lista, image=nova_imagem)
                self.casa_7_lista = nova_imagem
            elif i == 7:
                self.canvas_abre.itemconfig(self.img_casa_8_lista, image=nova_imagem)
                self.casa_8_lista = nova_imagem

        # Atualiza os textos dos labels
        # Lista de posições fixas no layout para as casas
        posicoes_x = [50, 150, 250, 350, 450, 550, 650, 750]  # As posições X para as 8 casas
        posicoes_y = 520  # Todas as casas têm a mesma posição Y fixada
        
        for i, label in enumerate(self.widgets_dinamicos):
            if isinstance(label, ctk.CTkLabel):
                if i < len(self.casas_exibidas):
                    label.configure(text=self.casas_exibidas[i]["texto"])
                    label.place(x=posicoes_x[i], y=posicoes_y + 65, anchor="center")  # Reposiciona

    def atualizar_tela2(self):
        """Atualiza os widgets e elementos gráficos baseados nas variáveis do backend."""
        
        # Atualizar a lista de casas exibidas
        self.casas_exibidas = self.exibir_casas(self.back_end.casas)
        if not self.casas_exibidas or len(self.casas_exibidas) < 8:
            print("Erro: A lista de casas exibidas está incompleta ou vazia.")
            return

        # Atualizar o texto do label de pontos
        self.label_pontos.configure(text=f"POINTS: {self.back_end.player_pontos}")
        
        # Atualiza as imagens das casas
        for i, casa in enumerate(self.casas_exibidas):
            nova_imagem = PhotoImage(file=casa["imagem"])
            if i == 0:
                self.canvas_abre.itemconfig(self.img_casa_1_lista, image=nova_imagem)
                self.casa_1_lista = nova_imagem
            elif i == 1:
                self.canvas_abre.itemconfig(self.img_casa_2_lista, image=nova_imagem)
                self.casa_2_lista = nova_imagem
            elif i == 2:
                self.canvas_abre.itemconfig(self.img_casa_3_lista, image=nova_imagem)
                self.casa_3_lista = nova_imagem
            elif i == 3:
                self.canvas_abre.itemconfig(self.img_casa_4_lista, image=nova_imagem)
                self.casa_4_lista = nova_imagem
            elif i == 4:
                self.canvas_abre.itemconfig(self.img_casa_5_lista, image=nova_imagem)
                self.casa_5_lista = nova_imagem
            elif i == 5:
                self.canvas_abre.itemconfig(self.img_casa_6_lista, image=nova_imagem)
                self.casa_6_lista = nova_imagem
            elif i == 6:
                self.canvas_abre.itemconfig(self.img_casa_7_lista, image=nova_imagem)
                self.casa_7_lista = nova_imagem
            elif i == 7:
                self.canvas_abre.itemconfig(self.img_casa_8_lista, image=nova_imagem)
                self.casa_8_lista = nova_imagem

        # Atualiza os labels das casas
        # Lista de posições fixas no layout para as casas
        posicoes_x = [50, 150, 250, 350, 450, 550, 650, 750]  # As posições X para as 8 casas
        posicoes_y = 520  # Todas as casas têm a mesma posição Y fixada
        
        # Remove os labels antigos e recria os novos com a posição correta
        for label in self.widgets_dinamicos:
            if isinstance(label, ctk.CTkLabel):
                label.destroy()  # Remove o widget antigo
        
        self.widgets_dinamicos = []  # Limpa a lista para recriar os labels

        for i, casa in enumerate(self.casas_exibidas):
            # Cria um novo label para cada casa, reposicionando-o corretamente
            label_nome_casa = ctk.CTkLabel(
                self.root,
                text=casa["texto"],  # Usando o texto da casa, que vem do dicionário
                text_color=self.cor_Layout,  # Cor do texto layout
                bg_color="black",
                font=("Gelio Fasolada", 17),
            )
            label_nome_casa.place(x=posicoes_x[i], y=posicoes_y + 65, anchor="center")  # Posição fixa para o texto
            self.widgets_dinamicos.append(label_nome_casa)
        
        # Debug para verificar o resultado da atualização
        for casa in self.casas_exibidas:
            print(f"Casa {casa['numero']}: {casa['texto']} - {casa['imagem']}")

    def atualizar_tela1(self):
        """Atualiza os widgets e elementos gráficos baseados nas variáveis do backend."""
        
        # Atualizar a lista de casas exibidas
        self.casas_exibidas = self.exibir_casas(self.back_end.casas)
        if not self.casas_exibidas or len(self.casas_exibidas) < 8:
            print("Erro: A lista de casas exibidas está incompleta ou vazia.")
            return

        # Atualizar o texto do label de pontos
        self.label_pontos.configure(text=f"POINTS: {self.back_end.player_pontos}")
        
        # Atualiza as imagens das casas
        for i, casa in enumerate(self.casas_exibidas):
            nova_imagem = PhotoImage(file=casa["imagem"])
            if i == 0:
                self.canvas_abre.itemconfig(self.img_casa_1_lista, image=nova_imagem)
                self.casa_1_lista = nova_imagem
            elif i == 1:
                self.canvas_abre.itemconfig(self.img_casa_2_lista, image=nova_imagem)
                self.casa_2_lista = nova_imagem
            elif i == 2:
                self.canvas_abre.itemconfig(self.img_casa_3_lista, image=nova_imagem)
                self.casa_3_lista = nova_imagem
            elif i == 3:
                self.canvas_abre.itemconfig(self.img_casa_4_lista, image=nova_imagem)
                self.casa_4_lista = nova_imagem
            elif i == 4:
                self.canvas_abre.itemconfig(self.img_casa_5_lista, image=nova_imagem)
                self.casa_5_lista = nova_imagem
            elif i == 5:
                self.canvas_abre.itemconfig(self.img_casa_6_lista, image=nova_imagem)
                self.casa_6_lista = nova_imagem
            elif i == 6:
                self.canvas_abre.itemconfig(self.img_casa_7_lista, image=nova_imagem)
                self.casa_7_lista = nova_imagem
            elif i == 7:
                self.canvas_abre.itemconfig(self.img_casa_8_lista, image=nova_imagem)
                self.casa_8_lista = nova_imagem
        
        # Atualiza os labels das casas
        for i, label in enumerate(self.widgets_dinamicos):
            if isinstance(label, ctk.CTkLabel) and i < len(self.casas_exibidas):
                label.configure(text=self.casas_exibidas[i]["texto"])

          
    # def rolar_dado_velhos(self):
    #     # sorteia um número entre 1 e 6
    #     numero_sorteado = random.randint(1, 6)
    #     print(f'Número sorteado: {numero_sorteado}')
        
    #     # Atualiza a posição od jogador
    #     self.back_end.casa_atual += numero_sorteado
    #     print(f'Casa atual {self.back_end.casa_atual}')
        
    #     # + 15 pontos para cada casa avançada
    #     self.back_end.player_pontos += ( 15 * numero_sorteado)
    #     print(f'Pontos do jogador: {self.back_end.player_pontos}')
    #     # Atualiza o Back_End com as novas informações
    #     self.back_end.atualizar_dados(nova_casa_atual, novo_pontos)

    #     #self.exibir_casas()
    #     self.atualizar_tijolos()
    #     self.atualizar_cor_layout()
    #     # self.atualizar_interface()


    
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
        
      