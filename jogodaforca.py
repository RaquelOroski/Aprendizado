#Jogo da forca

import random

#tabuleiro
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''','''

+---+
|   |
O   |
    |
    |
    |
=========''','''

+---+
|   |
O   |
|   |
    |
    |
=========''','''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''','''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''','''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman:

    def __init__(self, word): #Construção
        
    def __guess__(self, letter): #adivinhar a letra
        
    def __hangman_over(self): #verifica se o jogo terminou
        
    def __hangman_won(self): #verifica se ganhou
        
    def __hide_word(self): #não mostra a letra no board
        
    def __print_game_status(self): #checa e imprimi o status do jogo na tela

def rand_word():   #função para ler uma palavra de forma aleatória
    with open ("palavras.txt" , "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()

def main():
    game = Hangman(rand_word())
    
game.print_game_status()

if game.hangman_won():
    print('\nParabéns! Você venceu!')
    else:
        print('\nGame over!Você perdeu.')
        print('\nA palavra era ' + game.word)
        
if __name__ == "__main__":
    main()
    
    
    