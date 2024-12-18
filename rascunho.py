
    def atualizar_preview(self, img_path):# Atualiza o Canvas com a imagem de fundo e objetos sobrepostos.
        if img_path and os.path.exists(img_path):
            try:
                # Carregar e redimensionar a imagem de fundo
                img = Image.open(img_path).convert("RGBA")
                img = img.resize((400, 250), Image.LANCZOS)  # Redimensiona para o tamanho do Canvas

                # Salvar a imagem de fundo como referência para manipulações futuras
                self.fundo_preview = img

                # Converter a imagem para um formato compatível com Tkinter
                photo = ImageTk.PhotoImage(img)

                # Adicionar a imagem ao Canvas
                self.canvas.create_image(0, 0, image=photo, anchor="nw")

                # Manter a referência da imagem para evitar que seja descartada
                self.canvas.image = photo
                self.img_preview = photo

                # Atualizar o caminho da imagem de fundo no objeto settings
                self.settings.card_art = img_path

                # Adicionar objetos sobre a imagem (nome, número, QR Code)
                self.exibir_objetos_preview(self.canvas)

            except Exception as e:
                print(f"Erro ao carregar a imagem de fundo: {e}")
                self.canvas.create_text(200, 125, text="Erro ao carregar a imagem", font=("Arial", 12))
        else:
            self.canvas.create_text(200, 125, text="Nenhuma imagem selecionada", font=("Arial", 12))
            self.limpar_preview()


    def exibir_objetos_preview(self, canvas):  # Exibe os objetos sobre o Canvas
        # Remove widgets antigos do preview
        for widget in getattr(self, "widgets_preview", []):
            widget.destroy()
        self.widgets_preview = []

        largura_tela, altura_tela = 400, 250 # Dimensões do preview na tela

        coordenadas = self.settings.coordenadas_de_posicionamento_impressao # Coordenadas configuradas

        # Dados do sócio para o preview
        socio_number = " 123 "  # Exemplo fixo para o preview
        socio_name = " Nome do Sócio "  # Nome de exemplo
        qr_code_path = f"qrcodes/{socio_number}.png"

        # Garantir que a variável qr seja criada antes de usá-la
        qr = None  # Inicialização da variável qr

        # Gerar o QR Code se não existir
        if not os.path.exists(qr_code_path):
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data("https://github.com/Bressar") # Qr_code só para o preview
            qr.make(fit=True)

        # Se qr foi gerado (ou já existe), cria o QR Code
        if qr:
            # Gerar o QR Code em escala de cinza
            qr_img = qr.make_image(fill="black", back_color="white").convert("L")

            # Criar uma imagem RGBA com fundo transparente
            transparent = Image.new("RGBA", qr_img.size, (255, 255, 255, 0))

            # Adicionar os pixels do QR Code na imagem transparente
            for x in range(qr_img.width):
                for y in range(qr_img.height):
                    if qr_img.getpixel((x, y)) == 0:  # Ponto preto no QR Code
                        transparent.putpixel((x, y), (0, 0, 0, 255))  # Cor preta opaca

            # Salvar a imagem final com fundo transparente
            transparent.save(qr_code_path, "PNG")
            
         # Função para ajustar coordenadas usando escala
        escala_x = largura_tela / 400  # Referência baseada na largura do preview
        escala_y = altura_tela / 250  # Referência baseada na altura do preview

        # Função para ajustar coordenadas, não funciona direito, fiz uma gambiarra manualmente nos "Ys"
        def ajustar_y(y):
            return altura_tela - y  # Inverte o eixo Y

        # Adiciona Nome
        nome = coordenadas["nome"]
        pos_x = (int(nome["x"] * escala_x)) + 45 # gambiarra aqui! 
        pos_y = ajustar_y(int(nome["y"] * escala_y)) -3 # gambiarra aqui! 

        self.canvas.create_text(
            pos_x, pos_y,  # Coordenadas ajustadas
            text=socio_name, 
            fill=nome["cor"],  # Cor do texto
            font=(nome["fonte"], (nome["tamanho"])-2)  # gambiarra aqui!  Fonte e tamanho do texto
        )

        # Adiciona Número
        numero = coordenadas["numero"]
        pos_x = (int(numero["x"] * escala_x)) + 10 # gambiarra aqui! 
        pos_y = (ajustar_y(int(numero["y"] * escala_y))) - 5 # gambiarra aqui! 

        self.canvas.create_text(
            pos_x, pos_y,  # Coordenadas ajustadas
            text=socio_number, 
            fill=numero["cor"],  # Cor do texto
            font=(numero["fonte"], (numero["tamanho"])-4)  # gambiarra aqui! Fonte e tamanho do texto 
        )

        # Adiciona QR Code no preview
        qr_code = coordenadas["qr_code"]
        try:
            # Carregar e converter a imagem do QR Code para RGBA
            qr_img = Image.open(qr_code_path).convert("RGBA")
            qr_size_px = int(qr_code["tamanho"] * escala_x)
            qr_img = qr_img.resize((qr_size_px, qr_size_px), Image.LANCZOS)

            # Manter uma referência para a imagem
            qr_photo = ImageTk.PhotoImage(qr_img)

            # Calcular a posição do QR Code
            pos_x = int(qr_code["x"] * escala_x)
            pos_y = (ajustar_y(int(qr_code["y"] * escala_y) + qr_size_px)) + 95 # gambiarra aqui!

            # Adicionar a imagem ao canvas
            self.canvas.create_image(pos_x, pos_y - qr_size_px, image=qr_photo, anchor="nw")  # Ajuste para ancorar no canto superior

            # Manter a referência da imagem
            self.canvas.qr_photo = qr_photo  # Crucial para evitar que a imagem seja descartada

        except Exception as e:
            print(f"Erro ao carregar o QR Code no preview: {e}")
            print(f"Coordenadas Nome: {nome}")
            print(f"Coordenadas Número: {numero}")
            print(f"Coordenadas QR Code: {qr_code}")

