# Resumo dos Valores de anchor:
# "center": O centro do widget é alinhado ao ponto (x, y).
# "n": O topo do widget é alinhado ao ponto (x, y).
# "s": A base do widget é alinhada ao ponto (x, y).
# "e": O lado direito do widget é alinhado ao ponto (x, y).
# "w": O lado esquerdo do widget é alinhado ao ponto (x, y).
# Combinando direções: "ne" (topo-direito), "nw" (topo-esquerdo), "se" (base-direito), "sw" (base-esquerdo).


           
                
        # Imagem casa 1
        label_voce_aqui_1 = ctk.CTkLabel(
            self.root,
            text= "You are here!", # trocar o nome pela variável de sistema
            text_color=self.cor_Layout,  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
            bg_color="black",  
            font=("Gelio Fasolada", 14),
            )            
        label_voce_aqui_1.place(x=50, y=458, anchor="center") # relx=0.5, y=10, anchor="n"
        self.widgets_dinamicos.append(label_voce_aqui_1)
        
        self.casa_1_lista = PhotoImage(file="images/casa_teste.png")  # depois trocar pela variável dinâmica
        self.img_casa_1_lista = self.canvas_abre.create_image(50, 520, image=self.casa_1_lista)

        # Imagem casa 2
        self.casa_2_lista = PhotoImage(file="images/casa_teste.png")  # depois trocar pela variável dinâmica
        self.img_casa_2_lista = self.canvas_abre.create_image(150, 520, image=self.casa_2_lista)


        # Imagem casa 3
        self.casa_3_lista = PhotoImage(file="images/casa_teste.png")  # depois trocar pela variável dinâmica
        self.img_casa_3_lista = self.canvas_abre.create_image(250, 520, image=self.casa_3_lista)
        
        
        label_nome_casa_3 = ctk.CTkLabel(
            self.root,
            text= "Harpies", # trocar o nome pela variável de sistema
            text_color=self.cor_Layout,  # Cor 255/255, 140/255, 0/255, 1  # DarkOrange
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

        
        
        
        
         if hasattr(self, 'label_carta_menu1') and self.label_carta_menu1.winfo_exists():
            self.label_carta_menu1.configure(text=self.back_end.cartas_player[0]["action_p"],text_color="white")
        
        if hasattr(self, 'label_carta_menu2') and self.label_carta_menu2.winfo_exists():
            self.label_carta_menu2.configure(text=self.back_end.cartas_player[1]["action_p"],text_color="white")
            
        if hasattr(self, 'label_carta_menu3') and self.label_carta_menu3.winfo_exists():
            self.label_carta_menu3.configure(text=self.back_end.cartas_player[2]["action_p"],text_color="white")
        
        

            
            
            
            
            
            
            
                        self.label_carta_menu2 = ctk.CTkLabel(
            self.root,
            text= self.back_end.cartas_player[1]["action_p"], # Variável de sistema
            text_color= 'white',  
            bg_color="black",  
            font=("cambria", 14),
            )            
            self.label_carta_menu2.place(x=150, y=395, anchor='n' ) # relx=0.5, y=10, anchor="n"
            self.widgets_dinamicos.append(self.label_carta_menu2)
            
            
            
            
                        self.label_carta_menu3 = ctk.CTkLabel(
            self.root,
            text= self.back_end.cartas_player[2]["action_p"], # Variável de sistema
            text_color= 'white',  
            bg_color="black",  
            font=("cambria", 14),
            )            
            self.label_carta_menu3.place(x=250, y=395, anchor='n' ) # relx=0.5, y=10, anchor="n"
            self.widgets_dinamicos.append(self.label_carta_menu3)