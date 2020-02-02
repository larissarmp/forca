# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Hangman:

    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    def guess(self, letter):
        if letter in self.word or not self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter in self.word or not self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    def hangman_over(self):
        self.hangman_won() or (len(self.missed_letters) == 6)

    def hangman_won(self):
        if "_" not in self.hide_word():
            return True
        return False

    # metódo para não mostrar palavra na board
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                rtn += letter
            else:
                rtn += '_'
        return rtn

    def print_status_game(self):
        print(board(len(self.missed_letters)))
        print("\nPalavras:" + self.hide_word())
        print("Palavras erradas:",)
        for letter in self.missed_letters:
            print(letter,)
        print()
        print("\nPalavras Corretas:",)
        for letter in self.guessed_letters:
            print(letter,)
        print()


def rand_word():
    with open("palavra.txt", "rt") as f:
        bank = f.readline()
        return bank[random.randint(0, len(bank)).strip()]

def main():
    game = Hangman(rand_word())

    while not game.hangman_over():
        game.print_status_game()
        user_input = input("\nDigite uma letra")
        game.guess(user_input)

    game.print_status_game()


if __name__ == '__main__':
    main()