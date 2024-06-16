# TRILHA DE PYTHON DA FOR_CODE
# Membro: João Vitor dos Santos Oliveira
# Exercício A - Semana Dois

from random import randint
import time 
import sys
import os

def JogoDaForca():
    "Função responsável pela execução do jogo da forca."

    # Lista que contém todos os temas do jogo.
    listaDeTemas = ["Jogos", "Filmes", "Séries", "Animes"]

    # Dicionários que contém as palavras de cada tema e suas respectivas dicas.
    jogos = {"Fortnite": ["Gênero: Battle Royale", "Desenvolvedores: Epic Games e People Can Fly", "Plataformas: PC e Consoles", "Data de Lançamento: 21 de julho de 2017", "Característica: Possui crossovers com vários produtos de entretenimento"],
             "Call Of Duty": ["Gênero: Tiro em Primeira Pessoa", "Desenvolvedores: Infinity Ward e Nokia", "Plataformas: PC e Consoles", "Data de Lançamento: 29 de outubro de 2003", "Característica: Cada ano é lançado um novo jogo da franquia"],
             "League Of Legends": ["Gêneros: Multiplayer Online/Battle Arena", "Desenvolvedora: Riot Games", "Plataforma: PC", "Data de Lançamento: 27 de outubro de 2009", "Característica: Possui uma forte presença nos E-sports"],
             "GTA 5": ["Gêneros: Ação/Aventura/Tiro em terceira pessoa/Single-Player", "Desenvolvedora: Rockstar North", "Plataformas: PC e Consoles", "Data de Lançamento: 17 de setembro de 2013", "Característica: Sua continuação será lançada 12 anos depois"],
             "Minecraft": ["Gênero: Sobrevivência", "Desenvolvedores: Mojang Studios e Xbox Game Studios,", "Plataformas: PC e Consoles", "Data de Lançamento: 18 de novembro de 2011", "Característica: O jogo permite criar mundos interativos"],
             "Fifa 15": ["Gênero: Esportes", "Desenvolvedora: Electronic Arts", "Plataformas: PC e Consoles", "Data de Lançamento: 23 de setembro de 2014", "Característica: Cada ano é lançado um novo jogo da franquia"]}
    
    filmes = {"Os Vingadores": ["Gêneros: Super-Herói/Ação/Aventura/Ficção Científica", "Direção: Joss Whedon", "Duração: 2h 23min", "Elenco: Robert Downey Jr., Chris Evans e Mark Ruffalo", "Sinopse: Heróis se reunem para salvar o mundo"],
              "O Poderoso Chefao": ["Gêneros: Drama/Policial", "Direção: Francis Ford Coppola", "Duração: 2h 55min", "Elenco: Marlon Brando, Al Pacino e James Caan", "Sinopse: Uma família mafiosa luta para estabelecer sua supremacia nos Estados Unidos depois da Segunda Guerra Mundial"],
              "Um Sonho de Liberdade": ["Gênero: Drama", "Direção: Frank Darabont", "Duração: 2h 22min", "Elenco: Tim Robbins, Morgan Freeman e Bob Gunton", "Sinopse: Um homem é condenado a duas prisões perpétuas consecutivas pelas mortes de sua esposa e de seu amante."],
              "Forrest Gump": ["Gêneros: Comédia/Drama/Romance", "Direção: Robert Zemeckis", "Duração: 2h 20min", "Elenco: Tom Hanks, Gary Sinise e Robin Wright", "Sinopse: Um homem conta a história de sua vida para pessoas que se sentam ao lado dele enquanto aguardam o ônibus."],
              "Harry Potter e a Pedra Filosofal": ["Gêneros: Infantil/Fantasia", "Direção: Chris Columbus", "Duração: 2h 32min", "Elenco: Daniel Radcliffe, Emma Watson e Rupert Grint", "Sinopse: Um garoto órfão recebe é convidado para ingressar em uma escola de magias"]}
    
    series = {"The Boys": ["Gêneros: Drama/Ação/Quadrinhos", "Quantidade de Temporadas: 4", "Elenco: Karl Urban e Jack Quaid", "Protagonista: Billy Butcher", "Sinopse: Um grupo de vigilantes luta contra pessoas superpoderosas corruptas"],
              "Breaking Bad": ["Gênero: Drama", "Quantidade de Temporadas: 5", "Elenco: Bryan Cranston, Aaron Paul e Anna Gunn", "Protagonista: Walter White", "Sinopse: Um professor de química passa a produzir metanfetamina ao descobrir que tem um câncer em estado avançado"],
              "Supernatural": ["Gêneros: Drama/Terror/Fantasia", "Quantidade de Temporadas: 15", "Elenco: Jared Padalecki, Jensen Ackles e Misha Collins", "Protagonistas: Sam Winchester e Dean Winchester", "Sinopse: Dois irmãos investigam e combatem eventos paranormais e outras ocorrências inexplicáveis"],
              "Peaky Blinders": ["Gênero: Policial/Drama/Histórico", "Quantidade de Temporadas: 4", "Elenco: Cillian Murphy e Natasha O'Keeffe", "Protagonista: Thomas Shelby", "Sinopse: Uma família criminosa deseja dominar uma cidade"],
              "Stranger Things": ["Gênero: Drama/Fantasia/Ficção Científica/Suspense", "Quantidade de Temporadas: 4", "Elenco: Winona Ryder, David Harbour e Millie Bobby Brown", "Protagonistas: Will Byers, Jim Hopper e Eleven", "Sinopse: Um menino desaparece por meios de eventos paranormais"]}
    
    animes = {"Naruto": ["Gêneros: Aventura/Comédia Dramática/Fantasia/Shounen", "Número de Episódios: 220", "Autor: Masashi Kishimoto", "Protagonista: Naruto Uzumaki", "Sinopse: O protagonista sonha em se tornar o quinto Hokage, o maior guerreiro e governante de sua vila"],
              "Dragon Ball": ["Gêneros: Aventura/Fantasia/Shounen", "Número de Episódios: 153", "Autor: Akira Toriyama", "Protagonista: Goku", "Sinopse: O protagonista descobre ser parte de um legado de poderosos conquistadores alienígenas e passa a defender seu planeta adotivo"],
              "Death Note": ["Gêneros: Mistério/Suspense Psicológico/Suspense", "Número de Episódios: 37", "Autores: Tsugumi Ohba e Takeshi Obata", "Protagonista: Light Yagami", "Sinopse: O protagonista tem o poder de matar uma pessoa apenas escrevendo seu nome em um caderno"],
              "Attack On Titan": ["Gêneros: Ação/Fantasia Sombria/Ficção Pós-Apocalíptica/Drama/Shōnen", "Número de Episódios: 94", "Autor: Hajime Isayama", "Protagonista: Eren Yeager", "Sinopse: O protagonista presencia a destruição de sua cidade"],
              "One Punch Man": ["Gêneros: Comédia/Ação/Sátira", "Número de Episódios: 24", "Autores: One e Yusuke Murata", "Protagonista: Saitama", "Sinopse: O protagonista derrota seus inimigos com apenas um soco"]}
    
    # Introdução do Jogo da Forca.
    time.sleep(0.3)
    print("\n\t\t-----Jogo da Forca-----\n")
    time.sleep(0.5)

    # Inicialização das vidas do jogador, da lista que contém todos seus chutes e da variável que determina seu ele venceu a partida.
    vidasDoJogador = 6
    listaDeChutes = []

    # Estrutura de Repetição responsável pela inicialização do jogo.
    while True:

        # Pergunta ao usuário se o mesmo gostaria de jogar o jogo.
        inicializacaoDoJogo = input("Deseja jogar (S/N): ")
        
        # Caso o usuário insira "y", o jogo se inicia.
        if inicializacaoDoJogo.lower() == "s":

            # Estrutura de Repetição responsável pela escolha da obra do jogo.
            while True:
                
                # Escolhe um tema para a obra.
                temaDaObra = listaDeTemas[randint(0, len(listaDeTemas)-1)]

                # Escolhe uma obra, tendo como base seu tema.
                if temaDaObra == "Jogos":
                    dicionarioDoTema = jogos
                    obrasDoTema = [chave for chave in dicionarioDoTema.keys()]
                    obraEscolhida = obrasDoTema[randint(0, len(obrasDoTema)-1)]
                
                if temaDaObra == "Filmes":
                    dicionarioDoTema = filmes
                    obrasDoTema = [chave for chave in dicionarioDoTema.keys()]
                    obraEscolhida = obrasDoTema[randint(0, len(obrasDoTema)-1)]
                
                if temaDaObra == "Séries":
                    dicionarioDoTema = series
                    obrasDoTema = [chave for chave in dicionarioDoTema.keys()]
                    obraEscolhida = obrasDoTema[randint(0, len(obrasDoTema)-1)]
                
                if temaDaObra == "Animes":
                    dicionarioDoTema = animes
                    obrasDoTema = [chave for chave in dicionarioDoTema.keys()]
                    obraEscolhida = obrasDoTema[randint(0, len(obrasDoTema)-1)]

                # Ocultação a obra escolhida.
                obraOculta = ""
                for letra in obraEscolhida:
                    if letra == " ":
                        obraOculta += "  "

                    else:
                        obraOculta += "_ "
                
                # Estrutura de Repetição responsável pelo funcionamento do jogo.
                while True:

                    # Lista todas as letras da obra oculta, excluindo os espaços.
                    listaLetrasObraOculta = []
                    for letra in obraOculta:
                        if letra != " ":
                            listaLetrasObraOculta.append(letra)

                    # Lista todas as letras da obra escolhida, excluindo os espaços.
                    listaLetrasObraEscolhida = []
                    for letra in obraEscolhida:
                        if letra != " ": 
                            listaLetrasObraEscolhida.append(letra)

                    # Caso a lista de elementos da obra oculta for igual a da obra escolhida, o usuário venceu o jogo.
                    if listaLetrasObraOculta == listaLetrasObraEscolhida: 
                        time.sleep(0.5)
                        print("\n\t\tPARABÉNS! VOCÊ VENCEU!\n")
                        time.sleep(0.5)

                        # Pergunta ao usuário se o mesmo gostaria de jogar novamente.
                        jogarNovamente = input("Deseja jogar novamente (S/N): ")

                        if jogarNovamente.lower() == "s":
                            listaDeChutes.clear() # Limpa a lista de chutes
                            break

                        if jogarNovamente.lower() == "n":
                            time.sleep(0.5)
                            sys.exit("\nFinalizando o jogo...\n")
                        
                        else:
                            time.sleep(0.5)
                            print("\nOpção Inválida!")
                            time.sleep(0.5)
                            print("Por favor, tente novamente.\n")
                            continue   
                    
                    time.sleep(0.5)
                    print(f"\nObra: {obraOculta}\n")
                    time.sleep(0.5)
                    print(f"Vidas do Jogador: {vidasDoJogador}")
                    time.sleep(0.5)
                    print(f"Lista de Letras Chutadas: {listaDeChutes}\n")
                    time.sleep(0.5)
                    print(f"Dicas:")
                    time.sleep(0.5)

                    # Impressão das dicas com base nas vidas do jogador.
                    if vidasDoJogador == 6:
                        print(f"Dica 1 --> Tema da Obra: {temaDaObra}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 5:
                        print(f"Dica 1 --> Tema da Obra: {temaDaObra}")
                        time.sleep(0.5)
                        print(f"Dica 2 --> {dicionarioDoTema[obraEscolhida][0]}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 4:
                        print(f"Dica 1 --> Tema da Obra: {temaDaObra}")
                        time.sleep(0.5)
                        print(f"Dica 2 --> {dicionarioDoTema[obraEscolhida][0]}")
                        time.sleep(0.5)
                        print(f"Dica 3 --> {dicionarioDoTema[obraEscolhida][1]}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 3:
                        print(f"Dica 1 --> Tema da Obra: {temaDaObra}")
                        time.sleep(0.5)
                        print(f"Dica 2 --> {dicionarioDoTema[obraEscolhida][0]}")
                        time.sleep(0.5)
                        print(f"Dica 3 --> {dicionarioDoTema[obraEscolhida][1]}")
                        time.sleep(0.5)
                        print(f"Dica 4 --> {dicionarioDoTema[obraEscolhida][2]}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 2:
                        print(f"Dica 1 --> Tema da Obra: {temaDaObra}")
                        time.sleep(0.5)
                        print(f"Dica 2 --> {dicionarioDoTema[obraEscolhida][0]}")
                        time.sleep(0.5)
                        print(f"Dica 3 --> {dicionarioDoTema[obraEscolhida][1]}")
                        time.sleep(0.5)
                        print(f"Dica 4 --> {dicionarioDoTema[obraEscolhida][2]}")
                        time.sleep(0.5)
                        print(f"Dica 5 --> {dicionarioDoTema[obraEscolhida][3]}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 1:
                        print(f"Dica 1 --> Tema da Obra: {temaDaObra}")
                        time.sleep(0.5)
                        print(f"Dica 2 --> {dicionarioDoTema[obraEscolhida][0]}")
                        time.sleep(0.5)
                        print(f"Dica 3 --> {dicionarioDoTema[obraEscolhida][1]}")
                        time.sleep(0.5)
                        print(f"Dica 4 --> {dicionarioDoTema[obraEscolhida][2]}")
                        time.sleep(0.5)
                        print(f"Dica 5 --> {dicionarioDoTema[obraEscolhida][3]}")
                        time.sleep(0.5)
                        print(f"Dica 6 --> {dicionarioDoTema[obraEscolhida][4]}\n")
                        time.sleep(0.5)

                    # Pede um chute ao jogador.
                    chuteDoUsuario = input("Por favor, chute uma letra: ")
                    time.sleep(0.5)
                    os.system('cls')
                    time.sleep(0.5)

                    # Verifica se o usuário não inseriu uma letra.
                    if (chuteDoUsuario == " ") or (chuteDoUsuario == ""):
                        print("Chute Inválido.")
                        time.sleep(0.5)
                        print("Tente Novamente.") 

                    # Verifica se o chute já foi feito anteriormente.
                    elif (chuteDoUsuario.lower() in listaDeChutes):
                        print("Esta letra já foi inserida.")
                        time.sleep(0.5)
                        print("Tente Novamente.")                    
                    
                    # Verifica se o usuário acertou o chute.
                    elif (chuteDoUsuario.lower() in (obraEscolhida.lower())):
                        listaDeChutes.append(chuteDoUsuario.lower())
                        print("\t\t       BOM CHUTE!")

                        obraOculta = ""
                        for letra in obraEscolhida:
                            flag = False 

                            if letra == " ":
                                    obraOculta += "  "
                                    flag = True

                            for chute in listaDeChutes:
                                if ((letra == chute.lower()) or (letra == chute.upper())):
                                    obraOculta += f"{letra} "
                                    flag = True
                                else:
                                    continue
                            
                            if flag == False:
                                obraOculta += "_ "

                    # Verifica se o usuário errou o chute.            
                    else:
                        listaDeChutes.append(chuteDoUsuario.lower())
                        vidasDoJogador -= 1

                        # Verifica se o jogador perdeu o jogo.
                        if vidasDoJogador == 0:
                            print("\t\tVOCÊ PERDEU!\n")
                            time.sleep(0.5)
                            sys.exit("Finalizando o jogo...\n")

                        print("\t\t       ERROU O CHUTE!")

        # Caso o usuário insira "n", o loop é quebrado e o jogo é finalizado.
        if inicializacaoDoJogo.lower() == "n":
            break
        
        # Caso o usuário insira uma letra inválida, aparecerá uma mensagem de erro.
        else:
            time.sleep(0.5)
            print("\nOpção Inválida!")
            time.sleep(0.5)
            print("Por favor, tente novamente.\n")
            time.sleep(0.5)
            continue

    # Mensagem de finalização do jogo.
    time.sleep(0.5)
    print("\nFinalizando o jogo...\n")
    time.sleep(0.5)
    

if __name__ == "__main__":
    JogoDaForca()