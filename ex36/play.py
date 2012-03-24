#!/usr/bin/env python

import game as Game

game = Game.Game()

def run_game():
    while not game.is_game_over():
        game_state = game.get_game_state()
        player_input = game.get_player_input(game_state)
        new_game_state = game.player_act(user_input)
        game.set_game_state(new_game_state)

    game.lose_game()


run_game()
