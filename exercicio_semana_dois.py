# TRILHA DE PYTHON DA FOR_CODE
# Membro: João Vitor dos Santos Oliveira
# Exercício A - Semana Dois

from random import randint
import time 
import sys

def JogoDaForca():
    "Função responsável pela execução do jogo da forca."

    # Lista que contém todos os temas do jogo.
    listaDeTemas = ["Jogos", "Filmes", "Séries", "Animes"]

    # Dicionários que contém as palavras de cada tema e suas respectivas dicas.
    jogos = {"Fortnite": ["Gênero: Battle Royale", "Desenvolvedores: Epic Games e People Can Fly", "Plataformas: PC e Consoles", "Data de Lançamento: 21 de julho de 2017"],
             "Call Of Duty": ["Gênero: Tiro em Primeira Pessoa", "Desenvolvedores: Infinity Ward e Nokia", "Plataformas: PC e Consoles", "Data de Lançamento: 29 de outubro de 2003"],
             "League Of Legends": ["Gêneros: Multiplayer Online/Battle Arena", "Desenvolvedora: Riot Games", "Plataforma: PC", "Data de Lançamento: 27 de outubro de 2009"],
             "GTA 5": ["Gêneros: Ação/Aventura/Tiro em terceira pessoa/Single-Player", "Desenvolvedora: Rockstar North", "Plataformas: PC e Consoles", "Data de Lançamento: 17 de setembro de 2013"],
             "Minecraft": ["Gênero: Sobrevivência", "Desenvolvedores: Mojang Studios e Xbox Game Studios,", "Plataformas: PC e Consoles", "Data de Lançamento: 18 de novembro de 2011"],
             "Fifa 15": ["Gênero: Esportes", "Desenvolvedora: Electronic Arts", "Plataformas: PC e Consoles", "Data de Lançamento: 23 de setembro de 2014"]}
    
    filmes = {"Os Vingadores": ["Gêneros: Super-Herói/Ação/Aventura/Ficção Científica", "Direção: Joss Whedon", "Duração: 2h 23min", "Elenco: Robert Downey Jr., Chris Evans e Mark Ruffalo"],
              "O Poderoso Chefão": ["Gêneros: Drama/Policial", "Direção: Francis Ford Coppola", "Duração: 2h 55min", "Elenco: Marlon Brando, Al Pacino e James Caan"],
              "Um Sonho de Liberdade": ["Gênero: Drama", "Direção: Frank Darabont", "Duração: 2h 22min", "Elenco: Tim Robbins, Morgan Freeman e Bob Gunton"],
              "Forrest Gump": ["Gêneros: Comédia/Drama/Romance", "Direção: Robert Zemeckis", "Duração: 2h 20min", "Elenco: Tom Hanks, Gary Sinise e Robin Wright"],
              "Harry Potter e a Pedra Filosofal": ["Gêneros: Infantil/Fantasia", "Direção: Chris Columbus", "Duração: 2h 32min", "Elenco: Daniel Radcliffe, Emma Watson e Rupert Grint"]}
    
    series = {"The Boys": ["Gêneros: Drama/Ação/Quadrinhos", "Quantidade de Temporadas: 4", "Elenco: Karl Urban e Jack Quaid", "Protagonista: Billy Butcher"],
              "Breaking Bad": ["Gênero: Drama", "Quantidade de Temporadas: 5", "Elenco: Bryan Cranston, Aaron Paul e Anna Gunn", "Protagonista: Walter White"],
              "Supernatural": ["Gêneros: Drama/Terror/Fantasia", "Quantidade de Temporadas: 15", "Elenco: Jared Padalecki, Jensen Ackles e Misha Collins", "Protagonistas: Sam Winchester e Dean Winchester"],
              "Peaky Blinders": ["Gênero: Policial/Drama/Histórico", "Quantidade de Temporadas: 4", "Elenco: Cillian Murphy e Natasha O'Keeffe", "Protagonista: Thomas Shelby"],
              "Stranger Things": ["Gênero: Drama/Fantasia/Ficção Científica/Suspense", "Quantidade de Temporadas: 4", "Elenco: Winona Ryder, David Harbour e Millie Bobby Brown", "Protagonistas: Will Byers, Jim Hopper e Eleven"]}
    
    animes = {"Naruto": ["Gêneros: Aventura/Comédia Dramática/Fantasia/Shounen", "Número de Episódios: 220", "Autor: Masashi Kishimoto", "Protagonista: Naruto Uzumaki"],
              "Dragon Ball": ["Gêneros: Aventura/Fantasia/Shounen", "Número de Episódios: 153", "Autor: Akira Toriyama", "Protagonista: Goku"],
              "Death Note": ["Gêneros: Mistério/Suspense Psicológico/Suspense", "Número de Episódios: 37", "Autores: Tsugumi Ohba e Takeshi Obata", "Protagonista: Light Yagami"],
              "Attack on Titan": ["Gêneros: Ação/Fantasia Sombria/Ficção Pós-Apocalíptica/Drama/Shōnen", "Número de Episódios: 94", "Autor: Hajime Isayama", "Protagonista: Eren Yeager"],
              "One Punch Man": ["Gêneros: Comédia/Ação/Sátira", "Número de Episódios: 24", "Autores: One e Yusuke Murata", "Protagonista: Saitama"]}
    
    # Introdução do Jogo da Forca.
    time.sleep(0.3)
    print("\n\t\t-----Jogo da Forca-----\n")
    time.sleep(0.5)

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
                print(obraEscolhida)
                # Ocultação a obra escolhida.
                obraOculta = ""
                for letra in obraEscolhida:
                    if letra == " ":
                        obraOculta += "  "

                    else:
                        obraOculta += "_ "
                
                # Estrutura de Repetição responsável pelo funcionamento do jogo.
                while True:

                    # Condição que verifica se o usuário venceu o jogo.
                    if obraOculta == obraEscolhida: 
                        time.sleep(0.5)
                        print("\nParabéns! Você venceu!\n")
                        time.sleep(0.5)

                        # Pergunta ao usuário se o mesmo gostaria de jogar novamente.
                        jogarNovamente = input("Deseja jogar novamente (S/N): ")

                        if jogarNovamente.lower() == "s":
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
                    
                    print(f"\nObra: {obraOculta}\n")
                    time.sleep(0.5)

                    if vidasDoJogador == 0:
                        print("\nVocê perdeu!")
                        time.sleep(0.5)
                        sys.exit("Finalizando o jogo...")
                    
                    elif vidasDoJogador == 6:
                        print(f"Dica 1 --> Tema da Obra: {temaDaObra}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 5:
                        print(f"Dica 2 --> {dicionarioDoTema[obraEscolhida][0]}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 4:
                        print(f"Dica 3 --> {dicionarioDoTema[obraEscolhida][1]}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 3:
                        print(f"Dica 4 --> {dicionarioDoTema[obraEscolhida][2]}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 2:
                        print(f"Dica 5 --> {dicionarioDoTema[obraEscolhida][3]}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 1:
                        print(f"Dica 6 --> {dicionarioDoTema[obraEscolhida][4]}\n")
                        time.sleep(0.5)

                    chuteDoUsuario = input("Por favor, chute uma letra: ")

                    if (chuteDoUsuario.lower() in (obraEscolhida.lower())) and (chuteDoUsuario != " ") and (chuteDoUsuario != ""):
                        listaDeChutes.append(chuteDoUsuario)
                        print("\nBom chute!")
                        time.sleep(0.5)

                        obraOculta = ""
                        for letra in obraEscolhida:
                            print(letra)
                            if letra == " ":
                                obraOculta += "  "

                            for chute in listaDeChutes:
                                if letra == chute.lower():
                                    obraOculta += f"{letra} "
                                
                                if letra == chute.upper():
                                    obraOculta += f"{letra} "
                            
                                else:
                                    obraOculta += "_ "
                    
                    else:
                        vidasDoJogador -= 1
                        print("\nErrou o chute.")
                        time.sleep(0.5)
                        

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


    