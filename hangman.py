#! /usr/bin/env python

import random

with open('wordlist.10000', 'rt') as f:
    WORD_LIST = [line.strip() for line in f.readlines()]

class InvalidLetter():
    pass

MAX_STRIKES = 5
class GameState():
    def __init__(self):
        self.word = random.choice(WORD_LIST)
        self.strikes = 0
        self.guessed_letters = list()
    
    def try_letter(self, letter):
        if (letter in self.guessed_letters) or (len(letter) != 1):
            return InvalidLetter
        self.guessed_letters.append(letter)
        if letter not in self.word:
            self.strikes += 1
        return letter in self.word

    def state_string(self, just_tell_me = False):
        if just_tell_me:
            return ' '.join([x for x in self.word])
        return ' '.join(
            [x if x in self.guessed_letters else '_' for x in self.word])
    
    def did_user_win(self):
        return not [x for x in self.word if x not in self.guessed_letters]

    def guesses_remaining(self):
        return MAX_STRIKES - self.strikes

    def game_over(self):
        return self.did_user_win() or self.strikes >= MAX_STRIKES

def main():
    game_state = GameState()
    while not game_state.game_over():
        print(game_state.state_string())
        print(f'You have {game_state.guesses_remaining()} guesses left')
        while True:
            input_letter = input('Enter a letter: ')
            result = game_state.try_letter(input_letter)
            if result == InvalidLetter:
                print('Sorry. That wasn\'t a valid letter')
            else:
                break
        print()
    print(game_state.state_string(just_tell_me=True))
    if game_state.did_user_win():
        print('You win!!')
    else:
        print('You lose. :(')
        
if __name__ == '__main__':
    main()
