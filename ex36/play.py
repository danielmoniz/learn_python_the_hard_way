#!/usr/bin/env python

import game as Game

game = Game.Game()

def run_game():
    while not game.is_game_over():
        game_state = game.get_game_state()
        game.get_player_input(game_state)


run_game()
