# TRILHA DE PYTHON DA FOR_CODE
# Membro: João Vitor dos Santos Oliveira
# Exercício A - Semana Dois

from random import randint
import time 
import sys

def JogoDaForca():
    "Função responsável pela execução do jogo da forca."

    # Lista que contém todos os temas do jogo.
    listaDeTemas = ["Jogos Eletrônicos", "Filmes", "Séries", "Animes"]

    # Dicionários que contém as palavras de cada tema e suas respectivas dicas.
    jogosEletronicos = {"Fortnite": ["Gênero: Battle Royale"],
                        "Call Of Duty": ["Gênero: Jogo de Tiro"],
                        "League Of Legends": ["Gênero: "],
                        "GTA": ["Gênero: "],
                        "Minecraft": ["Gênero: "],
                        "Fifa": ["Gênero: "]}
    
    filmes = {"Os Vingadores": ["Gênero: Super-Herói/Ação/Aventura/Ficção Científica", "Direção: Joss Whedon", "Duração: 2h 23min"],
              "O Poderoso Chefão": ["Gênero: Drama/Policial", "Direção: Francis Ford Coppola", "Duração: 2h 55min"],
              "Um Sonho de Liberdade": ["Gênero: Drama", "Direção: Frank Darabont", "Duração: 2h 22min"],
              "Forrest Gump": ["Gênero: Comédia/Drama/Romance", "Direção: Robert Zemeckis", "Duração: 2h 20min"],
              "Harry Potter e a Pedra Filosofal": ["Gênero: Infantil/Fantasia", "Direção: Chris Columbus", "Duração: 2h 32min"]}
    
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
                if temaDaObra == "Jogos Eletrônicos":
                    dicionarioDoTema = jogosEletronicos
                    obrasDoTema = [chave for chave in dicionarioDoTema.keys()]
                    obraEscolhida = obrasDoTema[randint(0, len(obrasDoTema)-1)]
                
                if temaDaObra == "Filmes":
                    dicionarioDoTema = filmes
                    obrasDoTema = [chave for chave in dicionarioDoTema.keys()]
                    obraEscolhida = obrasDoTema[randint(0, len(obrasDoTema)-1)]
                
                if temaDaObra == "Séries":
                    obrasDoTema = [chave for chave in jogosEletronicos.keys()]
                    obraEscolhida = obrasDoTema[randint(0, len(obrasDoTema)-1)]
                
                if temaDaObra == "Animes":
                    obrasDoTema = [chave for chave in jogosEletronicos.keys()]
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
                        print(f"Dica 3 --> {dicionarioDoTema[obraEscolhida][0]}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 3:
                        print(f"Dica 4 --> {dicionarioDoTema[obraEscolhida][0]}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 2:
                        print(f"Dica 5 --> {dicionarioDoTema[obraEscolhida][0]}\n")
                        time.sleep(0.5)
                    
                    elif vidasDoJogador == 1:
                        print(f"Dica 6 --> {dicionarioDoTema[obraEscolhida][0]}\n")
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


    