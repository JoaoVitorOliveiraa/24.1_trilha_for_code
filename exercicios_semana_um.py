# TRILHA DE PYTHON DA FOR_CODE
# Membro: João Vitor dos Santos Oliveira
# Exercícios A e B - Semana Um 

from random import randint
import time
import sys

def Jokenpo():
    """Função responsável pelo jogo "Pedra, Papel e Tesoura" (Jokenpô)."""

    # Lista todos os símbolos de mão do jogo.
    listaDeSimbolos = ["pedra", "papel", "tesoura"]

    # Lista todas as mensagens que são impressas no terminal.
    listaDeMensagens = ["Pontos do Jogador: ", "Pontos da Máquina: ", "\nRodada Atual: "
                        , "Resultado da Rodada: EMPATE!", "Resultado da Rodada: PONTO DA MÁQUINA!"
                        , "Resultado da Rodada: PARABÉNS! PONTO DO JOGADOR!", "Jogada do Jogador: "
                        , "Jogada da Máquina: ", "\nResultado do Jogo: PARABÉNS! VOCÊ VENCEU!\n"
                        , "\nResultado do Jogo: Não foi dessa vez. Você perdeu!\n"
                        ,"\nResultado do Jogo: Empate! Na próxima você consegue.\n"]

    # Números de rodadas do jogo.
    contagemDasRodadas = 1

    # Inicialização dos pontos do jogo.
    pontosDoJogador = 0
    pontosDaMaquina = 0

    # Estrutura de Repetição que inicilaza as rodadas do jogo.
    while (contagemDasRodadas <= 5) and (pontosDoJogador < 3) and (pontosDaMaquina < 3):

        # Pede um símbolo ao jogador.
        time.sleep(0.3)
        simboloInserido = input("\nPor favor, insira um símbolo: ")
        #print("\n")
        time.sleep(0.3)

        # Condição que verifica se o usuário inseriu um símbolo inválido.
        if not(str.lower(simboloInserido) in listaDeSimbolos):
            sys.exit("\nSímbolo Inválido! Tente Novamente.\n")
        
        # Gera aleatoriamente a jogada da máquina.
        jogadaDaMaquina = randint(0, 2)

        # Condição que verifica se o jogador inseriu o símbolo "pedra".
        if str.lower(simboloInserido) == listaDeSimbolos[0]:
            
            # Caso a máquina tenha jogado "pedra", é impressa uma mensagem de empate e o laço é continuado.
            if listaDeSimbolos[jogadaDaMaquina] == "pedra":
                print(listaDeMensagens[2], contagemDasRodadas)
                time.sleep(0.3)
                print(listaDeMensagens[6], simboloInserido)
                time.sleep(0.3)
                print(listaDeMensagens[7], listaDeSimbolos[jogadaDaMaquina])
                time.sleep(0.3)
                print(listaDeMensagens[3])
                time.sleep(0.3)
                print(listaDeMensagens[0], pontosDoJogador)
                time.sleep(0.3)
                print(listaDeMensagens[1], pontosDaMaquina)
                contagemDasRodadas += 1
                continue
                
            # Caso a máquina tenha jogado "papel", seus pontos são incrementados.
            if listaDeSimbolos[jogadaDaMaquina] == "papel":
                pontosDaMaquina += 1 
                print(listaDeMensagens[2], contagemDasRodadas)
                time.sleep(0.3)
                print(listaDeMensagens[6], simboloInserido)
                time.sleep(0.3)
                print(listaDeMensagens[7], listaDeSimbolos[jogadaDaMaquina])
                time.sleep(0.3)
                print(listaDeMensagens[4])
                time.sleep(0.3)
                print(listaDeMensagens[0], pontosDoJogador)
                time.sleep(0.3)
                print(listaDeMensagens[1], pontosDaMaquina)
                contagemDasRodadas += 1
                continue
            
            # Caso a máquina tenha jogado "tesoura", os pontos do jogador são incrementados.
            if listaDeSimbolos[jogadaDaMaquina] == "tesoura":
                pontosDoJogador += 1
                print(listaDeMensagens[2], contagemDasRodadas)
                time.sleep(0.3)
                print(listaDeMensagens[6], simboloInserido)
                time.sleep(0.3)
                print(listaDeMensagens[7], listaDeSimbolos[jogadaDaMaquina])
                time.sleep(0.3)
                print(listaDeMensagens[5])
                time.sleep(0.3)
                print(listaDeMensagens[0], pontosDoJogador)
                time.sleep(0.3)
                print(listaDeMensagens[1], pontosDaMaquina)
                contagemDasRodadas += 1
                continue

        # Condição que verifica se o jogador inseriu o símbolo "papel".
        if str.lower(simboloInserido) == listaDeSimbolos[1]:
            
            # Caso a máquina tenha jogado "papel", é impressa uma mensagem de empate e o laço é continuado.
            if listaDeSimbolos[jogadaDaMaquina] == "papel":
                print(listaDeMensagens[2], contagemDasRodadas)
                time.sleep(0.3)
                print(listaDeMensagens[6], simboloInserido)
                time.sleep(0.3)
                print(listaDeMensagens[7], listaDeSimbolos[jogadaDaMaquina])
                time.sleep(0.3)
                print(listaDeMensagens[3])
                time.sleep(0.3)
                print(listaDeMensagens[0], pontosDoJogador)
                time.sleep(0.3)
                print(listaDeMensagens[1], pontosDaMaquina)
                contagemDasRodadas += 1
                continue
                
            # Caso a máquina tenha jogado "tesoura", seus pontos são incrementados.
            if listaDeSimbolos[jogadaDaMaquina] == "tesoura":
                pontosDaMaquina += 1 
                print(listaDeMensagens[2], contagemDasRodadas)
                time.sleep(0.3)
                print(listaDeMensagens[6], simboloInserido)
                time.sleep(0.3)
                print(listaDeMensagens[7], listaDeSimbolos[jogadaDaMaquina])
                time.sleep(0.3)
                print(listaDeMensagens[4])
                time.sleep(0.3)
                print(listaDeMensagens[0], pontosDoJogador)
                time.sleep(0.3)
                print(listaDeMensagens[1], pontosDaMaquina)
                contagemDasRodadas += 1
                continue
            
            # Caso a máquina tenha jogado "pedra", os pontos do jogador são incrementados.
            if listaDeSimbolos[jogadaDaMaquina] == "pedra":
                pontosDoJogador += 1
                print(listaDeMensagens[2], contagemDasRodadas)
                time.sleep(0.3)
                print(listaDeMensagens[6], simboloInserido)
                time.sleep(0.3)
                print(listaDeMensagens[7], listaDeSimbolos[jogadaDaMaquina])
                time.sleep(0.3)
                print(listaDeMensagens[5])
                time.sleep(0.3)
                print(listaDeMensagens[0], pontosDoJogador)
                time.sleep(0.3)
                print(listaDeMensagens[1], pontosDaMaquina)
                contagemDasRodadas += 1
                continue

        # Condição que verifica se o jogador inseriu o símbolo "tesoura".
        if str.lower(simboloInserido) == listaDeSimbolos[2]:
            
            # Caso a máquina tenha jogado "tesoura", é impressa uma mensagem de empate e o laço é continuado.
            if listaDeSimbolos[jogadaDaMaquina] == "tesoura":
                print(listaDeMensagens[2], contagemDasRodadas)
                time.sleep(0.3)
                print(listaDeMensagens[6], simboloInserido)
                time.sleep(0.3)
                print(listaDeMensagens[7], listaDeSimbolos[jogadaDaMaquina])
                time.sleep(0.3)
                print(listaDeMensagens[3])
                time.sleep(0.3)
                print(listaDeMensagens[0], pontosDoJogador)
                time.sleep(0.3)
                print(listaDeMensagens[1], pontosDaMaquina)
                contagemDasRodadas += 1
                continue
                
            # Caso a máquina tenha jogado "pedra", seus pontos são incrementados.
            if listaDeSimbolos[jogadaDaMaquina] == "pedra":
                pontosDaMaquina += 1
                print(listaDeMensagens[2], contagemDasRodadas)
                time.sleep(0.3) 
                print(listaDeMensagens[6], simboloInserido)
                time.sleep(0.3)
                print(listaDeMensagens[7], listaDeSimbolos[jogadaDaMaquina])
                time.sleep(0.3)
                print(listaDeMensagens[4])
                time.sleep(0.3)
                print(listaDeMensagens[0], pontosDoJogador)
                time.sleep(0.3)
                print(listaDeMensagens[1], pontosDaMaquina)
                contagemDasRodadas += 1
                continue
            
            # Caso a máquina tenha jogado "papel", os pontos do jogador são incrementados.
            if listaDeSimbolos[jogadaDaMaquina] == "papel":
                pontosDoJogador += 1
                print(listaDeMensagens[2], contagemDasRodadas)
                time.sleep(0.3)
                print(listaDeMensagens[6], simboloInserido)
                time.sleep(0.3)
                print(listaDeMensagens[7], listaDeSimbolos[jogadaDaMaquina])
                time.sleep(0.3)
                print(listaDeMensagens[5])
                time.sleep(0.3)
                print(listaDeMensagens[0], pontosDoJogador)
                time.sleep(0.3)
                print(listaDeMensagens[1], pontosDaMaquina)
                contagemDasRodadas += 1
                continue

    # Condições para o rsultado final do jogo.
    if pontosDoJogador > pontosDaMaquina:
        print(listaDeMensagens[8])
    
    elif pontosDoJogador < pontosDaMaquina:
        print(listaDeMensagens[9])
    
    else:
        print(listaDeMensagens[10])    

    # Retorno da função.
    return True
            

if __name__ == "__main__":
    
    time.sleep(0.5)
    print("\n\t\t-----Exercícios da Semana 1-----\n")
    time.sleep(0.5)

    # Pede para ao usuário escolher um dos exercícios.
    exercicio = input("Por favor, escolha um dos exercícios (A ou B): ")
    time.sleep(0.3)

    # Caso o usuário escolha o exercício A, o jogo "Jokenpô" é iniciado. 
    if str.upper(exercicio) == "A":
        print("\n--> Exercício A: Jokenpô")
        Jokenpo()

    # Caso o usuário escolha o exercício B, é pedido um símbolo para iniciar o jogo. 
    elif str.upper(exercicio) == "B":
        time.sleep(0.3)
        print("\n--> Exercício B\n")

    # Caso a opção seja inválida, aparecerá uma mensagem de erro.
    else:
        time.sleep(0.3)
        print("\nOpção Inválida! Tente Novamente.\n")
        time.sleep(0.3)
    
